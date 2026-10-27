---
name: alphabet-situationnel
description: "Lecture structurelle et exploration conditionnelle de situations par 16 cartes transversales candidates et 13 strates (dont la politique intérieure). Utiliser pour lire une situation factuelle, explorer ses suites à un horizon défini, coder un cas historique ou scorer un journal. Modes LIRE, PRÉVOIR, CODER, SCORER. Le moteur calcule des probabilités expérimentales quand les entrées sont recevables ; aucune performance prédictive n'est acquise. Ne pas utiliser pour un tirage symbolique, un diagnostic, une décision sur une personne, ou transformer un ressenti seul en fait. Une lecture sans prévision est explicitement admise."
license: MIT
metadata:
  version: '0.6.10'
  author: Othman Ben Brahim
---

# Alphabet situationnel

Lire une situation, écrire son état daté, expliciter des hypothèses sur sa suite et conserver les
conditions de chaque calcul. Les règles sont dans `references/protocole.md` ; les principes P1–P9 dans
`references/constitution.md`. La documentation n'établit aucune universalité prédictive.

> ⚠ Outil expérimental : calcul reproductible ne signifie pas probabilité calibrée. Ne jamais
> convertir un résultat « non estimé » en chiffre ni présenter le niveau ρ comme un taux de fiabilité.

## Contrôle d'intégrité

Version 0.6.10. Conserver `scripts/moteur.py`, `assets/parametres.json`, les 19 références principales,
les 13 fichiers `references/equivalences/strate-NN.md`, les bases et journaux d'exemple.
Exécuter `python3 scripts/moteur.py audit` ; après modification, `python3 scripts/moteur.py autotest`.
Le premier vérifie les fichiers, versions, paramètres exhaustifs, statuts, matrice et inerties ; le
second teste les régressions. Aucun ne certifie les faits ou l'utilité scientifique de l'alphabet.

## Les quatre modes

| Mode | Demande typique | Couches | Sortie |
|---|---|---|---|
| **LIRE** | « lis cette situation » | 0–2 | état daté, preuves et alternatives, sans prévision |
| **PRÉVOIR** | « que peut-il se passer d'ici… » | 0–5 et journal | événements définis, résultats du moteur ou non-estimation motivée |
| **CODER** | « code ce cas historique » | 0–3 | fiche validée ou archive à revoir explicitement exclue |
| **SCORER** | « voici ce qui s'est produit » | 6 | journal contrôlé, scores, exclusions, épisodes comparables |

## Ce qu'il faut charger

| Situation | Fichiers |
|---|---|
| Tout mode | ce fichier ; principes de `constitution.md` §2 et §5–6 |
| LIRE | `protocole.md` couches 0–2 ; `strates.md` ; `cartes-index.md` ; `grammaire.md` |
| PRÉVOIR | parcours LIRE, puis couches 4–6 du protocole ; `graphe.md`, `simulation.md` |
| CODER | parcours LIRE, puis couche 3 du protocole ; `base-de-cas.md` |
| SCORER | `validation.md` et couche 6 du protocole ; ne charger cartes/strates que pour un diagnostic demandé |
| Après rattachement des faits | les seuls `equivalences/strate-NN.md` concernés |
| Après choix des candidates | les seules fiches concernées de `cartes.md` |
| Paire incompatible ou configuration | `antagonismes.md` |
| Justification d'une dynamique | la fiche concernée de `dynamiques.md` ; la matrice est lue par le moteur |
| Ambiguïté ou exemple | l'exemple concerné de `exemples.md` ; un terme dans `glossaire.md` |
| « Où en est le skill ? », « que reste-t-il à faire ? » | `feuille-de-route.md` et `moteur.py bilan` |
| Situation française : chercher un fait, une source de résolution, une série chiffrée | `sources-france.md` |
| Sortie LIRE : « ce que l'alphabet ne voit pas ici » | `angles-morts.md` |
| Pourquoi une règle 0.6.x existe (garantie, option, barreau, jugement scellé, sensibilité, corroboration) | `apports-theoriques.md` |
| Politique intérieure (gouvernement, Parlement, partis, élections, mobilisations) | strate 13 : `strates.md` §2 et §4, `equivalences/strate-13.md` |

