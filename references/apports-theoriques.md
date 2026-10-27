# Alphabet situationnel — Apports théoriques et leur traduction en contrôles

> Version : 0.7.2

> Ce que trois analyses du corpus de Carlos E. Perez (*Intuition Machine* : essais 2016-2026 ; livres
> *Artificial Fluency*, 2024, et *Artificial Empathy*, 2023), versées au projet le 27 octobre 2026, ont
> changé dans le skill, ce qui attend et ce qui est refusé. Charger ce fichier pour comprendre **pourquoi**
> une règle de 0.6.0 existe, pas pour lire une situation.

---

## 1. Règle d'importation

> **Un concept n'entre que s'il ajoute un contrôle : un champ qui peut rester vide, un test qui peut
> échouer, une commande. S'il n'ajoute qu'un mot, il appauvrit le skill.**

Le corpus est un **générateur d'hypothèses et un diagnostic de dettes**, pas une autorité : aucun cas
codé, aucune prévision scorée, aucune reprise académique trouvée. Il ne se cite jamais dans une fiche
de cas ni comme référence d'un équivalent (A3).

---

## 2. Le diagnostic retenu

1. **Le moteur répond au barreau 1 et parle au barreau 3** (Pearl). Il compte des associations entre
   cartes ; sa sortie se lit comme une prévision sur un futur non advenu. L'écart n'était pas déclaré.
2. **L'ancrage était une relation à deux termes** (fait → carte). A6 vérifiait que le fait ne relève
   pas des voisines, jamais par quel mécanisme il relève de la carte : il manquait l'interprétant.
3. **Les cartes sont des catégories, pas des règles de transformation.** Une catégorie ne produit pas
   de transition : les 66 arêtes de la matrice sont stipulées, non dérivées.
4. **Le graphe de validation n'a pas d'ancre indépendante** tant que les cas réels ne sont pas actifs :
   « la topologie achète la sophistication, pas la vérité ».
5. **Le système est sous-déterminé** : une centaine de paramètres pour quatre cas réels.

---

## 3. Ce qui est entré en 0.6.0

