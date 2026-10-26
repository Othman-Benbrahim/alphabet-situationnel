#!/usr/bin/env python3
"""Alphabet situationnel 0.5.1 — calcul expérimental, validation et traçabilité.
Bibliothèque standard Python 3.8+. `autotest` exécute les contrôles de régression.
Les analogies structurales sont des hypothèses, jamais une calibration acquise.
Auteur : Othman Ben Brahim · Licence MIT (voir LICENSE).
"""
import argparse, calendar, contextlib, datetime, hashlib, io, json, math, os, re, sys, unicodedata
from collections import defaultdict
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
P = json.loads((RACINE / "assets/parametres.json").read_text(encoding="utf-8"))
NOMS = P["cartes"]
NS = P["nombre_strates"]  # nombre de strates (O3) ; toute borne 1..NS en dépend
QUALIFS = {"rétroaction amplifiante", "rétroaction stabilisante", "multi-échelle", "délai", "multi-strate"}
DEGRADE = {"F": "M", "M": "f", "f": None}
UNITES = {"jour": 1., "jours": 1., "semaine": 7., "semaines": 7., "mois": 30.4375, "an": 365.25, "ans": 365.25}
MOT_RE = re.compile(r"^(?P<c>[^@\[\]{}]+)@(?P<s>\d{1,2})\[(?P<i>[Ff])\](?P<q>(?: \{[^}]+\}){0,2})$")
ETAT_RE = re.compile(r"^\[(?P<d>\d{4}-\d{2}(?:-\d{2})?) \| (?P<f>\d+ (?:jours?|semaines?|mois|ans?))\] (?P<corps>.+)$")

def _plat(s):
    s = unicodedata.normalize("NFD", s)
    return "".join(ch for ch in s if unicodedata.category(ch) != "Mn").upper().replace(" ", "").replace("·", "")


_INDEX = {}
for _ab, _nom in NOMS.items():
    _INDEX[_plat(_ab)] = _ab
    _INDEX[_plat(_nom)] = _ab
_INDEX["TRACE"] = "TRC"


def carte_id(s):
    k = _plat(s.strip())
    if k not in _INDEX:
        raise ValueError(f"carte inconnue : {s!r}")
    return _INDEX[k]



def cle(m):
    return f'{m["c"]}@{m["s"]}'



def forces_changees(a, b):
    """Mots présents dans deux états successifs avec une force différente (F ↔ f)."""
    fa = {cle(m): m["i"] for m in a["mots"]}
    return {cle(m) for m in b["mots"] if cle(m) in fa and fa[cle(m)] != m["i"]}



def lire_cle(t):
    c, s = t.strip().split("@")
    return f"{carte_id(c)}@{int(s)}"



def erreurs_g6(etat):
    err = []
    vus = set()
    for m in etat["mots"]:
        if not 1 <= m["s"] <= NS:
            err.append(f"{cle(m)} : strate hors de 1–{NS}")
        if cle(m) in vus:
            err.append(f"{cle(m)} : carte répétée dans la même strate (G6)")
        vus.add(cle(m))
        if len(m["q"]) != len(set(m["q"])) or len(m["q"]) > 2:
            err.append(f"{cle(m)} : qualificatifs répétés ou plus de deux (G1)")
        for q in m["q"]:
            if q not in QUALIFS:
                err.append(f"{cle(m)} : qualificatif inconnu {{{q}}} (G1)")
    return err



_STATUTS_CACHE = {}


def statuts():
    """Statut de chaque équivalent (carte, strate), relu si un fichier de strate a changé."""
    d = os.path.join(RACINE, "references", "equivalences")
    fichiers = [os.path.join(d, f"strate-{s:02d}.md") for s in range(1, NS + 1)]
    cle_ = tuple(os.path.getmtime(f) if os.path.exists(f) else None for f in fichiers)
    if _STATUTS_CACHE.get('cle') == cle_:
        return dict(_STATUTS_CACHE['st'])
    st = {}
    for s, f in enumerate(fichiers, 1):
        if not os.path.exists(f):
            continue
        for l in open(f, encoding="utf-8"):
            m = re.match(r"^\| (\S+) \|.*\| (Attesté|Documenté|Proposé|Vide|Hors domaine) \| [^|]* \|\s*$", l)
            if m:
                try:
                    st[(carte_id(m.group(1)), s)] = m.group(2)
                except ValueError:
                    pass
    _STATUTS_CACHE.update(cle=cle_, st=st)
    return dict(st)


def hors_domaine(k):
    c, s = k.split('@')
    return statuts().get((c, int(s))) == 'Hors domaine'


def voisines():
    """Voisines de chaque carte, lues dans `cartes.md` (listes « À ne pas confondre avec »)."""
    out, cur, dans = {}, None, False
    for l in (RACINE/'references'/'cartes.md').read_text(encoding='utf-8').splitlines():
        if l.startswith('## '):
            try:
                cur = carte_id(l[3:]); out[cur] = set()
            except ValueError:
                cur = None
            dans = False
        elif l.startswith('**À ne pas confondre avec**'):
            dans = True
        elif dans and cur:
            m = re.match(r'^- \*([^*]+)\*', l)
            if m:
                out[cur].add(carte_id(m.group(1)))
            elif l.startswith('**'):
                dans = False
    return out


def verdicts_a6(ligne, raisons=False):
    """{carte: verdict} (ou {carte: (verdict, raison)}) d'une ligne A6 « CARTE@s : VOISINE → (raison) ; … »."""
    corps = ligne.split(':', 1)[1] if ':' in ligne else ligne
    out = {}
    for seg in corps.split(';'):
        m = re.match(r'^\s*(.+?)\s*(→|\+|←|\?)\s*\((.*)\)\s*$', seg.strip(), re.S)
        if m:
            try:
                out[carte_id(m.group(1))] = (m.group(2), m.group(3).strip()) if raisons else m.group(2)
            except ValueError:
                pass
    return out


def controle_a6(k, ligne):
    """Erreurs A6 d'un mot Fort : chaque voisine de `cartes.md` passée, tranchée pour la carte, justifiée.
    `→` (la question tranche pour cette carte) et `+` (voisine aussi présente, par d'autres faits) sont
    seuls compatibles avec F : `?` laisse la question ouverte, `←` attribue l'unique fait du mot à la
    voisine, qui ne compte alors plus pour cette carte."""
    v = verdicts_a6(ligne, raisons=True); attendues = voisines().get(k.split('@')[0], set())
    err = []
    if attendues - set(v):
        err.append(f'{k} : voisines non passées dans la ligne A6 {sorted(NOMS[x] for x in attendues - set(v))}')
    if any(r == '?' for r, _ in v.values()):
        err.append(f'{k} : voisine non tranchée (?) → au plus f')
    cedees = sorted(NOMS[x] for x, (r, _) in v.items() if r == '←')
    if cedees:
        err.append(f'{k} : fait attribué à la voisine (←) {cedees} → il ne compte pas pour cette carte, F impossible')
    vides = sorted(NOMS[x] for x, (_, j) in v.items() if not j)
    if vides:
        err.append(f'{k} : justification vide pour {vides} (A6 : obligatoire)')
    return err


PORTEES = ('marginale', 'substantielle', 'dominante', 'aucune')


def controle_a7(k, item, precedent=None):
    """A7 : la portée de la contre-observation fixe la force. Substantielle : F → f (f → rejet) ;
    dominante : rejet. La force notée est la force après A7 ; `force_initiale` dit d'où elle vient.
    `precedent` = (force à l'état précédent, force_initiale de son dernier enregistrement) si le mot
    était déjà présent, None s'il est nouveau : `force_initiale: "F"` sur un mot qui persiste n'est
    admissible que s'il était F, ou déjà rétrogradé depuis F, à l'état précédent."""
    po = item.get('portee'); fi = item.get('force_initiale'); err = []
    if po not in PORTEES:
        return [f'{k} : portee requise parmi {", ".join(PORTEES)} (A7)']
    if fi is not None and (fi != 'F' or po != 'substantielle'):
        err.append(f'{k} : force_initiale "F" seulement avec une portée substantielle (A7)')
    if po == 'dominante':
        err.append(f'{k} : contre-observation dominante → mot rejeté, ne pas le coder (A7)')
    if po == 'substantielle':
        if item.get('intensite') != 'f':
            err.append(f'{k} : contre-observation substantielle → noter f et force_initiale "F" (A7)')
        elif fi != 'F':
            err.append(f'{k} : substantielle sur un mot lu f → rejet ; si la lecture était F avant A7, déclarer force_initiale "F" (A7)')
        elif precedent is not None and precedent[0] != 'F' and precedent[1] != 'F':
            err.append(f'{k} : force_initiale "F" contredite par l’état précédent (f sans origine F) → rejet (A7)')
    return err


def incompatibles():
    """Paires incompatibles lues dans `antagonismes.md` §3 (relation symétrique)."""
    texte_ = (RACINE/'references'/'antagonismes.md').read_text(encoding='utf-8')
    sec = texte_.split('## 3.', 1)[1].split('\n## ', 1)[0]
    out = set()
    for a_, b_ in re.findall(r'^\| ([^|↮]+?) ↮ ([^|]+?) \|', sec, re.M):
        out.add(frozenset((carte_id(a_), carte_id(b_))))
    exiger(out, 'antagonismes.md §3 : aucune paire incompatible lue')
    return out


def norm_objet(x):
    return ' '.join(unicodedata.normalize('NFC', x).lower().split())


def erreurs_objets(objets, liaisons, incomp):
    """G6 : paire incompatible sur le même objet → rejet ; indépendance exige des objets distincts."""
    err = []; cles = sorted(objets)
    for i, a_ in enumerate(cles):
        for b_ in cles[i+1:]:
            if frozenset((a_.split('@')[0], b_.split('@')[0])) in incomp and norm_objet(objets[a_]) == norm_objet(objets[b_]):
                err.append(f'{a_} et {b_} : paire incompatible sur le même objet « {objets[a_]} » ; rejeter un des ancrages (G6)')
    for a_, t, b_ in liaisons:
        if t == 'indépendance' and a_ in objets and b_ in objets and norm_objet(objets[a_]) == norm_objet(objets[b_]):
            err.append(f'{a_} —indépendance→ {b_} : objets identiques ; indépendance exige des objets distincts (G6)')
    return err


def marqueur_local(ab, strate):
    f = os.path.join(RACINE, "references", "equivalences", f"strate-{int(strate):02d}.md")
    if not os.path.exists(f):
        return None
    for l in open(f, encoding="utf-8"):
        cells = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(cells) == 5 and cells[0] not in ("Carte", "---"):
            try:
                if carte_id(cells[0]) == ab:
                    return cells[1], cells[2], cells[3]
            except ValueError:
                pass
    return None



def _betacf(a, b, x):
    qab, qap, qam = a + b, a + 1, a - 1
    c, d = 1.0, 1 - qab * x / qap
    d = 1 / (d if abs(d) > 1e-30 else 1e-30)
    h = d
    for m in range(1, 300):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1 + aa * d; d = 1 / (d if abs(d) > 1e-30 else 1e-30)
        c = 1 + aa / c; c = c if abs(c) > 1e-30 else 1e-30
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1 + aa * d; d = 1 / (d if abs(d) > 1e-30 else 1e-30)
        c = 1 + aa / c; c = c if abs(c) > 1e-30 else 1e-30
        dl = d * c
        h *= dl
        if abs(dl - 1) < 1e-12:
            break
    return h



def ibeta(a, b, x):
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    lb = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1 - x)
    if x < (a + 1) / (a + b + 2):
        return math.exp(lb) * _betacf(a, b, x) / a
    return 1 - math.exp(lb) * _betacf(b, a, 1 - x) / b



def beta_quantile(a, b, q):
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if ibeta(a, b, mid) < q:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2



def forces(etat):
    return {cle(m): m["i"] for m in etat["mots"]}



def issue_evenement(typ, cible, a, b):
    """(transition éligible, événement réalisé) pour une transition a → b."""
    fa, fb = forces(a), forces(b)
    if typ == "apparait":
        return cible not in fa, cible in fb
    if typ == "persiste":
        return cible in fa, cible in fb
    if typ == "disparait":
        return cible in fa, cible not in fb
    if typ == "renforce":
        return fa.get(cible) == "f", fb.get(cible) == "F"
    if typ == "affaiblit":
        return fa.get(cible) == "F", fb.get(cible) == "f"
    raise ValueError(typ)



def sources_de(etat, cible, liaisons, bouge, manque):
    c, s = cible.split("@")
    s = int(s)
    transferts = {(a.split("@")[1], b.split("@")[1]) for a, t, b in liaisons if t == "transfert"}
    src = []
    for m in etat["mots"]:
        I = P["matrice"].get(m["c"], {}).get(c)
        note = "même strate"
        if m["s"] != s:
            spec = P["autre_strate"].get(m["c"], {}).get(c)
            if spec:
                I, note = spec, "autre strate, propagation documentée"
            elif (str(m["s"]), str(s)) in transferts:
                note = "autre strate, transfert ancré"
            elif I:
                I, note = DEGRADE[I], "autre strate, abaissée d'un cran"
        if I:
            lam = P["lambda"][I] * (P["multiplicateur_bouge"] if cle(m) in bouge else 1)
            src.append({"mot": cle(m), "intensite": I, "lambda": lam, "note": note})
    if cible in manque:
        src.append({"mot": "position manque", "intensite": "M", "lambda": P["lambda"]["M"], "note": "G4"})
    # redondance : sources liées par inclusion, renforcement ou transfert → on garde la plus forte
    groupes = {x["mot"]: x["mot"] for x in src}

    def racine(x):
        while groupes[x] != x:
            x = groupes[x]
        return x
    for a, t, b in liaisons:
        if t in ("inclusion", "renforcement", "transfert") and a in groupes and b in groupes:
            groupes[racine(a)] = racine(b)
    garde = {}
    for x in src:
        r = racine(x["mot"])
        if r not in garde or x["lambda"] > garde[r]["lambda"]:
            garde[r] = x
    ecartees = [x for x in src if x not in garde.values()]
    return list(garde.values()), ecartees



def jaccard(a, b):
    return len(a & b) / len(a | b) if a | b else 1.0



def appliquer(etat, typ, k):
    mots = [m for m in etat["mots"] if cle(m) != k]
    if typ == "apparait":
        c, s = k.split("@")
        mots.append({"c": c, "s": int(s), "i": "f", "q": []})
    return {"date": etat["date"], "fenetre": etat["fenetre"], "mots": mots}



def texte(etat):
    if not etat["mots"]:
        return "∅"
    return " + ".join(f"{NOMS[m['c']]}@{m['s']}[{m['i']}]" for m in sorted(etat["mots"], key=cle))


# ───────────────────────── données et calendrier ─────────────────────────

def exiger(condition, message):
    if not condition:
        raise ValueError(message)


def texte_requis(x, champ):
    exiger(isinstance(x, str) and bool(x.strip()) and x.strip() not in ('…', '...', 'À FOURNIR', 'à fournir'),
           f'{champ} : texte renseigné requis')
    return x


def proba(x, champ='probabilité'):
    exiger(type(x) in (int, float) and math.isfinite(x) and 0 <= x <= 1,
           f'{champ} : nombre fini entre 0 et 1 requis')
    return float(x)


def date_iso(s):
    exiger(isinstance(s, str) and re.fullmatch(r'\d{4}-\d{2}(?:-\d{2})?', s), f'date invalide : {s!r}')
    try:
        return datetime.date.fromisoformat(s + '-01' if len(s) == 7 else s)
    except ValueError:
        raise ValueError(f'date calendaire invalide : {s!r}') from None


def jour(s):
    return date_iso(s).toordinal()


