# Alphabet situationnel — Feuille de route

> Version : 0.7.14

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
| 4 | Bibliothèque de fréquences externes | Claude cherche, auteur vérifie | une référence vérifiée par type d'événement prévu dans la strate pilote ; méthode : `frequences-externes.md` ; sources : `sources-france.md` | mesuré (`bilan --references`) |
| 5 | Base réelle et second codeur | auteur, second codeur | 3 cas homologues (ρ1), puis 20 cas double-codés et 20 % (sortie du mode solo) | mesuré (`bilan`) |
| 6 | Code différé | Claude | déclenché par les données, voir §7 | déclaré (§9) |
| — | Test à l'aveugle | auteur | V4 : gain absolu de 2,5 points testé, épisodes ≥ max(50, effectif requis par σ̂(d)) | mesuré (`bilan --journal`) |
| — | Test à trois bras (audit V34, L1) | auteur, Claude assiste | questions futures préenregistrées, trois bras scellés : modèle seul (comparateur externe), inertie (`p_sans_cartes`), alphabet complet ; résultat publié, nul compris (`validation.md` §8) | proposé, non commencé |

**Décisions d'auteur ouvertes par l'audit V34 (0.7.12)** — instruites, non appliquées, parce qu'elles
changent une règle constitutive, un statut ou l'ordre de la feuille de route (`apports-theoriques.md` §16) :
(1) conditionner ρ1 à une homologie discernable du placebo, ce qui ferait de ρ une note de séparation et
plus seulement de provenance ; (2) lire V4 sur l'e-processus plutôt que sur le test exact à effectif
fixe ; (3) un statut d'arête « Éprouvée » (n occasions, k transitions sur cas réels), distinct de
l'échelle des équivalents ; (4) appliquer la règle d'érosion de P1 (`equivalences.md` §4) ; (5) faire le
test à trois bras **avant** la 0.8, et donner un responsable et une échéance au rédacteur indépendant de
la 1.0 — ou renoncer à la clause et l'écrire ; (6) réduire la boîte (une strate entièrement sourcée avant
toute autre) ; (7) dériver ou calibrer λ. **Ajoutées par l'audit comparatif (0.7.13)** : (8) une distribution
jointe sur quelques événements liés, dont trajectoires et événements isolés dériveraient ; (9) des
influences **défavorables** (multiplicateurs < 1, comme les impacts négatifs de CIB), qui changeraient p ;
(10) une similarité relationnelle (objets, rôles, liaisons typées) pour l'homologie ; (11) pour chaque
carte, une définition abstraite commune et ce que chaque traduction locale en conserve.

**Versions à venir** (apports théoriques, `apports-theoriques.md` §4 ; chaque bloc attend sa condition) :

