# Alphabet situationnel — Feuille de route

> Version : 0.5.1

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
| 1 | Trois décisions d'auteur | auteur | les trois choix sont inscrits au §9 et appliqués | 1a et 1c prises ; 1b reportée (§9) |
| 2 | Recoder les 4 cas réels | Claude, puis auteur | les 4 fiches sont `actif` et `valider` les reçoit | mesuré (`bilan`) |
| 3 | Sourcer une strate pilote | Claude cherche, auteur vérifie | 16/16 équivalents Documentés ou Attestés dans la strate | mesuré (`bilan`) |
| 4 | Bibliothèque de fréquences externes | Claude cherche, auteur vérifie | une référence vérifiée par type d'événement prévu dans la strate pilote ; sources : `sources-france.md` | mesuré (`bilan --references`) |
| 5 | Base réelle et second codeur | auteur, second codeur | 3 cas homologues (ρ1), puis 20 cas double-codés et 20 % (sortie du mode solo) | mesuré (`bilan`) |
| 6 | Code différé | Claude | déclenché par les données, voir §7 | déclaré (§9) |
| — | Test à l'aveugle | auteur | 50 épisodes comparables et gain mesuré (jalon V4) | mesuré (`bilan --journal`) |

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
| **1b · Cartes à agents** (RÉCIPROCITÉ, RÉCURSIVITÉ, COMMUNAUTÉ), qui portent 8 des 12 cases Vides, surtout en strates 1, 2 et 11 | A. universelles, cases Vides à combler ; B. universelles aux systèmes à agents : ces cases passent « Hors domaine » | **reportée.** Le statut Hors domaine existe depuis 0.4.8 (A3, moteur, audit) mais n'est attribué à aucune case |
| **1c · Licence et auteur** | — | **prise (0.4.8) : MIT, Othman Ben Brahim.** `LICENSE`, README, SKILL.md |

Pour appliquer 1b le moment venu : dans chaque `equivalences/strate-NN.md` concerné, passer la case
de Vide à Hors domaine avec le motif en colonne Référence, puis mettre à jour la ligne Bilan, le
tableau et la liste des cases Vides de `equivalences.md` §3 et les totaux de `protocole.md` (A3) ;
`audit` refuse toute divergence et toute case Hors domaine sans motif.

---

## 4. Étape 2 · Recoder les cas réels

**Fait (0.4.7).** Les quatre fiches sont recodées dans `assets/cas-reels.jsonl` avec le statut
`proposition` : contrôlées comme des cas actifs (A6, A7, G6, fenêtres, objets, disponibilité), elles
restent exclues des calculs. Le témoignage original est conservé sans réécriture dans
`assets/cas-reels-originaux.jsonl`.

**Décisions du recodage, à confirmer ou à contester** (chaque fiche les porte aussi, champs `codeur`,
`rejets_a7`, `renforcements_refuses`, `note_recodage`) :

| Cas | Décision | Règle |
|---|---|---|
| France C-0001-S05 | fenêtre 7 → 6 jours (19 → 25 octobre) | G5 |
| | COMMUNAUTÉ@5, INCERTITUDE@5, CONTRAINTE@8 du 19 octobre rejetées : f avec contre-observation substantielle | A7 |
| | CONTRAINTE@8 de l'issue recodée F sur l'objet « manifestation du 24 octobre », ligne A6 complète | A6, A7 |
| Ukraine C-0002-S07 | POLARITÉ et RÉSEAU : F → f (« F maintenu » malgré une contre-observation substantielle) | A7 |
| | état du 19 disponible le 23 (source rétrospective) | B1 |
| Yémen C-0003-S07 | POLARITÉ : F → f ; ligne A6 de CONTRAINTE complétée (TRACE·MÉMOIRE) | A6, A7 |
| | renforcements RÉSEAU et CROISSANCE de l'issue refusés : la structure ne change pas, cas sans événement ; l'escalade est à prévoir par « POLARITÉ@7 s'intensifie » avec une série chiffrée | A7, B4 |
| Alberta C-0004-S05 | fenêtre 6 → 7 jours (18 → 25 octobre) | G5 |
| | POLARITÉ et CONTRAINTE : F → f | A7 |

**Reste à faire par l'auteur, fiche par fiche :**

1. Lire chaque source citée dans `fait`, `source` et `retraits` ; corriger la fiche si une source ne
   dit pas ce qui lui est attribué.
2. Confirmer ou contester les décisions ci-dessus ; une lecture initiale F d'un mot rejeté se rétablit
   en f avec `force_initiale: "F"` et une ligne A6 complète.
3. Passer `sources_verifiees` à `true` et `statut_donnees` à `actif`.
4. `python3 scripts/moteur.py valider assets/cas-reels.jsonl` puis `bilan`.

Les quatre cas ont été codés après leur issue (rejeux) : c'est admis pour une base de cas, qui
enregistre des transitions passées, mais leurs prévisions associées restent hors V4.

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
| 2026-10-26 | 0 | À faire : installer la 0.5.1 |