Lire par rubrique (`rg -n '^##|^\*\*[OAGBTSV][0-9]' references/protocole.md`, ou `grep -nE` avec le même
motif si `rg` est absent, puis plage utile).
Ne pas charger toutes les références pour scorer un fichier. Aucun renvoi à une règle n'autorise
à l'inventer : ouvrir sa rubrique si elle devient nécessaire.

## Calcul : le moteur

Tout chiffre vient du moteur ; le modèle choisit les événements et contrôle le sens des preuves.

| Commande | Usage |
|---|---|
| `python3 scripts/moteur.py calculer --etat "…" --evenement "SEUIL@7 apparait" --json` | un événement, sortie structurée et empreintes ; avec `--json`, une erreur sort aussi en JSON (`{"erreur": …, "code": 2}`) |
| `… calculer --base B --etat "…" --evenement "…" --date-information AAAA-MM-JJ --references R.json` | base validée, références propres à chaque événement |
| `… calculer … --pas 4 --semantique presence` | présence à l'horizon ; alternatives : au-moins-une-fois, continue selon l'événement |
| `… calculer … --sans-cartes` | ablation : référence sans multiplicateurs ni sélection d'homologues |
| `… calculer … --temporalite programmee` (ou `duree_de_vie`) | échéance programmée ou durée de vie propre : « non estimée » sans référence de domaine ni cas |
| `… trajectoires --etat "…" --pas 2 [--strates 11,8] --json` | exploration à un changement par pas |
| `… valider B.jsonl` | validation commune aux fiches et au calcul |
| `… partager C-0042-S07` | partage par empreinte, fixé avant codage |
| `… bilan [--references R.json] [--journal J.jsonl]` | position mesurée sur la feuille de route |
| `… equivalences --carte SEUIL` | les 13 équivalents d'une carte (marqueur local, statut) : utile à l'étape 2 |
| `… scorer J.jsonl` | validation du journal, score des questions et épisodes |
| `… sceller J.jsonl` | empreinte à publier avant échéance ; ne prouve pas seul la prépublication |
| `… sceller-jugement --question Q --evenement E --p 0.3 --date AAAA-MM-JJ` | empreinte de votre propre probabilité, à calculer **avant** le moteur ; à recopier dans `jugement_scelle` |
| `… audit` / `… autotest` / `… parametres` | intégrité / tests / table documentaire générée ; l'audit vérifie la forme et les recoupements internes, pas la justesse du contenu |

`--fref` n'est admis que pour un événement simple, avec `--source-ref`, `--periode-ref`,
`--disponible-ref`. Pour les composés, utiliser `--references` et `--resolution` (formats :
`graphe.md`). L'horizon multiple des composés est refusé. F/f est une confiance, pas une grandeur :
`se renforce` et `s'affaiblit` sont refusés en prévision. F qualifie la lecture (fait précis, toutes
les voisines passées), pas le statut de l'équivalent : F est permis sur un équivalent Proposé, signalé
« équivalent non vérifié », et impossible sur un équivalent Vide (A3, A6). Le moteur affiche le marqueur
local que la résolution doit mesurer (S1). Les quatre cas réels historiques sont des archives exclues.

**Sans shell** : fournir la lecture et les commandes, sans probabilité. Si une estimation requiert une
référence absente, annoncer « non estimé », demander cette donnée ou proposer un événement mesurable.

## Fichiers de l'utilisateur

Le skill ne garantit aucune mémoire entre sessions. Identifier les fichiers réellement fournis.

| Fichier | Contenu | Format |
|---|---|---|
| `base-de-cas.jsonl` | fiches actives ou archives exclues | `base-de-cas.md` §2 |
| `journal-previsions.jsonl` | prévisions figées puis scores ajoutés | `validation.md` §1 |
| `journal-lacunes.md` | motifs et difficultés de lecture, séparés des erreurs du moteur | `validation.md` §6 |