| Version | Thème | Contenu | Condition |
|---|---|---|---|
| 0.6.0 (faite) | Déclarer et mesurer | barreau, garantie et option, questions, jugement scellé, sensibilité, difficulté, angles morts, rabbits | — |
| 0.7.0 (faite) | Prouver et décomposer | tests de preuve du process tracing (F exige un fait suffisant) ; décomposition de Murphy du Brier | — |
| 0.7.14 (faite) | Déclarer l'objet | bloc `modele` (estimande, pseudo-vraisemblance, quotient) ; table lu / non lu ; estimande et masse simultanée des trajectoires ; `noyau` (loi jointe d'un pas, marginales = `calculer`) ; gabarit (P, G, I) amorcé sur SEUIL ; clôture identique à la 0.7.9 | — |
| Chantier formel (note du 31 oct.) | Unifier | **Joindre** : remplacer le noyau de `trajectoires` par le noyau joint et ses deux estimandes, recodage sans force inventée — trajectoires seules changent ; **Signer** : θ < 0, `manque` et `conflit` dans le calcul — p change ; **Structurer** : objet dans le mot, homologie H1.7 par raffinage de couleurs — p change par la classe ; **Mélange** : codage latent pondéré par `accord` ; **Estimer** : θ par pseudo-vraisemblance, matrice en a priori | chaque étape : version séparée, décision d'auteur ; Mélange et Estimer : 20 cas actifs |
| 0.7.13 (faite) | Représentation, inférence, dynamique : dire où elles divergent | variantes de codage des mots f ; écart aux marginales des trajectoires ; de Finetti, hystérésis et lissage en deux étapes corrigés ; analogie, définition et transfert séparés ; décision 1b reformulée ; clôture identique à la 0.7.9 | — |
| 0.7.12 (faite) | Ce que le lecteur voit d'abord | paire (sans cartes, avec cartes) en tête quand aucun cas réel n'est actif ; bande d'horizon (1, 3, 6 fenêtres) ; homologie indiscernable du placebo signalée ; lecture séquentielle de V4 (e-processus, valide à tout instant) ; épreuve d'érosion de P1 comptée en strate 7 ; clôture identique à la 0.7.9 | — |
| 0.7.11 (faite) | Prouver par clôture | `passage` : `absent_de_la_piece` et `non_soutenu` au lieu d'`insuffisant` ; `independance` des sources corroborantes ; couverture remplacée par la mesure de chaque ancrage ; `conservativite` (clôture complète, empreinte) ; barreau A justifié par l'identifiabilité ; clôture identique à la 0.7.9 et à la 0.7.10 | — |
| 0.7.10 (faite) | Répondre et se mesurer soi-même | support du mécanisme (Toulmin), réfutation qui annule, F n'est pas un modalisateur ; répétabilité (`accord --repetabilite`) ; intérêt et référentiel des références externes ; procédure du jugement ; bras « modèle seul » recommandé ; probabilités identiques à la 0.7.9 | — |
| 0.7.9 (faite) | Accord et rejets | `accord` : κ, PABAK, accords spécifiques, deux taux de manque, verdict ; audit aveugle des rejets (`rejets`) ; journal des concessions ; probabilités identiques à la 0.7.8 | — |
| 0.7.8 (faite) | Se comparer à autre chose qu'à soi | comparateur externe aveugle et scellé (`sceller-comparateur`, rapport, `v4_reference`) ; `frequences-externes.md` et refus du gabarit et des classes tautologiques ; `export-codeur` ; probabilités identiques à la 0.7.7 | — |
| 0.7.7 (faite) | Paramétrer avant de mesurer | seuil d'ancrage dédoublé ; V4 absolu, testé, effectif calculé avec plancher ; questions discriminantes et double rapport V4 ; seuil de niveau séparé (valeur inchangée) ; règles figées ; strate 7 à 14/16 ; probabilités identiques à la 0.7.6 | — |
| 0.7.6 (faite) | Éprouver les paramètres | `sonde` (arêtes, intensités, inerties) contre la référence « cas seuls » ; couverture des arêtes ; Kish ; sondes d'atténuation ; circularité signalée ; `signe_suffisant` ; critère du premier cas ; probabilités identiques à la 0.7.5 | — |
| 0.7.5 (faite) | Confronter et tester | matrice confrontée aux observations (`confronter`) ; tests exacts du signe et de Wilcoxon, σ(d), score logarithmique ; poids des deux a priori et intervalle de f publiés ; épreuve commune des révisions ; `classe_source` ; κ 0,67 / 0,80 ; puissance des jalons ; probabilités identiques à la 0.7.4 | — |
| 0.7.4 (faite) | Version de preuve | décisions 1 à 4 du 2026-10-29 ; probabilités identiques à la 0.7.3 | — |
| 0.7.3 (faite) | Contrôler la lecture qui produit le chiffre | dossier de lecture scellé avant `calculer` ; bande de classe ; fragilité de niveau ; sources du calcul et propagation inter-strates affichées | — |
| 0.7.2 (faite) | Éprouver les étapes | questions avec résolution et justification par branche (« non A » ne vaut pas « B ») ; passage qui soutient chaque F ; banc d'essai des modifications (`validation.md` §9) | — |
| 0.8 | Structurer | objets-frontière sourcés (strate 7 en cours, §5) ; cases Vides à combler (décision 1b = universelles) ; échelle de dureté (portes par niveau ρ, date de révision des sources) ; comparateur de marché de prévision (étape 4) | étapes 2 et 3 |
| 0.9 | Éprouver | séquence H1.6 (motifs ordonnés), comparée à l'état courant seul ; banque de cas adverses ; mode « scénarios » à la manière d'ACH (`apports-theoriques.md` §7) ; registre de dépendances et dossier externe (`apports-theoriques.md` §10) | 30 cas actifs dans une strate ; pour le registre, une source corrigée dans un cas réel |
| 1.0 | Grammaire | cartes comme règles de transformation, écrites par un rédacteur indépendant de la matrice puis comparées à elle ; liaisons comme opérateurs ; dérivation de l'alphabet en note séparée | rédacteur indépendant |

