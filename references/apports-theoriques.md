# Alphabet situationnel — Apports théoriques et leur traduction en contrôles

> Version : 0.7.11

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
| Contrôle affirmation–passage | OpenScholar (Shao) ; spécifications (Hao Zhang) | `passage` {localisation, relation} requis pour F de cas actif ; F exige `soutient`, `partiel` donne f, `contredit` renvoie à A7, `insuffisant` n'ancre rien (scindé en 0.7.11, §15) ; « independantes » exige deux passages | `protocole.md` A6, `controle_passage` |
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

---

## 11. « Ce qu'il manque à l'Alphabet situationnel » (0.7.5)

Note versée par l'auteur le 30 octobre 2026, rédigée sur la 0.7.4 : de Finetti (1937), David et
Michaud (1989), Goldfarb et Pardoux (2011), Vidal (2004), Diebold et Mariano (1995), Gneiting et Raftery
(2007), Carletta (1996), Reidsma et Carletta (2008), Gruber (1995), Gómez-Pérez et al. (2004), Bartlett
(1932), Weidmann. Chaque chiffre a été **recalculé** sur le dépôt avant intégration. La note est
juste sur l'essentiel — la matrice n'était jamais confrontée aux observations, les écarts de score
n'étaient jamais testés, les jalons n'avaient pas de calcul de puissance — et se trompe sur sept points,
dont trois de conception.

### 11.1 Vérifié et retenu

| Point | Vérification | Contrôle ajouté | Où |
|---|---|---|---|
| Matrice jamais confrontée aux observations (§2.1) | exact ; mesure **corrigée** (11.2) | `confronter` : chaque apparition classée par la règle du moteur | `graphe.md` §2.4, `SKILL.md` |
| Écarts de score publiés sans test (§2.10) | exact : `apport_cartes` concluait sur une moyenne. Table du test du signe exacte (0,101 ; 0,033 ; 0,008 ; 0,001) | différentiel par épisode, σ(d), autocorrélation d'ordre 1, tests exacts du signe et de Wilcoxon ; lecture tirée du test | `validation.md` §5 |
| Résidus non testés (§2.8) | exact ; fondu dans le point précédent, comme la note le propose | autocorrélation des d d'épisodes, descriptive | idem |
| Précision de f (§2.6) | chiffres exacts (6,9 points, 138 %, 60 % de zéro succès sur 10) ; critère proposé corrigé (11.2) | intervalle de la loi de f, part de la référence, « ancré » qualifié | `graphe.md` §2.2 |
| Poids des deux a priori (§2.5) | exact (k₀ = 20, k = 2 sont des pseudo-observations) ; lecture corrigée (11.2) | deux poids dans la trace | `graphe.md` §4 |
| Seuil κ sans source (§2.3) | citations conformes ; repères d'α repris pour κ, déclaré | `kappa_min` 0,67, `kappa_rapportable` 0,80, réservés ; forme des désaccords | A4, `base-de-cas.md` §6 |
| Puissance des jalons (§2.9) | direction juste, chiffres **faux** (11.2) | table de puissance recalculée | `feuille-de-route.md` §1 |
| Classe de source (§2.4) | pertinent ; réalisable à coût nul tant qu'aucun cas n'est actif | `classe_source` requis pour un cas réel actif et un dossier | `base-de-cas.md` §2 |
| Fenêtre sans lien à la durée (§2.2) | chiffres exacts (96,75 / 86,62 / 65,00 / 42,25 %) ; option A retenue, option B refusée (elle mêlerait la question au modèle) | `duree_caracteristique_jours` sourcée, refus avec temporalité générique sous la moitié de la fenêtre | `graphe.md` §2.4 |
| Intervalle dit « approximatif » (§4.1) | la forme Beta-binomiale est exacte ; « intervalle exact » est **trop fort** (11.2) | libellé corrigé dans le moteur, `graphe.md`, `SKILL.md`, glossaire | `graphe.md` §4 |
| Taux constant (§2.7) | table d'âge reproduite (80/68, 45/40, 12/10) ; interprétation corrigée (11.2) | hypothèse déclarée ; mesure par `confronter` | `graphe.md` §2.4 |
| `p_sans_cartes` = f (§4.5) | vérifié à l'égalité exacte | identité écrite, décomposition p − f | `graphe.md` §3.3 |
| Score logarithmique (§4.3) | pertes vérifiées (0,9025 / 3,00 ; 0,9801 / 4,61 ; 0,998 / 6,91) | `log`, `log_sans_cartes`, `log_infini` | `validation.md` §5 |
| Cohérence au sens de de Finetti (§4.6) | exact : partitions sommant à 1 | limite écrite | `SKILL.md` Limites |
| Épreuve bien déterminée (§3.3) | principe juste, contrôle proposé **faux** (11.2) | une révision garde l'épreuve | `valider_journal` |