def duree_jours(fenetre):
    exiger(isinstance(fenetre, str) and re.fullmatch(r'[1-9]\d* (jours?|semaines?|mois|ans?)', fenetre),
           f'fenêtre strictement positive requise : {fenetre!r}')
    n, u = fenetre.split()
    return int(n) * UNITES[u]


def fin_fenetre(date, fenetre, pas=1):
    d = date_iso(date); duree_jours(fenetre)
    exiger(type(pas) is int and 1 <= pas <= P['pas_max'], f'pas : entier de 1 à {P["pas_max"]}')
    n, u = fenetre.split(); n = int(n) * pas
    if u in ('mois', 'an', 'ans'):
        n *= 12 if u != 'mois' else 1
        total = d.year * 12 + d.month - 1 + n
        y, month = divmod(total, 12); month += 1
        return datetime.date(y, month, min(d.day, calendar.monthrange(y, month)[1]))
    return d + datetime.timedelta(days=n * (7 if u.startswith('semaine') else 1))


def meme_fenetre(a, b):
    return abs(duree_jours(a) - duree_jours(b)) < 0.01


def lire_etat(texte):
    exiger(isinstance(texte, str), 'état : texte requis')
    m = ETAT_RE.fullmatch(texte.strip())
    exiger(m is not None, f'état mal formé : {texte!r}')
    date_iso(m['d']); duree_jours(m['f'])
    mots = []
    if m['corps'] != '∅':
        for brut in m['corps'].split(' + '):
            mm = MOT_RE.fullmatch(brut.strip())
            exiger(mm is not None, f'mot mal formé : {brut!r}')
            mots.append({'c': carte_id(mm['c']), 's': int(mm['s']), 'i': mm['i'], 'q': re.findall(r'\{([^}]+)\}', mm['q'])})
    e = {'date': m['d'], 'fenetre': m['f'], 'mots': mots}
    errors = erreurs_g6(e)
    exiger(not errors, '; '.join(errors))
    return e


def cle_valide(s):
    k = lire_cle(s); st = int(k.split('@')[1])
    exiger(1 <= st <= NS, f'strate hors de 1–{NS} : {s}')
    return k


def lire_texte(chemin, quoi):
    """Lit un fichier texte UTF-8 avec un message en français pour chaque échec prévisible."""
    texte_=str(chemin)
    exiger(not texte_.lstrip().startswith(('{','[')), f'{quoi} : chemin de fichier attendu, pas du JSON en ligne (écrire le JSON dans un fichier)')
    try:
        return Path(chemin).read_text(encoding='utf-8')
    except FileNotFoundError:
        raise ValueError(f'{quoi} : fichier introuvable — {texte_}') from None
    except IsADirectoryError:
        raise ValueError(f'{quoi} : un dossier a été donné, un fichier est attendu — {texte_}') from None
    except UnicodeDecodeError:
        raise ValueError(f'{quoi} : fichier non textuel ou non UTF-8 — {texte_}') from None
    except PermissionError:
        raise ValueError(f'{quoi} : lecture refusée — {texte_}') from None


def lire_json(chemin, quoi):
    try:
        return json.loads(lire_texte(chemin, quoi), parse_constant=lambda v: (_ for _ in ()).throw(ValueError(v)))
    except json.JSONDecodeError as e:
        raise ValueError(f'{quoi} : JSON invalide ligne {e.lineno}, colonne {e.colno} — {chemin}') from None


def charger(chemin):
    if not chemin:
        return []
    out = []
    for n, line in enumerate(lire_texte(chemin, 'fichier JSONL').splitlines(), 1):
        if line.strip():
            try:
                x = json.loads(line, parse_constant=lambda v: (_ for _ in ()).throw(ValueError(v)))
                exiger(isinstance(x, dict), 'objet JSON requis')
                out.append(x)
            except (ValueError, TypeError) as e:
                raise ValueError(f'{chemin}:{n} : {e}') from None
    return out


def usage_attendu(cid):
    return 'test' if hashlib.sha256(cid.encode()).hexdigest()[0] in P['partage_test'] else 'apprentissage'