| Concept | Source | Contrôle ajouté | Où |
|---|---|---|---|
| Barreaux de Pearl | *Artificial Empathy*, ch. 9 | barreau déclaré dans la ligne S5 ; toute transition A tant qu'aucune source ne documente une intervention ; lecture « si le motif observé se répète » | `constitution.md` §3, `dynamiques.md`, `barreau` (§H) |
| Interprétant (Peirce) et clôture sémantique | *Intuition Machine* (étape 4) ; *Artificial Fluency*, ch. 7 | champ `garantie` (mécanisme, attendu, contredirait), requis pour F ; forme type dans chaque fiche | A6, `cartes.md`, `base-de-cas.md` §2 |
| Pertinence (« différence qui fait une différence dans l'action ») | *Artificial Fluency*, ch. 2 et 10 | champ `option` (acteur, avant, après), requis pour F | O1, `base-de-cas.md` §2 |
| Abduction (« une bonne hypothèse rend une question évidente ») | *Artificial Fluency*, ch. 7 ; *Artificial Empathy*, ch. 4 | `questions` au premier état d'un cas réel : chacune départage deux cartes ; question décorative refusée | `grammaire.md` §7, `base-de-cas.md` §2, moteur |
| Journal à deux probabilités | *Artificial Empathy*, ch. 9 (Pearl) | `probabilite_jugement` scellée avant le moteur ; `moteur_contre_jugement` compte améliorations et dégradations | `validation.md` §1, `sceller-jugement` |
| Sous-spécification | *Artificial Empathy*, ch. 4 | bande de sensibilité sur six variantes ; « non identifié » si elle traverse 50 % | `graphe.md` §2.3 |
| Gaming de la métrique | *Artificial Empathy*, ch. 4 | difficulté par question, part des références extrêmes, Brier stratifié | `validation.md` §1, §7 |
| Appariement des boucles (Goodhart) | *Intuition Machine* (Grounded Loop Graph Model) | l'apport des cartes se lit avec la part de ruptures SEUIL | `validation.md` §7 |
| Objets-frontière | *Artificial Fluency*, ch. 12 | Documenté exige un texte de la discipline et un nom local ; `audit` le vérifie | `equivalences.md` §2 |
| Magic rabbits (traceback) | *Artificial Fluency*, ch. 9 | `assets/rabbits.jsonl` ; étape de traceback dans le codage | `base-de-cas.md` §3, `validation.md` §6 |
| Registre des angles morts | *Intuition Machine* (P8 sans instrument) | `angles-morts.md`, entrées réfutables ; ligne obligatoire en sortie LIRE | `simulation.md` §1 |
| Friction cognitive | *Intuition Machine* (essai de mai 2026) | bloc « coût du codage » en sortie | `simulation.md` §1 |

Aucun de ces contrôles ne change un chiffre du moteur, sauf la bande de sensibilité, qui en ajoute.

---

## 4. Ce qui attend, et à quelle condition

| Piste | Pourquoi pas maintenant | Condition | Version |
|---|---|---|---|
| Hors domaine attribué, boucle d'agence | **écarté par la décision 1b** (27 octobre 2026) : les cartes à agents sont universelles ; restent à instruire les anomalies de définition (`equivalences.md` §3) | — | — |
| Échelle de dureté : portes par niveau ρ, date de révision des sources | n'a d'objet qu'avec des cas actifs et des équivalents sourcés | étapes 2 et 3 de la feuille de route | Structurer |
| Séquence (niveau H1.6, motifs ordonnés) | inerte avec quatre cas : aucun homologue | 30 cas actifs dans une strate | Éprouver |
| Cartes comme règles de transformation (condition, opération, invariant, production) ; liaisons comme opérateurs | les 16 règles doivent être écrites **avant** d'être comparées à la matrice, par quelqu'un qui ne l'a pas vue ; écrites par l'auteur du skill, le test perdrait sa valeur | rédacteur indépendant de la matrice | Grammaire |
| Dérivation de l'alphabet (espace ou liste ?) | programme de recherche, hors du skill pour ne pas le contaminer | quatre distinctions préenregistrées, double codage | note de recherche |
| Agapique / anancastique, symétrie brisée, banque de cas adverses | gain local, ou après stabilisation des définitions | après les règles de transformation | Grammaire |

---

## 5. Ce qui est refusé

- **L'ontologie de QPT** (quatre modes « irréductibles ») : thèse d'universalité forte, contraire à
  P1 ; elle rendrait le skill moins réfutable. Utilisable comme générateur d'hypothèses seulement.
- **Le rapprochement des 16 cartes et des 16 espèces d'agence** : coïncidence numérique (9 + 7), objets
  différents (des agents, des situations).
- **La normativité** (« agapique », « sol de qualité ») sans marqueur observable : contraire à A5, P5, P9.
- **La critique bayésienne prise comme verdict** : « une heuristique humaine déguisée en mathématiques »
  est une polémique ; elle oblige à déclarer le barreau et à mesurer la sensibilité, elle ne prouve pas
  que la révision bayésienne est fausse.
- **Le théâtre théorique** : douze cases, neuf boucles, quatre modes n'entrent pas, faute de contrôle.

---

## 6. Ce que le skill faisait déjà mieux que le corpus

Préenregistrement par empreinte, score de Brier, comparateur sans cartes, provenance ρ calculée, refus
de chiffrer l'inconnu, journal non réécrit, audit et autotests, périmètre d'usage borné. Le transfert
est à sens unique : des concepts entrent, aucune autorité.

---

## 7. Deux apports reçus le 27 octobre 2026 (0.6.6)

Deux synthèses versées par l'auteur : *Pistes CIA* (Heuer 1999, Kent 1964, *Tradecraft Primer* 2009,
Gleeson 2023, Schlickenmaier 2026, Mulligan 2026) et *Spiral Semiosis* (deeplearningplaybook.com,
même corpus *Intuition Machine* que les trois premiers rapports). Même règle d'importation (§1).