Produire les lignes à conserver ; écrire dans les fichiers si l'utilisateur le demande. Ne pas
modifier un ancien pari. Les données fictives exigent `--demo` et sont exclues de toute évaluation.
Sans base éligible, ρ3 avec référence externe, ρ4 sinon ; afficher également l'absence de calibration.

## Procédure — mode PRÉVOIR

**0. Recevabilité.** Demander les faits manquants et un horizon précis. Ne pas déduire des faits d'un
ressenti, diagnostiquer ou décider sur une personne. Une question de conseil peut donner lieu à une
exploration des suites, sans faire passer celle-ci pour une prescription.

**1. Strates (O1).** Rattacher les faits selon leur mécanisme ; charger les équivalents concernés.

**2. Candidates.** Tester 2 à 4 candidates par strate, dont une contre-candidate ; ouvrir leurs fiches.

**3. Ancrage (A1, A5, A6).** Citer fait, objet, source, date ; attribuer F/f selon la preuve. F exige un
fait précis, une ligne A6 qui passe **toutes** les voisines de la carte (`cartes.md`), sans `?`, une
**garantie** (mécanisme, attendu, contredirait : forme type dans la fiche) et une **option** (acteur,
option avant, option après : un fait qui ne change l'espace d'action de personne ne s'ancre pas) ;
équivalent Vide : au plus f. Lister les équivalents Proposés dans « À vérifier auprès de vous ». Ne
jamais rétablir « Documenté » à partir d'un souvenir bibliographique.

**4. Anti-résonance (A7).** Chercher la contre-observation dans la situation, classer sa portée et
appliquer sa conséquence ; une contre-observation substantielle n'est pas compatible avec F maintenu.
Dans une fiche : champ `portee`, force notée après A7, `force_initiale: "F"` si elle a baissé.

**5. État (G1–G6).** Date, fenêtre, mots, objets, liaisons, lignes A6 et Q ; positions avec ≥3 mots.
Sortie LIRE, en plus : 1 à 3 questions qui départagent deux cartes (abduction), « ce que l'alphabet
ne voit pas ici » (`angles-morts.md`), coût du codage (faits écartés, candidates non retenues, rejets A7).
État nul : pas de prévision par défaut. → LIRE s'arrête ici. → CODER suit `base-de-cas.md` et `valider`.

**6. Événements et résolution.** Définir 2 à 5 questions observables, sans quotas forcés de rupture.
Figer objet, source, critère, seuil et sémantique temporelle. Une intensification porte sur une
mesure réelle, jamais sur f → F. Un événement fixé par un calendrier (scrutin, proclamation, échéance)
ou un phénomène à durée de vie propre (cyclone, grève) exige une référence externe ou reste non
chiffré : `calculer --temporalite programmee|duree_de_vie` (`simulation.md` §4). Déclarer binaire ou partition ; tester l'exclusivité et l'exhaustivité.

**7. Calcul.** **D'abord** écrire sa propre probabilité, en chiffre (un « probable » se fait préciser,
jamais convertir), et la sceller (`sceller-jugement`), **puis**
valider la base, fixer la date d'information et exécuter le moteur avec `--json` ; l'ordre est la
condition pour que l'écart jugement / moteur mesure ce que le moteur ajoute (le scellé prouve que le
jugement n'a pas été modifié, pas qu'il est antérieur : seul un dépôt externe daté le prouve). Recopier la bande de
sensibilité : si elle traverse 50 %, dire « non identifié ».
Recopier le résultat complet, ses références, avertissements et empreintes. Aucun cas/source futur.
Pour un composé sans référence conditionnelle : non estimé. Ne pas recycler une fréquence pour un
autre événement ni arrondir l'horizon sans l'indiquer. Recopier aussi `p_sans_cartes` : si les cartes
ne déplacent pas p, le dire, car la question ne teste alors que l'inertie (persistances et
disparitions sans base, notamment).

