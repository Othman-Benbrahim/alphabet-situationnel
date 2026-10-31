# Alphabet situationnel — Journal des versions

> Version : 0.5.1

## 0.5.1 — 2026-10-26 · après le second test sur la politique française (sénatoriales)

Chiffres du test reproduits (2,8 % / 1,6 % ; 1,6 % ; 18,4 % ; 1,7 % / 1,4 %). La strate 13 fait son
office : le mouvement s'ancre et les cartes déplacent p sur deux questions sur quatre. 75 autotests.

- **Marqueur de SEUIL@13 restreint** (défaut de la 0.5.0, relevé par le test) : « résultat électoral
  proclamé » faisait de tout scrutin un seuil ; désormais, seul un résultat qui change la majorité ou
  entraîne une alternance, avec censure, dissolution et démission du chef de l'État.
- **A6 : marqueur rempli, définition contredite** → carte non ancrée (ni F ni f), marqueur signalé au
  journal des lacunes. Le test avait gardé SEUIL@13 en f faute de règle.
- **Refus de « apparaît » sur un mot présent** : le message explique la règle d'un mot par carte et
  par strate et la sortie (retirer un mot mal ancré, ou questionner sa persistance).
- **Questions nominatives** (`"origine": "jugement"`) : « qui sera élu ? » n'est pas un événement de
  carte. Ces probabilités humaines se journalisent sans état ni ρ, et `scorer` les note à part
  (`jugements` : Brier, référence d'une réponse indifférente), jamais dans le score du moteur ni V4 ;
  une partition ne peut pas mêler les deux origines. Sur les trois jugements du test : 0,234.
- **Ordre des rejeux** (`validation.md` §8) : du plus ancien au plus récent ; une issue déjà vue,
  même dans un autre test, rend la question `rejeu: true`.
- Exemple 12.

Non retenu : rien. Le test proposait exactement la restriction du marqueur appliquée ici.

## 0.5.0 — 2026-10-26 · strate 13 « Politique intérieure », sources françaises, comparateur inertiel

Version mineure : la liste des strates change (O3). 73 autotests (71 + 2). Les fiches actives passent
en `version_regles` 0.5.0 après revalidation ; le journal d'exemple, figé, reste en 0.4.0.

### Test régressif sur la politique française (19 → 26 octobre), vérifié

Les deux probabilités scorées (0,8 % et 6,8 %) sont reproduites, et l'ablation `--sans-cartes` donne
bien les mêmes valeurs. Constats retenus :

- **Il manquait une strate.** Ni la 5 (règles d'appartenance), ni la 7 (rapports entre États), ni la
  8 (normes) ne couvraient la compétition pour le pouvoir et les mouvements sociaux. **Strate 13
  « Politique intérieure »** : fiche dans `strates.md`, 16 équivalents Proposés
  (`equivalences/strate-13.md`, dont ÉMERGENCE@13 « mouvement social auto-organisé » et SEUIL@13
  « gouvernement renversé, dissolution »), frontières avec les strates 5, 7, 8 et 9 (`strates.md` §4).
  Numéro 13 pour ne renuméroter aucune strate. Le nombre de strates devient un paramètre
  (`nombre_strates`) : le moteur, l'audit (208 équivalents) et les identifiants en dépendent.
- **Un bon score sans apport des cartes.** `calculer` imprime désormais la probabilité sans cartes et
  l'écart ; le journal l'exige (`p_sans_cartes`, à partir des prévisions 0.5) ; `scorer` calcule
  `apport_des_cartes`. **Constat de conception** mis au jour par le test : sans base, les cartes ne
  modulent que les apparitions ; une persistance ou une disparition ne teste que l'inertie
  (`graphe.md` §2.1).
- **« La contrainte s'étend-elle ? »** était déjà exprimable par `s'intensifie` avec une grandeur
  comptée ; l'exemple 11 le montre et `sources-france.md` §5 donne des grandeurs.

Non retenu tel quel : **SEUIL@8 « régime d'exception déclaré »**. Un état d'urgence est réversible :
c'est une CONTRAINTE@8 qui apparaît ou s'intensifie ; SEUIL@8 est étendu à la seule pérennisation
dans le droit commun, et la bascule politique irréversible devient SEUIL@13.

### Éléments repris d'EnVrai? (licence MIT)

- `references/sources-france.md` : sources officielles françaises par thème et par strate, voies
  d'accès (adaptées de `docs/puits.md`), séries Eurostat utilisables comme grandeurs (adaptées de
  `catalogue.ts`), ordre de préférence des sources par nature (sans les facteurs de Bayes, déclarés
  non calibrés par leurs auteurs) ; ajouts propres marqués **[ajout]**, à vérifier.
- `LICENCES-TIERS.md` : notice MIT d'EnVrai?, exigée par sa licence.
- Non repris : le code (serveur, add-on, capture audio), propre à un autre usage ; les 29 débats
  transcrits et leurs 4 713 affirmations, qui sont des énoncés à vérifier, pas des cas de situation ;
  le paquet bayésien (échelle de Jeffreys en décibans), dont le moteur n'a pas l'usage.

## 0.4.8 — 2026-10-26 · décisions d'auteur 1a et 1c, statut Hors domaine

71 autotests (70 + 1).

- **Strate 12 conservée (décision 1a, option A).** Registre de longue durée : un fait n'y entre que si
  sa signification dépend d'une période de plus d'un siècle. La « limite connue » de `strates.md`
  devient une hétérogénéité assumée ; la réduction à 11 strates est écartée.
- **Statut « Hors domaine » créé, non attribué.** Vide dit qu'on n'a rien trouvé ; Hors domaine dit
  qu'il n'y a rien à trouver. Décision d'auteur motivée (motif en colonne Référence, exigé par
  `audit`), aucun ancrage possible : `valider` refuse le mot, `calculer` refuse l'événement, les
  trajectoires ne le proposent pas. Bilans, tableau de `equivalences.md` §3 et totaux étendus à ce
  statut (0 partout). L'attribution aux cartes à agents attend la décision 1b, reportée par l'auteur.
- **Licence MIT, auteur Othman Ben Brahim (décision 1c).** `LICENSE`, en-tête du README, `license` et
  `author` dans SKILL.md, docstring du moteur.
- Lecture des statuts mise en cache (relue si un fichier de strate change) : les trajectoires
  l'appellent pour chaque candidate.

## 0.4.7 — 2026-10-26 · recodage des cas réels, feuille de route

70 autotests (68 + 2).

### Recodage des quatre cas réels (étape 2)

- **Nouveau statut `proposition`.** Une fiche recodée ne pouvait pas devenir active avant que l'auteur
  ait lu ses sources, et une archive n'est contrôlée que superficiellement : aucun moyen de prouver
  qu'un recodage était conforme. Une proposition est contrôlée comme un cas actif (A6, A7, G6,
  fenêtres, objets, disponibilité), porte `sources_verifiees: false` et `motif_proposition`, et reste
  exclue des calculs.
- **Les quatre fiches recodées** dans `assets/cas-reels.jsonl` ; témoignage original conservé tel quel
  dans `assets/cas-reels-originaux.jsonl`. Décisions, chacune inscrite dans la fiche :
  - deux fenêtres fausses, que le validateur aurait refusées : France 7 → 6 jours, Alberta 6 → 7 jours ;
  - A7 appliquée : 8 ancrages « F maintenu » malgré une contre-observation substantielle passent à f
    avec `force_initiale: "F"` ; trois mots f à contre-observation substantielle sans lecture F
    antérieure (France : COMMUNAUTÉ, INCERTITUDE, CONTRAINTE@8 du 19) sont rejetés, motifs inscrits ;
  - A6 complétée : CONTRAINTE@7 (Yémen, voisine TRACE·MÉMOIRE) ; CONTRAINTE@8 de l'issue française
    recodée sur son objet propre (manifestation du 24 octobre), ligne A6 complète ;
  - Yémen : les deux renforcements de l'issue sont refusés par A7 ; la structure ne change pas, le cas
    devient sans événement au sens structurel de B4, l'escalade relevant de « s'intensifie » ;
  - objets, portées, dates de disponibilité et preuves de liaisons renseignés.
  Vérifié : les quatre fiches passent `valider` en proposition, et en actif si les sources sont
  déclarées lues ; le moteur les utilise alors (2 cas homologues pour POLARITÉ@7).

### Feuille de route

- `references/feuille-de-route.md` : étapes restantes (installation, décisions d'auteur, cas réels,
  strate pilote, fréquences externes, base réelle et second codeur, code différé, test à l'aveugle),
  qui fait quoi, critère d'achèvement, journal de progression.
- `moteur.py bilan` : mesure les étapes 2 à 5 et le test à l'aveugle à partir des fichiers, pour que
  l'état ne soit pas tenu à la main. Référencé dans SKILL.md (« Où en est le skill »).

## 0.4.6 — 2026-10-26 · corrections fonctionnelles après l'audit « V13 »

L'audit déclare une « exécution mentale » du moteur : ses constats ont été vérifiés par exécution
avant toute correction. 68 autotests (67 + 1).

### Retenu

- **C-6 · Doublons du glossaire**, exacts : une cellule (« ne mesure pas sa calibration » deux fois) et
  un paragraphe recopié. Ils avaient survécu à la correction annoncée en 0.4.1. Supprimés, et `audit`
  détecte désormais tout paragraphe identique au précédent et tout segment « ; X ; X » répété dans une
  ligne (vérifié par réinjection des deux doublons).
- **C-7 · Numérotation héritée** : une seule mention restait dans les fiches (« R13 »), remplacée par
  G1 ; la table de correspondance est conservée pour lire les documents NEXUS-ARCHÊ.
- **S-4 · `kappa_min`** : déclaré **réservé** dans A4 (seuil du futur calcul de κ, lu par aucun calcul
  en 0.4.x), au lieu d'un paramètre muet.
- **S-3 · Empreinte du zip** : un zip ne peut contenir sa propre empreinte ; le README le dit, et le
  SHA-256 est communiqué à la livraison.

### Non retenu

- **D-3 · « La base d'exemple ne passe pas `valider` »** : faux, vérifié par exécution ; les 40 fiches
  portent `id_legacy: true` et sont recevables.
- **D-4 · Recouper les empreintes du journal avec les fichiers actuels** : contraire à leur fonction.
  Elles figent le moteur, les paramètres et la base **au moment de la prévision** ; toute évolution
  ultérieure du moteur invaliderait l'historique.
- **D-5 · Empreinte de la base par fichier plutôt que par contenu** : le contenu canonique (JSON trié)
  est voulu ; il ne dépend ni des espaces ni de l'encodage du fichier.
- **S-5 · Dossier suffixé par la version** : le nom du dossier doit égaler le nom du skill
  (`alphabet-situationnel`) pour son installation.
- **S-2 · `version_regles` 0.4.0 dans le journal et la base d'exemple** : le journal est figé (le
  modifier changerait ses empreintes), et la base est acceptée dans la même version mineure, comme
  documenté.
- **C-8** : `se renforce` et `s'affaiblit` ne sont pas présentés comme opératoires dans SKILL.md ; ils
  ne sont lus que pour être refusés avec un message.
- **Hors périmètre fonctionnel**, à la main de l'auteur ou des données : sourçage des équivalents
  (C-1, D-2), recodage des archives (C-2), test à l'aveugle (C-3), strate 12 (C-4), universalité des
  cartes à agents (C-5).

## 0.4.5 — 2026-10-26 · sortie conforme à la constitution, chiffres publiés contrôlés (audit Genspark)

L'audit Genspark ne relève aucun défaut de calcul et reproduit l'exemple 1 au chiffre près. Ses quatre
constats majeurs sont vérifiés et corrigés ; 67 autotests (64 + 3).

- **M3 · Une seule ligne d'ouverture.** Constitution, `simulation.md` et moteur en avaient trois. La
  constitution prime (« une règle qui la contredit est nulle ») : sa ligne
  `⚠ Prévision · cet outil prend un risque déclaré.` est désormais la seule, reprise mot pour mot par
  `simulation.md` et imprimée par le moteur, suivie de la ligne de signalement S5, que le moteur
  produit maintenant (`⚠ ρ1 · 10 cas distincts (H1) · p₀ 23 % · p ~22 % (large : 5–43) · échéance
  2026-12-01 · journal P-0101`). `audit` vérifie la présence de la ligne dans les deux documents ; un
  autotest fige la sortie humaine de l'exemple 1.
- **M4 · Intervalle large signalé.** `largeur_max_affichage` n'était lu par aucun code. Au-delà de 30
  points, la probabilité s'écrit `~y % (large : a–b)` comme S5 l'exige. L'exemple 1 (38 points) est
  désormais marqué.
- **M1 · Répartition des statuts recalculée.** `audit` compte les 192 cellules et les compare aux
  douze Bilans, au tableau et à la liste des cases Vides de `equivalences.md`, aux bilans de
  `protocole.md` et de `SKILL.md`. L'injection de l'audit (CROISSANCE@7 passé en Vide) est détectée.
- **M2 · Index des cartes recoupé.** Définition (première phrase), début de la structure mathématique
  et voisines de `cartes-index.md` comparés à `cartes.md`. L'injection de l'audit (définition de SEUIL
  altérée) est détectée. Aucune divergence existante : seules deux abréviations voulues de la
  structure (RÉCIPROCITÉ, CONTRAINTE), admises par la comparaison.
- **M5, M6 · Messages de ligne de commande.** `--strates abc`, JSON passé en ligne à `--references`
  ou `--resolution`, fichier introuvable, dossier, fichier binaire : messages en français, sans texte
  d'exception Python.
- **M7** : `equivalences --carte` documentée (SKILL, README). **M8** : exemples de fiche et de journal
  alignés sur la version courante ; la règle de version mineure reste documentée dans `base-de-cas.md`.
  **M10** : trois mentions de « 0.4.0 » décrivant l'état courant corrigées. **m11** : Python ≥ 3.8 et
  repli `grep` indiqués. **m13** : ligne de trace arrondie. **m14** : « l'audit vérifie la forme et les
  recoupements internes, pas la justesse du contenu » écrit dans SKILL. **m15** : `audit` vérifie aussi
  la version du README.
- **Trouvé en passant**, absent de l'audit : le README conseillait encore « utiliser f tant que les
  équivalents restent non vérifiés », règle abandonnée en 0.4.1. Corrigé.

Non traité : **M9**, le nom « V12 » est donné au zip après livraison ; le paquet porte le numéro
interne et le README dit comment rattacher un zip renommé. **m11**, licence et auteur : décision du
propriétaire, non prise ici.

## 0.4.4 — 2026-10-26 · robustesse des entrées et affichage, après l'audit Kimi

L'audit Kimi ne relève aucun défaut de calcul. Quatre points de code retenus ; 64 autotests (58 + 6).

- **Erreurs JSON.** Avec `--json`, une erreur sort en `{"erreur": …, "code": 2}` sur la sortie standard.
- **Aucune trace Python.** Un sondage par mutations (12 000 fiches et journaux altérés au hasard) a
  trouvé environ 300 entrées qui produisaient `AttributeError`, `TypeError` ou `KeyError` au lieu d'un
  refus lisible ; `AttributeError` n'était pas même intercepté. Corrigé dans `valider` et `scorer`, et
  `main` n'expose plus de trace. Deux autotests rejouent 3 000 mutations à chaque exécution.
- **Acceptations à tort trouvées par le même sondage.**
  - `liaisons` à `''`, `0` ou `{}` valait « aucune liaison » : une liste est exigée.
  - `codage.independants` et `au_moins_un_humain` acceptaient n'importe quelle valeur : booléens exigés.
  - `sans_evenement: true` était accepté sur un cas où la structure change : B4 est désormais contrôlée
    sur toute la séquence. Le cas fictif C-0012-GEO, ainsi marqué alors que RÉSEAU y apparaît puis
    disparaît, passe à `false` (sans effet sur l'exemple 1, en ρ1).
  - Journal : `probabilite` et `rho` n'étaient pas comparés au `calcul` figé qui les justifie ; une
    ligne pouvait annoncer 90 % pour un calcul à 22 %. Contrôlé ; `issue` obligatoire dans un score.
- **Affichage.** `22 % (intervalle 80 % : 5–43 %)` au lieu de `22.0379%` ; `ρ1 — provenance du
  chiffre, pas sa fiabilité`. Le JSON et le journal gardent les valeurs non arrondies.
- **Nommage.** Le README ne renvoie plus à « V8 » ; le paquet porte le numéro interne.

Non retenu : découpage en modules et `pyproject.toml` (un skill doit tenir en un fichier sans
installation), schéma JSON formel séparé (`valider` est plus strict et `audit` valide déjà le schéma
documenté), données recopiées dans le code au lieu de lire les références (divergence corrigée en
0.4.1), CI (relève de l'hébergement), triple numérotation (les empreintes SHA-256 du journal assurent
déjà la traçabilité moteur / paramètres / base), bandeau « fictif » (déjà présent avec `--demo`).

## 0.4.3 — 2026-10-26 · deux résidus de la 0.4.2

Les trois points de l'audit de la 0.4.2 sont reproduits et corrigés ; 58 autotests (55 + 3).

- **Schéma de fiche invalide (créé par l'ajout de `portee`).** Les deux mots f de `base-de-cas.md` §2
  n'avaient pas `portee` ; le schéma échouait à `valider`, alors que `exemples.md` le disait validé.
  Corrigé, et `audit` extrait désormais ce JSON et le passe à `valider` : un schéma qui ne valide pas
  fait échouer l'audit (vérifié par injection). C'était la deuxième fois que ce défaut revenait.
- **`force_initiale` recoupée avec l'état précédent.** Sur un mot qui persiste, `force_initiale: "F"`
  n'est admise que s'il était F, ou déjà rétrogradé depuis F, à l'état précédent ; sinon le mot était
  f, et une portée substantielle impose le rejet. Condition reprise de l'audit, qui distinguait à juste
  titre le mot rétrogradé une fois puis maintenu f. `force_initiale` hors portée substantielle est
  refusée.
- **Messages contradictoires.** Un mot noté F avec portée substantielle ne reçoit plus qu'un message
  (« noter f et force_initiale "F" ») ; le message « mot lu f → rejet » ne sort que pour un mot f.

## 0.4.2 — 2026-10-26 · A6 et A7 vérifiables

L'audit de la 0.4.1 confirme les cinq corrections et relève qu'en rendant F accessible, la 0.4.1 a
déplacé le risque : F n'était plus borné que par une ligne A6 contrôlée dans sa seule présence, et A7
n'était pas lue. Tout est reproduit ; 55 autotests.

### Retenu

- **A6, verdicts lus.** Pour un mot F d'un cas réel : chaque voisine nommée, verdict `→` ou `+`
  seulement, justification non vide. Plus strict que la proposition de l'audit (« au moins un `→`
  ou `+` ») : un mot n'a qu'un fait, et un seul `←` l'attribue à la voisine ; il ne compte alors plus
  pour cette carte. Les 12 lignes A6 des archives n'emploient que `→` : la règle ne casse aucun usage.
- **A7 structurée.** Champ `portee` (`marginale`, `substantielle`, `dominante`, `aucune`) ; la force
  notée est celle d'après A7. Substantielle ⇒ f avec `force_initiale: "F"` (un mot déjà f est rejeté) ;
  dominante ⇒ mot interdit. Les 40 cas fictifs reçoivent `portee: marginale`, lue dans leur texte.
- **Constat sur les archives**, sans les modifier : 8 des 12 ancrages F portent une contre-observation
  substantielle avec « F maintenu ». Ce sont des sur-affirmations au sens de A7, dont CONTRAINTE@8 de
  C-0001-S05, complétée en 0.3.2. Trois mots f substantiels ne disent pas s'ils viennent de F ; s'ils
  étaient déjà f, ils sont à rejeter. Avec les 4 échecs A6 de la 0.4.1, cela confirme le diagnostic de
  l'audit : sans frein, les codeurs maintiennent F.
- **Déclaré** (`validation.md` §8) : le moteur contrôle la forme de A6 et la cohérence de A7, pas la
  justesse d'un verdict ; le score d'un test à l'aveugle mesure aussi le jugement du codeur, d'où
  l'accord A4 à mesurer avant de comparer deux codeurs. Le statut de lecture (plafond « Spéculatif »
  d'une portée `aucune`) reste rédigé par l'analyste.
- **Détails.** `homologie —` au lieu de `None` ; modèle de sortie sans version figée ; schéma de
  `base-de-cas.md` §2 avec des lignes A6 valides et le champ `portee`.

## 0.4.1 — 2026-10-26 · contrôles rétablis après l'audit de la 0.4.0

La 0.4.0 est conservée dans son calcul (dates, disponibilité, pondération par cas, composés
conditionnels, journal strict, partitions, épisodes, ablation). Chaque constat de l'audit a été
reproduit avant correction ; 53 autotests (46 + 7).

### Retenu

- **F découplé du statut bibliographique (constat 2, option A).** Reproduit : avec 0 équivalent
  Documenté, F était inatteignable, et avec lui la ligne A6, *tient*, les configurations et le statut
  Descriptif, sans que le protocole le dise. Le statut porte sur la **correspondance** carte ↔
  traduction locale (il compte pour l'emprunt T4) ; la force porte sur la **lecture** (fait précis,
  voisines tranchées). Le plafond ne protégeait rien : si le marqueur est faux, la lecture l'est en f
  comme en F. F est permis sur Proposé (signalé « équivalent non vérifié »), impossible sur Vide.
  L'emprunt T4 reste fermé tant qu'aucun équivalent n'est Documenté, comme le déclarait déjà la 0.4.0.
- **Test des voisines contrôlé.** Pour un mot F d'un cas réel, `valider` lit les listes « À ne pas
  confondre avec » de `cartes.md` et exige que la ligne A6 passe chaque voisine, sans verdict `?`.
  C'est le mécanisme que l'audit jugeait le plus coûteux à perdre ; il n'était vérifié que par sa
  présence. Appliqué aux quatre archives : 4 ancrages F sur 12 ne passent pas toutes leurs voisines,
  dont CONTRAINTE@8 de C-0001-S05, complétée en 0.3.2 (INCERTITUDE et POLARITÉ omises). À reprendre au
  recodage ; les archives ne sont pas modifiées.
- **G6 contrôlée (constat 3).** Reproduit : INCERTITUDE et CONTRAINTE sur le même objet étaient
  acceptées. `valider` lit `antagonismes.md` §3 et suit l'objet de chaque mot à travers les états.
  Refusés : une paire incompatible de même objet, quelle que soit la liaison ; une *indépendance*
  entre deux mots de même objet. Limite : égalité des libellés normalisés seulement.
- **Renvois § (constat 4).** Reproduit : les deux injections de l'audit passaient. Table `RENVOIS`
  rétablie (existence et pertinence du titre, 37 renvois, `SKILL.md` et `README.md` compris) ; un
  renvoi non répertorié est signalé.
- **Homologie (constat 5).** Reproduit : H1 ⊆ H1.5, donc H1 n'était jamais retenu sous 30 cas. Règle :
  le niveau le plus strict qui atteint 3 cas distincts. Exemple 1 régénéré (SEUIL@7 0,2275 → 0,2204,
  H1.5 → H1, intervalle plus large).
- **Version des fiches.** Un cas actif devait porter exactement la version courante : tout correctif
  invalidait la base entière (constaté en passant à 0.4.1). Exigence ramenée à la même version mineure ;
  `valider` applique de toute façon les règles courantes à chaque fiche.
- **Mineurs.** Glossaire dédoublonné ; `references.json` présenté comme fichier utilisateur ; rappel du
  marqueur S1 rétabli au calcul (constat 6.4) ; `incertitude_annoncee_moyenne` ajoutée au score.

### Non retenu, ou retenu autrement

- **G6, correctif proposé.** L'audit proposait d'admettre la paire si la liaison est *indépendance*.
  G6 dit autre chose : une paire incompatible sur le même objet impose de rejeter un ancrage. La règle
  écrite est appliquée.
- **6.2, « une somme et non une moyenne ».** Pour une partition, la somme des p(1−p) est l'espérance du
  Brier de la question, lui-même une somme : elle est comparable au Brier qu'elle accompagne. Ce qui
  manquait était la moyenne du lot, ajoutée.
- **« Les quatre cas réels sont archivés à cause de F ».** Inexact : leur motif d'archive est « sources
  non revérifiées, codage antérieur à 0.4.0 ». Ils restent archivés après le découplage.
- **Pondération continue par la similarité** : plus cohérente, différée faute de données pour en fixer
  la forme.

### Principe de la 0.4.0 maintenu contre la 0.3.2

La 0.3.2 affirmait qu'un lot de faible p(1−p) « ne peut rien révéler ». La 0.4.0 corrige à juste titre :
c'est l'incertitude **annoncée**, et une probabilité extrême peut être fausse ; un tel lot peut révéler
une surconfiance. Le refus de `se renforce` comme événement (F/f n'est pas une intensité) est
également maintenu ; l'intensification passe par `s'intensifie` et une mesure.

## 0.4.0 — 2026-10-25 · corrections de calcul et contrats contrôlés

### Corrigés

- Probabilités négatives de *bouge* : accélération du taux de sortie ; contrôle [0,1] et valeurs finies.
- Dates civiles, fenêtre positive, écarts calendaires ; exclusion des transitions et sources futures.
- Références propres à chaque événement, conditionnelles pour les composés ; aucun carré accidentel
  de --fref, aucun 1/3 d'ignorance converti en estimation. Composés multi-pas explicitement refusés.
- Même horizon/sémantique pour prévision et comparateur ; pas d'intervalle propagé partiellement.
- Validation obligatoire au calcul ; correspondance état/documents, forces, strates, codeurs, liens.
- Journal strict, rejets des doublons et scores orphelins ; partitions scorées comme une question.
- Rejeux, fictifs et prépublications non établies exclus de V4 ; regroupement par épisode.
- H1 sur état complet non vide ; mots faibles inclus dans H1.5 ; poids total d'un cas plafonné à 1.
- Audit exhaustif des paramètres ; sortie JSON, empreintes, ablation et 46 autotests intégrés.
- Contrôle de la sémantique même à un pas, de l’état daté dans le journal et du lien entre une
  prépublication et l’empreinte de la prévision figée.

### Clarifiés

F/f est la confiance documentaire : les anciens renforcements f→F ne sont plus des événements
physiques prévus. Les 117 équivalents anciennement Documentés sans référence sont Proposés ; les
quatre cas transmis sont conservés en archives, sans réécriture des faits. Les démonstrations
sont régénérées et explicitement fictives. Les mêmes noms de fichiers et dossiers sont conservés.
Le chargement documentaire est routé par mode. Les paramètres sont des hypothèses et V4 un jalon
interne, pas une certification. L'utilité descriptive et la performance prédictive sont séparées.

### À établir par des données externes

Références vérifiées des équivalents, recodage indépendant des cas réels, accord κ par carte,
calibration des multiplicateurs et inerties, effets inhibiteurs, validation du transfert entre
strates, incertitude du gain par épisode et étude prospective. Aucun de ces résultats n'est inventé.
Les intervalles restent conditionnels approximatifs ; aucun intervalle composé ou multi-pas.
Les anciennes notes ci-dessous sont historiques et ne décrivent pas le comportement 0.4.0.

## 0.3.2 — 2026-10-25 · fiches FR et Alberta, quatrième test sur cas réel

### Vérifié

Les cinq probabilités du test Alberta sont reproduites à l'identique (1,30 %, 99,31 %, 98,94 %, 0,83 %,
0,34 %), de même que les Brier (moyenne 0,00008) et le contrefactuel (0,195 si P1 s'était réalisé). Les
deux fiches transmises passent le validateur de la 0.3.1. Aucune régression.

### Retenu

- **Changement de force non documenté (défaut trouvé dans la fiche FR, absent du test).** Le validateur
  exigeait un fait pour un mot apparu ou disparu, pas pour un mot qui change de force. Or depuis la 0.3.0,
  « se renforce » et « s'affaiblit » sont des événements prévus. La fiche FR passait CONTRAINTE@8 de f à
  F sans fait et était déclarée recevable. B1 et le validateur l'exigent désormais ; `mots: null` est
  refusé si une force a changé.
- **Fiche C-0001-FRA** : ajoutée sous C-0001-S05 (format B5, usage inchangé : apprentissage). L'entrée
  CONTRAINTE@8 manquante est complétée à partir des seuls faits et sources déjà présents dans la fiche
  (interdictions préfectorales, Capital 23-24 oct.), marquée « à confirmer par codeur-1 ».
- **Fiche C-0004-S05 (Alberta)** : ajoutée telle quelle ; première fiche réelle sans événement (B4).
  Champ `rejeu` documenté comme facultatif et informatif.
- **« Un test ne vaut que par l'incertitude qu'il contient »** : la conclusion du test est rendue
  mesurable. Le scorer affiche l'**incertitude contenue** du lot, moyenne de p(1 − p), Brier attendu si
  les probabilités sont justes (0,25 pour un lot indécis). Alberta : 0,0084. Le protocole du test à
  l'aveugle demande de la calculer et de la publier avec l'empreinte. Aucun seuil n'est fixé.
- **S1 affiché mais non respecté** : trois résolutions sur cinq du test mesurent autre chose que le
  marqueur affiché (P1, P4, P5 ; exemple 10). Le contrôle devient une étape explicite (SKILL.md étape 6,
  `validation.md` §8 étape 5).
- **Sens du biais de « se renforce »** (point 3 du test) : l'avertissement du moteur précise que la
  référence est probablement une borne basse.
- La ligne de commande accepte la notation des fiches pour les liaisons (`A —conflit→ B`).
- Identifiant hors format C-NNNN-SNN : avertissement non bloquant (la base d'exemple utilise l'ancien
  format ; renuméroter un cas déjà réparti changerait sa répartition).

### Non retenu

- **Référence « 50 % constant »** du test (« 3 000 fois mieux ») : le comparateur du protocole est la
  fréquence de base (V1), pas 0,5. Le chiffre est exact mais ne mesure rien d'utile, ce que le test
  reconnaît lui-même.
- **Ajouts au protocole du test à l'aveugle** : les conditions 2 et 3 proposées (scellement, au plus deux
  persistances, événements sur TRACE et TRANSFORMATION) figuraient déjà dans `validation.md` §8 ; seule
  la condition 1 manquait, traitée ci-dessus par l'incertitude contenue.

## 0.3.1 — 2026-10-25 · après le troisième test sur cas réel (Yémen)

### L'erreur mathématique, vérifiée

Constat du test, reproduit : `se renforce` et `s'affaiblit` renvoyaient une constante (0,3 % à 6 jours,
5 % à 3 mois), identique pour toute carte et tout état. **Cause précise** : leur a priori réutilisait la
fréquence par défaut d'**apparition** d'une carte absente. Or un changement de force porte sur une
structure déjà présente, dont le rythme de changement est mesuré par son inertie : ce sont deux
grandeurs différentes.

**Correction** : la référence d'un changement de force est le taux de changement propre de la carte,
1 − inertie, ramené à la fenêtre ; « se renforce » reçoit en plus les rapports de vraisemblance des
sources qui font apparaître la carte. Aucun paramètre nouveau. Vérification : à 6 jours, CROISSANCE
5,8 %, RÉSEAU 1,5 % dans le même état ; les valeurs varient avec la fenêtre (CROISSANCE 0,6 % à 1 jour,
39 % à 3 mois).

Le test proposait une table de 32 probabilités de changement de force par carte. Elle n'est pas retenue :
ce seraient 32 nombres inventés de plus, sans source ni cas, exactement ce que l'audit de la v0.1.0 a
reproché à l'échelle absolue. L'inertie existe déjà et porte l'information nécessaire.

### Le second défaut, que le test a mesuré sans le nommer

L'écart de ×1 628 selon le codage ne vient pas du modèle mais d'un **décalage entre l'événement calculé et
sa résolution** : « CROISSANCE@7 se renforce » (marqueur : surfaces contrôlées en série datée) était
résolu par « au moins deux attaques en 6 jours ». **Nouvelle exigence (S1)** : la résolution externe
doit opérationnaliser le marqueur local de la carte ; le moteur l'affiche pour chaque événement, et le
journal porte un champ `resolution.marqueur`.

### Ajouts

- **`s'intensifie`** (point 3 du test) : disponible pour un mot F ; P = P(persiste) × P(hausse), avec
  P(hausse) = fréquence externe citée, sinon indifférence 1/3, modulée par les qualificatifs de
  rétroaction ; résolution par une série chiffrée.
- **Intervalle** : la ligne de calcul affiche « — (aucun cas : non estimé) » au lieu de [0,000 ; 0,000]
  (point 5).
- **Cas réel C-0003-S07** ajouté à `assets/cas-reels.jsonl` (recevable).

### Non traité

- La fiche du cas français (« C-0001-FRA ») n'a jamais été jointe à la conversation : elle ne peut pas
  être ajoutée. Elle devra être renumérotée `C-0001-S05` et validée par `moteur.py valider`.

### Rejeu

Exemple 9 : Brier 0,3975 → 0,3715 avec les issues codées par le test. Le rejeu reste mauvais parce que
deux prévisions étaient résolues par une grandeur que l'événement ne mesurait pas ; c'est l'objet de
l'exigence S1 ci-dessus, pas d'un réglage.

## 0.3.0 — 2026-10-25 · après le second test sur cas réel (Ukraine)

Version mineure : la matrice des dynamiques change et le vocabulaire des événements s'élargit.

### Ce que le test affirme, et ce qui a été vérifié

Le test conclut : « l'alphabet voit ce qui dure et ce qui rompt, pas ce qui se transforme ». Vérifié
séparément, cela recouvre trois choses distinctes :

1. **Un manque d'expression — confirmé, corrigé.** Aucun type d'événement ne pouvait dire « une
   structure présente change de forme sans disparaître », ni « une structure passe de f à F » (déjà
   rencontré en France : la prévision P2 mal formée). Trois types sont ajoutés : `se renforce`,
   `s'affaiblit`, `se transforme` (T1).
2. **Une matrice incohérente — confirmé, et plus large que relevé.** Le test note que RÉSEAU n'a qu'un
   parent et qu'INCERTITUDE et RÉCURSIVITÉ n'en ont aucun. La cause est une incohérence interne : les
   lignes « Entrées » des fiches, écrites dès la v0.1.0, annonçaient **17 transitions** absentes de la
   matrice. Elles sont ajoutées, toutes à l'intensité faible, et l'audit vérifie désormais la cohérence
   (test par injection : une transition retirée est détectée).
3. **Une probabilité trop basse pour les changements de forme — confirmé, non corrigé par réglage.**
   Même exprimable, « RÉSEAU@7 se transforme » reste à 0,4 % : c'est la fréquence par défaut d'une
   apparition non ancrée. Les transitions vers TRANSFORMATION et TRACE ne sont pas modifiées : leurs
   fiches étaient cohérentes, et les deux tests qui les ont manquées sont des rejeux. Ce qui manque est
   une **fréquence de référence** des changements de forme (base de cas ou `--fref`) ; l'exemple 8 montre
   qu'avec une référence externe de 10 % par semaine, la même prévision passe à 12 % (ρ3).

### Ajoutés

- **Rejeux exclus de V4** : champ `"rejeu"` dans le journal ; `scorer` les affiche à part. Raison :
  dans un rejeu, les événements sont choisis en connaissant l'issue, et les échecs confiants y sont
  sur-représentés.
- **Test à l'aveugle** : protocole dans `validation.md` §8 (repris du test, avec l'obligation de
  chercher une classe de référence externe pour chaque apparition) ; commande `moteur.py sceller`
  (empreinte SHA-256 du journal, à publier avant l'échéance).
- **Lacune n° 2** au journal (`assets/journal-lacunes.md`) ; la fiche réelle du test est jointe
  (`assets/cas-reels.jsonl`, recevable).

### Effet sur les exemples

Exemple 1 : les prévisions ne changent pas ; les trajectoires bougent de quelques dixièmes de point
(nouvelles transitions candidates). Exemple 8 ajouté.

### Réserve sur la méthode des tests

Les deux tests sont des rejeux : leurs Brier (0,2495 et 0,1992) ne mesurent pas la calibration. Le
prochain test utile est un test à l'aveugle, scellé, portant surtout sur des changements.

## 0.2.2 — 2026-10-25 · corrections après le test sur cas réel

Le test (France, 19 → 25 octobre 2026, fenêtre de 7 jours) a été reproduit sur le moteur 0.2.1 avant
correction. Ses constats sont fondés ; un point est traité autrement que proposé, et un autre est
volontairement non corrigé.

### Corrigés

| Test | Constat reproduit | Correction |
|---|---|---|
| 6.1 Fenêtres courtes impossibles | `mois("2026-10-19") = mois("2026-10-25")` ; fiche hebdomadaire refusée, transitions perdues sans erreur | Dates au jour près partout (`jour()`) : ordre, âge, stationnarité, validation. Fenêtres comparées en jours (`7 jours` = `1 semaine`). Contre-test : 2026-12-31 < 2027-01-01. |
| 6.2 Une fiche fait monter p₀ | lissage de Jeffreys : 0,25 pour une transition sans événement | Fréquence lissée **vers la référence** par 20 pseudo-transitions ; déclarée instable sous 10 transitions (a priori non ancré). Une transition sans événement fait désormais légèrement baisser f. |
| 6.3 Trop de changements par pas | statu quo 6,2 % à 7 jours | **Cause plus précise que celle du test** : les inerties, la fréquence par défaut et les intensités étaient « par pas », quelle que soit la durée du pas. Elles sont désormais définies pour 3 mois et ramenées à la fenêtre (1 − (1 − p)^(d / 3 mois)). Statu quo : 80,5 % à 7 jours. Le test proposait de calibrer P(aucun changement) par fenêtre ; la conversion d'unité règle la cause sans ajouter de paramètre. |
| 6.5 Un cas suffit pour ρ1 | ρ1 avec c_A = 1 | ρ1 (et ρ2) exigent 3 cas distincts ; 1 ou 2 cas comptent dans P, pas dans le niveau. Le barème progressif proposé (1–2 → ρ3, 3–9 → ρ2…) n'est pas retenu : il mêlerait nombre de cas et provenance, alors que ρ2 désigne un emprunt et ρ3 un a priori ancré. |
| 6.6 `1 semaine` refusé | erreur de syntaxe | Singuliers admis (`jour`, `semaine`, `an`). |
| §0 Faisceau à 8 pas | 72 % de la masse abandonnée, sans avertissement | Alerte quand R2 > 30 %. |
| §8 Identifiants | convention d'abréviation de strate inexistante | `C-NNNN-SNN` (numéro de la strate principale). |

### Ajoutés en vérifiant

- **Événement mal formé** : la prévision P2 du test (« CONTRAINTE@8 apparaît ») portait sur un mot déjà
  présent. Le moteur refuse désormais « apparaît » pour un mot présent et « persiste / disparaît » pour
  un mot absent. Un changement de force (f → F) n'est pas encore un type d'événement (question ouverte).
- **Intervalle sans cas** : il était incohérent (p = 2 %, intervalle [0–1]) ; il est déclaré « non
  estimé ». Un intervalle qui exclut sa propre moyenne (petits effectifs) est signalé.

### Non corrigé, volontairement

- **6.4 TRACE inaccessible** : ajouter une arête vers TRACE parce que ce cas l'a montré reviendrait à
  ajuster le modèle sur une issue connue, ce que V3 interdit. Le motif est consigné comme **lacune n° 1**
  (`assets/journal-lacunes.md`). Deux autres entrées indépendantes ouvriraient A2 et trancheraient entre
  une carte nouvelle et des arêtes.
- La fiche `cas-reel-2026-10-FR.jsonl` du test n'était pas jointe : elle n'est pas intégrée. Elle doit
  être recevable par `moteur.py valider` en 0.2.2 (une fiche équivalente l'est).

### Rejeu

Exemple 7 de `exemples.md` : Brier 0,2835 → 0,2495, au niveau du « 50 % constant » (0,25). Le gain vient
des persistances (correction d'unité) ; l'erreur dominante reste TRACE. L'issue étant connue d'avance,
ce rejeu ne mesure pas la calibration.

## 0.2.1 — 2026-10-25 · corrections après contre-audit

Les trois régressions et les cinq points du §5 du contre-audit ont été reproduits avant correction.
Tous sont retenus.

### Régressions corrigées

| Contre-audit | Constat reproduit | Correction | Vérification |
|---|---|---|---|
| 3.1 Trajectoires vides au-delà de 2 pas | 5 trajectoires à 1 pas, 1 à 3 pas, **0 à 4 pas** (résiduel 100 %) : l'élagage testait la probabilité cumulée | Élagage sur la probabilité **du pas** ; faisceau plafonné à 300 branches ; fusion et seuil d'affichage appliqués aux états finaux ; deux résiduels distincts (R1 états rares, R2 branches abandonnées) | à 4 pas : 8 états affichés, résiduel total 26 % (critère du contre-audit : ≥ 5 états, résiduel < 50 %) |
| 3.2 Statu quo étiqueté ρ0 | ligne la plus probable affichée ρ0 sans aucun cas | Le statu quo prend le niveau le plus élevé des estimations dont il dépend | statu quo ρ1 sur l'exemple ; ρ4 quand une estimation non ancrée entre dans le calcul |
| 3.3 Mode solo binaire | une seule fiche double-codée levait le plafond pour toute la base | Solo si la part de cas double-codés est sous 20 % (B3) | 199 + 1 → solo ; 32 + 8 → non solo |

La revendication du CHANGELOG 0.2.0 « somme des probabilités des trajectoires : 100 % » était vraie mais
vide à 4 pas (100 % de résiduel). Elle est maintenant accompagnée d'un critère de contenu.

### Points du §5 corrigés

1. **Trajectoires vers une strate nouvelle** : option `--strates` (strates examinées sans mot, O1) ; les
   apparitions candidates les couvrent. En testant cette option, un **bug latent de l'emprunt entre
   strates (T4)** est apparu : le code n'avait jamais été exécuté et plantait. Il est réécrit et testé
   (emprunt vers la strate 8, ρ2).
2. **Mot apparu toujours noté `[f]`** : comportement conservé (un mot simulé n'est ancré par aucun fait),
   désormais écrit dans `simulation.md` §3 et dans les limites de `SKILL.md`.
3. **Pertinence des renvois** : l'audit compare chaque renvoi `fichier.md` §N à une table de titres
   attendus (`RENVOIS` dans `moteur.py`) ; un renvoi non répertorié est signalé. Test : réinjecter
   l'erreur v0.1.0 (`validation.md` §5 pour le journal des lacunes) est détecté.
4. **Base fictive non signalée** : champ `"fictif": true` dans les fiches d'exemple ; le moteur ouvre
   chaque calcul par « ⚠ BASE FICTIVE » et `valider` compte les cas fictifs.
5. **« niveau Fort » résiduels** : remplacés par « force F » (`equivalences.md`, `grammaire.md`,
   `protocole.md`).

### Ajout demandé au §4 du contre-audit

- `base-de-cas.md` §1 : **choisir et dater les configurations avant de connaître les issues**, contre le
  biais de sélection entre configurations, que B4 ne corrige pas.

### Toujours reportés (inchangé)

Cas réel codé de bout en bout ; sourçage des 117 équivalents Documentés ; matrice de Brown ; décisions
de structure (strate 12, forme / régime) ; universalité aux systèmes à agents. Le contre-audit classe le
cas réel en priorité 3 : c'est le prochain chantier.

## 0.2.0 — 2026-10-25 · corrections après audit

Chaque point de l'audit v0.1.0 a été vérifié avant d'être traité (recalcul des sommes de lignes, du
rayon spectral, des renvois, des compteurs). Décision par point :

### Retenus

| Audit | Correction |
|---|---|
| 2.1 Graphe non composable, états qui explosent | Trajectoires par **noyau à risques concurrents** : statu quo ou un seul changement par pas, probabilités qui somment à 1 (S3, `simulation.md` §3). Un événement isolé sur plusieurs pas passe par une chaîne à deux états (`graphe.md` §2.4). La probabilité est conditionnée à l'état entier (T1). |
| 2.2 A priori non ancré, surestimé | p₀ part d'une **fréquence de référence** (base, ou classe de référence externe citée) que la structure module par un rapport de vraisemblance, **sur les cotes** (T2). Sans référence : a priori déclaré non ancré, ρ4. Produit des λ plafonné à 10. |
| 2.3 ρ0 inatteignable, a priori trop lourd | k = 2 au lieu de 10 ; homologie H1.5 (Jaccard ≥ 0,7) ; seuil ρ0 sur les cas distincts ; constitution de la base **par configuration** (`base-de-cas.md` §1) ; intervalle de crédibilité à 80 % sur chaque probabilité. |
| 2.4 Variable cible dépendante de l'instrument | Chaque prévision porte une **résolution externe** (source, critère, seuil) ; l'issue est décidée par la source, pas par un recodage ; cas ambigu = « non résolue », exclu du score (S1, V1). |
| 3.1 Seuil n_A / c_A | Aligné sur c_A partout. |
| 3.2 Exception non nommée à A3 | Quatre statuts : Attesté, **Documenté**, Proposé, Vide. Les 117 anciens « Attesté » deviennent Documenté, référence « à fournir ». |
| 3.3 Normalisation de non-exclusifs | Deux régimes, binaire ou partition ; décomposition en 2ⁿ issues avant toute somme ; exemple 3 refait. |
| 3.4 Format de la ligne de signalement | Format unique à six champs plus intervalle, appliqué partout. |
| 3.5 Renvoi §5 → §6 | Corrigé (SKILL.md, A8). |
| 3.6 Trous du schéma de fiche | `issue.mots` obligatoire ; `null` = rien de nouveau, `[]` = non documenté (refusé) ; disparitions documentées dans `retraits`. |
| 3.7 Script qui viole sa règle | Remplacé par `scripts/moteur.py` : filtre par fenêtre et strate, ignore une issue non postérieure. |
| 3.8 Inertie par étiquette | Inertie numérique par carte (0,40 à 0,97 ; CONTRAINTE formelle 0,90, matérielle 0,65). |
| 3.9 A2 circulaire | Étape 3 : motif documenté dans deux strates par le journal des lacunes ou la littérature. |
| 4.3 Index à l'envers | Équivalents rangés **par strate** (12 fichiers) ; vue par carte par `moteur.py equivalences`. |
| 4.4 Coût de chargement | Index des cartes (fiches chargées pour les seules candidates) et chargement des seules strates utiles. Gain mesuré : environ 64 Ko en mode LIRE contre 86 Ko, soit ~18 000 tokens au lieu de ~24 000. L'objectif de l'audit (< 10 000) n'est pas atteint : `protocole.md` reste chargé, parce qu'il porte les règles appliquées à chaque étape. |
| 4.5 Pas d'incertitude | Intervalle bêta sur chaque probabilité ; affichage « ~ » au-delà de 30 points de largeur. |
| 4.7 Non-stationnarité | Poids des cas selon l'âge (demi-vie 20 ans) et test de rupture entre moitiés (T5). |
| 4.8 Protocole pour une équipe | **Mode solo** déclaré : pas d'accord revendiqué, plafond ρ1. |
| 5.1 Description trop longue | 856 caractères. |
| 5.3 Renvois vers des fichiers absents | Remplacés dans `cartes.md` et `antagonismes.md`. |
| 5.4 Section non applicable | Déplacée en annexe d'`antagonismes.md`. |
| 5.7 Qualificatifs sans exemple | Cinq exemples dans `grammaire.md` §3. |
| 5.8 Arrondis | Méthode du plus fort reste ; valeurs non arrondies dans la colonne Calcul. |
| 5.9 Modes sans exemple | Exemples LIRE, CODER et SCORER avec diagnostic ajoutés (6 exemples). |
| 5.11 Glossaire, polysémie de « niveau » | `glossaire.md` ; F / f s'appelle désormais **force d'ancrage**. |
| 5.12 Pas de moteur, pas de jeu d'essai | `scripts/moteur.py` (audit, valider, partager, calculer, trajectoires, scorer, equivalences), `assets/parametres.json`, base et journal d'exemple fictifs, `README.md`. |
| 5.13 Données personnelles | `constitution.md` §6, `base-de-cas.md` §7. |
| 5.14 Décision sur une personne | Usage interdit, refus à l'étape 0. |

### Retenus avec modification

- **2.1, option A** : le code proposé normalisait les seules apparitions et disparitions, **sans statu
  quo** ; il forçait un changement à chaque pas. Le noyau retenu inclut le statu quo (probabilité
  e^(−H)).
- **2.2** : la formule proposée multipliait une probabilité par un rapport de vraisemblance, ce qui peut
  dépasser 1 ; la règle retenue multiplie la **cote**. L'audit proposait de ne plus afficher p₀ sans
  base ; la version retenue garde ρ3 si une classe de référence externe est citée, conformément au
  choix de prise de risque déclarée (P5).
- **2.3** : ρ0 n'est pas supprimé, il est rendu atteignable par configuration. Le calcul de l'audit
  (51 840 cas) supposait de couvrir toutes les cellules ; ρ0 n'est requis que pour les configurations
  étudiées, d'où la constitution de la base par configuration.
- **Équivalents vides** : l'audit écrit que les 12 cases vides sont toutes dans RÉCIPROCITÉ, RÉCURSIVITÉ
  et COMMUNAUTÉ ; le recomptage en trouve 8 sur 12 (les autres : ÉMERGENCE, RÉSONANCE ×2,
  HIÉRARCHIE). L'index le dit.

### Non retenus

| Audit | Raison |
|---|---|
| 5.2 Skills cités « non installés » | Inexact dans l'environnement de l'auteur, où ils sont installés. Une phrase de repli est ajoutée quand même. |
| 5.5 `NOEUD`, classe grammaticale des mots-codes | Ces mots-codes viennent de l'alphabet STÈLE ; les modifier ici désynchroniserait les deux skills. À traiter dans STÈLE s'il y a lieu. |
| 5.6 Glyphes confondables | Rien à faire : déjà documenté, la ligne des noms fait foi. |

### Reportés (décisions ou travaux de fond)

| Audit | État |
|---|---|
| 4.1 Strate 12 = échelle de temps | Décision de structure à prendre par l'auteur : 11 strates + attribut de durée, ou liste plate. Limite documentée dans `strates.md`. |
| 4.2 Forme / régime | Direction pour une v0.3 : dynamiques réservées aux cartes de régime. |
| 4.6 Matrice de Brown | Utile pour mesurer P8 ; demande la liste complète des universaux et un travail de correspondance. |
| 5.10 Cas réel de bout en bout | Demande une recherche sourcée ; à faire en premier pour la strate 6, 7 ou 11. |
| Chantier 7 · Sourcer les 117 équivalents | Travail documentaire ; jusque-là, colonne Référence « à fournir ». |
| Chantier 8.3 · Universalité | Question laissée à l'auteur : universelles, ou universelles aux systèmes à agents (P1) ? |

### Mesures de référence

| Indicateur | v0.1.0 | v0.2.0 |
|---|---|---|
| Changements de l'état par pas (trajectoires) | non borné ; 17 mots en espérance à 8 pas depuis 2 | au plus 1 |
| Somme des probabilités des trajectoires | non définie | 100 % (vérifié par le moteur) |
| Poids de l'a priori à 2 transitions | 83 % | 50 % |
| Ancrage de l'a priori | aucun | fréquence de base, référence externe, ou déclaré non ancré |
| Contradictions de seuil | 3 | 0 |
| Modes couverts par un exemple | 2 / 4 | 4 / 4 |
| Probabilités produites par un moteur vérifiable | non | oui |
| Équivalents sourcés | 0 / 117 | 0 / 117 (inchangé, reporté) |
| Cas réels dans la base | 0 | 0 (inchangé, reporté) |

### Questions de conception encore ouvertes

1. La force d'un mot (F / f) ne module pas encore l'a priori : faut-il un λ réduit pour une source
   Faible ?
2. Les configurations (Scission, Reproduction, Lacune contradictoire) sont signalées mais n'entrent pas
   dans le calcul.
3. L'emprunt entre strates (T4) choisit une seule strate source par transition.
4. Les valeurs de §H et les intensités de `dynamiques.md` restent à calibrer sur des cas réels.

## 0.1.0 — 2026-10-25 · première version

Constitution « Alphabet universel de situations » v0.2 (7 couches), dérivée de NEXUS-ARCHÊ v0.4.2.
Reprise des 16 cartes, des incompatibilités, de l'ancrage, des voisines, de l'anti-résonance, du
résultat nul, des relations et des positions ; suppression de l'interdiction de prévoir (R12), du
tirage aléatoire et du Mode 4 ; ajout des strates, des équivalents, de la grammaire, des dynamiques,
de la base de cas, du graphe, de la simulation, de la validation et des paramètres.