**Corrections préalables.** Les deux documents décrivent un skill légèrement différent de celui-ci :
16 cartes, pas 36 ; modes LIRE, PRÉVOIR, CODER, SCORER ; barreau, garantie, option, rabbits introduits
en 0.6.0 (le nom local aussi) ; le barreau n'est pas présenté comme une probabilité ; les *rabbits* sont
des constructions ad hoc à résorber, pas des signaux faibles ; garantie et option ne mesurent pas la
qualité d'une source. Les pistes qui reposaient sur ces lectures sont jugées sur le skill réel.

### 7.1 Ce qui entre

| Piste | Source | Contrôle ajouté | Où |
|---|---|---|---|
| Qualité de l'information (*Quality of Information Check*) ; sources fabriquées par IA générative | *Tradecraft Primer* ; Mulligan 2026 | `corroboration` requis pour un mot F de cas réel actif : `independantes` (au moins deux sources nommées) ou `unique` (signalée) ; refus si « indépendantes » ne nomme qu'une source | `base-de-cas.md` §2, `controle_corroboration` |
| Langage probabiliste brouillé | Kent 1964 | aucun mot de probabilité sans son chiffre ; un jugement donné en mots se fait préciser avant scellé, jamais convertir | `simulation.md` §2, `SKILL.md` étape 7 |
| Désinformation cohérente | Mulligan 2026 | angle mort « véracité d'un fait », déclaré délibéré : l'alphabet lit la forme, pas l'authenticité | `angles-morts.md` |

**Le mode « calibrer » proposé (mot → chiffre par la table de Kent) est refusé** pour la raison même
que donne Kent : le même mot (« serious possibility ») était lu de 20 à 80 % par les membres de son
propre comité. Convertir un mot par une table impose au lecteur l'interprétation de la table, pas
celle de l'auteur du jugement. Le contrôle utile est l'inverse : exiger le chiffre.

### 7.2 Ce que le skill fait déjà

| Piste | Déjà couvert par |
|---|---|
| Hypothèses concurrentes (Heuer, ACH) : chercher l'information qui *infirme* | A7 (contre-observation exigée et classée) ; `questions` qui départagent deux cartes, c'est-à-dire la diagnosticité d'ACH |
| *Key Assumptions Check* | `indicateur_bascule` et `refutation` du journal ; ligne A6 (voisines écartées et pourquoi) |
| Confiance dans le modèle, distincte de p | barreau, bande de sensibilité, niveau ρ |
| Transparence face aux LLM ; export lisible par un LLM ; mode « agent » | le skill *est* lu par un modèle de langage ; `--json` ; CODER est déjà l'assistance au codage, la décision restant au codeur |
| « What if we're wrong ? » | A7, angles morts, `moteur_contre_jugement` |
| Interprétants rejetés (Spiral, P1) | `rejets_a7`, ligne A6, bloc « coût du codage » |
| Lectures ouvertes `OPEN` (P4) | statut Spéculatif ; « non identifié » ; questions non tranchées |
| « La différence qui fait une différence » (P10, Bateson) | `option` depuis 0.6.0 (pertinence, *Artificial Fluency*) |
| Clôture conditionnelle (P6) | une case Vide close « ne se rouvre que sur une source nouvelle » (0.6.5) |

### 7.3 Ce qui attend

| Piste | Condition | Version |
|---|---|---|
| Mode « scénarios » à la manière d'ACH (matrice informations × états concurrents, score d'incohérence) | cas actifs : sans eux, la matrice se remplit de jugements que rien ne recoupe | Éprouver |
| Mode sémiotique du fait (règle, occurrence, qualité ; Spiral P8) : CONTRAINTE ancrée sur une occurrence sans règle, PÉRIODICITÉ sur une seule occurrence | 30 cas actifs, pour mesurer si la distinction change un codage | Grammaire |

### 7.4 Ce qui est refusé

