# Alphabet situationnel — Dynamiques des cartes (couche 4, a priori)

> Version : 0.7.2

> Ce que chaque structure **tend à produire au pas suivant**, proposé comme hypothèse à partir de sa représentation structurelle.
> Ces intensités **modulent** une fréquence de base (T2) : elles ne sont pas des probabilités. Valeurs
> numériques : `protocole.md` §H ; procédure : `graphe.md` §2. La matrice et les inerties de ce fichier
> sont recopiées à l'identique dans `assets/parametres.json`, que lit le moteur ; `moteur.py audit`
> vérifie l'égalité.
>
> **Statut : hypothèses structurelles non calibrées.** Aucun effet inhibiteur n’est estimé dans la
> matrice actuelle ; comparer systématiquement avec la référence sans cartes. Chaque ligne dit une hypothèse de mécanisme associée à la
> carte, avec un mécanisme. Aucune ligne n'est encore vérifiée par la base de cas. La
> couche 6 les corrige (V3) ; une ligne systématiquement démentie est révisée.

---

## 0. Lecture des fiches

- **Inertie** : probabilité a priori que la carte reste ancrée **sur 3 mois** (fenêtre de référence),
  **valeur propre à chaque carte** (§Inerties) ; le moteur la ramène à la fenêtre de l'état. Sa disparition a la probabilité complémentaire.
- **Transitions** : événements que la carte rend **plus probables** au pas suivant, avec une intensité
  (forte F / moyenne M / faible f) traduite en multiplicateur hypothétique λ (§H), et le mécanisme. Sauf mention, l'événement se produit **dans la même
  strate** ; « autre strate » signale une propagation possible (G3, transfert).
- **Indicateurs de bascule** : faits observables qui annoncent la transition. Ils servent à remplir
  le champ « indicateur de bascule » des prévisions (S1).
- **Entrées** : cartes qui mènent le plus souvent à celle-ci (lecture inverse des transitions).
- Les transitions vers « retour à l'état antérieur » ne sont listées que lorsqu'elles sont
  structurellement improbables (SEUIL) ; ailleurs, elles sont couvertes par l'inertie.

---

## SEUIL ⊥
- **Inertie** : 0,97 (forte) — par définition, le retour par le même chemin est fermé.
- **Transitions** :
  - TRACE·MÉMOIRE apparaît — **forte** — le franchissement laisse un résidu qui conditionne la suite
    (inclusion SEUIL ⊂ TRACE).
  - TRANSFORMATION apparaît — **moyenne** — l'entité se réorganise dans le nouveau régime.
  - SEUIL apparaît dans une autre strate — **moyenne** — propagation d'une irréversibilité (défaut
    économique → rupture diplomatique).
  - PÉRIODICITÉ apparaît — **faible** — nouveau régime cyclique après bifurcation.
  - Retour à l'état antérieur par le même chemin — **non documentée** (exclu par la définition).