**Décisions d'auteur du 2026-10-29** (fiche « cinq arbitrages de la 0.7.3 ») :

| # | Décision | État |
|---|---|---|
| 1 | À compter du 2026-10-29, une prévision n'est éligible à V4 que si son dossier de lecture porte un sceau publié au plus tard à la date d'information ; les prévisions antérieures restent au journal, hors V4 sans être invalidées | appliquée (0.7.4) |
| 2 | `partager` inscrit `{id, usage, date}` au registre ; `valider_base` exige le partage par empreinte **et** sa date ; un partage non daté rend la fiche non valide | appliquée (0.7.4), date comparée à `codage.debut` et non au premier état (sinon tout cas historique serait refusé) ; registre `partage.jsonl` dans le dossier de travail et non dans `assets/` (remplacé à chaque installation) |
| 3 | `calculer` rend `p_placebo`, `graine_placebo` et `apport_homologie` ; exigés au journal comme `p_sans_cartes` | appliquée (0.7.4), placebo moyenné sur 200 tirages, graine dérivée de la question |
| 4 | Le dossier consigne ses requêtes A7 par carte et par famille ; une famille ou une paire de candidates sans discrimination manquante → dossier incomplet, lecture Spéculative | appliquée (0.7.4) |
| 5 | Principe retenu : la qualité de l'ancrage atténue l'inférence (λ_eff = 1 + (λ − 1)·w, w = 1 pour F, 0,5 pour f) ; d'abord comme variante de la bande de sensibilité, sans effet sur p ; promotion au défaut en version mineure dédiée, à ≥ 20 cas, quand l'effet se distingue de la sélection des homologues | à faire, version séparée de la 0.7.4 |

**Décisions ouvertes par la note du 2026-10-30 (0.7.5)**, aucune prise :

| Décision | Effet | Coût |
|---|---|---|
| **Appliquée (0.7.7)** : seuil dédoublé, `n_min_publication` 1, `n_min_ancrage` 20 (= k₀). Proposition d'origine : porter `n_min_frequence` de 10 à 19 ou 40, ou le dédoubler : un seuil bas pour publier, un seuil haut (données au moins deux fois plus lourdes que l'a priori, n ≥ 40) pour « ancré » et ρ3 | « ancré » signifie que les données dominent | **ne change aucun p** (correction : la 0.7.5 écrivait « change des p ») ; retire le comparateur de V4 (`frequence_de_base`) et ρ3 aux questions sous le seuil ; `p_sans_cartes` reste toujours publié |
| Atténuer λ par `corroboration` et `passage` plutôt que par F/f (variante de la décision 5) | la fiabilité du signal pèse sur l'inférence, sans colinéarité avec la sélection H1/H1.5 | **sondes écrites (0.7.6)**, hors du p publié : `effet_attenuation.force` toujours, `corroboration_passage` avec un dossier ; promotion au défaut d'une seule des deux, à l'étape 5, sur mesure |
| Loi de persistance à taux variable (Weibull discrète) | la dépendance à l'âge entre dans le calcul | version dédiée, quand `confronter` sur cas réels montre un effet |
| Protocole d'« idéologie sémiotique » au second codeur : chaque codeur déclare, avant tout codage, ce qui fait un signe suffisant (déclaration, exécution, trace) ; κ intra et inter-déclaration | explique ou non les désaccords systématiques | **champ écrit (0.7.6)**, `signe_suffisant` daté avant `codage.debut` ; rempli à l'étape 5 seulement |
| Contrôle de circularité de la garantie (nom de la carte dans `garantie.mecanisme`) | attrape « c'est un seuil parce qu'il y a hystérésis » | **signalement (0.7.6)** dans le dossier, jamais un refus ; faux signalements à mesurer sur cas réels avant d'en faire une règle |

**Décisions du 2026-10-30 pour la 0.7.7** (fiche « paramétrer avant de mesurer ») :