def empreinte(x):
    return hashlib.sha256(json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def empreinte_prevision(prediction):
    # A publication receipt can be added later without changing the frozen substantive forecast.
    return empreinte({k:v for k,v in prediction.items() if k != 'preuve_prepublication'})


def fichier_sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def transitions(cas):
    seq = cas['sequence'] + [cas['issue']]
    return [(cas['id'], lire_etat(a['etat']), lire_etat(b['etat'])) for a, b in zip(seq, seq[1:])]


def disponible(cas, a, b, asof):
    # A transition cannot be used before both the outcome and its evidence were available.
    states = cas['sequence'] + [cas['issue']]
    sa = next(x for x in states if x['date'] == a['date'])
    sb = next(x for x in states if x['date'] == b['date'])
    return max(jour(a['date']), jour(b['date']), jour(sa['disponible_le']), jour(sb['disponible_le'])) <= jour(asof)


def base_active(base, asof, demo=False):
    return [c for c in base if c.get('statut_donnees') == 'actif' and c.get('usage') == 'apprentissage'
            and (demo or not c.get('fictif')) and any(disponible(c, a, b, asof) for _, a, b in transitions(c))]


def mode_solo(base, strate=None):
    lot = [c for c in base if strate is None or strate in c.get('strates', [])]
    doubles = [c for c in lot if len(set(c['codage']['codeurs'])) >= 2 and c['codage'].get('independants') is True
               and c['codage'].get('au_moins_un_humain') is True]
    return not lot or len(doubles) < P['double_codage_min_cas'] or len(doubles)/len(lot) < P['double_codage_part']


def lire_liaisons(liste, etat=None):
    types = {'echo':'écho', 'écho':'écho', 'independance':'indépendance', 'indépendance':'indépendance',
             **{x:x for x in ['transfert','conflit','renforcement','inclusion','appui','reproduction','tension']}}
    out = []
    for raw in liste or []:
        exiger(isinstance(raw, str), 'liaison : texte requis')
        p = raw.split(); exiger(len(p) == 3, f'liaison mal formée : {raw}')
        a, t, b = p; t = t.strip('—-→>')
        exiger(t in types, f'liaison inconnue : {t}')
        a, b, t = cle_valide(a), cle_valide(b), types[t]
        exiger(a != b, 'liaison réflexive interdite')
        same = a.split('@')[1] == b.split('@')[1]
        exiger((same and t not in ('transfert','écho')) or (not same and t in ('transfert','écho','conflit')),
               f'liaison incompatible avec ses strates : {raw}')
        if etat is not None:
            exiger(a in forces(etat) and b in forces(etat), f'liaison vers un mot absent : {raw}')
        out.append((a,t,b))
    exiger(len(out) == len(set(out)), 'liaisons dupliquées')
    return out


def valider_base(base):
    ids = set(); stat = statuts(); archive = 0; propositions = 0; incomp = incompatibles()
    for c in base:
        cid = texte_requis(c.get('id'), 'id')
        exiger(cid not in ids, f'identifiant en double : {cid}'); ids.add(cid)
        exiger(re.fullmatch(r'C-\d{4}-S(?:0[1-9]|[1-9]\d)', cid) is not None or c.get('id_legacy') is True,
               f'{cid} : identifiant C-NNNN-SNN requis ; ancien id seulement avec id_legacy=true')
        for field in ('version_regles','titre','fenetre'):
            texte_requis(c.get(field), f'{cid}.{field}')
        duree_jours(c['fenetre'])
        exiger(type(c.get('sans_evenement')) is bool and type(c.get('fictif')) is bool, f'{cid} : booléens requis')
        exiger(c.get('usage') == usage_attendu(cid), f'{cid} : partage apprentissage/test incorrect')
        strata = c.get('strates')
        exiger(isinstance(strata,list) and bool(strata) and all(type(s) is int and 1<=s<=NS for s in strata)
               and len(set(strata)) == len(strata), f'{cid} : strates invalides')
        exiger(c.get('statut_donnees') in ('actif','proposition','archive_a_revoir'), f'{cid} : statut_donnees requis (actif, proposition ou archive_a_revoir)')
        exiger(isinstance(c.get('sequence'),list) and c['sequence'] and isinstance(c.get('issue'),dict), f'{cid} : séquence et issue requises')
        states = c['sequence']+[c['issue']]
        exiger(all(isinstance(x,dict) for x in states), f'{cid} : chaque état de la séquence et l’issue doivent être des objets JSON')
        if c['statut_donnees'] == 'archive_a_revoir':
            texte_requis(c.get('motif_archive'), f'{cid}.motif_archive')
            for x in states:
                lire_etat(x['etat']); date_iso(x['date'])
            archive += 1
            continue # Conserved evidence, never an eligible training or validation observation.
        # Même version mineure : un correctif (0.4.x) ne force pas à recoder, puisque le validateur applique
        # de toute façon les règles courantes à chaque fiche ; un changement mineur (0.5) l'exige.
        exiger(c['version_regles'].split('.')[:2] == P['version'].split('.')[:2], f'{cid} : recodage requis pour cette version')
        coding = c.get('codage')
        exiger(isinstance(coding,dict) and coding.get('mode') in ('manuel','declenche'), f'{cid} : mode de codage requis')
        coders = coding.get('codeurs')
        exiger(isinstance(coders,list) and bool(coders) and all(isinstance(x,str) and x.strip() for x in coders)
               and len(set(coders))==len(coders), f'{cid} : codeurs distincts requis')
        for flag in ('independants','au_moins_un_humain'):
            exiger(coding.get(flag) is None or type(coding[flag]) is bool, f'{cid} : codage.{flag} doit être true ou false')
        if len(coders) >= 2:
            exiger(coding.get('independants') is True and coding.get('au_moins_un_humain') is True,
                   f'{cid} : double codage indépendant avec au moins un humain requis')
        if coding['mode']=='declenche':
            texte_requis(coding.get('regle_declenchement'), f'{cid}.regle_declenchement')
        if not c['fictif']:
            if c['statut_donnees']=='proposition':
                # Recodage complet, contrôlé comme un cas actif, en attente de la vérification humaine des
                # sources ; exclu des calculs (base_active ne retient que « actif »).
                texte_requis(c.get('motif_proposition'), f'{cid}.motif_proposition')
                exiger(c.get('sources_verifiees') is False, f'{cid} : une proposition porte sources_verifiees=false ; une fois les sources lues, passer en actif')
                propositions += 1
            else:
                exiger(c.get('sources_verifiees') is True, f'{cid} : sources non vérifiées ; passer en proposition ou archiver en attendant')
        observed = set(); prev=None; objets = {}; origine_f = {}
        for ix,x in enumerate(states):
            e = lire_etat(x.get('etat')); date_iso(x.get('date'))
            exiger(e['date']==x['date'], f'{cid} : date de fiche différente de celle de l’état')
            exiger(meme_fenetre(e['fenetre'],c['fenetre']), f'{cid} : fenêtres différentes')
            date_iso(x.get('disponible_le'))
            exiger(jour(x['disponible_le'])>=jour(x['date']), f'{cid} : disponibilité antérieure à l’observation')
            if prev:
                exiger(date_iso(e['date']) == fin_fenetre(prev['date'],c['fenetre']), f'{cid} : écart des dates différent de la fenêtre')
            fm=forces(e); observed.update(m['s'] for m in e['mots'])
            expected=set(fm) if prev is None else (set(fm)-set(forces(prev))) | forces_changees(prev,e)
            docs=x.get('mots','ABSENT')
            if not expected:
                exiger(docs is None or (isinstance(docs,list) and bool(docs)), f'{cid} : mots=null si aucun changement, [] interdit')
            else:
                exiger(isinstance(docs,list) and bool(docs), f'{cid} : documentation des mots requise')
            documented=set()
            for item in docs or []:
                exiger(isinstance(item,dict), f'{cid} : mot documenté invalide')
                k=cle_valide(f"{item.get('carte')}@{item.get('strate')}")
                exiger(k not in documented and k in fm, f'{cid} : mot documenté absent ou dupliqué : {k}'); documented.add(k)
                exiger(stat.get((k.split('@')[0],int(k.split('@')[1])))!='Hors domaine', f'{cid} : {k} est Hors domaine : aucun ancrage possible dans cette strate (A3)')
                exiger(item.get('intensite')==fm[k], f'{cid} : force contradictoire pour {k}')
                for field in ('fait','source','contre_observation','objet'):
                    texte_requis(item.get(field), f'{cid}.{k}.{field}')
                pr=None if prev is None or k not in forces(prev) else (forces(prev)[k], origine_f.get(k))
                errs=controle_a7(k,item,pr); exiger(not errs, f'{cid} : '+' ; '.join(errs))
                if fm[k]=='F':
                    # A6 : F qualifie la lecture (fait précis, voisines tranchées), pas la bibliographie (A3).
                    texte_requis(item.get('a6'), f'{cid}.{k}.a6')
                    if not c['fictif']:
                        errs=controle_a6(k,item['a6']); exiger(not errs, f'{cid} : '+' ; '.join(errs))
                    ab,s=k.split('@')
                    exiger(stat.get((ab,int(s)))!='Vide', f'{cid} : F impossible sur un équivalent Vide {k} (A3)')
            exiger(expected <= documented, f'{cid} : mots nouveaux ou modifiés non documentés {sorted(expected-documented)}')
            removed=set(forces(prev))-set(fm) if prev else set()
            retrait=x.get('retraits',[])
            exiger(isinstance(retrait,list), f'{cid} : retraits doit être une liste')
            rd=set()
            for item in retrait:
                exiger(isinstance(item,dict) and isinstance(item.get('mot'),str), f'{cid} : retrait = objet avec "mot" (texte), "fait", "source"')
                k=cle_valide(item['mot']); exiger(k not in rd, f'{cid} : retrait dupliqué');rd.add(k)
                texte_requis(item.get('fait'),'fait de retrait');texte_requis(item.get('source'),'source de retrait')
            exiger(rd==removed, f'{cid} : retraits incohérents')
            # Objets courants : documentés à l'apparition, conservés tant que le mot persiste.
            objets={k:v for k,v in objets.items() if k in fm}
            origine_f={k:v for k,v in origine_f.items() if k in fm}
            for item in docs or []:
                origine_f[cle_valide(f"{item.get('carte')}@{item.get('strate')}")]=item.get('force_initiale')
            for item in docs or []:
                objets[cle_valide(f"{item.get('carte')}@{item.get('strate')}")]=item['objet']
            exiger(isinstance(x.get('liaisons',[]),list), f'{cid} : liaisons doit être une liste (vide si aucune)')
            links=lire_liaisons(x.get('liaisons',[]),e)
            errs=erreurs_objets(objets,links,incomp); exiger(not errs, f'{cid} : '+' ; '.join(errs))
            if links:
                facts=x.get('preuves_liaisons')
                exiger(isinstance(facts,list) and len(facts)==len(links), f'{cid} : preuves de liaisons requises')
                for fact in facts: texte_requis(fact,'preuve de liaison')
            qkeys={cle(m) for m in e['mots'] if m['q']}
            for k in qkeys:
                texte_requis(x.get('preuves_qualificatifs',{}).get(k), f'{cid}.{k} : ligne Q')
            pos=x.get('positions')
            if pos is not None:
                exiger(isinstance(pos,dict) and len(fm)>=3, f'{cid} : positions avec au moins trois mots')
                for label,k in pos.items():
                    exiger(label in ('tient','bouge','manque'), f'{cid} : position inconnue')
                    kk=cle_valide(k)
                    exiger((kk not in fm) if label=='manque' else (kk in fm), f'{cid} : position incompatible')
                    if label=='tient': exiger(fm[kk]=='F', f'{cid} : tient exige F')
                texte_requis(x.get('preuve_positions'), f'{cid} : preuve des positions')
            prev=e
        exiger(observed<=set(strata), f'{cid} : strate d’état absente de la fiche')
        if c['sans_evenement']:
            # B4 : « rien ne s'est produit » — aucune apparition, disparition ni changement de force.
            etats_=[lire_etat(x['etat']) for x in states]
            exiger(all(forces(a)==forces(b) for a,b in zip(etats_,etats_[1:])), f'{cid} : sans_evenement=true alors que la structure change (B4)')
    return {'cas':len(base),'actifs':len(base)-archive-propositions,'propositions':propositions,'archives_exclues':archive}


def valider(chemin):
    result=valider_base(charger(chemin))
    print(f"{result['cas']} cas · {result['actifs']} actifs recevables · {result['propositions']} propositions conformes, sources à vérifier"
          f" · {result['archives_exclues']} archives à revoir ; propositions et archives exclues des calculs")
    print('Contrôle structurel seulement : ne certifie ni la vérité des sources ni le jugement du codeur.')
    return True

# ───────────────────────── prévisions conditionnelles ─────────────────────────

def a_l_echelle(p, fenetre):
    return -math.expm1(math.log1p(-proba(p)) * duree_jours(fenetre)/P['fenetre_reference_jours']) if p<1 else 1.


def odds_module(f, lr):
    proba(f);exiger(math.isfinite(lr) and lr>0,'multiplicateur strictement positif requis')
    if f in (0.,1.): return f
    return f*lr/(1-f+f*lr)


def refs_valider(refs, fenetre, asof):
    exiger(isinstance(refs,dict),'références : objet indexé par événement requis')
    for event,r in refs.items():
        exiger(isinstance(r,dict),f'{event} : référence invalide')
        proba(r.get('frequence'),event)
        for k in ('source','definition','periode','fenetre','disponible_le'):
            texte_requis(r.get(k),f'{event}.{k}')
        exiger(meme_fenetre(r['fenetre'],fenetre), f'{event} : référence d’une autre fenêtre')
        exiger(jour(r['disponible_le'])<=jour(asof),f'{event} : référence indisponible à la date de prévision')
        key,typ=event.split(' ',1);cle_valide(key)
        exiger(typ in ('apparait','persiste','disparait','hausse|persiste','transformation|persiste'),f'{event} : type de référence inconnu')
    return refs


def reference(refs, cible, typ):
    r=refs.get(cible+' '+typ)
    return r['frequence'] if r else None


def echantillon(base, typ, cible, fenetre, asof):
    s=int(cible.split('@')[1]);out=[]
    for c in base:
        if s not in c['strates'] or not meme_fenetre(c['fenetre'],fenetre): continue
        for cid,a,b in transitions(c):
            if not disponible(c,a,b,asof): continue
            ok,hit=issue_evenement(typ,cible,a,b)
            if ok: out.append((cid,a,b,bool(hit),c['sans_evenement']))
    return out


def ponderer(trans, asof, emprunt=False):
    counts=defaultdict(int)
    for t in trans: counts[t[0]]+=1
    out=[]
    for cid,a,b,hit,sans in trans:
        age=max(0,(jour(asof)-jour(b['date']))/365.25)
        # A case contributes at most one effective observation, even if it has many transitions.
        w=(.5**(age/P['demi_vie_ans'])) / counts[cid]
        if emprunt: w*=P['w_emprunt']
        out.append({'id':cid,'debut':a['date'],'fin':b['date'],'poids':w,'issue':int(hit),'sans_evenement':sans})
    return out


def frequence_de_base(base, typ, cible, fenetre, asof, ref):
    samples=ponderer(echantillon(base,typ,cible,fenetre,asof),asof)
    n=sum(x['poids'] for x in samples); hit=sum(x['poids']*x['issue'] for x in samples)
    c=len({x['id'] for x in samples})
    value=(hit+P['k0_frequence']*ref)/(n+P['k0_frequence'])
    return value,c,n


def apriori(etat,typ,cible,base,liaisons=(),bouge=(),manque=(),refs=None,ctr_materielle=(),asof=None,sans_cartes=False):
    refs=refs or {}; asof=asof or etat['date'];c,s=cible.split('@');fen=etat['fenetre']
    inert=P['inertie_contrainte_materielle'] if c=='CTR' and s in ctr_materielle else P['inertie'][c]
    inert=inert**(duree_jours(fen)/P['fenetre_reference_jours'])
    if cible in bouge and not sans_cartes: inert=inert**P['multiplicateur_bouge']
    external=reference(refs,cible,typ)
    if external is None and typ in ('persiste','disparait'):
        comp=reference(refs,cible,'disparait' if typ=='persiste' else 'persiste')
        external=None if comp is None else 1-comp
    default=a_l_echelle(P['f_defaut'],fen) if typ=='apparait' else (inert if typ=='persiste' else 1-inert)
    ref=default if external is None else external
    f,cnt,neff=frequence_de_base(base,typ,cible,fen,asof,ref)
    anchored=external is not None or neff>=P['n_min_frequence']
    src,removed=sources_de(etat,cible,liaisons,bouge,manque) if typ=='apparait' and not sans_cartes else ([],[])
    lr=math.prod(x['lambda'] for x in src)
    capped=lr>P['plafond_LR'];lr=min(lr,P['plafond_LR'])
    p=odds_module(f,lr)
    # Exact externally supplied boundaries are supported; never manufacture a beta law with zero parameters.
    if 0<p<1: p=min(p,P['plafond_p0'])
    return {'p0':proba(p),'f_base':f if anchored else None,'reference_interne':f,'ancrage':anchored,
            'reference_externe':external,'cas_reference':cnt,'effectif_reference':neff,'LR':lr,'LR_plafonne':capped,
            'sources':src,'ecartees':removed,'inertie':inert}


def intervalle_beta(nE,nA,p0):
    a=nE+P['k']*p0;b=nA-nE+P['k']*(1-p0)
    if nA<=0 or a<=0 or b<=0: return None
    q=(1-P['intervalle'])/2
    return [proba(beta_quantile(a,b,q)),proba(beta_quantile(a,b,1-q))]


def calculer(etat,typ,cible,base,liaisons=(),bouge=(),manque=(),refs=None,ctr_materielle=(),asof=None,sans_cartes=False,**unused):
    exiger(typ in ('apparait','persiste','disparait'),'type non prévisionnel : F/f mesure la confiance, pas une intensité physique')
    asof=asof or etat['date']; date_iso(asof);cible=cle_valide(cible)
    fm=forces(etat)
    exiger((cible not in fm) if typ=='apparait' else (cible in fm),
           f'{cible} déjà présent dans l’état : « apparaît » est impossible. Un mot par carte et par strate (G6) : '
           'si le mot présent ne remplit pas vraiment le marqueur local, le retirer de l’état ; sinon la '
           'question porte sur sa persistance ou sa disparition' if typ=='apparait' else
           f'{cible} absent de l’état : seul « apparaît » est possible')
    exiger(not hors_domaine(cible), f'{cible} : carte Hors domaine dans cette strate, aucun événement à prévoir (A3)')
    ap=apriori(etat,typ,cible,base,liaisons,bouge,manque,refs,ctr_materielle,asof,sans_cartes)
    allkeys=set(fm);strong={k for k,v in fm.items() if v=='F'}
    sourcekeys={x['mot'] for x in ap['sources'] if '@' in x['mot']}
    if typ!='apparait': sourcekeys={cible}
    levels={'H1':[],'H1.5':[],'H2':[]}
    for t in echantillon(base,typ,cible,etat['fenetre'],asof):
        fa=forces(t[1]);ka=set(fa);sa={k for k,v in fa.items() if v=='F'}
        # H1 is equality of the full, nonempty structural state including qualifiers.
        qa={(cle(m),m['i'],tuple(sorted(m['q']))) for m in t[1]['mots']}
        qe={(cle(m),m['i'],tuple(sorted(m['q']))) for m in etat['mots']}
        if allkeys and qa==qe: levels['H1'].append(t)
        wa={k:(1. if fa[k]=='F' else .5) for k in ka};we={k:(1. if fm[k]=='F' else .5) for k in allkeys}
        union=ka|allkeys
        score=sum(min(wa.get(k,0),we.get(k,0)) for k in union)/sum(max(wa.get(k,0),we.get(k,0)) for k in union) if union else 0
        if ka & allkeys and score>=P['jaccard_H15']: levels['H1.5'].append(t)
        if sourcekeys and sourcekeys<=ka: levels['H2'].append(t)
    counts={h:len({x[0] for x in ts}) for h,ts in levels.items()}
    # Niveau le plus strict qui atteint c_min_rho1 cas distincts ; sinon le plus strict non vide.
    # Raison : H1 ⊆ H1.5, donc « le niveau qui offre le plus de cas » ne retenait jamais H1 sous 30 cas
    # et échangeait la comparabilité contre l'effectif sans le dire.
    h=next((h for h in levels if counts[h]>=P['c_min_rho1']),None)
    if h is None: h=next((h for h in levels if counts[h]>0),'H1')
    hom=[] if sans_cartes else levels[h]; borrowed=False
    if not hom and not sans_cartes and sourcekeys:
        statuses=statuts();target,st=cible.split('@');st=int(st)
        original=sourcekeys|{cible}
        if all(statuses.get((k.split('@')[0],int(k.split('@')[1]))) in ('Attesté','Documenté') for k in original):
            cards={k.split('@')[0] for k in sourcekeys}
            for case in base:
                if not meme_fenetre(case['fenetre'],etat['fenetre']):continue
                for cid,a,b in transitions(case):
                    if not disponible(case,a,b,asof):continue
                    for s in sorted(set(case['strates'])-{st}):
                        if not all(statuses.get((ab,s)) in ('Attesté','Documenté') for ab in cards|{target}):continue
                        if not {f'{ab}@{s}' for ab in cards}<=set(forces(a)):continue
                        ok,hit=issue_evenement(typ,f'{target}@{s}',a,b)
                        if ok:hom.append((cid,a,b,hit,case['sans_evenement']));break
            if hom:h='H3';borrowed=True
    samples=ponderer(hom,asof,borrowed)
    nA=sum(x['poids'] for x in samples);nE=sum(x['poids']*x['issue'] for x in samples);cA=len({x['id'] for x in samples})
    prob=(nE+P['k']*ap['p0'])/(nA+P['k'])
    rho=2 if borrowed and cA>=P['c_min_rho1'] else 0 if cA>=P['seuil_rho0_cas_distincts'] else 1 if cA>=P['c_min_rho1'] else 3 if ap['ancrage'] else 4
    flags=['Modèle expérimental : multiplicateurs hypothétiques, performance prospective non établie.']
    if rho==0 and (mode_solo(base,int(cible.split('@')[1])) or not any(x['sans_evenement'] for x in samples)):
        rho=1;flags.append('ρ0 inaccessible : double codage insuffisant ou aucun cas sans événement.')
    if rho<=1 and samples:
        ordered=sorted(samples,key=lambda x:jour(x['fin']));mid=len(ordered)//2;halves=(ordered[:mid],ordered[mid:])
        if all(len({x['id'] for x in half})>=P['min_transitions_par_moitie'] for half in halves):
            rates=[(sum(x['poids']*x['issue'] for x in half)+.5)/(sum(x['poids'] for x in half)+1) for half in halves]
            if max(rates)/min(rates)>P['ratio_non_stationnarite']:rho=max(1,rho);flags.append('Non-stationnarité : plafond ρ1.')
    if not ap['ancrage']: flags.append('A priori non ancré : aucune référence externe vérifiée fournie et effectif de base insuffisant.')
    if ap['LR_plafonne']:flags.append('Produit des multiplicateurs plafonné.')
    return {'evenement':cible+' '+typ,'p':proba(prob),'intervalle':intervalle_beta(nE,nA,ap['p0']),
            'rho':rho,'homologie':h if hom else None,'nb_cas_par_niveau':counts,'c_A':cA,'n_A':nA,'n_E':nE,
            'a_priori':ap,'comparateur':ap['f_base'],'transitions':samples,'drapeaux':flags,
            'incertitude':'intervalle conditionnel approximatif : un cas pèse au plus une observation ; incertitude de codage et de modèle non intégrée'}


def cumul(a,r,h,q0=0):
    q=q0
    for _ in range(h):q=q*r+(1-q)*a
    return proba(q)


def horizon_result(etat,typ,cible,base,opts,h,semantique):
    r=calculer(etat,typ,cible,base,**opts)
    exiger(type(h) is int and 1 <= h <= P['pas_max'], 'nombre de pas invalide')
    allowed = ('presence','continue') if typ == 'persiste' else ('presence','au-moins-une-fois')
    exiger(semantique in allowed, 'sémantique incompatible avec cet événement')
    if h==1:return dict(r,semantique=semantique,pas=1)
    present=cible in forces(etat)
    ea=appliquer(etat,'disparait',cible);ep=appliquer(ea,'apparait',cible)
    ea['date']=ep['date']=etat['date']
    ra=calculer(ea,'apparait',cible,base,**opts);rp=calculer(ep,'persiste',cible,base,**opts)
    def f(a,p):
        if typ=='apparait':
            exiger(semantique in ('presence','au-moins-une-fois'),'apparition : presence ou au-moins-une-fois')
            return cumul(a,p,h) if semantique=='presence' else 1-(1-a)**h
        if typ=='persiste':
            exiger(semantique in ('presence','continue'),'persistance : presence ou continue')
            return cumul(a,p,h,1) if semantique=='presence' else p**h
        exiger(semantique in ('presence','au-moins-une-fois'),'disparition : absence finale (presence) ou au-moins-une-fois')
        return 1-cumul(a,p,h,1) if semantique=='presence' else 1-p**h
    used=[ra,rp] if semantique=='presence' else [ra] if typ=='apparait' else [rp]
    baseline=f(ra['comparateur'],rp['comparateur']) if ra['comparateur'] is not None and rp['comparateur'] is not None else None
    if semantique!='presence':
        b=used[0]['comparateur'];baseline=None if b is None else (1-(1-b)**h if typ=='apparait' else b**h if typ=='persiste' else 1-b**h)
    r.update(p=proba(f(ra['p'],rp['p'])),comparateur=baseline,rho=max(x['rho'] for x in used),intervalle=None,
             pas=h,semantique=semantique,composantes={'apparition':ra,'persistance':rp})
    r['drapeaux']+=['Sources et probabilités supposées fixes sur l’horizon. Intervalle multi-pas non estimé : aucune propagation partielle de bornes.']
    return r


def compose(etat,typ,cible,base,opts,resolution):
    exiger(cible in forces(etat),'événement composé : mot absent')
    exiger(isinstance(resolution,dict),'événement composé : --resolution JSON obligatoire')
    for k in ('source','critere','seuil','marqueur','objet'):
        texte_requis(resolution.get(k),'resolution.'+k)
    if typ=='intensifie':
        for k in ('grandeur','unite','comparaison'):texte_requis(resolution.get(k),'resolution.'+k)
        values=resolution.get('observations')
        exiger(isinstance(values,list) and len(values)>=2,'intensification : deux observations datées au minimum')
        dates=[]
        for v in values:
            exiger(isinstance(v,dict) and type(v.get('valeur')) in (int,float) and math.isfinite(v['valeur']),'mesure numérique finie requise')
            d=jour(v.get('date'));exiger(d<=jour(opts['asof']),'observation de résolution postérieure à la date de prévision');dates.append(d)
        exiger(dates==sorted(set(dates)),'observations dans l’ordre, dates distinctes')
        key='hausse|persiste'
    else:
        exiger(not cible.startswith('TRA@') and 'TRA@'+cible.split('@')[1] not in forces(etat),'transformation déjà présente ou objet TRANSFORMATION')
        key='transformation|persiste'
    rp=calculer(etat,'persiste',cible,base,**opts)
    cond=reference(opts.get('refs',{}),cible,key)
    if cond is None:
        return {'evenement':cible+' '+typ,'p':None,'intervalle':None,'rho':4,'comparateur':None,
                'drapeaux':['Probabilité non estimée : fournir une référence conditionnelle propre à cet objet et à cette fenêtre. Aucun produit de marginales ni 1/3 par défaut.'],
                'composantes':{'persistance':rp},'resolution':resolution}
    return {'evenement':cible+' '+typ,'p':proba(rp['p']*cond),'intervalle':None,'rho':max(3,rp['rho']),
            'comparateur':None if rp['comparateur'] is None else rp['comparateur']*cond,
            'composantes':{'persistance':rp,'conditionnelle':cond},'resolution':resolution,
            'drapeaux':['P(composé)=P(persiste) × P(changement | persiste). Intervalle conjoint non estimé.']}


# ───────────────────────── trajectoires ─────────────────────────

def trajectoires(etat,h,base,opts,strates_sup=()):
    exiger(all(type(s) is int and 1<=s<=NS for s in strates_sup),f'strates supplémentaires hors 1–{NS}')
    branches=[(1.,etat,[],0)];elague=0.;rho_el=0
    for step in range(h):
        new=[]
        for weight,e,path,rho in branches:
            candidates=[];present=set(forces(e))
            # Fixed original evidence cutoff; remove links and positions invalidated by simulated changes.
            op=dict(opts);op['liaisons']=[x for x in opts.get('liaisons',[]) if x[0] in present and x[2] in present]
            op['bouge']=[x for x in opts.get('bouge',[]) if x in present];op['manque']=[x for x in opts.get('manque',[]) if x not in present]
            for k in sorted(present):candidates.append(('disparait',k,calculer(e,'disparait',k,base,**op)))
            for s in sorted({m['s'] for m in e['mots']}|set(strates_sup)):
                for ab in NOMS:
                    k=f'{ab}@{s}'
                    if k not in present and not hors_domaine(k) and sources_de(e,k,op['liaisons'],op['bouge'],op['manque'])[0]:
                        candidates.append(('apparait',k,calculer(e,'apparait',k,base,**op)))
            # This competing-risk kernel is exploratory. Normalization depends on ALL candidates.
            hazards=[-math.log1p(-min(x[2]['p'],1-1e-12)) for x in candidates];H=sum(hazards)
            sq=math.exp(-H);rr=max([rho]+[x[2]['rho'] for x in candidates])
            new.append((weight*sq,e,path+['statu quo'],rr,sq))
            for (t,k,r),haz in zip(candidates,hazards):
                q=(1-sq)*haz/H if H else 0
                new.append((weight*q,appliquer(e,t,k),path+[k+' '+t],rr,q))
        keep=[]
        for x in new:
            if x[4]<P['seuil_affichage']:elague+=x[0];rho_el=max(rho_el,x[3])
            else:keep.append(x)
        keep.sort(key=lambda x:-x[0])
        for x in keep[P['faisceau_max']:]:elague+=x[0];rho_el=max(rho_el,x[3])
        branches=[x[:4] for x in keep[:P['faisceau_max']]]
    merged={}
    for w,e,path,rho in branches:
        sig=json.dumps(sorted((cle(m),m['i'],sorted(m['q'])) for m in e['mots']),ensure_ascii=False)
        if sig not in merged:merged[sig]={'p':0.,'etat':texte(e),'qualificatifs':{cle(m):m['q'] for m in e['mots'] if m['q']},'rho':0,'chemins':[]}
        x=merged[sig];x['p']+=w;x['rho']=max(x['rho'],rho);x['chemins'].append(path)
    shown=sorted([v for v in merged.values() if v['p']>=P['seuil_affichage']],key=lambda x:-x['p'])
    rare=sum(v['p'] for v in merged.values() if v['p']<P['seuil_affichage'])
    total=sum(x['p'] for x in shown)+rare+elague
    exiger(abs(total-1)<1e-8,'perte de masse dans les trajectoires')
    return {'trajectoires':shown,'R1':rare,'R2':elague,'rho_R2':rho_el,'somme':total,
            'drapeaux':['Noyau exploratoire : un seul changement par pas ; calculer fait foi pour un événement isolé.']+
            (['Masse abandonnée > 30 % : distribution non représentative.'] if elague>P['alerte_R2'] else [])}

# ───────────────────────── journal et score ─────────────────────────

def valider_journal(data):
    prev={};scores={};partitions=defaultdict(list)
    for x in data:
        exiger(isinstance(x,dict),'ligne de journal : objet JSON requis')
        typ=x.get('type');exiger(typ in ('prevision','score'),'type de ligne : prevision ou score')
        ident=texte_requis(x.get('id'),'id');date_iso(x.get('date'))
        dest=prev if typ=='prevision' else scores
        exiger(ident not in dest,f'doublon {typ} : {ident}');dest[ident]=x
        if typ=='score':
            exiger('issue' in x,f'{ident} : champ issue requis (0, 1, ou null si non résolue)')
            exiger(x.get('issue') is None or (type(x['issue']) is int and x['issue'] in (0,1)),f'{ident} : issue 0, 1 ou null')
            texte_requis(x.get('preuve'),f'{ident}.preuve');continue
        origine=x.get('origine','moteur')
        exiger(origine in ('moteur','jugement'),f'{ident} : origine « moteur » ou « jugement »')
        if origine=='jugement':
            # Question nominative ou hors alphabet (« qui sera élu ? ») : probabilité humaine, journalisée
            # et scorée à part, jamais mêlée au score du moteur ni à V4.
            for field in ('version_regles','question','evenement','episode_id','refutation'):
                texte_requis(x.get(field),f'{ident}.{field}')
            date_iso(x.get('echeance'));exiger(jour(x['date'])<jour(x['echeance']),f'{ident} : prévision datée à échéance ou après')
            proba(x.get('probabilite'),ident+'.probabilite')
            exiger(type(x.get('rejeu')) is bool and type(x.get('fictif')) is bool,f'{ident} : rejeu et fictif explicites requis')
            res=x.get('resolution');exiger(isinstance(res,dict),f'{ident} : résolution externe requise')
            for field in ('source','critere','seuil'):texte_requis(res.get(field),f'{ident}.resolution.{field}')
            part=x.get('partition');exiger(part is None or (isinstance(part,str) and part.strip()),f'{ident} : partition invalide')
            if part:partitions[part].append(x)
            continue
        for field in ('version_regles','question','evenement','episode_id','indicateur_bascule','refutation','semantique'):
            texte_requis(x.get(field),f'{ident}.{field}')
        date_iso(x.get('echeance')); state = lire_etat(x.get('etat_present'))
        exiger(jour(state['date']) <= jour(x['date']), f'{ident} : état postérieur à la prévision')
        exiger(type(x.get('pas')) is int and 1 <= x['pas'] <= P['pas_max'], f'{ident} : nombre de pas requis')
        exiger(fin_fenetre(state['date'], state['fenetre'], x['pas']) == date_iso(x['echeance']), f'{ident} : échéance incompatible avec état, fenêtre et pas')
        exiger(jour(x['date']) < jour(x['echeance']), f'{ident} : prévision datée à échéance ou après')
        exiger(jour(x['date'])<=jour(x['echeance']),f'{ident} : date après échéance')
        proba(x.get('probabilite'),ident+'.probabilite')
        calc=x.get('calcul')
        if calc is not None:
            # Le calcul figé est la preuve de la probabilité journalisée : ils doivent coïncider.
            exiger(isinstance(calc,dict),f'{ident} : calcul doit être le résultat JSON du moteur')
            if calc.get('p') is not None:
                exiger(type(calc['p']) in (int,float) and abs(calc['p']-x['probabilite'])<1e-12,f'{ident} : probabilite différente du calcul figé')
            if calc.get('rho') is not None:
                exiger(str(x.get('rho'))==f"ρ{calc['rho']}",f'{ident} : rho différent du calcul figé')
        exiger('frequence_de_base' in x,f'{ident} : fréquence de base requise (null si non évaluable)')
        if [int(v) for v in re.findall(r'\d+',x['version_regles'])[:2]]>=[0,5]:
            exiger('p_sans_cartes' in x,f'{ident} : p_sans_cartes requis depuis 0.5 (null pour un composé) : comparateur inertiel')
        if x.get('p_sans_cartes') is not None:proba(x['p_sans_cartes'],ident+'.p_sans_cartes')
        if x['frequence_de_base'] is not None:proba(x['frequence_de_base'],ident+'.frequence_de_base')
        exiger(type(x.get('rejeu')) is bool and type(x.get('fictif')) is bool,f'{ident} : rejeu et fictif explicites requis')
        exiger(re.fullmatch(r'ρ[0-4]',str(x.get('rho',''))) is not None,f'{ident} : rho invalide')
        itv=x.get('intervalle')
        if itv is not None:
            exiger(isinstance(itv,list) and len(itv)==2,f'{ident} : intervalle invalide')
            proba(itv[0]);proba(itv[1]);exiger(itv[0]<=itv[1],f'{ident} : intervalle inversé')
        res=x.get('resolution');exiger(isinstance(res,dict),f'{ident} : résolution externe requise')
        for field in ('source','critere','seuil','marqueur','objet'):texte_requis(res.get(field),f'{ident}.resolution.{field}')
        exiger(type(x.get('resolution_verifiee')) is bool,f'{ident} : contrôle S1 explicite requis')
        part=x.get('partition');exiger(part is None or (isinstance(part,str) and part.strip()),f'{ident} : partition invalide')
        if part:partitions[part].append(x)
        else:
            key,event_type=evenement_lire(x['evenement'])
            exiger(event_type not in ('renforce','affaiblit'),f'{ident} : ancien changement de confiance non prévisionnel')
            present = key in forces(state)
            exiger((not present) if event_type=='apparait' else present, f'{ident} : événement incompatible avec état')
            if event_type in ('transforme','intensifie'):
                exiger(x['pas']==1 and x['semantique']=='compose', f'{ident} : composé à un pas seulement')
            else:
                allowed=('presence','continue') if event_type=='persiste' else ('presence','au-moins-une-fois')
                exiger(x['semantique'] in allowed, f'{ident} : sémantique incompatible')
        for k in ('preuve_prepublication','empreintes'):
            exiger(k in x,f'{ident} : champ {k} requis (null si indisponible)')
        if x['empreintes'] is not None:
            exiger(isinstance(x['empreintes'],dict),f'{ident} : empreintes invalides')
            for key in ('moteur','parametres','base'):
                value=x['empreintes'].get(key)
                exiger(isinstance(value,str) and re.fullmatch(r'[0-9a-f]{64}',value),f'{ident} : SHA-256 {key} requis')
        proof=x['preuve_prepublication']
        if proof is not None:
            exiger(isinstance(proof,dict),f'{ident} : preuve de prépublication invalide')
            for k in ('source','date','empreinte_prevision'):texte_requis(proof.get(k),f'{ident}.preuve_prepublication.{k}')
            exiger(proof['empreinte_prevision']==empreinte_prevision(x), f'{ident} : preuve rattachée à une autre version de la prévision')
            exiger(jour(x['date'])<=jour(proof['date'])<jour(x['echeance']),f'{ident} : prépublication hors délai')
    for ident,s in scores.items():
        exiger(ident in prev,f'score orphelin : {ident}')
        exiger(jour(s['date'])>=jour(prev[ident]['echeance']),f'{ident} : score avant échéance')
    for key,items in partitions.items():
        exiger(len(items)>=2,f'partition {key} : au moins deux issues')
        exiger(len({x['question'] for x in items})==1 and len({x['echeance'] for x in items})==1 and len({x['date'] for x in items})==1
               and len({x['episode_id'] for x in items})==1,f'partition {key} : question, dates et épisode communs requis')
        exiger(len({x['evenement'] for x in items})==len(items),f'partition {key} : issues dupliquées')
        exiger(abs(sum(x['probabilite'] for x in items)-1)<1e-8,f'partition {key} : probabilités ne somment pas à 1')
        exiger(len({x.get('origine','moteur') for x in items})==1,f'partition {key} : origines mêlées (moteur et jugement)')
        fb=[x.get('frequence_de_base') for x in items]
        exiger(all(x is None for x in fb) or (all(x is not None for x in fb) and abs(sum(fb)-1)<1e-8),f'partition {key} : comparateur incomplet ou non normalisé')
        outcomes=[scores.get(x['id'],{}).get('issue') for x in items]
        if all(x is not None for x in outcomes):exiger(sum(outcomes)==1,f'partition {key} : exactement une issue réalisée')
    return prev,scores,partitions


def apport_cartes(units):
    """Brier avec cartes moins Brier sans cartes, sur les questions qui portent p_sans_cartes.
    Négatif : les cartes améliorent le score ; nul : le score ne vient que de l'inertie."""
    v=[x for x in units if x['brier_sans_cartes'] is not None]
    if not v:return None
    d=sum(x['brier']-x['brier_sans_cartes'] for x in v)/len(v)
    return {'questions':len(v),'brier_avec':sum(x['brier'] for x in v)/len(v),'brier_sans':sum(x['brier_sans_cartes'] for x in v)/len(v),
            'difference':d,'lecture':'les cartes améliorent le score' if d<0 else 'les cartes dégradent le score' if d>0 else 'score dû à l’inertie seule'}


def jugements(units):
    """Score des probabilités humaines (origine « jugement »), séparé du moteur : c'est la calibration
    du codeur, que le moteur ne mesure pas. Référence : Brier d'une réponse à 50 %."""
    v=[x for x in units if x['origine']=='jugement']
    if not v:return None
    ref=sum(0.25 if not x['partition'] else (1-1/len(x['ids'])) for x in v)/len(v)
    return {'questions':len(v),'dont_rejeux':sum(x['rejeu'] for x in v),'brier':sum(x['brier'] for x in v)/len(v),
            'brier_reponse_indifferente':ref,'incertitude_annoncee':sum(x['incertitude_annoncee'] for x in v)/len(v)}


def score_result(data):
    prev,scores,partitions=valider_journal(data);units=[];used=set();unresolved=0;missing=0
    groups=list(partitions.values())+[[x] for x in prev.values() if not x.get('partition')]
    for items in groups:
        if any(x['id'] not in scores for x in items):missing+=1;continue
        if any(scores[x['id']]['issue'] is None for x in items):unresolved+=1;continue
        b=sum((x['probabilite']-scores[x['id']]['issue'])**2 for x in items)
        origine=items[0].get('origine','moteur')
        bb=None if any(x.get('frequence_de_base') is None for x in items) else sum((x['frequence_de_base']-scores[x['id']]['issue'])**2 for x in items)
        bsc=None if any(x.get('p_sans_cartes') is None for x in items) else sum((x['p_sans_cartes']-scores[x['id']]['issue'])**2 for x in items)
        verified=all(x.get('preuve_prepublication') is not None and x.get('empreintes') is not None and x.get('resolution_verifiee') for x in items)
        excluded=origine=='jugement' or any(x['rejeu'] or x['fictif'] for x in items) or not verified
        units.append({'ids':[x['id'] for x in items],'episode_id':items[0]['episode_id'],'origine':origine,'rejeu':any(x['rejeu'] for x in items),
                      'brier':b,'brier_base':bb,'brier_sans_cartes':bsc,
                      'hors_V4':excluded,'partition':bool(items[0].get('partition')),
                      'rho':'jugement' if origine=='jugement' else max(x['rho'] for x in items),
                      'cartes':[] if origine=='jugement' else sorted({x['evenement'].split('@')[0] for x in items}),
                      'strate':'jugement' if origine=='jugement' else items[0]['evenement'].split('@')[1].split()[0] if '@' in items[0]['evenement'] and not items[0].get('partition') else 'partition',
                      'incertitude_annoncee':sum(x['probabilite']*(1-x['probabilite']) for x in items)})
    eligible=[x for x in units if not x['hors_V4']];episodes=defaultdict(list)
    for x in eligible:
        if x['brier_base'] is not None:episodes[x['episode_id']].append(x)
    # Equal weight per episode. Ten related forecasts cannot manufacture ten independent cases.
    b=sum(sum(x['brier'] for x in v)/len(v) for v in episodes.values())/len(episodes) if episodes else None
    bb=sum(sum(x['brier_base'] for x in v)/len(v) for v in episodes.values())/len(episodes) if episodes else None
    gain=1-b/bb if bb is not None and bb>0 else None
    status='non encore évalué' if len(episodes)<P['v4_n'] else 'jalon interne atteint — validation externe non établie' if gain is not None and gain>=P['v4_gain'] else 'jalon interne non atteint'
    by={}
    for field in ('rho','strate'):
        groups=defaultdict(list)
        for x in eligible:groups[x[field]].append(x)
        by[field]={k:{'questions':len(v),'episodes':len({x['episode_id'] for x in v}),'brier':sum(x['brier'] for x in v)/len(v)} for k,v in groups.items()}
    bins=defaultdict(list)
    ok_ids={i for u in eligible if not u['partition'] for i in u['ids']}
    for i in ok_ids:
        x=prev[i];bins[min(9,int(x['probabilite']*10))].append((x['probabilite'],scores[i]['issue']))
    calibration={f'{k*10}–{k*10+10}':{'n':len(v),'p_moyenne':sum(x[0] for x in v)/len(v),'frequence':sum(x[1] for x in v)/len(v)} for k,v in sorted(bins.items())}
    return {'questions_resolues':len(units),'questions_eligibles':len(eligible),
            'incertitude_annoncee_moyenne':sum(x['incertitude_annoncee'] for x in units)/len(units) if units else None,
            'apport_des_cartes':apport_cartes([x for x in units if x['origine']=='moteur']),
            'jugements':jugements(units),'questions_hors_V4':len(units)-len(eligible),
            'sans_score':missing,'non_resolues':unresolved,'episodes_comparables':len(episodes),'brier_par_episode':b,
            'brier_base_par_episode':bb,'gain':gain,'statut':status,'par_groupe':by,'calibration':calibration,'details':units,
            'limites':['Prépublication déclarée : authenticité à vérifier humainement.',
                       '50 épisodes et 10 % de gain constituent un jalon interne, pas une preuve statistique.',
                       'p(1-p) décrit la confiance annoncée ; une valeur faible ne démontre pas que le test est inutile.']}


def scorer(path):
    r=score_result(charger(path))
    return json.dumps(r,ensure_ascii=False,indent=2,allow_nan=False)


# ───────────────────────── intégrité et paramètres ─────────────────────────

def parametres_markdown():
    rows=['| Paramètre | Valeur |','|---|---|']
    def visit(prefix,x):
        if isinstance(x,dict):
            for k,v in x.items():visit(prefix+'.'+k if prefix else k,v)
        else:rows.append('| `'+prefix+'` | `'+json.dumps(x,ensure_ascii=False,separators=(',',':'))+'` |')
    visit('',P)
    return '\n'.join(rows)


# Renvois « fichier.md §N » attendus → mot qui doit figurer dans le titre de la section visée.
# L'audit vérifie l'existence ET la pertinence ; un renvoi absent de cette table est signalé.
RENVOIS = {
    ('antagonismes.md','3'):'incompatibilités', ('antagonismes.md','4'):'Tensions',
    ('antagonismes.md','4bis'):'Inclusions', ('antagonismes.md','6'):'même objet',
    ('base-de-cas.md','2'):'Fiche', ('base-de-cas.md','3'):'Coder', ('base-de-cas.md','5'):'Partage',
    ('constitution.md','2'):'principes', ('constitution.md','3'):'risque', ('constitution.md','4'):'couches',
    ('constitution.md','5'):"n'est pas", ('constitution.md','6'):'Données personnelles', ('equivalences.md','3'):'Bilan',
    ('grammaire.md','4'):'liaisons', ('grammaire.md','5'):'Positions', ('grammaire.md','7'):'bonne formation',
    ('graphe.md','2'):'priori', ('graphe.md','2.1'):'Sources', ('graphe.md','2.2'):'Fréquence',
    ('graphe.md','2.3'):'Combinaison', ('graphe.md','3'):'homologues',
    ('protocole.md','H'):'Paramètres', ('simulation.md','2'):'remplissage',
    ('strates.md','2'):'Fiches', ('strates.md','3'):'taxonomie', ('strates.md','4'):'rattachement',
    ('validation.md','1'):'Journal des prévisions', ('validation.md','4'):'Diagnostic',
    ('validation.md','6'):'lacunes', ('validation.md','8'):'aveugle',
}
RENVOI_RE = re.compile(r'`?([a-z\-]+\.md)`?\s*§\s*([0-9]+(?:\.[0-9]+)?(?:bis)?|[A-Z]\b)')


def titre_section(fichier, sec):
    path = RACINE/'SKILL.md' if fichier == 'SKILL.md' else RACINE/'references'/fichier
    if not path.is_file():
        return None
    texte_ = path.read_text(encoding='utf-8')
    niveau = '###' if '.' in sec else '##'
    m = re.search(r'^' + niveau + r' (?:§)?' + re.escape(sec) + r'(?:\.|\s·|\s|$)(.*)$', texte_, re.M)
    return m.group(1).strip() if m else None


def erreurs_renvois(chemins):
    err = []
    for path in chemins:
        for fic, sec in RENVOI_RE.findall(path.read_text(encoding='utf-8')):
            t = titre_section(fic, sec)
            if t is None:
                err.append(f'{path.name} : renvoi {fic} §{sec} vers une section absente')
            elif (fic, sec) not in RENVOIS:
                err.append(f'{path.name} : renvoi {fic} §{sec} non répertorié dans RENVOIS (vérifier, puis l’ajouter)')
            elif RENVOIS[(fic, sec)].lower() not in t.lower():
                err.append(f'{path.name} : renvoi {fic} §{sec} pointe vers « {t} », attendu « {RENVOIS[(fic, sec)]} »')
    return err


def erreurs_statuts():
    """M1 : la répartition des statuts publiée (Bilans, equivalences.md, protocole.md, SKILL.md) est
    recalculée à partir des 16 × NS cellules, jamais crue sur parole."""
    st=statuts();err=[];ordre=('Attesté','Documenté','Proposé','Vide','Hors domaine')
    tot={s:sum(v==s for v in st.values()) for s in ordre}
    for s in range(1,NS+1):
        f=RACINE/'references/equivalences'/f'strate-{s:02}.md';t=f.read_text(encoding='utf-8')
        m=re.search(r'Bilan : (\d+) Documenté, (\d+) Proposé, (\d+) Vide, (\d+) Hors domaine, (\d+) Attesté',t)
        vrai=[sum(v==x for (c,ss),v in st.items() if ss==s) for x in ('Documenté','Proposé','Vide','Hors domaine','Attesté')]
        if not m or [int(x) for x in m.groups()]!=vrai:err.append(f'{f.name} : Bilan ≠ cellules {vrai}')
    eq=(RACINE/'references/equivalences.md').read_text(encoding='utf-8')
    sec3=eq.split('## 3.',1)[1].split('\n## ',1)[0]
    lignes=re.findall(r'^\| (\d+) [^|]+\| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$',sec3,re.M)
    if len(lignes)!=NS:err.append(f'equivalences.md §3 : tableau par strate incomplet ({NS} lignes, 4 statuts)')
    for s,d,pr,v,hd in lignes:
        vrai=[sum(x==y for (c,ss),x in st.items() if ss==int(s)) for y in ('Documenté','Proposé','Vide','Hors domaine')]
        if [int(d),int(pr),int(v),int(hd)]!=vrai:err.append(f'equivalences.md §3, strate {s} : {[d,pr,v,hd]} ≠ {vrai}')
    vides=sorted(f'{c}@{s}' for (c,s),x in st.items() if x=='Vide')
    m=re.search(r'Les (\d+) cases Vides \(carte : strates\) : (.+?)\. ',sec3,re.S)
    if m:
        lus=sorted(f'{carte_id(n)}@{int(x)}' for n,xs in re.findall(r'([A-ZÉÈ·][A-ZÉÈ· ]+?) \(([\d, ]+)\)',m.group(2)) for x in xs.split(','))
        if int(m.group(1))!=len(vides) or lus!=vides:err.append(f'equivalences.md §3 : liste des cases Vides ≠ cellules {vides}')
    else:err.append('equivalences.md §3 : liste des cases Vides absente')
    for f in ('references/equivalences.md','references/protocole.md'):
        for a,d,pr,v,hd in re.findall(r'(\d+) Attesté, (\d+) Documenté, (\d+) Proposé, (\d+) Vide, (\d+) Hors domaine',(RACINE/f).read_text(encoding='utf-8')):
            if [int(a),int(d),int(pr),int(v),int(hd)]!=[tot[x] for x in ordre]:err.append(f'{f} : bilan {a}/{d}/{pr}/{v}/{hd} ≠ {[tot[x] for x in ordre]}')
    for pr,v in re.findall(r'(\d+) Proposé, (\d+) Vide',(RACINE/'SKILL.md').read_text(encoding='utf-8')):
        if [int(pr),int(v)]!=[tot['Proposé'],tot['Vide']]:err.append(f'SKILL.md : {pr} Proposé / {v} Vide ≠ cellules')
    return err


def erreurs_index():
    """M2 : `cartes-index.md` (chargé en premier) recoupe `cartes.md` : définition (première phrase),
    début de la structure mathématique, voisines A6."""
    def norm(x):return ' '.join(x.replace('**','').split()).strip().rstrip('.').strip()
    fiches={}
    for sec in re.split(r'^## ',(RACINE/'references/cartes.md').read_text(encoding='utf-8'),flags=re.M)[1:]:
        try:ab=carte_id(sec.split('\n',1)[0])
        except ValueError:continue
        d=re.search(r'\*\*Définition\*\*\s*:\s*(.+?)(?:\n\n|$)',sec,re.S);s_=re.search(r'\*\*Structure mathématique\*\*\s*:\s*(.+?)(?:\n\n|$)',sec,re.S)
        if d and s_:fiches[ab]=(norm(d.group(1)),norm(s_.group(1)))
    err=[];vus=set();V=voisines()
    for l in (RACINE/'references/cartes-index.md').read_text(encoding='utf-8').splitlines():
        c=[x.strip() for x in l.strip().strip('|').split('|')]
        if len(c)!=5 or c[0] in ('Carte','---'):continue
        ab=carte_id(c[0]);vus.add(ab)
        if ab not in fiches:err.append(f'cartes-index.md : {c[0]} sans fiche lisible');continue
        d,s_=fiches[ab]
        if not d.startswith(norm(c[2])):err.append(f'cartes-index.md : définition de {c[0]} ≠ cartes.md')
        if not s_.startswith(norm(c[3]).split('(')[0].strip()):err.append(f'cartes-index.md : structure de {c[0]} ≠ cartes.md')
        if {carte_id(x) for x in c[4].split(',')}!=V.get(ab):err.append(f'cartes-index.md : voisines de {c[0]} ≠ cartes.md')
    if vus!=set(NOMS):err.append(f'cartes-index.md : cartes manquantes {sorted(set(NOMS)-vus)}')
    return err


def erreurs_repetitions(chemins):
    """Texte recopié par erreur : paragraphe identique au précédent, ou segment « ; X ; X » répété
    dans une même ligne (défaut revenu deux fois dans le glossaire)."""
    err=[]
    for path in chemins:
        t=path.read_text(encoding='utf-8')
        pars=[' '.join(x.split()) for x in re.split(r'\n\s*\n',t) if x.strip()]
        for a,b in zip(pars,pars[1:]):
            if a==b and len(a)>40 and not a.startswith(('|','---','```')):err.append(f'{path.name} : paragraphe répété « {a[:50]}… »')
        for l in t.splitlines():
            seg=[x.strip(' |*') for x in re.split(r' ; |\|',l)]
            for a,b in zip(seg,seg[1:]):
                if a==b and len(a)>15:err.append(f'{path.name} : segment répété « {a[:50]} »')
    return err


def bilan(base_chemin=None, refs_chemin=None, journal_chemin=None):
    """Position mesurée sur la feuille de route (`feuille-de-route.md`) : seules les étapes
    mesurables sont calculées ; les décisions d'auteur restent déclarées dans le document."""
    out=[f'Bilan de la feuille de route · version {P["version"]}']
    st=statuts();par={s:sum(st.get((ab,s)) in ('Attesté','Documenté') for ab in NOMS) for s in range(1,NS+1)}
    best=max(par,key=par.get)
    base=charger(base_chemin or RACINE/'assets/cas-reels.jsonl');valider_base(base)
    reels=[c for c in base if not c.get('fictif')]
    n={k:sum(c.get('statut_donnees')==k for c in reels) for k in ('actif','proposition','archive_a_revoir')}
    out.append(f"Étape 2 · cas réels : {n['actif']} actifs · {n['proposition']} propositions (sources à lire) · {n['archive_a_revoir']} archives"
               +(' → terminée' if reels and n['actif']==len(reels) else ' → en cours' if n['proposition'] else ''))
    out.append(f"Étape 3 · strate pilote : {par[best]}/16 équivalents Documentés ou Attestés ({'meilleure : strate '+str(best) if par[best] else 'aucune strate entamée'}) ; "
               f"{sum(v==16 for v in par.values())} strate(s) complète(s) ; emprunt T4 {'possible' if sum(v>0 for v in par.values())>=2 else 'fermé'}")
    if refs_chemin:
        r=lire_json(refs_chemin,'--references');exiger(isinstance(r,dict),'--references : objet attendu')
        out.append(f'Étape 4 · références externes : {len(r)} événements référencés')
    else:
        out.append('Étape 4 · références externes : aucun fichier fourni (--references)')
    act=[c for c in reels if c.get('statut_donnees')=='actif']
    for s in sorted({s for c in act for s in c['strates']}):
        lot=[c for c in act if s in c['strates']]
        dbl=sum(len(set(c['codage']['codeurs']))>=2 and c['codage'].get('independants') is True for c in lot)
        sans=sum(bool(c['sans_evenement']) for c in lot)
        out.append(f"Étape 5 · strate {s} : {len(lot)} cas actifs (ρ1 dès {P['c_min_rho1']} homologues, ρ0 dès {P['seuil_rho0_cas_distincts']}) · "
                   f"{dbl} double-codés (sortie du mode solo : {P['double_codage_min_cas']} et {P['double_codage_part']:.0%}) · {sans} sans événement")
    if not act:out.append('Étape 5 · base réelle : aucun cas actif')
    if journal_chemin:
        r=score_result(charger(journal_chemin))
        out.append(f"Test à l'aveugle · {r['questions_eligibles']} questions éligibles V4 · {r['episodes_comparables']}/{P['v4_n']} épisodes comparables · {r['statut']}")
    else:
        out.append("Test à l'aveugle : aucun journal fourni (--journal)")
    out.append('Étapes 0, 1 et 6 (installation, décisions d’auteur, code différé) : état déclaré dans references/feuille-de-route.md')
    return '\n'.join(out)


def schema_documente():
    """Premier bloc JSON de `base-de-cas.md` §2 : le schéma qu'un lecteur recopiera."""
    sec=(RACINE/'references'/'base-de-cas.md').read_text(encoding='utf-8').split('## 2.',1)[1].split('\n## ',1)[0]
    m=re.search(r'```json\n(.*?)\n```',sec,re.S)
    exiger(m is not None,'base-de-cas.md §2 : schéma JSON absent')
    return json.loads(m.group(1))


def audit():
    exiger(P['version']=='0.5.1','version du moteur et des paramètres différente')
    for k in ('f_defaut','plafond_p0','w_emprunt','jaccard_H15','seuil_affichage','intervalle','double_codage_part','kappa_min','v4_gain','alerte_R2'):
        proba(P[k],k)
    for k in ('k','k0_frequence','demi_vie_ans','fenetre_reference_jours','multiplicateur_bouge','plafond_LR'):
        exiger(type(P[k]) in (int,float) and math.isfinite(P[k]) and P[k]>0,f'paramètre positif : {k}')
    for k in ('seuil_rho0_cas_distincts','double_codage_min_cas','v4_n','faisceau_max','pas_max','n_min_frequence','c_min_rho1'):
        exiger(type(P[k]) is int and P[k]>0,f'paramètre entier positif : {k}')
    for ab,p in P['inertie'].items():exiger(ab in NOMS and 0<proba(p)<1,'inertie invalide')
    exiger(set(P['inertie'])==set(NOMS),'inerties incomplètes')
    for key in ('matrice','autre_strate'):
        for a,row in P[key].items():
            exiger(a in NOMS and isinstance(row,dict),'matrice invalide')
            for b,intensity in row.items():exiger(b in NOMS and intensity in P['lambda'],'transition invalide')
    for v in P['lambda'].values():exiger(math.isfinite(v) and v>0,'multiplicateur positif requis')
    files=['constitution','protocole','glossaire','strates','cartes-index','cartes','equivalences','antagonismes','grammaire','dynamiques','base-de-cas','graphe','simulation','validation','exemples','feuille-de-route','sources-france']
    paths=[RACINE/'references'/f'{x}.md' for x in files]+[RACINE/'references/equivalences'/f'strate-{s:02}.md' for s in range(1,NS+1)]
    for path in paths:
        exiger(path.is_file(),f'fichier absent : {path.relative_to(RACINE)}')
        exiger('> Version : '+P['version'] in path.read_text(encoding='utf-8'),f'version absente/différente : {path.name}')
    sk=(RACINE/'SKILL.md').read_text(encoding='utf-8')
    exiger("version: '"+P['version']+"'" in sk,'version SKILL.md différente')
    protocol=(RACINE/'references/protocole.md').read_text(encoding='utf-8')
    begin='<!-- PARAMETRES:BEGIN -->';end='<!-- PARAMETRES:END -->'
    exiger(begin in protocol and end in protocol,'table exhaustive des paramètres absente')
    mirror=protocol.split(begin,1)[1].split(end,1)[0].strip()
    exiger(mirror==parametres_markdown(),'parametres.json et protocole §H diffèrent ; générer avec parametres')
    dyn=(RACINE/'references/dynamiques.md').read_text(encoding='utf-8')
    for ab,name in NOMS.items():
        lines=[x for x in re.findall(r'^\| '+re.escape(name)+r' \|(.*)\|$',dyn,re.M) if x.count('|')==15]
        exiger(bool(lines),f'matrice documentaire absente : {name}')
        cells=[x.strip() for x in lines[0].split('|')]
        exiger({list(NOMS)[j]:cells[j] for j in range(16) if cells[j]}==P['matrice'][ab],f'matrice documentaire différente : {name}')
        mi=re.search(r'^\| '+re.escape(name)+r' \| (0,\d+)',dyn,re.M)
        exiger(mi is not None and abs(float(mi[1].replace(',','.'))-P['inertie'][ab])<1e-9,f'inertie documentaire différente : {name}')
    exiger(type(P['nombre_strates']) is int and P['nombre_strates']>0,'nombre_strates : entier positif')
    exiger(len(statuts())==16*NS,f'{16*NS} équivalents attendus (16 cartes × {NS} strates)')
    for s in range(1,NS+1):
        for line in (RACINE/'references/equivalences'/f'strate-{s:02}.md').read_text(encoding='utf-8').splitlines():
            cells=[x.strip() for x in line.strip('|').split('|')]
            if len(cells)==5 and cells[3] in ('Documenté','Attesté'):
                exiger(cells[4].lower() not in ('à fournir','—',''),f'équivalent non sourcé : {cells[0]}@{s}')
            if len(cells)==5 and cells[3]=='Hors domaine':
                exiger(cells[4].lower() not in ('à fournir','—',''),f'Hors domaine sans motif : {cells[0]}@{s} (A3 : décision d’auteur motivée)')
    # Check actual local Markdown paths; numbered sections are checked where explicit.
    for path in [RACINE/'SKILL.md']+paths:
        text=path.read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)]+\.md)\)',text):
            if '://' not in target:exiger((path.parent/target).is_file(),f'lien absent : {path.name} → {target}')
    schema=schema_documente()
    try:valider_base([schema])
    except ValueError as e:raise ValueError(f'base-de-cas.md §2 : le schéma documenté ne passe pas valider — {e}') from None
    errs=erreurs_statuts()+erreurs_index()+erreurs_repetitions([RACINE/'SKILL.md',RACINE/'README.md']+paths)
    for f in ('constitution.md','simulation.md'):
        if OUVERTURE not in (RACINE/'references'/f).read_text(encoding='utf-8'):errs.append(f'{f} : ligne d’ouverture normative absente (« {OUVERTURE} »)')
    if not re.search(r'^Version '+re.escape(P['version'])+r'\b',(RACINE/'README.md').read_text(encoding='utf-8'),re.M):
        errs.append('README.md : « Version '+P['version']+' » absente')
    exiger(not errs,'cohérence documentaire : '+' ; '.join(errs))
    errs=erreurs_renvois([RACINE/'SKILL.md',RACINE/'README.md']+paths)
    exiger(not errs,'renvois : '+' ; '.join(errs))
    exiger(voisines() and all(voisines().get(ab) for ab in NOMS),'cartes.md : listes de voisines illisibles (A6)')
    incompatibles()
    print(f'audit : conforme — fichiers, versions, {16*NS} statuts, paramètres exhaustifs, matrice et inerties, '
          f'{sum(len(RENVOI_RE.findall(p.read_text(encoding="utf-8"))) for p in [RACINE/"SKILL.md",RACINE/"README.md"]+paths)} renvois §, '
          'voisines A6, incompatibilités G6, schéma de fiche validé, répartition des statuts, index des cartes, répétitions ; '
          'contrôle de forme et de recoupement interne, pas de la justesse du contenu ni certification empirique')
    return True