**8. Horizon et proxémie.** Choisir présence finale, occurrence au moins une fois ou persistance
continue. Comparateur au même horizon. Trajectoires seulement si utiles, avec leur masse abandonnée.

**9. Journal.** Conserver les probabilités non arrondies, la résolution, l'épisode, les empreintes,
`rejeu`, `fictif` et les conditions de prépublication. Les lignes sans preuve restent hors V4. Une
question nominative (« qui sera élu ? ») n'est pas un événement de carte : la journaliser avec
`"origine": "jugement"` et une probabilité humaine, scorée à part (`validation.md` §1). Rejeux
successifs : du plus ancien au plus récent ; une issue déjà vue rend la question `rejeu: true`.

**10. Sortie.** Suivre `simulation.md` : analytique, symbolique sans chiffre, lignes de journal,
points à vérifier. Expliquer ce que les données permettent et ce qui reste non estimé.

## Limites

- Le moteur est **associationnel** (barreau A de Pearl) : il extrapole des motifs observés et ne
  répond ni à « que produirait telle action ? » ni à « que se serait-il passé autrement ? ». Toute
  sortie se lit « si le motif observé se répète, alors… ».
- L'alphabet décrit des structures, pas des issues nominatives : qui gagne, quel nom, quel effectif
  exact relèvent du jugement, journalisé à part (`origine: jugement`).
- Treize équivalents ont une référence lue, tous en strate 7 : 13 Documenté, 182 Proposé,
  13 Vide. Les 117 anciens
  Documentés sont rétrogradés. Aucun cas réel actif : les quatre premiers, codés avant les règles
  courantes, sont archivés (décision d'auteur, 0.6.8) ; le premier cas actif sera codé sous la version
  courante, de préférence avant son issue (`feuille-de-route.md`, étape 2).
- Multiplicateurs et inerties non calibrés ; aucune performance prospective démontrée.
- Intervalles conditionnels approximatifs ; incertitudes de codage/modèle non intégrées ; pas
  d'intervalle joint pour les composés et les horizons multiples.
- Un seul changement par pas en trajectoire ; ni simultanéité ni distribution de trajectoires calibrée.
- L'accord κ et la vérification scientifique des sources/résolutions restent humains.
- La strate 12 est un registre de longue durée, pas un domaine (décision d'auteur, `strates.md`) : un
  fait n'y entre que si sa signification dépend d'une période de plus d'un siècle.

## Où en est le skill

Le cadre et le moteur sont complets ; ce qui manque est empirique ou relève de l'auteur.
`references/feuille-de-route.md` liste les étapes restantes, dans l'ordre : installation (0),
décisions d'auteur (1 : 1a, 1b et 1c prises), cas réels (2), strate
pilote (3), fréquences externes (4), base réelle et second codeur (5), code différé (6), test à
l'aveugle. `python3 scripts/moteur.py bilan [--references R.json] [--journal J.jsonl]` mesure les étapes
2 à 5 et le test à l'aveugle ; les autres sont déclarées au journal de progression du document.
À une question sur l'avancement, exécuter `bilan` puis lire le journal de progression, plutôt que de
répondre de mémoire. Toute construction ad hoc d'un codage (carte, strate ou règle inventée en
cours de route) s'inscrit dans `assets/rabbits.jsonl` : c'est une dette, pas une solution.

## Articulations

| Skill | Relation |
|---|---|
| `nexus-arche` | parent descriptif ; LIRE fonctionne aussi de façon autonome ici |
| `prediction-engine`, `superforecasting-protocol` | reformulation des événements ; ne remplacent pas le moteur |
| `calibration-engine` | suivi complémentaire ; journal exportable, mêmes critères de résolution |
| `bayesian-updater` | nouvelle prévision versionnée, sans réécriture de l'ancienne |
| `osint-intel` | recherche et vérification des faits et classes de référence |
| `stele` | compression symbolique sans ajouter de fait ni de chiffre |
| `zetetique-broch` | audit des interprétations et hypothèses |

Ces articulations sont facultatives. L'absence d'un autre skill n'empêche pas les modes autonomes.