| # | Décision | Vérification | État |
|---|---|---|---|
| 1 | Dédoubler le seuil d'ancrage : publication 1, ancrage 20 | p inchangé (vérifié) ; ρ3 plus rare, comparateur plus fréquent | appliquée |
| 2 | V4 en gain absolu (2,5 points), testé (signe) | cohérente ; plus exigeante que 10 % sur les événements rares (écrit) | appliquée |
| 3 | `v4_n` calculé par σ̂(d) | corrigée : la formule seule permettait de déclarer V4 sur trois épisodes au σ̂ sous-estimé ; plancher de 50 conservé, cible = max(50, requis) | appliquée, avec plancher |
| 4 | Niveau d'homologie choisi à 2 cas (`c_min_niveau`), ρ à 3 | **incohérente avec la vérification du lot** : change un calcul de démonstration (52,0 % → 51,7 %, ρ1 → ρ4), alors que la fiche l'annonçait sans effet | seuil séparé, valeur 3 (statu quo) ; passage à 2 réservé à une version dédiée |
| 5 | Âge mesuré dans `confronter` | existait depuis 0.7.5 ; ajout des intervalles de Wilson et du critère figé | appliquée |
| 6 | `discriminant` (δ = 0,02 en points de probabilité, non « de Brier ») et double rapport V4 | cohérente ; calculé avant l'issue, jamais filtre | appliquée |
| — | CROISSANCE@7 → Vide | deux lectures déjà faites (Choucri, Altman) | appliquée : 181 Proposé, 14 Vide |
| — | PÉRIODICITÉ@7 : garder « Cycles électoraux », chercher un texte ouvert | la définition admet le forçage par calendrier ; la piste Modelski (0.7.6) relève de la strate 12 | appliquée (note) |
| — | RÉSONANCE@7 : troisième recherche, clore | faite sur résumés consultés le 30 oct. 2026 (Granovetter 1978, Kuran 1991), pas de mémoire | appliquée : close, non concluant |

**Règles figées avant les données** (ce qui se décide après la mesure est une rationalisation) :