- **Tout poids sur les sources** (`fiabilite_source` qui modulerait p, `poids_source` décroissant avec
  la persuasion, `fabrication_risque` qui élargirait la bande) : paramètres non calibrés ajoutés à un
  modèle déjà sous-déterminé. La corroboration se déclare ; elle ne pondère pas.
- **Test de biais par « état inverse »** : inverser des antagonismes ne produit pas une lecture
  plausible ; A7 et les questions qui départagent font le travail sur des faits.
- **Lecture multi-échelle de la bande de sensibilité (Spiral P2)** : la bande mesure les hypothèses du
  modèle, pas l'échelle de lecture ; l'échelle est déjà portée par le qualificatif `multi-échelle`.
- **Phases perceptive à scientifique (P3), quatre stabilités (P5)** : vocabulaire sans marqueur ni
  donnée ; aucun contrôle ne peut échouer.
- **Récursion automatique issue → nouvel état (P7)** : un système qui recode sa propre clôture contamine
  ses cas ; une nouvelle prévision part d'un nouvel état observé, et l'ancienne n'est jamais réécrite.
- **Sceau conditionnel (P6)** : un scellé qui se rouvre ne prouve plus rien ; la révision est une
  nouvelle prévision versionnée.
- **Standard ouvert, API REST** : prématuré avant la 1.0 ; le schéma documenté et validé par `audit`
  tient lieu de contrat.

---

## 8. *Intuition Machine*, site et QPT (0.6.7)

Synthèse versée par l'auteur le 27 octobre 2026 : intuitionmachine.com, Quaternion Process Theory
(3 niveaux × 4 colonnes, 4 lettres, 12 boucles ; « 7 axiomes, 9 théorèmes, 43 vérifications »). Même
auteur et même corpus que le rapport « Intuition Machine » de 0.6.0, dont l'ontologie QPT a été
refusée (§5). Les vérifications « machine-checkable » sont celles du modèle QPT sur lui-même : elles
établissent sa cohérence interne, pas sa correspondance avec des organisations ou des situations.

**Corrections préalables** (comme au §7) : 16 cartes, pas 36 ; modes LIRE, PRÉVOIR, CODER, SCORER ;
`version_regles` ne mesure pas la péremption d'un contexte (c'est la date d'information et
`disponible_le`, B1) ; `option` n'est pas « une rotation au niveau convention sans ancrage » : elle
nomme un acteur et un changement observable.

### 8.1 Ce qui entre

| Piste | Contrôle ajouté | Où |
|---|---|---|
| « Unchecked output » : une sortie de modèle enregistrée comme fait | un cas actif dont le codage a été proposé par un modèle (`codage.recodage`) exige `codage.recodage_confirme` `{par, date}`, signé par un codeur humain nommé ; le modèle ne peut pas se confirmer lui-même. Visait d'abord les quatre propositions, dont Claude avait écrit garanties, options et questions (archivées en 0.6.8) ; vaut pour tout cas que Claude codera | `base-de-cas.md` §2, `feuille-de-route.md` §4 |

### 8.2 Ce que le skill fait déjà

| Piste | Déjà couvert par |
|---|---|
| Système de mots, axiomes (P1) | règles O, A, G, B, T, S, V ; grammaire formelle (`grammaire.md` §2) ; `audit` |
| *Grounding* contre *knowledge* (P2) | garantie et option sont déjà deux champs distincts, aux clés distinctes, contrôlés séparément |
| *Evaluation drift* : comparer à la réalité, pas au rapport précédent (P4) | le Brier se calcule contre une résolution externe figée avant échéance (S1, V1), jamais contre une prévision antérieure |
| *Stale context* (P4) | date d'information, `disponible_le` (B1) : aucune preuve postérieure n'entre dans un calcul |
| Saboteur licencié, remise en cause du graphe (P10) | différé déjà : règles de transformation écrites par un rédacteur indépendant de la matrice, banque de cas adverses (§4) |
| Plafond de procéduralisation (P8) | A4 exige un codeur humain ; CODER assiste, ne décide pas (§7.2) |

### 8.3 Ce qui attend