# ───────────────────────── interface ─────────────────────────

def evenement_lire(raw):
    parts=raw.split(' ',1);exiger(len(parts)==2,'événement : CARTE@strate type')
    types={'apparaît':'apparait','apparait':'apparait','persiste':'persiste','disparaît':'disparait','disparait':'disparait',
           'se renforce':'renforce','renforce':'renforce',"s'affaiblit":'affaiblit','affaiblit':'affaiblit',
           'se transforme':'transforme','transforme':'transforme',"s'intensifie":'intensifie','intensifie':'intensifie'}
    exiger(parts[1] in types,'type d’événement inconnu')
    return cle_valide(parts[0]),types[parts[1]]


def metadata(base,asof,demo=False):
    return {'version':P['version'],'date_information':asof,'demo':demo,'evaluation':'non encore évalué prospectivement',
            'empreintes':{'moteur':fichier_sha(__file__),'parametres':fichier_sha(RACINE/'assets/parametres.json'),'base':empreinte(base)}}


def pct(x,unite=True):
    """Pourcentage affiché sans fausse précision : entier entre 1 et 99 %, une décimale aux extrêmes.
    Le JSON et le journal gardent la valeur non arrondie."""
    v=x*100;s=f'{v:.0f}' if 1<=v<=99 else f'{v:.1f}'.replace('.',',')
    return s+(' %' if unite else '')