### 11.2 Corrigé avant intégration

1. **Mesure de la matrice.** Sur `cas-reels.jsonl`, la note compte 1 apparition non atteignable sur 3
   (TRACE·MÉMOIRE@5) ; il y en a **2** : CONTRAINTE@8 depuis RÉSEAU@5 n'est atteignable par aucune arête
   (RÉSEAU n'en a aucune vers CONTRAINTE). Sur la base d'exemple, l'unique cas signalé part de l'état
   nul, qui n'est pas une divergence de matrice ; une autre apparition n'est atteignable que par une
   arête inter-strates abaissée. Ces quatre cas sont des archives exclues : la mesure illustre le
   contrôle, elle ne confronte la matrice à rien.
2. **Puissance de κ.** La note traite κ comme une proportion (erreur-type √(κ(1 − κ)/n)). L'erreur-type
   de κ dépend de l'accord attendu par hasard pₑ et vaut environ √(pₒ(1 − pₒ)/n) / (1 − pₑ) (Cohen
   1960), nettement plus grande : pour distinguer 0,80 de 0,60, environ 83 unités et non 33 (pₑ = 0,5).
   La conclusion de la note est renforcée, ses chiffres sont faux. Et l'unité est la décision codée,
   pas le cas.
3. **Puissance de V4.** La colonne « 2,5 points » de la note est calculée pour 2 points : 49 épisodes
   pour σ(d) = 0,05 au lieu de 32 (les colonnes 5 et 10 points sont justes). Le seuil de suffisance de
   50 épisodes est σ(d) ≲ 0,063, non 0,05. L'exemple de modèle informé (Brier 0,0446) n'est pas
   reproductible : calibré sur une fréquence de 5 %, il donne 0,0465.
4. **Taux constant et hystérésis.** La note écrit que le modèle « nie la mémoire » de SEUIL et de
   TRACE·MÉMOIRE. C'est confondre la dépendance au chemin de la **situation** — portée par l'état, son
   inertie et ses arêtes — avec la dépendance à l'**âge** d'un mot, seule absente. Une chaîne de Markov
   représente l'hystérésis : c'est l'inertie de 0,97.
5. **Ce que teste le placebo.** La note en fait le test de l'échangeabilité de la classe. Il teste
   l'inverse : que la classe **diffère** du reste de la strate. Un apport nul est ce que prédirait une
   strate entièrement échangeable ; l'échangeabilité interne à la classe reste postulée (`graphe.md`
   §3.3).
6. **Épreuve commune.** Imposer le même critère à toutes les lignes d'un même `evenement` refuserait
   SEUIL@7 sur deux objets différents. Le phénomène est déjà fixé par le marqueur local, contrôlé ;
   l'épreuve (source, critère, seuil, objet) est propre à une question. Le contrôle retenu : une
   révision — même épisode, même événement, même échéance — garde son épreuve.