| Piste | Condition | Version |
|---|---|---|
| Test du témoin, chaîne fait → interprétation → trace → événement (P3, P7) | cas actifs avec `corroboration` : mesurer d'abord combien de mots F reposent sur une source unique, puis décider s'il faut typer la distance à l'événement (document primaire, presse, analyse) | Éprouver |
| Date de révision des règles et paramètres (« orphaned rules », P4, P6) | déjà inscrite dans l'échelle de dureté (§4) | Structurer |

### 8.4 Ce qui est refusé

- **Le sceau conditionnel par propriétaire inactif** (P6) : même motif qu'au §7.4 ; un scellé qui se
  rouvre ne prouve plus rien.
- **Restructurer `audit` en diagnostic à sept couches** (P5), **nommer les contrôles par édit
  pathologique** (P11) : renommage sans contrôle nouveau.
- **Transaction d'apprentissage en sept étapes** (P9) : le cycle état → événement → état est déjà
  tracé par la fiche, le journal et le CHANGELOG ; ajouter sept rubriques à chaque changement d'état
  alourdirait le codage sans qu'aucune puisse échouer.
- **Protocole d'interopérabilité « Common Ground »** (P12) : comme l'API REST au §7.4, prématuré avant 1.0.
- **Opérateur formel `qml_q` comme modèle du moteur** (P1) : « modèle aspiratif » selon le document
  lui-même ; un opérateur sans équivalent dans le calcul n'ajoute pas de contrôle.

---

## 9. Pistes bibliographiques (0.7.0)

Note versée par l'auteur le 27 octobre 2026 : une quarantaine de références (Heuer, Tetlock, Pearl,
Murphy, process tracing, QCA, scénarios, impacts croisés, sensemaking, marchés de prévision). Triée par
la règle d'importation (§1).

**Entré.** Les tests de process tracing (Van Evera 1997 ; Collier 2011, *PS* 44(4), 823-830, lu) donnent
au choix F/f un critère de preuve : F exige un fait suffisant (`test` : pistolet ou double), un fait qui
remplit seulement le marqueur est un cerceau et donne f (`protocole.md` A6). La décomposition de Murphy
(1973) sépare, dans le Brier, la fiabilité, la résolution et l'incertitude (`validation.md` §5).

**Retenu pour plus tard.** Un marché de prévision (Metaculus, Polymarket) comme comparateur externe au
même horizon, plus exigeant que l'inertie, si sa probabilité peut être figée à la date de la prévision
(0.8, étape 4). Les *Cross-Impact Balances* (Weimer-Jehle 2006) pour le mode « scénarios » (0.9).
L'agrégation de codeurs par calibration passée (Cooke 1991), au second codeur (étape 5).

**Déjà présent.** ACH (A7, questions qui départagent) ; barreau de Pearl ; Tetlock (scellé, comparateur,
Brier par épisode) ; boîte morphologique (l'alphabet lui-même, cartes × strates, paires incompatibles).

**Non retenu.** Sensemaking, apprentissage en double boucle, niveaux logiques, autopoïèse, perspectives
T/O/P : vocabulaire sans contrôle. QCA et ensembles flous pour F/f : la force est une qualité de preuve,
pas un degré d'appartenance. La note contenait des correspondances inexactes (numéros et noms de strates,
règles) et une référence introuvable (« EL-DRUIN », arXiv 2604.10087), non citée ici.

---

## 10. Cinq apports reçus le 27 octobre 2026 (0.7.2)

Cinq analyses versées par l'auteur, toutes rédigées sur la 0.7.1 (commit `0d92b34`) : *Inquisitive
Semantics* (Ciardelli, Groenendijk et Roelofsen, Oxford UP, 2019, ch. 2, 5 et 9) ; VECTOR (Nour et al.,
arXiv 2509.14455) ; les travaux de Rulin Shao (OpenScholar, ReasonIR, Context Language Models,
DR Tulu, *Spurious Rewards*) ; ceux de Hao Zhang (spécifications, LLM-as-a-judge, ReFoRCE, Certaindex,
GameArena, LongPack) ; ceux d'Alex L. Zhang (*Recursive Language Models*, généralisation
compositionnelle, *Language-Guided World Models*, KernelBench). Même règle d'importation (§1). Les
cinq décrivent correctement le skill ; elles convergent sur un point : **le skill déclare beaucoup et
éprouve peu ses propres étapes** (source → fait → marqueur → carte → question), et l'évaluation risque
de mesurer la forme ou le style plutôt que la lecture.