OUVERTURE='⚠ Prévision · cet outil prend un risque déclaré.'  # constitution.md §3, ligne normative unique


def texte_probabilite(p,itv):
    """S5 : « p [a–b] », ou « ~p (large : a–b) » si l'intervalle dépasse largeur_max_affichage (§H)."""
    if p is None:return 'non estimée'
    if not itv:return pct(p)+' [intervalle non estimé]'
    a,b=pct(itv[0],False),pct(itv[1],False)
    return f'~{pct(p)} (large : {a}–{b})' if itv[1]-itv[0]>P['largeur_max_affichage'] else f'{pct(p)} [{a}–{b}]'


def ligne_signalement(result):
    """Ligne S5 (protocole.md, constitution.md §3) :
    ⚠ ρ[n] · [source en clair] · p₀ [x] % · p [y] % [intervalle] · échéance [date] · journal [id]"""
    h=result.get('homologie');c=result.get('c_A') or 0;ap=result.get('a_priori')
    if c and h=='H3':src=f'{c} cas empruntés (H3)'
    elif c:src=f'{c} cas distincts ({h})'
    elif 'conditionnelle' in result.get('composantes',{}):src='composé : persistance × référence conditionnelle'
    elif result.get('p') is None:src='référence conditionnelle manquante'
    else:src='a priori '+('ancré' if ap and ap.get('ancrage') else 'non ancré')+', aucun cas'
    p0=f" · p₀ {pct(ap['p0'])}" if ap else ''
    return (f"⚠ ρ{result['rho']} · {src}{p0} · p {texte_probabilite(result.get('p'),result.get('intervalle'))}"
            f" · échéance {result.get('echeance') or '[date]'} · journal {result.get('journal') or '[à attribuer]'}")