7. **Lectures trop fortes.** « Intervalle exact » : exact pour une vraisemblance pondérée, approché pour
   ce qu'il vise. « Dix fois plus de confiance dans le défaut que dans les homologues » : k₀ et k
   portent sur deux quantités différentes. « Refuser “ancré” tant que l'intervalle de f contient 0 » :
   l'intervalle d'une loi Beta lissée ne contient jamais 0. « 30 est la borne du théorème central
   limite » : c'est une règle d'usage, et ρ0 ne repose sur aucune approximation normale. Le dépôt ne
   citait ni CAMEO ni Weidmann, contrairement à ce que dit la note ; ρ4 est calculé. La perte
   quadratique comme critère de la prévision est développée surtout dans des textes postérieurs de de
   Finetti (années 1960 et 1970) ; le texte de 1937 fonde la cohérence sur le pari.

### 11.3 Ce qui attend, et ce qui est refusé

**Attend** (`feuille-de-route.md` §1) : seuil d'ancrage, atténuation par corroboration et passage,
loi de Weibull, idéologie sémiotique à l'étape 5, contrôle de circularité de la garantie, test de
représentativité (sans population de référence, il reste vide), évaluation des 208 cases contre les
critères de Gruber (clarté, cohérence, extensibilité, biais d'encodage minimal, engagement ontologique
minimal). La distinction vérification / validation de Gómez-Pérez est celle que le dépôt écrit déjà
(« l'audit vérifie la forme, pas la vérité ») ; elle est désormais attribuée. Que les trois arêtes fortes
soient « dérivables des définitions » n'est pas établi et n'est pas repris.

**Refusé**, avec la note elle-même : statistique de Diebold-Mariano asymptotique comme premier outil,
appareil ARIMA, indices de prix, lois de distribution, tests de comparaison de moyennes, p-value comme
critère de décision, ontologie greimassienne, dix-septième carte, mode d'abduction, aspectualité à la
place de `temporalite`. Renommer le champ `frequence_de_base` casserait le schéma du journal : le champ
garde son nom, `graphe.md` §2.2 dit ce qu'il est (une moyenne a posteriori, non une fréquence observée).

---

## 12. « Capacité et généralisation » et « Réponses à la feuille de route » (0.7.6)

Deux notes versées par l'auteur le 30 octobre 2026. La première lit Dreyfus et al. (2008), *Apprentissage
statistique*, ch. 1 et 2, pour la méthodologie d'évaluation seulement ; la seconde répond aux décisions
ouvertes de `feuille-de-route.md` §1. Chiffres recalculés avant intégration.

### 12.1 Vérifié et retenu

| Point | Vérification | Ajout | Où |
|---|---|---|---|
| Variable sonde sur les paramètres | reproduite : matrice réelle au 99ᵉ centile des arêtes aléatoires (la note : 97ᵉ, autres tirages), au 83ᵉ des intensités permutées (la note : 71ᵉ) ; inerties sans effet sur une apparition à un pas | `moteur.py sonde`, avec la référence « cas seuls » qui manquait | `graphe.md` §3.4 |
| `n_min_frequence` ne change pas p | exact : p = 22,04 % de n_min = 3 à 76 ; la feuille de route 0.7.5 se trompait | ligne corrigée ; effet réel écrit (comparateur V4, ρ3) | `feuille-de-route.md` §1 |
| Concentration des poids (Kish) | exact : 9,34 pour 10 cas, cas le plus lourd 15,5 % | `n_eff_kish`, `part_cas_le_plus_lourd` dans la trace | `graphe.md` §3.2 |
| Variante corroboration / passage avant la décision 5 | orthogonale à F/f, sans effet sur p | sondes `effet_attenuation` (force ; corroboration et passage avec un dossier) | `feuille-de-route.md` §1 |
| Circularité de la garantie : signaler, ne pas refuser | juste : faux signalements inconnus | signalement dans le dossier | idem |
| Champ d'idéologie écrit avant l'étape 5 | juste : une déclaration rétrospective ne prouve rien | `signe_suffisant`, `declare_le` ≤ `codage.debut` | `base-de-cas.md` §2 |
| Critère du premier cas | juste, et la mise en garde contre le tri sur l'informativité aussi | critère écrit | `feuille-de-route.md` §4 |
| Étape 3 possible avant l'étape 2 | exact ; RÉSONANCE@7 a 2 recherches sur 3 | écrit | idem |
| Capacité relative aux exemples | juste dans sa direction | mesure arête par arête (`couverture_aretes`), P8 complété | `graphe.md` §3.4 |

### 12.2 Corrigé

1. **Ce que reproduit le hasard.** La note conclut que « 68 % de l'apport revendiqué est reproduit par une
   matrice aléatoire », artefact de la densité du graphe. Sa médiane aléatoire (18,87 %) est **exactement**
   le p obtenu sans aucun multiplicateur : ce que le hasard « reproduit » est la révision par les cas,
   présente quelle que soit la matrice. Avec la bonne référence, une matrice aléatoire médiane apporte
   +0,0 point, la vraie +3,2. La densité explique qu'un tirage sur trois environ déclenche un multiplicateur,
   pas que l'apport soit un artefact.
2. **Parcimonie.** La note lit la règle de niveau comme « le niveau qui offre le plus de cas, donc le plus
   complexe ». C'est l'inverse : la règle retient le niveau le plus **spécifique** (H1, le plus complexe)
   dès 3 cas, et ne regroupe qu'en dessous ; la parcimonie de Dreyfus et al. favoriserait le regroupement,
   et elle suppose des scores de validation qui n'existent pas. L'« option 2 » de la note est la règle
   actuelle. Le choix est écrit comme compromis biais-variance (`graphe.md` §3.2).
3. **« Proposé clos ».** Refusé : il compterait comme traitée une correspondance qu'aucun texte ne
   soutient. La règle existante suffit si elle est appliquée : non soutenu à la lecture → Vide, puis clos.
4. **Richardson pour CROISSANCE.** Ne convient pas : taux fonction du niveau adverse, terme propre
   d'amortissement, pas de capacité limite. **Modelski et Thompson pour PÉRIODICITÉ** : à vérifier contre
   la règle de la strate 12. **« `p_sans_cartes` n'est publié que si la question est ancrée »** : faux ; il
   l'est toujours ; c'est `frequence_de_base`, comparateur de V4, qui dépend de l'ancrage.
5. **Comptes.** 121 paramètres « libres » mêle paramètres de modèle et seuils d'affichage ou de
   validation ; « de l'ordre de 120 cas pour 121 paramètres » n'est pas une règle, et la dimension de
   Vapnik-Chervonenkis n'est pas le nombre de paramètres en général. Les 28 cas d'exemple sont fictifs :
   le rapport utile est zéro. La mesure qui convient est la couverture des arêtes.
6. **Validation croisée.** Le partage apprentissage / test du dépôt ne sert pas à sélectionner un modèle
   (rien n'est ajusté) ; l'épreuve de généralisation est le journal prospectif. La validation croisée est
   différée, avec la réserve de la note sur les cas dépendants.

### 12.3 Refusé ou différé

Réseaux, SVM, cartes topologiques, régularisation, arrêt anticipé, bornes numériques de
Vapnik-Chervonenkis : refusés avec la note. Weibull : différé, le diagnostic d'âge existe depuis 0.7.5
(`confronter`). Seuil d'ancrage dédoublé, rétrogradation de CROISSANCE@7, troisième recherche de
RÉSONANCE@7, lecture d'un texte pour PÉRIODICITÉ@7 : décisions et travaux de l'auteur
(`feuille-de-route.md` §1 et §4).

---

## 13. Accord sous faible prévalence, rejets, concessions (0.7.9)

Document versé par l'auteur le 30 octobre 2026. Il signale que la nécessité de ces contrôles a été
constatée en examinant un projet public de skills sous licence CC-BY-NC 4.0 ; **aucun texte, tableau,
gabarit ni code de ce projet n'est repris**, et seules les sources primaires sont citées : Cohen (1960) ;
Feinstein et Cicchetti (1990, « High agreement but low kappa: I ») ; Cicchetti et Feinstein (1990,
« … II. Resolving the paradoxes », accords spécifiques positif et négatif) ; Byrt, Bishop et Carlin
(1993) ; Krippendorff (1980) via Carletta (1996) ; Reidsma et Carletta (2008). Les formules sont celles de
ces articles ; la rédaction est propre au dépôt.

### 13.1 Retenu

| Point | Vérification | Contrôle ajouté | Où |
|---|---|---|---|
| κ s'effondre sous faible prévalence | juste ; κ = −0,009 pour 116 accords sur 118 reproduit | table 2×2, κ indéfini déclaré, PABAK, accords spécifiques | `moteur.py accord`, `base-de-cas.md` §6, A4 |
| PABAK seul ne voit pas un codeur qui n'ancre jamais | juste : 0,908 contre κ = 0 | verdict sous plafond des taux de manque (`fnr_max` 0,20) | idem |
| Erreurs directionnelles | juste dans l'idée ; corrigé (13.2) | **deux** taux de manque | idem |
| Les rejets ne sont relus par rien | juste | `rejets` : feuille aveugle, tirage fixé par le sceau, contrôle de l'audit | `validation.md` §6 |
| Révision sous insistance | juste ; déjà en partie couvert par A7 et A5 | journal des concessions, contrôles de cohérence | `validation.md` §6 |

### 13.2 Corrigé

1. **Prévalence mesurée.** La note compte 87 ancrages sur 1 888 décisions (4,6 %) ; il y en a 205 (10,9 %)
   — elle comptait les seuls mots documentés à leur apparition, pas leur présence dans chaque état. Les huit
   cartes jamais présentes sont exactes ; la conclusion tient, moins fortement.
2. **Tables de κ.** La ligne « 0 ancrage » (pₒ 0,983, PABAK 0,966) est impossible : sans ancrage, pₒ = 1 et
   PABAK = 1. « Un désaccord → κ 0,496 » ne se reproduit pas : un désaccord donne κ = 0 (un seul ancrage, non
   partagé) ou 0,663 (un ancrage commun, un en plus) ; 0,491 correspond à deux désaccords.
3. **FNR et FPR prennent le premier codeur pour référence.** A4 n'en reconnaît aucune. Les deux taux de
   manque se publient ; c/(c+d), voisin de zéro sous faible prévalence, n'informe pas.
4. **Le seuil de 15 % de prévalence** pour passer de κ à PABAK n'est dans aucune des sources citées : non
   repris. PABAK sous plafond des taux de manque porte le verdict à toute prévalence ; κ est toujours publié.
5. **Les « 95 % de rejets ».** Les 1 888 décisions comptent toutes les cartes de tous les états ; un rejet
   au sens du dossier est une candidate écartée avec motif, soit quelques-unes par dossier. Les cartes
   jamais candidates ne sont pas relues. Le **rejet « near-miss »** (tous les marqueurs présents dans les
   faits) n'est pas calculable par machine : un marqueur est une phrase, pas un champ ; non repris, la
   liste ne pourrait pas être « recalculée ».
6. **Numéro.** 0.7.9, la 0.8 restant réservée aux étapes 2 et 3.

### 13.3 Refusé

Les mécanismes que la note écarte elle-même (§5 : déjà présents, souvent mieux ancrés) ; un barème
d'accord concurrent ; tout texte du projet examiné.


---

## 14. Six notes et un audit des rivaux (0.7.10)

Versés par l'auteur le 30 octobre 2026 : notes sur Green et Armstrong (analogies structurées), sur les
profils apparentés à Perez, sur Toulmin (lu par Plantin), sur MACTOR (Godet), sur la recension de *Noise*
par Sood et Gelman, et sur trois rivaux (Wardley, Cynefin, Bueno de Mesquita) ; puis un complément et un
audit de ces notes. Lus sur le code de la 0.7.9, pas sur les notes seules. **Aucune probabilité ne
change** (144 calculs de démonstration identiques ; `scorer` ne diffère que par des clés ajoutées).

### 14.1 Retenu

| Point | Vérification | Contrôle ajouté | Où |
|---|---|---|---|
| Le mécanisme n'a pas de répondant (*backing*, Toulmin 1958, ch. III) | juste : `garantie` couvre loi de passage et réfutation, pas le support | `garantie.support` {type, reference, disponible_le} ; `argument` refusé ; prospectif | protocole A6 « Support », `base-de-cas.md` §2 |
| Une réfutation qui n'annule rien n'est pas une réfutation | juste ; aucun contrôle ne le voyait | `contredirait` ≠ `attendu` (refus) ; `contredirait` qui nomme la carte (signalé) | idem, `moteur.py dossier` |
| F occupe la place du modalisateur de Toulmin sans en être un | juste ; le texte le laissait entendre | écrit : F n'est pas un « probablement », la force d'une conclusion est p et ρ | protocole A6 |
| Bruit d'occasion (répétabilité) non mesuré | juste ; la source est la métrologie, et pour des codes catégoriels l'**analyse d'accord par attributs**, pas Gage R&R | `accord --repetabilite --ecart-jours`, `repetabilite_ecart_min_jours` 30 | A4, `base-de-cas.md` §6 |
| Représentation stratégique (Flyvbjerg 2008) | juste ; mais Flyvbjerg est contesté sur le référentiel (Love et Ahiaga-Dagbui 2018 ; réponse Flyvbjerg et al. 2018) | `interet` (promoteur refusé), `fourni_par`, `referentiel`, facultatifs | `frequences-externes.md` §2 |
| « Jugement » sans procédure | juste : la condition la moins bien mesurée ; un étalon public existe (modèle de compromis, Thomson et al. 2006) | `procedure` requise à compter de `jugement_procedure_depuis` ; Brier par procédure | `validation.md` §1 |
| Le bras externe le plus exigeant est le modèle sans le skill | juste ; le dispositif existait (0.7.8), pas la consigne | méthode recommandée du comparateur externe | `validation.md` §1 |

### 14.2 Corrigé dans les notes

1. **« Le moteur retient un homologue unique, régime à 38 % » (note Toulmin §5) : faux.** Le moteur compte
   **tous** les cas de la base au niveau d'homologie retenu (H1, H1.5, H2), pondérés ; il publie `c_A`,
   `n_eff_kish`, `nb_cas_par_niveau`, la fragilité de niveau et un placebo d'homologie (`graphe.md` §3).
   La contrainte d'ordre de Green et Armstrong (lister avant de noter) est satisfaite **par construction**
   pour le moteur : la sélection est une règle fixée d'avance, appliquée à toute la base, sans arrêt à la
   première analogie — c'est exactement la « règle qui bat la synthèse de l'expert ». Le champ
   `homologues_listes` proposé n'entre donc pas. Le risque d'arrêt prématuré se déplace vers la
   **composition de la base** (quels cas on code) : il relève de B5 (registre daté du partage avant
   codage) et du test à l'aveugle, pas d'un champ du dossier.
2. **De même, la question critique de Walton** (« un autre cas semblable a-t-il une issue contraire ? »)
   est déjà dans le calcul : les homologues à issue contraire comptent dans n_A − n_E. Le
   « contre-homologue » proposé par le complément n'entre pas.
3. **« Pluralité forcée mesurée trois fois par des équipes différentes » (note des rivaux §6) : faux.**
   Green 2002, Green 2005 et Green et Armstrong 2007 sont d'un même laboratoire. La seule réplication
   indépendante trouvée (Nikolopoulos et al. 2015, *J. Business Research* 68(8)) donne un gain **faible**
   des analogies structurées (+5 à 8 %, deux versions du résumé) et un gain fort des groupes qui mettent en
   commun leurs analogies : le « travail individuel vaut mieux » ne se généralise pas, et l'expérience y
   améliore la justesse. Le refus des architectures multi-agents **comme corroboration** (§10.4) tient, par
   la dépendance des sources ; il ne s'appuie plus sur Green et Armstrong.
4. **Green 2005** : publié (*IJF* 21(3), 463-472) ; la note citait le document de travail, et ses chiffres
   (31 % contre 32 %) au lieu de ceux de l'article (31 % contre 31 %).
5. **Bueno de Mesquita** : l'étalon n'est ni Feder ni le jeu de rôle, mais le modèle de compromis, testé
   avec le modèle de défi sur les décisions de l'UE (Thomson, Stokman, Achen et König 2006 ; Achen, ch. 10).
6. **« Les deux concurrents oubliés »** (complément) : le modèle nul existe depuis 0.5 (`--sans-cartes`,
   `p_sans_cartes`, V4 lu contre l'inertie), le bras externe depuis 0.7.8. Ce qui manquait était la
   consigne de jouer **le modèle seul** comme bras externe.
7. **Gage R&R** (note *Noise*) : outil des grandeurs continues ; pour des cartes, l'analyse d'accord par
   attributs. Recension : *CHANCE* 37(3), 70-72. Théorème des piranhas : *Notices of the AMS* 72(1),
   15-25 (2025), six auteurs.

### 14.3 Ce qui attend

| Apport | Condition | Note |
|---|---|---|
| Analyse CIB (Weimer-Jehle 2006, *TFSC* 73(4) ; ScenarioWizard) : sonde de **cohérence** de la configuration des cartes ancrées | une matrice d'impacts entre **états** publiée et datée, distincte des 66 arêtes | plus proche de la « proxémie » que MICMAC ; sujette à l'erreur de spécification, comme les arêtes |
| MICMAC : invariant ΣI = ΣD et quadrants influence × dépendance comme sonde | décision d'auteur sur le sort d'une arête non structurante | arithmétique incompatible avec les λ : sonde, jamais multiplicateur |
| Couverture de l'alphabet (TRIZ : une matrice tirée d'un corpus daté perd de la couverture ; ~40 % contre ~80 % pour une matrice reconstruite, doi:10.1007/s10845-010-0466-4) | premiers cas actifs (étape 2) | part des faits d'un dossier récent exprimés sans « non classé », par strate et période ; **indicateur d'usure, jamais garantie de lecture** (§15 : un taux agrégé monte quand on lit plus, pas quand on lit juste) |
| Typologie des contraintes de Cynefin (contrainte **habilitante**) | décision d'auteur : touche A1 | CONTRAINTE n'a qu'un type, qui retire des options |
| Marqueurs de maturité de Wardley (types de publications) | décision d'auteur : marqueur nouveau | candidat pour CROISSANCE et TRANSFORMATION |
| Épreuves des rivaux : Cynefin (accord **à structure égale**, ≥ 30 situations), Wardley (persistance d'un composant sous la règle de décomposition), SenseMaker (signification par les acteurs contre codeur extérieur) | lots du banc d'essai (`validation.md` §9) | un κ sur cinq domaines exclusifs ne se compare pas à un κ sur ensembles de cartes |
| Théorème des piranhas comme borne des λ | cas réels actifs | argument externe, analogie de forme : pas de calcul transposable |

### 14.4 Refusé

Les doctrines et prescriptions des rivaux (40 principes de Wardley, « probe-sense-respond », phase 5 de
MACTOR, 40 principes de TRIZ) : `constitution.md` §5. Les chiffres des rivaux et de *Noise* comme
fréquences externes. Le seuil « ≥ 2 analogies et expérience directe » (sous-groupe post-hoc de 23
prévisions) comme filtre. Un champ nommé `qualifier` ou `qualificatif` (collision avec G1). Toute
conversion de F en force modale. La collaboration entre codeurs comme corroboration.

---

## 15. *open-ontologies* : un régime de preuve, pas un rival (0.7.11)

Note versée par l'auteur le 30 octobre 2026 sur le dépôt `fabio-rovai/open-ontologies` (MIT), à partir de
son README, de sa décision 0007 et du résumé de CIVeX (arXiv:2605.09168) ; ni code lu ni outil exécuté.
Tout ce qu'elle rapporte de ce dépôt est donc affirmé par lui, non vérifié ici. Le dépôt ne dispute pas
l'objet de l'alphabet ; il dit comment rendre une dérivation re-vérifiable par un tiers. **Aucune
probabilité ne change, et c'est désormais établi par clôture** : 2 790 conséquences sur les 111 états de la
base d'exemple, empreinte identique pour la 0.7.9, la 0.7.10 et la 0.7.11
(`b1a592c8184d505becf216d07b83a2b5545e08527c4c67f2311b20b5530fdade`).

### 15.1 Ce que le skill fait déjà

Six règles du dépôt coïncident avec des règles du skill, trouvées séparément dans une discipline sans
rapport (ingénierie d'ontologies) : aucun chiffre sans producteur ; vocabulaires séparés et non
permutables ; l'incertitude portée par l'artefact, pas par une note ; sceller avant l'issue et ne jamais
réécrire ; un contrôle non exécuté ne s'affiche pas comme un contrôle réussi ; la partie stipulée se
déclare. C'est une corroboration **de méthode**, venue d'une source qui ignore l'alphabet — pas un
apport, et pas une preuve que la lecture est juste. Les deux systèmes prouvent ce qui est en aval de leur
partie stipulée et laissent celle-ci en prose : ici, les 66 arêtes et le barreau déclaré.

### 15.2 Retenu

| Point | Vérification | Contrôle ajouté | Où |
|---|---|---|---|
| `insuffisant` confond une lecture trop étroite et un fait sans source, aux remèdes opposés | juste : le message disait « corriger le fait, chercher une autre pièce, ou ne pas ancrer », trois remèdes pour deux causes | `absent_de_la_piece` (élargir) et `non_soutenu` (retirer) ; `insuffisant` refusé | protocole A6, `controle_passage` |
| « La couverture est mesurée » nomme un proxy qui monte quand on lit plus, pas quand on lit juste | juste ; l'intention (profondeur plutôt qu'étendue) était bonne, le mot mauvais | écrit : chaque ancrage se mesure, un par un ; la couverture TRIZ (§14.3) reste un indicateur d'usure, jamais une garantie | `SKILL.md`, §14.3 |
| « independantes » ne dit pas ce qui rend les pièces indépendantes | juste : deux identifiants peuvent partager une origine ; l'accord ne protège alors que des erreurs de transcription | `independance` {critere : origine, producteur, transmission ; motif}, prospectif | protocole A6, `controle_corroboration` |
| « Aucune probabilité ne change » vérifié par témoins, pas par conservativité | juste ; le vocabulaire est fini, la clôture calculable | `conservativite` : clôture complète, empreinte, comparaison ; désarmés comptés | `validation.md` §9 |
| Le refus du barreau 2 | juste : CIVeX montre qu'une intervention exige l'identifiabilité, donc un graphe causal engagé | rédaction : conséquence de P1, non prudence | `SKILL.md`, Limites |

### 15.3 Refusé

Le vérificateur formel (Lean) : un mécanisme est une phrase, on ne vérifie pas une phrase par machine,
et le vouloir serait le théâtre théorique (§5). Les certificats de dérivation comme format de fiche : une
dérivation qui citerait une arête postulée certifierait une pétition de principe ; le dépôt lui-même
change le mot du verdict dans ce cas. Aucune sortie du skill ne doit dire qu'une issue « découle » ou est
« impliquée » par les cartes. CIVeX comme outil : il agit sur des actions d'agent dans un environnement
instrumenté ; une lecture n'a ni action ni graphe engagé. Les ontologies du marché, les plongements et le
vocabulaire de production (« blast radius », « drift », « rollback ») : hors périmètre.