| Sujet | Règle |
|---|---|
| Atténuation de λ | sur ≥ 20 cas double-codés, promouvoir au défaut **une seule** variante (force, ou corroboration et passage) : celle dont le différentiel de Brier contre le p par défaut est négatif et significatif au test du signe à 5 % sur les mêmes épisodes ; si les deux, la plus grande ; si aucune, aucune. (La fiche disait « dont l'effet dépasse celui du placebo » : les deux effets ne mesurent pas la même chose ; reformulé.) |
| Loi à taux variable | ouvrir Weibull si, en cas réels actifs, l'écart de maintien âge ≥ 1 − âge 0 atteint deux écarts-types, avec au moins 30 occasions de chaque côté (`weibull_occasions_min`) ; `confronter` l'affiche |
| Circularité en refus | passer du signalement au refus si, sur au moins 20 fiches réelles relues, moins de 10 % des signalements sont des faux positifs (garantie qui nomme la carte sans être circulaire) |

**Puissance des jalons (0.7.5).** Aucun effectif de la feuille de route n'était justifié par un calcul.
Calculs indicatifs, approximation normale (unilatéral 5 %, puissance 80 % pour κ ; bilatéral 5 %,
puissance 80 % pour V4) :

| Jalon | Effectif fixé | Ce qu'il permet |
|---|---|---|
| A4 · accord κ par carte | 20 cas | erreur-type de κ (Cohen 1960) ≈ √(pₒ(1 − pₒ)/n) / (1 − pₑ). Avec pₑ = 0,5, distinguer κ = 0,80 de 0,60 demande environ **83 unités codées**, 0,75 de 0,60 environ 156 ; avec pₑ = 0,3, 55 et 102. L'unité est la décision codée (carte × strate × état), pas le cas : 20 cas peuvent ou non suffire selon le nombre de décisions par cas, à compter au premier double codage |
| ρ0 · 30 cas distincts | 30 | compte les cas, pas l'effectif pondéré : sur la démonstration, 10 cas valent 4,8 observations effectives. La règle « n > 30 » n'est pas une borne du théorème central limite, et ρ0 ne repose pas sur une approximation normale ; le seuil est une convention, déclarée comme telle |
| V4 · 50 épisodes, gain de 10 % (jusqu'en 0.7.6 ; règle calculée depuis 0.7.7) | 50 | sur un Brier de référence de 0,25, 10 % font 2,5 points ; n ≈ (2,80 σ(d) / 0,025)² : 32 épisodes si σ(d) = 0,05, 126 si σ(d) = 0,10, 503 si σ(d) = 0,20. **50 épisodes ne suffisent que si σ(d) ≲ 0,063**, valeur inconnue : `scorer` la publie dès les premiers épisodes résolus |

Ces calculs supposent un accord attendu pₑ de 0,3 à 0,5. Sous faible prévalence, pₑ approche 1 et
l'effectif requis pour κ devient inaccessible : c'est PABAK, sous le plafond des taux de manque, qui
porte le verdict (0.7.9), et la puissance se recalcule avec pₑ = p₁p₂ + (1 − p₁)(1 − p₂) observé.
Ces chiffres ne changent aucun seuil : ils disent ce qu'un seuil atteint permettra de conclure. Un κ de
0,70 sur un petit effectif ne prouve pas le franchissement de 0,67 ; il se publie avec son intervalle.

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
2. LIRE puis CODER selon `base-de-cas.md` §3 : questions qui départagent (avec résolution et
   justification par branche), garantie, option, `corroboration` et `passage` pour chaque F,
   contre-observations, ligne A6.
3. Si Claude propose le codage : `codage.recodage`, puis relecture et `codage.recodage_confirme`.
4. Sceller votre jugement (`sceller-jugement`), puis calculer et journaliser 2 à 5 prévisions.
5. À l'échéance : coder l'issue, `statut_donnees: actif`, `valider`, `scorer`, `bilan`.

**Choisir le premier cas (0.7.6).** Un cas apprend quelque chose au protocole si le dispositif peut y
produire une prévision distincte de ses comparateurs. Conditions, vérifiables avant de journaliser :
(1) strate 7, où 13 équivalents sont Documentés ; (2) au moins une **apparition**, seul type où la
matrice agit (une persistance ne teste que l'inertie) ; (3) carte visée Documentée, pour une
résolution sur un marqueur vérifié ; (4) sources publiques, datées, disponibles à la date
d'information ; (5) issue attendue dans la fenêtre (trois mois), pour un cas prospectif. Un état où une
arête mène à la cible teste l'apport des cartes ; un état sans arête teste que l'absence d'arête prédit
l'absence d'événement : bon second cas. **Ne pas trier sur l'informativité calculée** : choisir les
questions où p s'écarte de `p_sans_cartes` et de `p_placebo` flatterait le modèle. Une question où les
trois coïncident se journalise quand même et se lit « ne teste que l'inertie » (`difficulte`). On choisit
un cas où l'on peut **savoir** si les cartes marchent, pas un cas où elles marchent.

**Étape 3 avant l'étape 2.** Les trois cases restantes de la strate 7 ne demandent aucun cas réel :
RÉSONANCE, une troisième recherche documentée la clôt ; CROISSANCE, rétrogradation en Vide puis
recherches (`equivalences.md`, « Une case Proposé ne se clôt pas ») ; PÉRIODICITÉ, lecture d'un texte.
Mise à jour 0.7.7 : RÉSONANCE close (trois recherches), CROISSANCE rétrogradée en Vide (deux recherches,
une troisième la clôt), PÉRIODICITÉ conserve « Cycles électoraux » — un forçage par calendrier entre
dans la définition — et attend un texte ouvert qui établisse la répétition ; les cycles longs de
Modelski et Thompson, rythme d'environ un siècle, relèvent de la strate 12 et sont écartés pour la 7.
Strate 7 : 14 cases traitées sur 16. Candidats d'origine, **non lus** : pour CROISSANCE, la course aux armements de Richardson
**ne convient pas** — son taux dépend du niveau adverse, son terme propre est un amortissement, et le
modèle n'a pas de capacité limite : c'est une escalade réciproque, pas une croissance auto-entretenue
bornée ; pour RÉSONANCE, les modèles à seuil (Granovetter, Kuran) décrivent des cascades, pas un couplage
d'oscillateurs : une recherche qui le constate est une troisième recherche valable.

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
| Calcul de l'accord par carte depuis deux fiches d'un même cas (la statistique, `accord`, existe depuis 0.7.9) | premiers cas double-codés | `kappa_min`, `kappa_rapportable`, `fnr_max` |
| Pondération continue des homologues par similarité | au moins une strate avec 30 cas actifs | `jaccard_H15` |
| Intervalles des événements composés et multi-pas | premières références conditionnelles vérifiées | — |
| Calibration des multiplicateurs et des inerties | jalon V4 atteint | `lambda`, `inertie` |
| Scinder `moteur.py` en modules (validation, calcul, score, autotests) | jalon V4 atteint ; d'ici là, un fichier unique reste plus simple à auditer et à recopier | — |

---

## 8. Test à l'aveugle

Protocole : `validation.md` §8. Il peut commencer dès que l'étape 2 est terminée ; il ne mesure la
calibration qu'après les étapes 3 et 4. Jalon interne (0.7.7) : gain absolu de 2,5 points testé, sur au moins 50 épisodes et l'effectif requis par σ̂(d), contre le
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
| 2026-10-27 | — | Audit Manus traité (0.6.14) : prévisions moteur liées à leur calcul, codeurs {id, role}, manifeste, CI 3.8/3.12 |
| 2026-10-27 | — | Audit Scira traité (0.6.15) : corrections documentaires ; deux anomalies écartées après vérification |
| 2026-10-27 | — | 0.7.0 : tests de preuve (F exige un fait suffisant) et décomposition de Murphy ; fin de la série d'audits, début des tests à l'aveugle |
| 2026-10-27 | — | Audit hacker.ai traité (0.7.1) : sortie Windows, CI Windows et macOS, sources, `scorer --csv` |
| 2026-10-27 | — | Cinq apports triés (0.7.2) : sémantique inquisitive, VECTOR, Shao, Hao Zhang, Alex Zhang ; questions résolubles, `passage`, banc d'essai ; le fichier *Intuition Machine* reversé était déjà trié (0.6.7) |
| 2026-10-29 | — | Audit d'ingénierie traité (0.7.3) : correctif reçu repris et corrigé (six défauts) ; décisions laissées à l'auteur : atténuation λ par F/f, datation du partage, plancher de recherche A7, placebo d'homologie, dossier exigé pour V4 |
| 2026-10-29 | 1 | Cinq arbitrages tranchés par l'auteur ; décisions 1 à 4 appliquées en 0.7.4 (version de preuve), décision 5 réservée à une version dédiée |
| 2026-10-30 | — | Note « ce qu'il manque » triée (0.7.5) : douze points vérifiés, sept corrigés avant intégration (`apports-theoriques.md` §11) |
| 2026-10-30 | — | Apport « capacité et généralisation » et réponses à la feuille de route triés (0.7.6, `apports-theoriques.md` §12) ; une erreur de la feuille de route corrigée (`n_min_frequence` ne change pas p) |
| 2026-10-30 | 1 | Décisions 0.7.7 vérifiées : 1, 2, 5, 6 appliquées ; 3 avec plancher ; 4 séparée de la version (change un p) ; strate 7 : RÉSONANCE close, CROISSANCE Vide |
| 2026-10-30 | 3 | Strate 7 : 14 cases traitées sur 16 (13 Documentées, RÉSONANCE close) ; restent CROISSANCE (une recherche) et PÉRIODICITÉ (un texte) |
| 2026-10-30 | — | Document « mesures à prendre » trié (0.7.8) : comparateur externe, fréquences externes, export du second codeur ; quatre corrections avant intégration |
| 2026-10-30 | — | Document « accord et rejets » trié (0.7.9) : trois apports retenus, cinq corrections, aucun texte tiers |
| 2026-10-30 | — | Six notes et un audit des rivaux triés (0.7.10, `apports-theoriques.md` §14) : quatre contrôles retenus, deux affirmations des notes réfutées sur le code (homologue unique, pluralité « trois équipes ») |
| 2026-10-30 | — | Note *open-ontologies* triée (0.7.11, `apports-theoriques.md` §15) : quatre imports retenus, certificats formels refusés ; clôture 0.7.9 → 0.7.11 : 0 conséquence changée sur 2 790 |
| 2026-10-31 | — | Audit V34 trié (0.7.12, `apports-theoriques.md` §16) : quatre sorties ajoutées sans changer aucune probabilité (clôture identique), sept décisions d'auteur ouvertes, trois points de l'audit corrigés |
| 2026-10-31 | — | Audit comparatif trié (0.7.13, `apports-theoriques.md` §17) : deux sorties ajoutées, quatre justifications corrigées, quatre décisions d'auteur ouvertes ; aucune probabilité ne change |
| 2026-10-31 | — | Note « unifier représentation, inférence et dynamique » triée (0.7.14, `apports-theoriques.md` §18) : temps « Déclarer » appliqué, « Joindre » ajouté à côté sans remplacer, quatre temps planifiés ; numéro 0.7.14, la 0.8 restant réservée |
| 2026-10-31 | 0 | À faire : installer la 0.7.14 ; compléter la provenance amont d'EnVrai? (`LICENCES-TIERS.md`) ; mesurer la répétabilité dès les premiers cas codés en solo |

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
11. En dernier : `moteur.py manifeste`, puis `audit` (qui vérifie `SHA256SUMS`) ; publication avec
    `publier-github.ps1` (étiquette et release, `SHA256SUMS` joint).