def afficher(result,as_json=False):
    if as_json or 'p' not in result:
        print(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False));return
    print(OUVERTURE)
    print(ligne_signalement(result))
    print(f"Événement : {result['evenement']} · ρ = provenance du chiffre, pas sa fiabilité")
    print('Comparateur au même horizon : '+('non évaluable' if result.get('comparateur') is None else pct(result['comparateur'])))
    if result.get('p_sans_cartes') is not None:
        d=result['apport_cartes']*100
        print(f"Sans cartes (inertie et fréquences seules) : {pct(result['p_sans_cartes'])} — "
              +('les cartes ne changent rien à ce calcul : un bon score ne validerait pas la lecture' if abs(d)<0.05
                else f"les cartes déplacent la probabilité de {d:+.1f} points".replace('.',',')))
    if 'a_priori' in result:
        ap=result['a_priori'];print(f"Trace : multiplicateur {ap['LR']:.2f} · homologie {result['homologie'] or '—'} · c_A {result['c_A']} · n_A {result['n_A']:.1f} · n_E {result['n_E']:.1f}")
    ml=result.get('marqueur_local')
    if ml:print(f"Résolution (S1) : la source doit mesurer le marqueur local « {ml['marqueur']} » ({ml['equivalent']}, {ml['statut']}) ; sinon reformuler l'événement")
    for flag in result.get('drapeaux',[]):print('! '+flag)
    print('Valeurs non arrondies, détails et empreintes : ajouter --json. Aucun score de validation acquis.')


