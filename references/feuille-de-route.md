# Alphabet situationnel — Feuille de route

> Version : 0.6.13

> Ce qui reste à faire pour que le skill passe de cadre cohérent à instrument éprouvé, dans l'ordre,
> avec qui fait quoi et à quoi l'on reconnaît qu'une étape est terminée. Les étapes mesurables sont
> calculées par `python3 scripts/moteur.py bilan [--references R.json] [--journal J.jsonl]` : leur
> état ne s'écrit pas à la main, il se lit. Les décisions et l'installation sont déclarées ci-dessous,
> dans le journal de progression (§9).

---

## 1. Vue d'ensemble

| Étape | Objet | Qui | Terminée quand | État |
|---|---|---|---|---|
| 0 | Installer la version courante | auteur | le skill installé porte la version de `assets/parametres.json` | déclaré (§9) |
| 1 | Trois décisions d'auteur | auteur | les trois choix sont inscrits au §9 et appliqués | prises (§9) |
| 2 | Premiers cas réels sous les règles courantes | auteur, Claude assiste | au moins un cas `actif`, codé sous la version courante, de préférence avant son issue, relu par l'auteur | mesuré (`bilan`) |
| 3 | Sourcer une strate pilote | Claude cherche, auteur vérifie | 16/16 cases traitées dans la strate (Documenté, Attesté, Vide clos ou Hors domaine) | mesuré (`bilan`) |
| 4 | Bibliothèque de fréquences externes | Claude cherche, auteur vérifie | une référence vérifiée par type d'événement prévu dans la strate pilote ; sources : `sources-france.md` | mesuré (`bilan --references`) |
| 5 | Base réelle et second codeur | auteur, second codeur | 3 cas homologues (ρ1), puis 20 cas double-codés et 20 % (sortie du mode solo) | mesuré (`bilan`) |
| 6 | Code différé | Claude | déclenché par les données, voir §7 | déclaré (§9) |
| — | Test à l'aveugle | auteur | 50 épisodes comparables et gain mesuré (jalon V4) | mesuré (`bilan --journal`) |

**Versions à venir** (apports théoriques, `apports-theoriques.md` §4 ; chaque bloc attend sa condition) :

| Version | Thème | Contenu | Condition |
|---|---|---|---|
| 0.6.0 (faite) | Déclarer et mesurer | barreau, garantie et option, questions, jugement scellé, sensibilité, difficulté, angles morts, rabbits | — |
| 0.7 | Structurer | objets-frontière sourcés (strate 7 en cours, §5) ; cases Vides à combler (décision 1b = universelles) ; échelle de dureté (portes par niveau ρ, date de révision des sources) | étapes 2 et 3 |
| 0.8 | Éprouver | séquence H1.6 (motifs ordonnés) ; banque de cas adverses ; mode « scénarios » à la manière d'ACH (`apports-theoriques.md` §7) | 30 cas actifs dans une strate |
| 1.0 | Grammaire | cartes comme règles de transformation, écrites par un rédacteur indépendant de la matrice puis comparées à elle ; liaisons comme opérateurs ; dérivation de l'alphabet en note séparée | rédacteur indépendant |

Le test à l'aveugle peut commencer dès la fin de l'étape 2. Avant les étapes 3 et 4, il mesure la
lecture structurelle, pas la calibration : sans équivalent sourcé ni fréquence externe, toute
prévision réelle est ρ4.

---

## 2. Étape 0 · Installer la version courante

Le skill installé dans le compte doit être remplacé à chaque version livrée, sinon les conversations
suivantes appliquent d'anciennes règles. Contrôle : `python3 scripts/moteur.py audit` dans le dossier
installé affiche la version attendue.

---

## 3. Étape 1 · Décisions d'auteur

Trois questions de structure, sans réponse technique.