Un sixième fichier versé le même jour, `apports-intuition-machine.md`, est la synthèse QPT déjà triée
au §8 (0.6.7), mêmes pistes P1–P12 et mêmes inexactitudes (36 cartes, modes SIMULER et VALIDER) :
aucun apport nouveau.

### 10.1 Ce qui entre

| Piste | Source | Contrôle ajouté | Où |
|---|---|---|---|
| Conditions de résolution d'une question ; « non A » ne vaut pas « B » | *Inquisitive Semantics*, ch. 2, §2.3–2.5 | pour un cas réel, chaque question porte `resolution` ; une question de discrimination porte `justification` {oui, non}, une par branche menant à une carte ; une branche peut mener à `indetermine` (les deux, refusé). L'exemple du schéma (« pas de troisième groupe → POLARITÉ ») commettait l'erreur : corrigé | `grammaire.md` §7, `base-de-cas.md` §2, `controle_questions` |
| Toutes les questions utiles ne départagent pas | *Inquisitive Semantics*, ch. 5, §5.4 et ch. 9, §9.2 | `type: "documentation"` (`carte`, `manque`) ; ne remplace pas la question qui départage, exigée au premier état | idem |
| Questions qui restent ouvertes, levées ou invalidées | *Inquisitive Semantics* ; GameArena (Hao Zhang) | `statut` (ouverte, partielle, resolue avec `reponse`, presuppose_invalide), chacun avec sa `preuve` | idem |
| Contrôle affirmation–passage | OpenScholar (Shao) ; spécifications (Hao Zhang) | `passage` {localisation, relation} requis pour F de cas actif ; F exige `soutient`, `partiel` donne f, `contredit` renvoie à A7, `insuffisant` n'ancre rien ; « independantes » exige deux passages | `protocole.md` A6, `controle_passage` |
| Annonce ≠ réalisation | VECTOR ; OpenScholar | A5 : une possibilité, une condition, une décision non entrée en vigueur ne sont pas une réalisation | `protocole.md` A5 |
| Requêtes qui ne présupposent pas la lecture ; contradictions conservées | ReasonIR (Shao) | trois familles de requêtes (observation, discrimination, contradiction), jamais sur le nom de la carte | `protocole.md` A7, `sources-france.md` §1 |
| Arrêt sur contrôles faits, pas sur sentiment de certitude | Certaindex, DeepConf (Hao Zhang) | budget épuisé = dossier incomplet ; la convergence de réponses n'est pas une corroboration | `protocole.md` A7 |
| Sens d'une série avant usage | ReFoRCE, Arctic-Text2SQL (Hao Zhang) | liste : objet compté, unité, période, périmètre, manquants, agrégation, révisions | `sources-france.md` §5 |
| Conservation de l'information après résumé | Context Language Models (Shao) ; RLM (Alex Zhang) | contenu minimal de l'état de travail ; pièces, état révisable et prévisions scellées séparés | `simulation.md` §7 |
| Évaluer la représentation, pas seulement le résultat ; juge biaisé ; gain mal attribué | VECTOR ; LLM-as-a-judge, Chatbot Arena (Hao Zhang) ; *Spurious Rewards*, DR Tulu (Shao) ; généralisation compositionnelle, KernelBench (Alex Zhang) | banc d'essai : trois résultats séparés, épreuves de stabilité et de réexamen, corrigé indépendant, une variante à la fois, sorties anonymisées, lots séparés par épisode ; une règle constitutive ne se retire pas faute d'échec | `validation.md` §9 |