def main():
    parser=argparse.ArgumentParser(description=__doc__);subs=parser.add_subparsers(dest='cmd',required=True)
    for name in ('audit','autotest','parametres'):subs.add_parser(name)
    for name in ('valider','scorer','sceller'):
        s=subs.add_parser(name);s.add_argument('fichier')
    p=subs.add_parser('partager');p.add_argument('ids',nargs='+')
    q=subs.add_parser('equivalences');q.add_argument('--carte',required=True)
    b=subs.add_parser('bilan');b.add_argument('--base');b.add_argument('--references');b.add_argument('--journal')
    for name in ('calculer','trajectoires'):
        c=subs.add_parser(name);c.add_argument('--base');c.add_argument('--etat',required=True)
        c.add_argument('--date-information');c.add_argument('--liaison',action='append',default=[])
        c.add_argument('--bouge',action='append',default=[]);c.add_argument('--manque',action='append',default=[])
        c.add_argument('--ctr-materielle',action='append',default=[]);c.add_argument('--references')
        c.add_argument('--fref',type=float);c.add_argument('--source-ref');c.add_argument('--periode-ref');c.add_argument('--disponible-ref')
        c.add_argument('--pas',type=int,default=1);c.add_argument('--semantique');c.add_argument('--resolution')
        c.add_argument('--echeance');c.add_argument('--journal');c.add_argument('--strates',default='')
        c.add_argument('--json',action='store_true');c.add_argument('--demo',action='store_true')
        c.add_argument('--sans-cartes',action='store_true')
        if name=='calculer':c.add_argument('--evenement',required=True)
    a=parser.parse_args()
    if a.cmd=='audit':audit();return
    if a.cmd=='autotest':autotest();return
    if a.cmd=='parametres':print(parametres_markdown());return
    if a.cmd=='valider':valider(a.fichier);return
    if a.cmd=='bilan':print(bilan(a.base,a.references,a.journal));return
    if a.cmd=='partager':
        for ident in a.ids:print(ident+' → '+usage_attendu(ident))
        return
    if a.cmd=='equivalences':
        ab=carte_id(a.carte)
        for s in range(1,NS+1):print(s,marqueur_local(ab,s))
        return
    if a.cmd=='scorer':print(scorer(a.fichier));return
    if a.cmd=='sceller':
        data=charger(a.fichier);valider_journal(data)
        predictions=[x for x in data if x['type']=='prevision']
        now=datetime.date.today()
        exiger(predictions,'aucune prévision à sceller')
        exiger(all(date_iso(x['echeance'])>now for x in predictions),'scellement prospectif impossible : échéance atteinte')
        print(json.dumps({'sha256':fichier_sha(a.fichier),'previsions_sha256':empreinte([empreinte_prevision(p) for p in predictions]),'empreintes_previsions':{p['id']:empreinte_prevision(p) for p in predictions},'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                          'instruction':'Publier cette empreinte avant échéance ; conserver le fichier exact. La date locale seule ne prouve pas la prépublication.'},ensure_ascii=False));return
    base=charger(a.base);summary=valider_base(base)
    exiger(a.demo or not any(c.get('fictif') and c.get('statut_donnees')=='actif' for c in base),'base fictive : --demo obligatoire ; chiffres interdits en prévision réelle')
    etat=lire_etat(a.etat);asof=a.date_information or etat['date'];date_iso(asof)
    exiger(jour(asof)>=jour(etat['date']),'date d’information antérieure à l’état')
    exiger(type(a.pas) is int and 1<=a.pas<=P['pas_max'],f'pas entre 1 et {P["pas_max"]}')
    end=fin_fenetre(etat['date'],etat['fenetre'],a.pas).isoformat()
    if a.echeance:exiger(date_iso(a.echeance).isoformat()==end,'échéance différente de date état + pas × fenêtre')
    exiger(jour(asof)<jour(end),'date d’information à l’échéance ou après : rejeu explicite requis hors calcul prospectif')
    st=statuts()
    for m in etat['mots']:
        exiger(m['i']!='F' or st.get((m['c'],m['s']))!='Vide',f'{cle(m)} : F impossible sur un équivalent Vide (A3)')
        exiger(st.get((m['c'],m['s']))!='Hors domaine',f'{cle(m)} : carte Hors domaine dans cette strate, aucun ancrage possible (A3)')
    active=base_active(base,asof,a.demo)
    refs=lire_json(a.references,'--references') if a.references else {}
    if a.fref is not None:
        proba(a.fref,'fref');exiger(a.cmd=='calculer','--fref scalaire interdit pour plusieurs événements ; utiliser --references')
        cible,typ=evenement_lire(a.evenement)
        exiger(typ in ('apparait','persiste','disparait'),'événement composé : fournir des références séparées dans --references')
        for name in ('source_ref','periode_ref','disponible_ref'):texte_requis(getattr(a,name),name)
        exiger(cible+' '+typ not in refs,'référence fournie deux fois')
        refs[cible+' '+typ]={'frequence':a.fref,'source':a.source_ref,'definition':a.evenement,'periode':a.periode_ref,'fenetre':etat['fenetre'],'disponible_le':a.disponible_ref}
    refs_valider(refs,etat['fenetre'],asof)
    for key in list(refs):
        # Keys are canonical abbreviations; reject aliases instead of silently missing a supplied reference.
        k,t=key.split(' ',1);exiger(k==cle_valide(k),f'référence : employer la clé canonique {cle_valide(k)} {t}')
    links=lire_liaisons(a.liaison,etat);bouge=[cle_valide(x) for x in a.bouge];manque=[cle_valide(x) for x in a.manque]
    if bouge or manque:
        exiger(len(etat['mots'])>=3,'positions : au moins trois mots ancrés requis')
        exiger(all(x in forces(etat) for x in bouge) and all(x not in forces(etat) for x in manque),'positions incompatibles avec l’état')
    exiger(all(x.isdigit() and 1<=int(x)<=NS for x in a.ctr_materielle),'strate de contrainte matérielle invalide')
    opts=dict(liaisons=links,bouge=bouge,manque=manque,refs=refs,ctr_materielle=a.ctr_materielle,asof=asof,sans_cartes=a.sans_cartes)
    if a.cmd=='trajectoires':
        exiger(not a.sans_cartes,'trajectoires : comparaison sans cartes disponible via calculer')
        brut=[x.strip() for x in a.strates.split(',') if x.strip()]
        exiger(all(x.isdigit() for x in brut),f'--strates : numéros de strate séparés par des virgules (ex. 8,11), reçu « {a.strates} »')
        sup=[int(x) for x in brut];result=trajectoires(etat,a.pas,active,opts,sup)
    else:
        cible,typ=evenement_lire(a.evenement)
        exiger(typ not in ('renforce','affaiblit'),'f ↔ F est une révision de confiance, pas un événement physique ; utiliser s’intensifie avec une mesure ou reformuler le critère observable')
        if typ in ('intensifie','transforme'):
            exiger(a.pas==1,'événements composés : --pas > 1 non pris en charge')
            res=lire_json(a.resolution,'--resolution') if a.resolution else None
            result=compose(etat,typ,cible,active,opts,res)
        else:
            sem=a.semantique or ('continue' if typ=='persiste' else 'au-moins-une-fois' if typ=='disparait' else 'presence')
            result=horizon_result(etat,typ,cible,active,opts,a.pas,sem)
            if not a.sans_cartes:
                # Comparateur inertiel : même calcul sans cartes (inertie, fréquences, références seules).
                # Sans lui, un bon Brier peut ne venir que du statu quo (exemple 11).
                nu=horizon_result(etat,typ,cible,active,dict(opts,sans_cartes=True),a.pas,sem)
                result['p_sans_cartes']=nu['p'];result['apport_cartes']=result['p']-nu['p']
        result['echeance']=end;result['journal']=a.journal
    if a.cmd=='calculer':
        ml=marqueur_local(*cible.split('@'))
        st_=statuts().get((cible.split('@')[0],int(cible.split('@')[1])))
        result['marqueur_local']=None if ml is None else {'equivalent':ml[0],'marqueur':ml[1],'statut':st_}
    result['contexte']=metadata(base,asof,a.demo);result['base']=summary
    result['base']['cas_apprentissage_disponibles']=len(active)
    nv=[cle(m) for m in etat['mots'] if m['i']=='F' and st.get((m['c'],m['s'])) not in ('Attesté','Documenté')]
    if nv:result.setdefault('drapeaux',[]).append('Ancrage F sur équivalent non vérifié (Proposé) : '+', '.join(nv)+' — la lecture est tranchée, la correspondance reste à documenter (A3).')
    if a.demo:result.setdefault('drapeaux',[]).insert(0,'DÉMONSTRATION FICTIVE — ne constitue ni une prévision réelle ni une preuve de calibration.')
    afficher(result,a.json)

# ───────────────────────── tests de régression intégrés ─────────────────────────

def autotest():
    import copy, unittest
    def fake_case(year=2020, count=1):
        cid=next(f'C-{i:04d}-S07' for i in range(9000,9999) if usage_attendu(f'C-{i:04d}-S07')=='apprentissage')
        states=[]
        for j in range(count+1):
            dt=fin_fenetre(f'{year}-01-01','3 mois',j).isoformat() if j else f'{year}-01-01'
            states.append({'date':dt,'disponible_le':dt,'etat':f'[{dt} | 3 mois] POLARITÉ@7[f]',
                           'mots':[{'carte':'POL','strate':7,'intensite':'f','fait':'deux camps observés',
                                    'source':'source de test fictive','contre_observation':'médiation observée, marginale','portee':'marginale','objet':'conflit-test'}] if not j else None,
                           'retraits':[],'liaisons':[],'positions':None})
        return {'id':cid,'version_regles':P['version'],'titre':'Cas technique fictif','strates':[7],'fenetre':'3 mois',
                'sequence':states[:-1],'issue':states[-1],'sans_evenement':True,'fictif':True,'statut_donnees':'actif',
                'codage':{'mode':'manuel','codeurs':['test']},'usage':'apprentissage'}
    def forecast(ident='P-1',**kw):
        x={'type':'prevision','id':ident,'date':'2026-01-01','echeance':'2026-04-01','version_regles':P['version'],
           'question':'Une rupture survient-elle ?','evenement':'SEU@7 apparait','episode_id':'episode-A','pas':1,
           'indicateur_bascule':'rappel d’un ambassadeur','refutation':'aucune rupture','semantique':'presence',
           'etat_present':'[2026-01-01 | 3 mois] POLARITÉ@7[f]','probabilite':.2,'intervalle':None,'rho':'ρ4',
           'resolution':{'source':'registre public','critere':'rupture publiée','seuil':'une publication','marqueur':'rupture diplomatique','objet':'relation A-B'},
           'resolution_verifiee':True,'frequence_de_base':.3,'p_sans_cartes':None,'rejeu':False,'fictif':True,'partition':None,
           'empreintes':None,'preuve_prepublication':None}
        x.update(kw);return x
    def score(i='P-1',issue=0):return {'type':'score','id':i,'date':'2026-04-02','issue':issue,'preuve':'registre consulté'}
    class Tests(unittest.TestCase):
        def test_calendar_invalid(self):
            for d in ('2026-99-99','2026-02-29','2026-04-31'):
                with self.assertRaises(ValueError):date_iso(d)
        def test_leap(self):self.assertEqual(date_iso('2024-02-29').day,29)
        def test_calendar_month_end(self):self.assertEqual(fin_fenetre('2026-01-31','1 mois').isoformat(),'2026-02-28')
        def test_window_invalid(self):
            for f in ('0 jours','-1 mois','1 minute'):
                with self.assertRaises(ValueError):duree_jours(f)
        def test_probability_limits(self):
            for x in (-.1,1.1,float('nan'),float('inf'),True):
                with self.assertRaises(ValueError):proba(x)
        def test_odds_boundaries(self):
            self.assertEqual(odds_module(0,3),0);self.assertEqual(odds_module(1,3),1)
        def test_negative_regression(self):
            e=lire_etat('[2026-01-01 | 1 an] INCERTITUDE@7[f] + RÉSEAU@7[f] + POLARITÉ@7[f]')
            r=calculer(e,'persiste','INC@7',[],bouge=['INC@7']);self.assertGreaterEqual(r['p'],0);self.assertLessEqual(r['p'],1)
        def test_invalid_state(self):
            for s in ('[2026-01 | 3 mois] SEUIL@99[f]','[2026-01 | 3 mois] SEUIL@7[f] + SEUIL@7[F]'):
                with self.assertRaises(ValueError):lire_etat(s)
        def test_valid_case(self):self.assertEqual(valider_base([fake_case()])['actifs'],1)
        def test_case_strata(self):
            c=fake_case();c['strates']=[12]
            with self.assertRaises(ValueError):valider_base([c])
        def test_case_force(self):
            c=fake_case();c['sequence'][0]['mots'][0]['intensite']='F'
            with self.assertRaises(ValueError):valider_base([c])
        def test_missing_coders(self):
            c=fake_case();c['codage']={}
            with self.assertRaises(ValueError):valider_base([c])
        def test_ten_year_transition(self):
            c=fake_case();c['issue']['date']=c['issue']['disponible_le']='2030-01-01';c['issue']['etat']='[2030-01-01 | 3 mois] POLARITÉ@7[f]'
            with self.assertRaises(ValueError):valider_base([c])
        def test_future_exclusion(self):self.assertEqual(base_active([fake_case(2090)],'2026-01-01',True),[])
        def test_delayed_source(self):
            c=fake_case();c['issue']['disponible_le']='2090-01-01';self.assertEqual(base_active([c],'2026-01-01',True),[])
        def test_fiction_exclusion(self):self.assertEqual(base_active([fake_case()],'2026-01-01'),[])
        def test_archive_exclusion(self):
            c=fake_case();c['statut_donnees']='archive_a_revoir';self.assertEqual(base_active([c],'2026-01-01',True),[])
        def test_homology_empty_strong(self):
            e=lire_etat('[2026-01-01 | 3 mois] RÉSEAU@7[f]');r=calculer(e,'apparait','SEU@7',[fake_case()]);self.assertEqual(r['nb_cas_par_niveau']['H1'],0)
        def test_case_weight_cap(self):
            e=lire_etat('[2026-01-01 | 3 mois] POLARITÉ@7[f]');r=calculer(e,'persiste','POL@7',[fake_case(count=10)]);self.assertLessEqual(r['n_A'],1)
        def test_reference_future(self):
            r={'POL@7 persiste':{'frequence':.2,'source':'x','definition':'x','periode':'x','fenetre':'3 mois','disponible_le':'2090-01-01'}}
            with self.assertRaises(ValueError):refs_valider(r,'3 mois','2026-01-01')
        def test_reference_scope(self):
            e=lire_etat('[2026-01-01 | 3 mois] POLARITÉ@7[f]');r=calculer(e,'persiste','POL@7',[],refs={'POL@7 hausse|persiste':{'frequence':.2}});self.assertAlmostEqual(r['p'],.85)
        def test_reference_disappearance(self):
            e=lire_etat('[2026-01-01 | 3 mois] POLARITÉ@7[f]');r=calculer(e,'disparait','POL@7',[],refs={'POL@7 disparait':{'frequence':.2}});self.assertAlmostEqual(r['p'],.2)
        def test_beta_uniform(self):self.assertAlmostEqual(beta_quantile(1,1,.1),.1,places=9)
        def test_beta_degenerate(self):self.assertIsNone(intervalle_beta(0,0,0))
        def test_single_step_invalid_semantics(self):
            e=lire_etat('[2026-01-01 | 3 mois] POLARITÉ@7[f]')
            for sem in ('invalide','continue'):
                with self.assertRaises(ValueError):horizon_result(e,'apparait','SEU@7',[],{},1,sem)
        def test_journal_future_state(self):
            p=forecast(etat_present='[2028-01-01 | 3 mois] POLARITÉ@7[f]')
            with self.assertRaises(ValueError):valider_journal([p])
        def test_journal_horizon_mismatch(self):
            p=forecast(echeance='2026-05-01')
            with self.assertRaises(ValueError):valider_journal([p])
        def test_prepublication_binds_probability(self):
            p=forecast(fictif=False,preuve_prepublication={'source':'registre','date':'2026-01-02'})
            p['preuve_prepublication']['empreinte_prevision']=empreinte_prevision(p)
            p['probabilite']=.9
            with self.assertRaises(ValueError):valider_journal([p])
        def test_horizon_baseline(self):
            e=lire_etat('[2026-01-01 | 3 mois] POLARITÉ@7[f]');opts={'refs':{'SEU@7 apparait':{'frequence':.2},'SEU@7 persiste':{'frequence':.8}}}
            r=horizon_result(e,'apparait','SEU@7',[],opts,4,'presence');self.assertAlmostEqual(r['comparateur'],cumul(.2,.8,4));self.assertIsNone(r['intervalle'])
        def test_ever_vs_final(self):self.assertGreater(1-(1-.2)**4,cumul(.2,.8,4))
        def test_compound_conditional(self):
            e=lire_etat('[2026-01-01 | 3 mois] POLARITÉ@7[f]');op={'asof':'2026-01-01','refs':{'POL@7 hausse|persiste':{'frequence':.2}}}
            res={'source':'x','critere':'x','seuil':'x','marqueur':'x','objet':'x','grandeur':'x','unite':'x','comparaison':'x','observations':[{'date':'2025-11-01','valeur':1},{'date':'2025-12-01','valeur':2}]}
            self.assertAlmostEqual(compose(e,'intensifie','POL@7',[],op,res)['p'],.17)
        def test_compound_missing_reference(self):
            e=lire_etat('[2026-01-01 | 3 mois] RÉSEAU@7[f]');res={k:'x' for k in ('source','critere','seuil','marqueur','objet')}
            self.assertIsNone(compose(e,'transforme','RES@7',[],{'asof':'2026-01-01'},res)['p'])
        def test_journal_duplicate(self):
            with self.assertRaises(ValueError):valider_journal([forecast(),forecast()])
        def test_journal_missing_rejeu(self):
            p=forecast();p.pop('rejeu')
            with self.assertRaises(ValueError):valider_journal([p])
        def test_journal_early_score(self):
            s=score();s['date']='2026-02-01'
            with self.assertRaises(ValueError):valider_journal([forecast(),s])
        def test_journal_orphan(self):
            with self.assertRaises(ValueError):valider_journal([score()])
        def test_partition_sum(self):
            p=forecast(partition='A');q=forecast('P-2',partition='A',evenement='SEU@7 absent')
            with self.assertRaises(ValueError):valider_journal([p,q])
        def test_partition_issues(self):
            p=forecast(partition='A',probabilite=.5,frequence_de_base=.5);q=forecast('P-2',partition='A',probabilite=.5,frequence_de_base=.5,evenement='SEU@7 absent')
            with self.assertRaises(ValueError):valider_journal([p,q,score(issue=1),score('P-2',1)])
        def test_partition_brier(self):
            p=forecast(partition='A',probabilite=.5,frequence_de_base=.5);q=forecast('P-2',partition='A',probabilite=.5,frequence_de_base=.5,evenement='SEU@7 absent')
            r=score_result([p,q,score(issue=1),score('P-2',0)]);self.assertEqual(r['questions_resolues'],1);self.assertAlmostEqual(r['details'][0]['brier'],.5)
        def test_missing_score_counted(self):self.assertEqual(score_result([forecast()])['sans_score'],1)
        def test_fiction_never_validated(self):self.assertEqual(score_result([forecast(),score()])['questions_eligibles'],0)
        def test_unverified_never_validated(self):self.assertEqual(score_result([forecast(fictif=False),score()])['questions_eligibles'],0)
        def test_episode_count(self):
            data=[]
            for i in range(50):
                p=forecast(f'P-{i}',fictif=False,empreintes={k:'0'*64 for k in ('moteur','parametres','base')},preuve_prepublication={'source':'registre externe','date':'2026-01-02'})
                p['preuve_prepublication']['empreinte_prevision']=empreinte_prevision(p)
                data.extend([p,score(f'P-{i}')])
            r=score_result(data);self.assertEqual(r['episodes_comparables'],1);self.assertEqual(r['statut'],'non encore évalué')
        def test_trajectory_mass(self):
            e=lire_etat('[2026-01-01 | 3 mois] POLARITÉ@7[f]');r=trajectoires(e,2,[],{'liaisons':[],'bouge':[],'manque':[]});self.assertAlmostEqual(r['somme'],1)
        def test_audit_parameter_mismatch(self):
            old=P['k'];P['k']=999
            try:
                with self.assertRaises(ValueError):audit()
            finally:P['k']=old
        def test_f_proposed_allowed_vide_refused(self):
            c=fake_case();m=c['sequence'][0]['mots'][0];c['fictif']=False;c['sources_verifiees']=True
            m['intensite']='F';m['a6']='POLARITÉ@7 : CONTRAINTE → (deux camps, pas une règle) ; SEUIL → (aucun passage irréversible)'
            for s_ in c['sequence']+[c['issue']]:s_['etat']=s_['etat'].replace('[f]','[F]')
            self.assertEqual(valider_base([c])['actifs'],1)
            self.assertEqual(statuts().get(('COM',1)),'Vide')
        def test_a6_neighbours_required(self):
            c=fake_case();m=c['sequence'][0]['mots'][0];c['fictif']=False;c['sources_verifiees']=True
            m['intensite']='F';m['a6']='POLARITÉ@7 : CONTRAINTE → (deux camps, pas une règle)'
            for s_ in c['sequence']+[c['issue']]:s_['etat']=s_['etat'].replace('[f]','[F]')
            with self.assertRaises(ValueError):valider_base([c])
            m['a6']='POLARITÉ@7 : CONTRAINTE → (x) ; SEUIL ? (non tranché)'
            with self.assertRaises(ValueError):valider_base([c])
        def _g6_case(self,o1,o2,link):
            c=fake_case();st0=c['sequence'][0];st0['etat']=st0['etat'].replace('POLARITÉ@7[f]','INCERTITUDE@7[f] + CONTRAINTE@7[f]')
            c['issue']['etat']=c['issue']['etat'].replace('POLARITÉ@7[f]','INCERTITUDE@7[f] + CONTRAINTE@7[f]')
            base_m=st0['mots'][0];st0['mots']=[dict(base_m,carte='INC',objet=o1),dict(base_m,carte='CTR',objet=o2)]
            st0['liaisons']=[link];st0['preuves_liaisons']=['preuve fictive'];return c
        def test_g6_same_object_refused(self):
            with self.assertRaises(ValueError):valider_base([self._g6_case('le plafond','le plafond','INCERTITUDE@7 renforcement CONTRAINTE@7')])
        def test_g6_distinct_objects_accepted(self):
            self.assertEqual(valider_base([self._g6_case('le plafond','le périmètre','INCERTITUDE@7 renforcement CONTRAINTE@7')])['actifs'],1)
        def test_g6_independence_same_object(self):
            c=self._g6_case('x','y','INCERTITUDE@7 indépendance CONTRAINTE@7');self.assertEqual(valider_base([c])['actifs'],1)
            self.assertTrue(erreurs_objets({'POL@7':'a','RES@7':'A '},[('POL@7','indépendance','RES@7')],incompatibles()))
        def test_renvoi_detection(self):
            import tempfile
            with tempfile.TemporaryDirectory() as d:
                f=Path(d)/'x.md';f.write_text('voir `strates.md` §9 et `validation.md` §5',encoding='utf-8')
                self.assertEqual(len(erreurs_renvois([f])),2)
                f.write_text('voir `validation.md` §6',encoding='utf-8');self.assertEqual(erreurs_renvois([f]),[])
        def test_homology_strictest(self):
            # 3 cas identiques (H1) + 2 cas avec un mot de plus (H1.5 seulement) : 0.4.0 prenait H1.5.
            mots4='POLARITÉ@7[f] + CONTRAINTE@7[f] + RÉSEAU@7[f] + HIÉRARCHIE@7[f]'
            ids=[f'C-{i:04d}-S07' for i in range(9000,9999) if usage_attendu(f'C-{i:04d}-S07')=='apprentissage'][:5]
            base=[]
            for n,cid in enumerate(ids):
                c=fake_case();c['id']=cid;ms=mots4+(' + PROPORTION@7[f]' if n>=3 else '')
                for s_ in c['sequence']+[c['issue']]:s_['etat']=s_['etat'].replace('POLARITÉ@7[f]',ms)
                d=c['sequence'][0]['mots'][0]
                c['sequence'][0]['mots']=[dict(d,carte=k,objet='objet-'+k) for k in ('POL','CTR','RES','HIE')+(('PRO',) if n>=3 else ())]
                base.append(c)
            e=lire_etat('[2026-01-01 | 3 mois] '+mots4);r=calculer(e,'persiste','POL@7',base)
            self.assertEqual(r['nb_cas_par_niveau']['H1'],3);self.assertEqual(r['nb_cas_par_niveau']['H1.5'],5)
            self.assertEqual(r['homologie'],'H1')
        def _f_case(self,a6,**mot):
            c=fake_case();m=c['sequence'][0]['mots'][0];c['fictif']=False;c['sources_verifiees']=True
            m.update(intensite='F',a6=a6,**mot)
            for s_ in c['sequence']+[c['issue']]:s_['etat']=s_['etat'].replace('[f]','[F]')
            return c
        def test_a6_verdicts(self):
            ok='POLARITÉ@7 : CONTRAINTE → (deux camps) ; SEUIL + (rupture datée, autre fait)'
            self.assertEqual(valider_base([self._f_case(ok)])['actifs'],1)
            for bad in ('POLARITÉ@7 : CONTRAINTE → () ; SEUIL → ()','POLARITÉ@7 : CONTRAINTE ← (r) ; SEUIL ← (r)',
                        'POLARITÉ@7 : CONTRAINTE → (r) ; SEUIL ← (r)'):
                with self.assertRaises(ValueError):valider_base([self._f_case(bad)])
        def test_a7_portee(self):
            ok='POLARITÉ@7 : CONTRAINTE → (deux camps) ; SEUIL → (aucune rupture)'
            for kw in ({'portee':'substantielle'},{'portee':'dominante'},{'portee':'inconnue'}):
                with self.assertRaises(ValueError):valider_base([self._f_case(ok,**kw)])
            c=fake_case();c['sequence'][0]['mots'][0].update(portee='substantielle')
            with self.assertRaises(ValueError):valider_base([c])
            c['sequence'][0]['mots'][0]['force_initiale']='F';self.assertEqual(valider_base([c])['actifs'],1)
        def test_a7_force_initiale_cross_state(self):
            c=fake_case(count=2)
            c['sequence'][1]['mots']=[dict(fake_case()['sequence'][0]['mots'][0],portee='substantielle',force_initiale='F')]
            with self.assertRaises(ValueError):valider_base([c])   # f à l'état précédent, sans origine F → rejet
            c['sequence'][0]['mots'][0].update(portee='substantielle',force_initiale='F')
            self.assertEqual(valider_base([c])['actifs'],1)          # déjà rétrogradé depuis F : cohérent
        def test_a7_messages(self):
            errs=controle_a7('POL@7',{'portee':'substantielle','intensite':'F','force_initiale':'F'})
            self.assertEqual(len(errs),1);self.assertIn('noter f',errs[0])
            self.assertTrue(controle_a7('POL@7',{'portee':'marginale','intensite':'f','force_initiale':'F'}))
        def test_schema_documente(self):self.assertEqual(valider_base([schema_documente()])['actifs'],1)
        def _mutations(self,base,n,graine):
            import random
            def chemins(x,p=()):
                if isinstance(x,dict):
                    for k,v in x.items():yield p+(k,);yield from chemins(v,p+(k,))
                elif isinstance(x,list):
                    for i,v in enumerate(x):yield p+(i,);yield from chemins(v,p+(i,))
            P_=list(chemins(base));rng=random.Random(graine)
            valeurs=[None,[],{},'',0,-1,1.5,True,'x','2005-13','[2005-04 | 0 mois] ∅',float('nan')]
            for _ in range(n):
                c=copy.deepcopy(base);ch=rng.choice(P_);parent=c
                for k in ch[:-1]:parent=parent[k]
                if rng.random()<.3 and isinstance(parent,dict):del parent[ch[-1]]
                else:parent[ch[-1]]=rng.choice(valeurs)
                yield ch,c
        def test_fuzz_valider(self):
            # Toute fiche altérée est acceptée ou refusée par un message (ValueError), jamais par une trace.
            for ch,c in self._mutations(schema_documente(),1500,42):
                try:valider_base([c])
                except ValueError:pass
                except Exception as e:self.fail(f'{ch} : {type(e).__name__} {e}')
        def test_fuzz_journal(self):
            base=charger(RACINE/'assets/journal.exemple.jsonl')
            for ch,c in self._mutations(base,1500,7):
                try:score_result(c)
                except ValueError:pass
                except Exception as e:self.fail(f'{ch} : {type(e).__name__} {e}')
        def test_journal_calcul_coherent(self):
            base=charger(RACINE/'assets/journal.exemple.jsonl');x=next(l for l in base if l.get('calcul'))
            x['probabilite']=min(1,x['probabilite']+.1)
            with self.assertRaises(ValueError):valider_journal(base)
        def test_sans_evenement_coherent(self):
            c=fake_case();c['sans_evenement']=True;self.assertEqual(valider_base([c])['actifs'],1)
            c['issue']['etat']=c['issue']['etat'].replace('POLARITÉ@7[f]','∅');c['issue']['retraits']=[{'mot':'POLARITÉ@7','fait':'x','source':'y'}]
            with self.assertRaises(ValueError):valider_base([c])
        def test_affichage_pourcentage(self):
            self.assertEqual(pct(.220379),'22 %');self.assertEqual(pct(.00724),'0,7 %');self.assertEqual(pct(.9931),'99,3 %')
        def test_erreur_json(self):
            import subprocess
            r=subprocess.run([sys.executable,__file__,'calculer','--etat','[2026-09 | 3 mois] POLARITÉ@7[F]','--evenement','SEUIL@99 apparait','--json'],capture_output=True,text=True)
            self.assertEqual(r.returncode,2);self.assertIn('erreur',json.loads(r.stdout))
        def test_sortie_doree(self):
            # Sortie humaine de l'exemple 1 : ouverture constitutionnelle, ligne S5, marquage « large ».
            e=lire_etat('[2026-09 | 3 mois] POLARITÉ@7[F] + CONTRAINTE@6[F]')
            base=base_active(charger(RACINE/'assets/base-de-cas.exemple.jsonl'),'2026-09-01',True)
            r=horizon_result(e,'apparait','SEU@7',base,{'liaisons':lire_liaisons(['CONTRAINTE@6 echo POLARITÉ@7'],e),'asof':'2026-09-01'},1,'presence')
            r.update(echeance='2026-12-01',journal='P-0101')
            out=io.StringIO()
            with contextlib.redirect_stdout(out):afficher(r)
            lignes=out.getvalue().splitlines()
            self.assertEqual(lignes[0],'⚠ Prévision · cet outil prend un risque déclaré.')
            self.assertEqual(lignes[1],'⚠ ρ1 · 10 cas distincts (H1) · p₀ 23 % · p ~22 % (large : 5–43) · échéance 2026-12-01 · journal P-0101')
        def test_intervalle_large(self):
            self.assertEqual(texte_probabilite(.22,[.05,.43]),'~22 % (large : 5–43)')
            self.assertEqual(texte_probabilite(.22,[.15,.30]),'22 % [15–30]')
            self.assertEqual(texte_probabilite(None,None),'non estimée')
        def test_fichiers_messages(self):
            for arg in ('{"a":1}','/introuvable.json',str(RACINE/'scripts')):
                with self.assertRaises(ValueError):lire_json(arg,'--references')
        def test_repetitions(self):
            import tempfile
            with tempfile.TemporaryDirectory() as d:
                f=Path(d)/'x.md'
                f.write_text('| X | provenance ; ne mesure pas sa calibration ; ne mesure pas sa calibration |',encoding='utf-8')
                self.assertEqual(len(erreurs_repetitions([f])),1)
                para='Un paragraphe suffisamment long pour être contrôlé par le détecteur.'
                f.write_text(para+'\n\n'+para,encoding='utf-8');self.assertEqual(len(erreurs_repetitions([f])),1)
                f.write_text(para,encoding='utf-8');self.assertEqual(erreurs_repetitions([f]),[])
        def test_bilan(self):
            t=bilan(journal_chemin=RACINE/'assets/journal.exemple.jsonl')
            self.assertIn('Étape 2',t);self.assertIn('Étape 3',t);self.assertIn("Test à l'aveugle",t)
        def test_proposition(self):
            c=fake_case();c['fictif']=False;c['statut_donnees']='proposition';c['sources_verifiees']=False;c['motif_proposition']='recodage à vérifier'
            r=valider_base([c]);self.assertEqual((r['actifs'],r['propositions']),(0,1))
            self.assertEqual(base_active([c],'2026-01-01'),[])
            c['sources_verifiees']=True
            with self.assertRaises(ValueError):valider_base([c])
        def test_hors_domaine(self):
            # Simule une case Hors domaine : aucun ancrage, aucun événement, aucune trajectoire vers elle.
            st=statuts();cle_=_STATUTS_CACHE['cle'];st[('SEU',7)]='Hors domaine';_STATUTS_CACHE.update(st=st)
            try:
                e=lire_etat('[2026-01-01 | 3 mois] POLARITÉ@7[f]')
                with self.assertRaises(ValueError):calculer(e,'apparait','SEU@7',[])
                r=trajectoires(e,1,[],{'liaisons':[],'bouge':[],'manque':[]})
                self.assertFalse(any('SEU@7' in str(t['chemins']) for t in r['trajectoires']))
            finally:_STATUTS_CACHE.clear()
        def test_strate_13(self):
            self.assertEqual(NS,13);lire_etat('[2026-10-19 | 1 semaine] ÉMERGENCE@13[f]')
            with self.assertRaises(ValueError):lire_etat('[2026-10-19 | 1 semaine] ÉMERGENCE@14[f]')
            self.assertEqual(len(statuts()),16*NS)
        def test_comparateur_inertiel(self):
            p=forecast(version_regles='0.5.0');p.pop('p_sans_cartes')
            with self.assertRaises(ValueError):valider_journal([p])          # p_sans_cartes absent
            p=forecast(version_regles='0.4.8');p.pop('p_sans_cartes');valider_journal([p])  # journaux antérieurs admis
            p=forecast(version_regles='0.5.0',p_sans_cartes=.2,probabilite=.2)
            r=score_result([p,score()]);self.assertEqual(r['apport_des_cartes']['difference'],0)
            p=forecast(version_regles='0.5.0',p_sans_cartes=.5,probabilite=.2)
            self.assertLess(score_result([p,score()])['apport_des_cartes']['difference'],0)
        def test_jugement(self):
            j=lambda i,p:{'type':'prevision','id':i,'date':'2026-09-28','echeance':'2026-10-26','version_regles':'0.5.1',
                          'origine':'jugement','question':'q','evenement':'Larcher élu','episode_id':'E','refutation':'non',
                          'probabilite':p,'rejeu':False,'fictif':False,'resolution':{'source':'s','critere':'c','seuil':'t'}}
            s=lambda i,o:{'type':'score','id':i,'date':'2026-10-26','issue':o,'preuve':'p'}
            r=score_result([j('J1',.8),s('J1',1),j('J2',.45),s('J2',1),j('J3',.6),s('J3',0)])
            self.assertAlmostEqual(r['jugements']['brier'],0.2341666667,places=6);self.assertEqual(r['questions_eligibles'],0)
            self.assertIsNone(r['apport_des_cartes'])
            m=forecast('P-9',partition='A',probabilite=.5,frequence_de_base=None);jj=dict(j('J9',.5),partition='A')
            with self.assertRaises(ValueError):valider_journal([m,jj])          # origines mêlées dans une partition
        def test_apparait_message(self):
            e=lire_etat('[2026-01-01 | 3 mois] SEUIL@13[f]')
            with self.assertRaises(ValueError) as c:calculer(e,'apparait','SEU@13',[])
            self.assertIn('déjà présent',str(c.exception))
        def test_audit(self):
            with contextlib.redirect_stdout(io.StringIO()):self.assertTrue(audit())
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    exiger(result.wasSuccessful(),'tests de régression échoués')


if __name__=='__main__':
    try:
        main()
    except Exception as e:
        # Une entrée invalide ne doit jamais produire une trace Python. Avec --json, l'erreur est du JSON.
        msg=str(e) if isinstance(e,ValueError) else f'{type(e).__name__} : {e} (entrée inattendue)'
        if '--json' in sys.argv[1:]:
            print(json.dumps({'erreur':msg,'code':2},ensure_ascii=False))
        else:
            print('Erreur : '+msg,file=sys.stderr)
        sys.exit(2)