- **Indicateurs de bascule** (avant franchissement, observés sur les cartes d'entrée) : retour plus
  lent après une perturbation (ralentissement critique), variance et autocorrélation croissantes,
  oscillations entre deux états.
- **Entrées** : CROISSANCE, CONTRAINTE qui se resserre, POLARITÉ en escalade, RÉCURSIVITÉ (panique),
  RÉSEAU (cascade), RÉSONANCE (amplification).

## RÉCIPROCITÉ ⊗
- **Inertie** : 0,65 (moyenne) — la boucle se maintient tant que les retours suivent.
- **Transitions** :
  - POLARITÉ apparaît — **moyenne** — un non-retour déclenche la rétorsion (réciprocité négative,
    donnant-donnant en spirale).
  - HIÉRARCHIE apparaît — **moyenne** — une dette qui ne peut être rendue crée une dépendance
    (relation patron-client).
  - SEUIL apparaît — **faible** — rupture définitive de la relation.
  - COMMUNAUTÉ apparaît — **faible** — élargissement à plus de deux parties.
- **Indicateurs de bascule** : un transfert non rendu à l'échéance d'usage ; rappel explicite d'une
  dette ; retard croissant des contre-transferts.
- **Entrées** : COMMUNAUTÉ qui se fragmente, POLARITÉ en désescalade négociée.

## PÉRIODICITÉ ↻
- **Inertie** : 0,90 (forte) — un cycle limite est stable ; la phase suivante est la transition la plus
  probable.
- **Transitions** :
  - Phase suivante du cycle (même carte, phase avancée) — **forte**.
  - RÉSONANCE apparaît — **moyenne** — couplage avec un autre cycle.
  - SEUIL apparaît — **faible** — un forçage externe brise le cycle.
- **Indicateurs de bascule** : dérive de la période, amplitude croissante, phase manquée.
- **Entrées** : SEUIL (nouveau régime cyclique), CONTRAINTE à échéance fixe, TRACE·MÉMOIRE (rite).

## RÉCURSIVITÉ ↺
- **Inertie** : 0,65 (moyenne) — l'auto-représentation persiste tant qu'elle est diffusée.
- **Transitions** :
  - CROISSANCE {rétroaction amplifiante} apparaît — **moyenne** — prophétie autoréalisatrice.
  - SEUIL apparaît — **moyenne** — une représentation partagée déclenche un basculement (panique,
    retrait massif).
  - CONTRAINTE apparaît — **faible** — l'indicateur détourné est encadré par de nouvelles règles.
  - Disparition — **faible** — prophétie autodestructrice : la prévision publiée annule ce qu'elle
    annonce.
- **Indicateurs de bascule** : publication très diffusée d'une mesure, notation ou prévision ;
  changement de comportement immédiat des acteurs mesurés.
- **Entrées** : HIÉRARCHIE (classements), RÉSEAU (diffusion), INCERTITUDE (recherche de signaux).

## ÉMERGENCE ⊙
- **Inertie** : 0,65 (moyenne) — une régularité naissante reste fragile.
- **Transitions** :
  - TRACE·MÉMOIRE apparaît — **forte** — verrouillage par adoption auto-renforcée.
  - CROISSANCE apparaît — **moyenne** — diffusion par imitation.
  - HIÉRARCHIE ou CONTRAINTE apparaît — **moyenne** — institutionnalisation, codification.
  - Disparition — **faible** — la régularité ne trouve pas d'adoptants.
- **Indicateurs de bascule** : taux d'adoption ; premiers acteurs qui défendent la régularité ;
  première mise par écrit.
- **Entrées** : INCERTITUDE (une forme tranche entre des possibles), RÉSEAU (interactions locales
  denses), CROISSANCE (changement d'échelle).

## HIÉRARCHIE ✦
- **Inertie** : 0,88 (forte) — un ordre de préséance se reproduit.
- **Transitions** :
  - POLARITÉ apparaît — **moyenne** — contestation, surtout au moment d'une succession.
  - TRANSFORMATION apparaît — **faible** — réforme de l'ordre, sommet conservé.
  - SEUIL apparaît — **faible** — renversement.
- **Indicateurs de bascule** : succession ouverte ou incertaine ; perte d'une ressource par le
  sommet ; défections d'échelons intermédiaires.
- **Entrées** : RÉCIPROCITÉ (dette), COMMUNAUTÉ (garant), POLARITÉ (un pôle l'emporte), ÉMERGENCE
  (institutionnalisation).

## RÉSEAU ⊛
- **Inertie** : 0,90 (forte) — une topologie change lentement.
- **Transitions** :
  - PROPORTION apparaît (concentration) — **moyenne** — attachement préférentiel vers les nœuds
    centraux.
  - SEUIL apparaît — **moyenne** — cascade par défaillance d'un nœud central ou perte d'un pont ;
    peut toucher une **autre strate** (chaîne d'approvisionnement → économie).
  - POLARITÉ apparaît — **faible** — fragmentation en deux composantes après perte d'un pont.
- **Indicateurs de bascule** : centralité croissante d'un nœud ; pont unique entre deux groupes ;
  défaillance d'un nœud central.
- **Entrées** : CROISSANCE (expansion), ÉMERGENCE, COMMUNAUTÉ.

## POLARITÉ ⥀
- **Inertie** : 0,85 (forte) — un champ à deux pôles se maintient.
- **Transitions** :
  - CROISSANCE {rétroaction amplifiante} apparaît — **moyenne** — escalade (spirale de rétorsions).
  - SEUIL apparaît — **moyenne** — rupture.
  - HIÉRARCHIE apparaît — **moyenne** — un pôle domine l'autre.
  - RÉCIPROCITÉ apparaît — **faible** — désescalade par échanges conditionnels.
- **Indicateurs de bascule** : rétorsions successives de plus en plus fortes ; disparition des
  intermédiaires ; alignements exclusifs exigés des tiers.
- **Entrées** : RÉCIPROCITÉ (non-retour), RÉSEAU (perte d'un pont), HIÉRARCHIE (contestation).

## INCERTITUDE Ø
- **Inertie** : 0,40 (faible) — les possibles se résolvent avec le temps.
- **Transitions** :
  - ÉMERGENCE apparaît — **moyenne** — une forme tranche entre les possibles.
  - CONTRAINTE apparaît — **moyenne** — une option se ferme (séquentiel, donc compatible avec
    l'incompatibilité sur un même objet *au même moment*).
  - SEUIL apparaît — **faible** — résolution par basculement.
- **Indicateurs de bascule** : échéance de décision ; couvertures qui se défont ; un acteur abandonne
  une option publiquement.
- **Entrées** : CONTRAINTE qui se relâche, RÉSEAU (signaux contradictoires), HIÉRARCHIE (succession
  ouverte).

## CONTRAINTE ⊘
- **Inertie** : 0,90 pour une contrainte formelle, 0,65 pour une contrainte matérielle (option du moteur `--ctr-materielle`) — forte pour une contrainte formelle (loi, traité), moyenne pour une
  contrainte matérielle.
- **Transitions** :
  - RÉSEAU apparaît — **moyenne** — contournement par des canaux parallèles.
  - SEUIL apparaît — **moyenne** — la contrainte se resserre jusqu'à rendre l'état actuel intenable.
  - TRANSFORMATION apparaît — **faible** — adaptation qui conserve l'invariant.
  - Disparition (relâchement) — couverte par l'inertie.
- **Indicateurs de bascule** : coût d'opportunité croissant (ce que la contrainte empêche vaut de plus
  en plus) ; tentatives de contournement documentées ; échéance de révision.
- **Entrées** : CROISSANCE (capacité atteinte), ÉMERGENCE (codification), POLARITÉ (sanctions).

## PROPORTION ◯
- **Inertie** : 0,85 (forte) — tant que l'échelle ne change pas.
- **Transitions** :
  - TRANSFORMATION apparaît — **moyenne** — réorganisation pour restaurer un rapport rompu par un
    changement d'échelle.
  - SEUIL apparaît — **faible** — rupture de proportion non absorbée.
  - POLARITÉ apparaît — **faible** — concentration extrême qui sépare deux groupes.
- **Indicateurs de bascule** : changement d'échelle rapide ; écart croissant à la loi d'échelle
  habituelle.
- **Entrées** : CROISSANCE, RÉSEAU (concentration).

## TRANSFORMATION ∿
- **Inertie** : 0,65 (moyenne) — un processus en cours tend à se poursuivre.
- **Transitions** :
  - TRACE·MÉMOIRE apparaît — **moyenne** — fin du processus, la forme nouvelle se fixe.
  - SEUIL apparaît — **moyenne** — le processus franchit un point de non-retour (tension documentée
    SEUIL ~ TRANSFORMATION).
  - ÉMERGENCE d'une entité nouvelle — **faible** — l'invariant est perdu : ce n'est plus la même
    entité.
- **Indicateurs de bascule** : menace sur l'invariant (mission, membres, identité) ; accélération du
  changement.
- **Entrées** : SEUIL, CONTRAINTE (adaptation), PROPORTION.

## TRACE·MÉMOIRE ◊
- **Inertie** : 0,96 (forte) — par définition, le passé continue d'agir.
- **Transitions** :
  - POLARITÉ apparaît — **faible** — réactivation d'un grief ancien.
  - PÉRIODICITÉ apparaît — **faible** — commémorations, retours rituels.
  - SEUIL apparaît — **faible** — seul un choc rompt un verrouillage.
- **Indicateurs de bascule** : anniversaire d'un événement fondateur ; réactivation publique d'un
  grief ; coût de changement qui chute.
- **Entrées** : SEUIL, ÉMERGENCE (verrouillage), TRANSFORMATION achevée.

## CROISSANCE ▲
- **Inertie** : 0,65 (moyenne) — dépend de la phase (exponentielle, inflexion, saturation).
- **Transitions** :
  - CONTRAINTE apparaît — **forte** — la capacité limite devient active (logistique).
  - SEUIL apparaît — **moyenne** — dépassement de la capacité puis effondrement (bulle).
  - ÉMERGENCE apparaît — **faible** — propriétés nouvelles par changement d'échelle.
  - Peut toucher une **autre strate** : une croissance économique active une contrainte climatique.
- **Indicateurs de bascule** : taux de croissance qui baisse (passage du point d'inflexion) ;
  approche d'une capacité nommée ; financement de la croissance par la croissance elle-même.
- **Entrées** : RÉCURSIVITÉ, ÉMERGENCE (diffusion), RÉSEAU (effets de réseau).

## COMMUNAUTÉ ⟶
- **Inertie** : 0,65 (moyenne) — dépend des sanctions contre les passagers clandestins.
- **Transitions** :
  - SEUIL apparaît (dissolution) — **moyenne** — les passagers clandestins non sanctionnés vident le
    bien commun.
  - HIÉRARCHIE apparaît — **moyenne** — un garant ou une autorité de sanction se met en place.
  - RÉCIPROCITÉ apparaît — **faible** — retour à des échanges bilatéraux.
- **Indicateurs de bascule** : contributions en baisse ; défections sans sanction ; contestation des
  règles d'accès.
- **Entrées** : RÉCIPROCITÉ élargie, ÉMERGENCE, CONTRAINTE commune.

## RÉSONANCE ✶
- **Inertie** : 0,85 (forte) — au-delà du couplage critique, la synchronisation se maintient.
- **Transitions** :
  - CROISSANCE apparaît (amplitude collective) — **moyenne** — des oscillations alignées s'additionnent.
  - SEUIL apparaît — **moyenne** — oscillation synchronisée qui dépasse la tolérance du système ; peut
    toucher une **autre strate**.
  - Disparition (désynchronisation) — couverte par l'inertie, si le couplage faiblit.
- **Indicateurs de bascule** : force de couplage (nombre et intensité des liens) ; alignement de phase
  mesuré ; amplitude commune croissante.
- **Entrées** : PÉRIODICITÉ (cycles couplés), RÉSEAU (couplage).

---

## Barreau des transitions (0.6.0)

Chaque transition porte un barreau de l'échelle de Pearl : **A** association (co-occurrence observée
ou supposée entre cartes), **I** intervention documentée (une action datée produit la carte d'arrivée,
mécanisme établi par une source), **C** contrefactuel documenté. En 0.6.0, **toutes les transitions
sont A** (`barreau` en §H : défaut A, aucune exception). Ce n'est pas un défaut de saisie : c'est la
mesure exacte de ce qui manque au moteur pour répondre à une question causale. Une exception s'inscrit
dans `parametres.json` (`"SRC>CIB": "I"`) seulement avec la source qui documente le mécanisme, et
`audit` refuse toute autre valeur. Conséquence pratique : une transition A ne garantit pas son
transport vers un contexte différent, ce que l'emprunt entre strates (T4, poids 0,5) reconnaissait déjà.

## Synthèse : matrice des transitions a priori

Lignes : carte présente. Colonnes : carte qui apparaît (même strate). F = forte, M = moyenne,
f = faible ; vide = non documentée. Les propagations vers une autre strate admises sans abaissement
sont listées dans les fiches (« autre strate ») et dans `assets/parametres.json` (`autre_strate`).

| De \ Vers | SEU | REC | PER | RCS | EME | HIE | RES | POL | INC | CTR | PRO | TRA | TRC | CRO | COM | RSN |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SEUIL | | | f | | | | | | | | | M | F | | | |
| RÉCIPROCITÉ | f | | | | | M | | M | | | | | | | f | |
| PÉRIODICITÉ | f | | | | | | | | | | | | | | | M |
| RÉCURSIVITÉ | M | | | | | | | | | f | | | | M | | |
| ÉMERGENCE | | | | | | M | f | | | M | | | F | M | f | |
| HIÉRARCHIE | f | | | f | | | | M | f | | | f | | | | |
| RÉSEAU | M | | | f | f | | | f | f | | M | | | f | | f |
| POLARITÉ | M | f | | | | M | | | | f | | | | M | | |
| INCERTITUDE | f | | | f | M | | | | | M | | | | | | |
| CONTRAINTE | M | | f | | | | M | | f | | | f | | | f | |
| PROPORTION | f | | | | | | | f | | | | M | | | | |
| TRANSFORMATION | M | | | | f | | | | | | | | M | | | |
| TRACE·MÉMOIRE | f | | f | | | | | f | | | | | | | | |
| CROISSANCE | M | | | | f | | f | | | F | f | | | | | |
| COMMUNAUTÉ | M | f | | | | M | f | | | | | | | | | |
| RÉSONANCE | M | | | | | | | | | | | | | M | | |

## Transitions ajoutées en v0.3.0 : réconciliation des « Entrées »

Les lignes **Entrées** des fiches, écrites dès la v0.1.0, annonçaient 17 transitions absentes de la
matrice. La matrice ne pouvait donc pas produire RÉCURSIVITÉ ni INCERTITUDE (aucun parent), ni faire
apparaître un RÉSEAU autrement que par contournement d'une CONTRAINTE. Ces 17 transitions sont
ajoutées avec l'intensité **faible** (f), la plus basse : elles rétablissent la cohérence du document
avec lui-même, sans prétendre à une force que rien ne mesure. Leur mécanisme est celui que la fiche de
la carte cible donne déjà. `moteur.py audit` vérifie désormais que chaque entrée annoncée est un parent
dans la matrice.

| De → Vers | Mécanisme (repris de la fiche cible) |
|---|---|
| CONTRAINTE → PÉRIODICITÉ | contrainte à échéance fixe |
| HIÉRARCHIE → RÉCURSIVITÉ | classements publiés |
| RÉSEAU → RÉCURSIVITÉ | diffusion d'une représentation du système |
| INCERTITUDE → RÉCURSIVITÉ | recherche de signaux sur soi-même |
| RÉSEAU → ÉMERGENCE | interactions locales denses |
| COMMUNAUTÉ → RÉSEAU | un collectif tisse des liens |
| CROISSANCE → RÉSEAU | expansion |
| ÉMERGENCE → RÉSEAU | une régularité nouvelle crée des liens |
| CONTRAINTE → INCERTITUDE | une contrainte qui se relâche rouvre des possibles |
| RÉSEAU → INCERTITUDE | signaux contradictoires |
| HIÉRARCHIE → INCERTITUDE | succession ouverte |
| POLARITÉ → CONTRAINTE | sanctions |
| CROISSANCE → PROPORTION | changement d'échelle |
| RÉSEAU → CROISSANCE | effets de réseau |
| CONTRAINTE → COMMUNAUTÉ | contrainte commune |
| ÉMERGENCE → COMMUNAUTÉ | une régularité partagée devient un collectif |
| RÉSEAU → RÉSONANCE | couplage |

Ce qui **n'est pas** ajouté : aucune transition vers TRACE·MÉMOIRE ni vers TRANSFORMATION. Leurs fiches
étaient déjà cohérentes avec la matrice, et les deux tests sur cas réel qui les ont manquées étaient des
rejeux (issue connue avant le calcul). Les modifier sur cette base serait ajuster le modèle à l'issue,
ce que V3 interdit ; elles sont au journal des lacunes.

## Inerties

Probabilité a priori de persistance d'une carte ancrée **sur 3 mois**. Pour une fenêtre de d jours,
le moteur utilise inertie^(d / 91,3) : INCERTITUDE, 0,40 sur 3 mois, vaut 0,93 sur 7 jours. Utilisée
seulement quand la base ne fournit pas de fréquence de persistance stable (`graphe.md` §2.3).

| Carte | Inertie | Justification |
|---|---|---|
| SEUIL | 0,97 | état absorbant : une disparition est plus souvent un défaut de codage qu'un retour |
| TRACE·MÉMOIRE | 0,96 | dépendance au chemin |
| PÉRIODICITÉ | 0,90 | cycle limite stable |
| RÉSEAU | 0,90 | une topologie change lentement |
| CONTRAINTE | 0,90 | contrainte formelle (0,65 si matérielle) |
| HIÉRARCHIE | 0,88 | ordre de préséance qui se reproduit |
| POLARITÉ | 0,85 | champ à deux pôles qui se maintient |
| PROPORTION | 0,85 | rapport stable tant que l'échelle ne change pas |
| RÉSONANCE | 0,85 | synchronisation stable au-delà du couplage critique |
| RÉCIPROCITÉ | 0,65 | boucle entretenue seulement si les retours suivent |
| RÉCURSIVITÉ | 0,65 | dure tant que la représentation est diffusée |
| ÉMERGENCE | 0,65 | régularité naissante, fragile |
| TRANSFORMATION | 0,65 | processus en cours |
| COMMUNAUTÉ | 0,65 | dépend des sanctions contre les passagers clandestins |
| CROISSANCE | 0,65 | dépend de la phase de croissance |
| INCERTITUDE | 0,40 | les possibles se résolvent avec le temps |

## Observation pour l'audit

SEUIL est la cible la plus fréquente (14 des 15 autres cartes y mènent ; seule ÉMERGENCE n'y mène pas ;
en v0.3.0, RÉSEAU a 4 parents, INCERTITUDE et RÉCURSIVITÉ 3 chacune). Cela ne découle pas à lui seul de sa définition, mais cela expose l'outil à un biais : sur-prédire des
ruptures. La couche 6 doit surveiller en priorité le score des prévisions « SEUIL apparaît »
(`validation.md` §4).