**Règle d'importation, complétée.** Depuis 0.7.2, un contrôle nouveau entre avec son épreuve : le
défaut qu'il doit détecter, construit au banc (`validation.md` §9). Les contrôles ci-dessus ont leurs
autotests (forme) ; leur utilité (lecture) reste à mesurer au banc sur des dossiers qu'ils n'ont pas
inspirés.

### 10.2 Ce que le skill fait déjà

| Piste | Déjà couvert par |
|---|---|
| Hypothèses concurrentes, critères de résolution externes, refus de chiffrer sans données | A7, S1, « non estimé » |
| Incertitude de l'analyste distincte de celle des acteurs | carte INCERTITUDE (`cartes.md`) |
| Trois chronologies (ordre du récit, date des faits, date de disponibilité) | `date`, `disponible_le`, date d'information (B1) ; l'ordre du récit n'entre dans aucun calcul |
| Plusieurs appels au même modèle ne sont pas plusieurs sources | `corroboration`, codeurs `{id, role}`, `recodage_confirme` |
| Comparer à une référence sans le mécanisme proposé | `--sans-cartes`, `p_sans_cartes`, `moteur_contre_jugement` |
| Chargement sélectif du contexte | table « Ce qu'il faut charger » de `SKILL.md` |
| Critères figés avant l'issue | scellés, résolution figée, journal non réécrit |
| Rattachement d'un attribut au bon acteur (*Language-Guided World Models*) | `option` (acteur nommé) et `objet` ; renforcé par `passage` |

### 10.3 Ce qui attend

| Piste | Condition | Version |
|---|---|---|
| Registre de dépendances : une source corrigée signale les mots, états et prévisions qui en dépendent (Alex Zhang) | un premier cas réel où une source est corrigée ; sans lui, le registre serait une documentation de plus | Éprouver |
| Dossier externe et sous-tâches bornées (*Recursive Language Models*) | dossiers réels assez longs pour que le banc montre une perte de pièces ; comparer d'abord un simple index à la décomposition, coût compris | Éprouver |
| Comparaison de trajectoires datées, contre l'état courant seul (VECTOR) | avec H1.6, 30 cas actifs dans une strate | Éprouver |
| Aide apprise proposant des marqueurs ou des cas voisins (VECTOR, ReasonIR) | corpus annoté, séparé par épisode et par date ; la proposition reste vérifiée par le codeur | après 1.0 |
| Corpus documentaire figé et son manifeste (MassiveDS, DataComp-LM) | premières comparaisons de recherche au banc | Éprouver |

### 10.4 Ce qui est refusé

- **Distances vectorielles converties en probabilités**, déplacement dans un espace de textes lu comme
  TRANSFORMATION, sortie de classifieur sommée à 100 % entre cartes : ces grandeurs ne mesurent pas
  l'objet du moteur, et plusieurs cartes coexistent.
- **Cartes ordonnées en étapes** : les cartes ne forment pas une succession unique.
- **Indices de confiance internes** (tokens, stabilité de réponse) comme force F/f ou comme
  probabilité : une erreur peut être stable.
- **Consensus de modèles ou de générations** comme corroboration ; **architecture multi-agent** ou
  récursion par principe : à comparer d'abord à une procédure simple, mêmes sources et budget.
- **Retirer une règle parce qu'aucune sortie ne l'enfreint** (rubriques sans variance de DR Tulu) :
  valable pour un signal d'entraînement, pas pour une règle constitutive.
- **Écarter les observations difficiles** (filtrage de données d'Arctic) : un résultat nul ou une
  abstention sont des observations.
- **« Indéterminé » comme troisième issue probabilisée** : c'est un état de l'information.
- **Nouvelles cartes « contexte », « recherche », « récompense »** : elles décrivent l'outil, pas une
  structure observée. Aucun de ces travaux ne justifie les 16 cartes, les 13 strates, la matrice ou
  les multiplicateurs.
- **Usage individuel ou clinique** des trajectoires de pensée (VECTOR) : hors périmètre (`constitution.md` §6).