| Décision | Options | État |
|---|---|---|
| **1a · Strate 12 (Histoire longue)**, échelle de temps et non domaine | A. la garder comme registre de longue durée ; B. la supprimer et ajouter un attribut de durée aux faits | **prise (0.4.8) : A.** Appliquée dans `strates.md` |
| **1b · Cartes à agents** (RÉCIPROCITÉ, RÉCURSIVITÉ, COMMUNAUTÉ), qui portent 8 des 12 cases Vides, surtout en strates 1, 2 et 11 | A. universelles, cases Vides à combler ; B. universelles aux systèmes à agents : ces cases passent « Hors domaine » | **prise (2026-10-27) : A, universelles.** Les cases Vides restent à combler ; Hors domaine reste disponible pour un autre motif, attribué à aucune case |
| **1c · Licence et auteur** | — | **prise (0.4.8) : MIT, Othman Ben Brahim.** `LICENSE`, README, SKILL.md |

Conséquence de 1b = A : une case Vide d'une carte à agents (par exemple RÉCIPROCITÉ@1) est une
lacune de recherche, pas une impossibilité. La combler demande un équivalent qui remplit le marqueur
abstrait de la carte sans supposer d'agent, ou une raison documentée de ne pas en trouver. Si une case
devait un jour passer Hors domaine pour un autre motif : la modifier dans `equivalences/strate-NN.md`
avec le motif en colonne Référence, puis mettre à jour la ligne Bilan, `equivalences.md` §3 et les
totaux de `protocole.md` ; `audit` refuse toute divergence et toute case Hors domaine sans motif.

---

## 4. Étape 2 · Premiers cas réels sous les règles courantes

**Les quatre premiers cas sont abandonnés (décision d'auteur, 2026-10-27, 0.6.8).** Codés après leur
issue (rejeux), sous les règles 0.3 à 0.4, recodés par Claude en 0.4.7 et 0.6.0 sans relecture humaine,
deux de leurs ancrages F ne remplissaient plus les marqueurs de la strate 7 une fois Documentée. Les
activer aurait demandé la relecture complète de leurs sources pour des cas qui ne pouvaient de toute
façon pas tester une prévision. Ils restent dans `assets/cas-reels.jsonl` en `archive_a_revoir` (motif
dans chaque fiche) : exclus de tout calcul, conservés comme trace de ce qui a fait naître les lacunes 1
et 2, la strate 13 et la règle « origine jugement ». Le témoignage original reste dans
`assets/cas-reels-originaux.jsonl`. La lacune 3 est close avec eux.

**Ce qui remplace l'étape.** Coder un premier cas réel sous la version courante, de préférence
**prospectif** : une situation en cours, codée à sa date, avant l'issue. Un tel cas sert deux fois :
il entre dans la base quand l'issue est connue, et les prévisions faites à T0 sont les premières
questions éligibles au test à l'aveugle (V4), ce qu'aucun rejeu ne peut être. Ordre :

1. Choisir une situation de la strate pilote (7) ou de la strate 13, avec des sources datées.
2. LIRE puis CODER selon `base-de-cas.md` §3 : questions qui départagent, garantie, option et
   `corroboration` pour chaque F, contre-observations, ligne A6.
3. Si Claude propose le codage : `codage.recodage`, puis relecture et `codage.recodage_confirme`.
4. Sceller votre jugement (`sceller-jugement`), puis calculer et journaliser 2 à 5 prévisions.
5. À l'échéance : coder l'issue, `statut_donnees: actif`, `valider`, `scorer`, `bilan`.

Les épisodes déjà cités dans le skill (France, Ukraine, Yémen, Alberta, sénatoriales, présidentielle
brésilienne, ouragan Polo) ont servi à corriger le moteur : ce sont des tests de régression, plus des
épreuves de généralisation. Le premier test de l'apport des cartes porte sur des épisodes nouveaux,
critères fixés avant l'issue, scores **et** abstentions mesurés ensemble.

---

## 5. Étape 3 · Sourcer une strate pilote

Recommandation : strate 7 (géopolitique). Trois des quatre cas réels y sont, et les sources codées y
sont abondantes (ACLED, UCDP, POLECAT, GDELT). Alternative pour les situations françaises : la
strate 13 (politique intérieure, ajoutée en 0.5.0), dont les sources officielles sont inventoriées dans
`sources-france.md` (open data de l'Assemblée et du Sénat, résultats électoraux, Légifrance).

Pour chaque équivalent de `equivalences/strate-07.md` : trouver une référence qui soutient **la
traduction exacte et son marqueur local**, la lire, puis passer le statut de Proposé à Documenté avec
la référence dans la colonne Référence, et mettre à jour la ligne Bilan du fichier, le tableau de
`equivalences.md` §3 et les totaux de `protocole.md` (A3) et de `SKILL.md`. `audit` recalcule ces
totaux et refuse toute divergence. Une référence de mémoire ne suffit jamais (A3).

Effet : rien sur le calcul dans la strate (F n'en dépend plus depuis 0.4.1) ; ouverture de l'emprunt
entre strates (T4) dès qu'une seconde strate est sourcée.

### 5.1 Strate 7 · références candidates (0.6.1)

Trouvées par Claude le 27 octobre 2026 : chaque référence existe (catalogue d'éditeur, notice ou
première page consultés) et son résumé nomme le phénomène. En 0.6.1, aucun texte n'avait été lu en entier ; en 0.6.2 et 0.6.3, Claude a lu
les textes accessibles et promu ceux dont un passage soutient l'équivalent (colonne État). Pour
les autres, lire le passage, confirmer le nom local, trancher l'écart, puis passer la case en
Documenté avec la référence et le nom local « … » (A3).

Prêt : la référence couvre l'équivalent tel quel. Ajuster : elle couvre l'équivalent si le marqueur
ou l'intitulé change. À trancher : l'équivalent est peut-être mal placé.

| Carte | Référence candidate | Nom local | Écart à trancher | État |
|---|---|---|---|---|
| SEUIL | Morgan, F. E. et al. (2008), *Dangerous Thresholds*, RAND MG-614-AF (remplace Kahn 1965) | « escalation thresholds » | marqueur changé : seuils reconnus par les parties ; « rupture diplomatique » et « annexion déclarée » retirés | **Documenté (0.6.4)** : texte lu, p. xiii, 8, 17 |
| RÉCIPROCITÉ | Axelrod, R., Keohane, R. O. (1985), « Achieving Cooperation under Anarchy », *World Politics* 38(1), 226-254 (remplace Keohane 1986, non accessible) | « Tit-for-Tat » | — | **Documenté (0.6.3)** : texte lu, p. 244-245, 249 |
| PÉRIODICITÉ | Payne, A. (2019), « Presidents, Politics, and Military Strategy », *International Security* 44(3), 163-203 (Gaubatz 1999 et 1991 non accessibles) | « electoral cycle » | résumé seulement ; le texte n'est pas en libre accès | Proposé : à lire |
| RÉCURSIVITÉ | Gustafson, K. et al. (2024), « Intelligence Warning in the Ukraine War », *Intelligence and National Security* 39(3), 400-419 (remplace Buzan et al. 1998) | « prebuttal » | intitulé changé : « Évaluation publiée devenue acte du conflit » ; la sécuritisation (énoncé d'acteur) est abandonnée | **Documenté (0.6.4)** : texte lu, p. 400, 405 |
| ÉMERGENCE | de Souza, E. M. (2008), « Re-evaluating the Contribution and Legacy of Hedley Bull », *Brazilian Political Science Review* 2(1), 96-126, citant Bull 1977, p. 13 (remplace Bull, non accessible) | « international society » | intitulé changé : chez Bull, la gestion par les grandes puissances est une institution de la société internationale ; « sans puissance dominante » et « sans traité » sont retirés | **Documenté (0.6.3)** : texte lu ; Bull cité, non lu directement |
| HIÉRARCHIE | Zarakol, A. (2017), « Theorising Hierarchies », dans *Hierarchies in World Politics*, Cambridge University Press (remplace Lake 2009) | « vertical relations of super- and subordination » | marqueur changé : veto et préséance retirés (non soutenus par la source) ; protectorat, alliance inégale, sphère d'influence | **Documenté (0.6.4)** : extrait lu, p. 1-2 |
| RÉSEAU | Hafner-Burton, E. M., Kahler, M., Montgomery, A. H. (2009), « Network Analysis for International Relations », *International Organization* 63(3), 559-592 (remplace Crawford 2003) | « brokerage » | intitulé changé : « État courtier entre groupes » | **Documenté (0.6.4)** : texte lu, p. 571 |
| POLARITÉ | Wayman, F. W. (1984), « Bipolarity and War », *Journal of Peace Research* 21(1), 61-78 (remplace Waltz 1964, non accessible) | « cluster bipolarity » | Wayman distingue la bipolarité de puissance (deux puissances dominantes) de la bipolarité de blocs ; le marqueur « deux blocs, alignements exclusifs » est la seconde | **Documenté (0.6.3)** : texte lu, p. 63 |
| INCERTITUDE | Chang-Liao, N., Fang, C. (2021), « The Case for Maintaining Strategic Ambiguity in the Taiwan Strait », *The Washington Quarterly* 44(2), 45-60 (remplace Pan 2003, non accessible) | « strategic ambiguity » | — | **Documenté (0.6.3)** : texte lu, p. 46 |
| CONTRAINTE | Morgan, Bapat, Kobayashi (2014), TIES, *Conflict Management and Peace Science* 31(5) ; Woolf (2010), CRS R40084 (remplacent Hufbauer et al. 2007) | « economic sanctions » ; « limits … the number of delivery systems and … warheads » | complété : les traités de limitation sont couverts par Woolf | **Documenté (0.6.4)** : textes lus |
| PROPORTION | Singer, J. D., Bremer, S., Stuckey, J. (1972), « Capability Distribution, Uncertainty, and Major Power War, 1820-1965 », dans B. Russett (dir.), *Peace, War, and Numbers*, Beverly Hills, Sage, 19-48 | « indice composite des capacités nationales » (CINC) | — | **Documenté (0.6.2)** : documentation NMC v5.0 lue, p. 8-9 ; le chapitre de 1972 n'est pas accessible en ligne |
| TRANSFORMATION | Wallander, C. A. (2000), « Institutional Assets and Adaptability: NATO After the Cold War », *International Organization* 54(4), 705-735 | « persistence through its adaptation » | **tranché** : l'équivalent devient « Adaptation d'une alliance » ; la transition de régime pactée relève de la strate 13 (à y proposer) | **Documenté (0.6.4)** : texte lu, p. 711, 716, 731 |
| TRACE·MÉMOIRE | CIJ (1986), *Différend frontalier (Burkina Faso/Mali)*, arrêt du 22 décembre, par. 20-23, 30 (remplace Ratner 1996) | « uti possidetis » | intitulé réduit aux frontières héritées ; les griefs sont retirés. Source jurisprudentielle, pas doctrinale | **Documenté (0.6.4)** : texte lu |
| CROISSANCE | Choucri, N. (2017), « The Theory of Lateral Pressure », *Oxford Encyclopedia of Empirical IR Theory* ; Altman 2017 | « lateral pressure » ; « fait accompli » | aucune des deux ne montre un taux d'expansion qui dépend de la grandeur atteinte, ni une limite de capacité : la carte n'est pas soutenue | Proposé : source à trouver |
| COMMUNAUTÉ | Olson, M., Zeckhauser, R. (1966), « An Economic Theory of Alliances », *Review of Economics and Statistics* 48(3), 266-279 | « partage du fardeau » (les plus grands membres portent une part disproportionnée, p. 268) | — | **Documenté (0.6.2)** : texte lu, p. 267-268 |
| RÉSONANCE | Beissinger 2007 (lu) ; recherche de synchronisations géopolitiques sans résultat | — | la vague est une diffusion ; les synchronisations documentées sont économiques (strate 6) | **Vide (0.6.4)** |

Bilan après lecture (0.6.4) : 13 Documentés sur textes lus, passage cité ; 2 Proposés (PÉRIODICITÉ :
texte fermé ; CROISSANCE : aucune source ne soutient la carte) ; 1 Vide (RÉSONANCE). Onze références
d'origine sont remplacées par des textes en libre accès. Une promotion n'exige pas que ce soit l'auteur
qui lise, mais qu'un texte soit lu et le passage cité ; l'auteur peut contester chacune.

**Conséquence pour le codage (A1).** Les équivalents Documentés ont des marqueurs plus précis : un
fait qui ne remplit que le marqueur abstrait de la carte s'ancre par le noyau, en f. C'est ce décalage
qui a, entre autres, conduit à archiver les quatre premiers cas (§4 ; lacune 3, close).

---

## 6. Étapes 4 et 5 · Fréquences externes et base réelle

**Étape 4.** Constituer le fichier passé à `--references` (format : `graphe.md` §2.2) : pour chaque
événement que l'on compte prévoir dans la strate pilote (rupture diplomatique, passage au conflit
armé, cessez-le-feu, suspension de sanctions…), une fréquence publiée, avec source, définition,
période, fenêtre et date de disponibilité. Effet : les prévisions passent de ρ4 à ρ3 (a priori
ancré).

**Étape 5.** Coder de nouveaux cas réels selon `base-de-cas.md` §3, en commençant par la strate
pilote. Seuils, tous lus dans §H :

| Seuil | Effet |
|---|---|
| 3 cas homologues distincts | ρ1 : la prévision s'appuie sur des cas |
| 20 cas double-codés et 20 % de la strate | sortie du mode solo (A4) : ρ0 devient accessible |
| 30 cas homologues distincts | ρ0 |
| 30 % de cas sans événement | fin de l'alerte de biais du survivant (B4) |

Double codage : deux codeurs distincts codent le même état sans voir le travail de l'autre, dont au
moins un humain (A4). L'auteur et Claude, codant séparément, satisfont la règle ; un second humain la
satisfait mieux.

---

## 7. Étape 6 · Code différé

Chaque élément attend une condition de données ; le coder avant serait coder à vide.

| Élément | Condition de déclenchement | Paramètre concerné |
|---|---|---|
| Calcul de l'accord κ par carte | premiers cas double-codés | `kappa_min` (réservé) |
| Pondération continue des homologues par similarité | au moins une strate avec 30 cas actifs | `jaccard_H15` |
| Intervalles des événements composés et multi-pas | premières références conditionnelles vérifiées | — |
| Calibration des multiplicateurs et des inerties | jalon V4 atteint | `lambda`, `inertie` |

---

## 8. Test à l'aveugle

Protocole : `validation.md` §8. Il peut commencer dès que l'étape 2 est terminée ; il ne mesure la
calibration qu'après les étapes 3 et 4. Jalon interne : 50 épisodes comparables et 10 % de gain sur le
comparateur, à titre de jalon et non de preuve.

---

## 9. Journal de progression

Une ligne datée par avancée déclarée : installation, décision d'auteur, élément de code différé.
Les étapes mesurées se lisent dans `bilan`.

| Date | Étape | Avancée |
|---|---|---|
| 2026-10-26 | 2 | Quatre cas réels recodés en `proposition` (0.4.7) ; sources à lire par l'auteur |
| 2026-10-26 | 1 | Décision 1a : strate 12 conservée comme registre de longue durée (option A) |
| 2026-10-26 | 1 | Décision 1c : licence MIT, auteur Othman Ben Brahim |
| 2026-10-26 | 1 | Décision 1b reportée ; statut « Hors domaine » créé, non attribué |
| 2026-10-26 | 1 | Structure : strate 13 « Politique intérieure » ajoutée (0.5.0) |
| 2026-10-26 | 0 | 0.5.1 livrée |
| 2026-10-27 | 2 | Propositions recodées en 0.6.0 (garantie, option, questions) ; sources toujours à lire |
| 2026-10-27 | 1 | Décision 1b : cartes à agents universelles (option A) ; aucune case Hors domaine |
| 2026-10-27 | 3 | Strate pilote 7 : 16 références candidates trouvées par Claude (§5), à lire par l'auteur |
| 2026-10-27 | 3 | Strate 7 : PROPORTION et COMMUNAUTÉ Documentées (textes lus) ; RÉSONANCE à trancher (0.6.2) |
| 2026-10-27 | 3 | Strate 7 : RÉCIPROCITÉ, ÉMERGENCE, POLARITÉ, INCERTITUDE Documentées sur sources en libre accès (0.6.3) |
| 2026-10-27 | 3 | Strate 7 : 13 Documentés, 2 Proposés, 1 Vide (0.6.4) ; trois ancrages de cas réels à revoir (A1) |
| 2026-10-27 | — | Audit de la 0.6.4 traité (0.6.5) : documentation, `difficulte` inversée, bande large, clôture des Vides, rabbits à statut |
| 2026-10-27 | — | Apports CIA et *Spiral Semiosis* triés (0.6.6) : `corroboration`, aucun mot de probabilité sans chiffre ; ACH différé à 0.8 |
| 2026-10-27 | — | Apport *Intuition Machine* (QPT) trié (0.6.7) : `recodage_confirme` avant activation d'un cas proposé par un modèle |
| 2026-10-27 | 2 | Décision d'auteur : les quatre premiers cas réels sont abandonnés et archivés (0.6.8) ; l'étape 2 devient « premiers cas sous les règles courantes, de préférence prospectifs » |
| 2026-10-27 | — | Audit du test brésilien traité (0.6.9) : plafond, journal lié au calcul, événements de calendrier |
| 2026-10-27 | — | Audit V21 et test Polo traités (0.6.10) : journal entièrement lié au calcul, temporalité déclarée |
| 2026-10-27 | — | Audit V22 traité (0.6.11) : abstentions journalisées et comptées, `trajectoires` refuse la temporalité |
| 2026-10-27 | — | Temporalité obligatoire (0.6.12) : le moteur pose la question, Claude la pose à l'utilisateur avec celle du critère |
| 2026-10-27 | — | Audit de la 0.6.12 traité (0.6.13) : M1 à M3, m1 à m7, mineurs |
| 2026-10-27 | 0 | À faire : installer la 0.6.13 |

---

## 10. Liste de contrôle de publication

`audit` contrôle la forme et les recoupements, pas la cohérence entre un texte et une décision : trois
textes périmés ont passé tous les contrôles automatiques en 0.6.4. Avant chaque paquet :

1. `audit` et `autotest` passent ; `valider` passe sur les deux bases.
2. Version identique partout (`audit`), y compris `README.md` et ses plages de versions.
3. Totaux de statuts recoupés (`equivalences.md`, `SKILL.md`, `protocole.md` ; `audit`).
4. Toute décision d'auteur prise est répercutée dans `SKILL.md` (« Où en est le skill ») et ici (§3, §9).
5. Tout champ requis par `valider` figure dans `base-de-cas.md` §2, dans l'exemple **et** le tableau.
6. Tout terme nouveau figure au glossaire.
7. Toute sous-commande nouvelle figure dans la table des commandes de `SKILL.md`.
8. Les exemples montrent la sortie courante (format), pas seulement les valeurs courantes.
9. Aucun texte ne décrit un état révolu (« restante », « à faire », ancienne plage de versions).
10. Tout constat du CHANGELOG qui engage une décision est recopié au journal des lacunes ou ici.
