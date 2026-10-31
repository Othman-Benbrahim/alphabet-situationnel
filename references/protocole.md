# Alphabet situationnel — Protocole

> Version : 0.5.1
>
> **Source de vérité des règles.** Chaque règle est définie une seule fois, ici. Les autres fichiers
> donnent des données (cartes, équivalents, dynamiques), des formats (fiche de cas, journal, sortie)
> et des procédures de calcul ; ils appliquent les règles sans les redéfinir. En cas de désaccord, le
> protocole fait foi. Les principes P1–P9 (`constitution.md`) priment sur ce protocole.
>
> **Calcul.** Toute probabilité affichée est produite par `scripts/moteur.py`, qui lit
> `assets/parametres.json`. Les valeurs de §H et le contenu de `parametres.json` sont identiques ;
> `moteur.py audit` le vérifie.

Sommaire : Couche 0 (O1–O3) · Couche 1 (A1–A8) · Couche 2 (G1–G6) · Couche 3 (B1–B5) ·
Couche 4 (T1–T6) · Couche 5 (S1–S5) · Couche 6 (V1–V4) · Paramètres (§H)

---

## Couche 0 · Ontologie

**O1 · Rattachement d'une situation.** Une situation est rattachée aux strates où se trouvent ses
**faits**, pas à celles de son sujet apparent. Une crise énergétique dont les faits sont des prix, des
sanctions et des températures relève des strates 6, 7 et 11. Une strate sans fait n'est pas examinée.

**O2 · Niveau 2 emprunté.** Les disciplines viennent d'une taxonomie scientifique existante
(`strates.md` §3). Chaque discipline est rattachée à une seule strate. L'outil ne crée pas de
classification des savoirs.

**O3 · Stabilité.** La liste des 13 strates ne change qu'en révision mineure, sans renuméroter une strate existante (la 13e, Politique intérieure, ajoutée en 0.5.0, a pris le numéro suivant). Ajouter une discipline
au niveau 2 ne demande aucune révision.

---

## Couche 1 · Alphabet

**A1 · Ancrage par strate.** Une carte est ancrée dans une strate quand un fait de cette strate remplit
un marqueur de son **équivalent local** (`equivalences/strate-NN.md`). Si l'équivalent est Proposé ou
la case Vide, l'ancrage passe par les marqueurs abstraits du noyau (`cartes.md`) et sa force ne
dépasse pas **Faible**.

**A2 · Évolution de l'alphabet.** Une nouvelle carte n'est admise qu'au terme de quatre étapes, dans
l'ordre ; une étape échouée arrête la procédure.

1. Au moins 3 entrées du journal des lacunes (A8) portant sur le même motif, issues de situations
   indépendantes et réelles.
2. Le motif n'est réductible à aucune carte existante, qualifiée ou non (test A6 + qualificatifs G1),
   dans au moins deux cas sur trois.
3. Une structure mathématique **nommée**, et le motif documenté avec ses marqueurs observables dans au
   moins **deux strates distinctes** : par des entrées du journal des lacunes portant sur ces strates,
   ou par des références de la littérature (statut Documenté). Raison : une carte qui n'existe pas
   encore ne peut pas avoir d'équivalent Attesté ; exiger l'attestation fermerait la procédure.
4. Fiche complète au format de `cartes.md`, voisines ajoutées symétriquement, ligne et inertie dans
   `dynamiques.md` et `assets/parametres.json`, ligne dans chacun des 13 fichiers d'équivalents,
   version mineure incrémentée.

Un motif propre à une seule strate ne devient pas une carte : il devient l'équivalent local d'une carte
existante, ou reste au journal des lacunes. Raison : une carte mono-strate casserait P1.

**A3 · Statut des équivalents.**

| Statut | Condition | Ce que le statut permet |
|---|---|---|
| **Attesté** | source vérifiée, cas réel recodé selon la version courante, contrôle A6/A7 ; identifiant du cas cité | ancrage F ou f ; emprunt entre strates (T4) |
| **Documenté** | référence vérifiée soutenant la correspondance précise et ses marqueurs | ancrage F ou f ; emprunt entre strates (T4) |
| **Proposé** | correspondance plausible, référence absente ou non vérifiée | ancrage F ou f, signalé « équivalent non vérifié » ; aucun emprunt |
| **Vide** | aucune correspondance locale convaincante **trouvée** | ancrage f seulement, par le marqueur du noyau ; aucun emprunt |
| **Hors domaine** | décision d'auteur motivée : la structure de la carte ne s'applique pas aux objets de la strate ; colonne Référence = motif | **aucun ancrage** dans cette strate ; aucun emprunt |

**Vide et Hors domaine (0.4.8).** Vide dit qu'on n'a rien trouvé ; Hors domaine dit qu'il n'y a rien à
trouver. Le second est une affirmation plus forte : il ne s'attribue que par décision d'auteur motivée,
jamais par défaut de recherche, et interdit tout ancrage de la carte dans la strate (le moteur refuse
le mot). Aucune case n'est Hors domaine en 0.4.8 : l'attribution attend la décision sur les cartes à
agents (`feuille-de-route.md`, décision 1b).

**Ce que le statut mesure, et ce qu'il ne mesure pas (0.4.1).** Le statut porte sur la
**correspondance** entre la carte et sa traduction locale : c'est une affirmation bibliographique, qui
compte quand on transporte une dynamique d'une strate à l'autre (T4). La force (A6) porte sur la
**lecture** : un fait précis remplit-il le marqueur, et les voisines ont-elles été tranchées ? Ce sont
deux incertitudes distinctes. En 0.4.0, la première plafonnait la seconde ; avec 0 équivalent
Documenté, F devenait inatteignable et avec lui la ligne A6, les positions *tient*, les configurations
et le statut Descriptif. Le plafond ne protégeait rien : si le marqueur local est faux, la lecture est
fausse en f comme en F. Le statut reste affiché et rappelé dans « À vérifier auprès de vous ».

Les 117 anciens « Documentés » à référence « à fournir » sont rétrogradés en **Proposé** en 0.4.0.
Le bilan est 0 Attesté, 0 Documenté, 196 Proposé, 12 Vide, 0 Hors domaine. Aucun résultat historique n’est réécrit
pour fabriquer une attestation. Promotion seulement après lecture de la source et recodage ; la
bibliographie du noyau ne valide pas automatiquement chaque traduction locale. Les cas fictifs peuvent
stipuler F sans valeur empirique ; leurs chiffres restent réservés au mode `--demo`.

**A4 · Accord entre codeurs.** Au moins 20 cas par strate et 20 % des cas de cette strate sont
codés indépendamment par deux codeurs distincts, dont au moins un humain. Le moteur contrôle les
identités déclarées, les attestations d’indépendance et les effectifs ; il ne certifie pas l’indépendance
réelle et ne calcule pas encore κ ; le seuil `kappa_min` de §H est donc **réservé** : déclaré pour le
futur calcul, lu par aucun calcul en 0.4.x. Tant que l’accord par carte (κ ≥ 0,6) n’est pas vérifié et archivé,
aucun accord empirique n’est revendiqué. Effectif insuffisant : mode solo, ρ0 inaccessible.
Une carte dont l’accord est insuffisant revient en Proposé ; rechercher les divergences de définition.

**A5 · Ce qui compte comme fait.** Un fait est un acte, un document, un événement daté, une mesure ou
un comportement décrit avec précision — ce qu'un tiers présent aurait pu constater — ou une donnée
issue d'un flux identifié (source, date, identifiant). Un discours compte comme fait **sur le
discours** (qui a dit quoi), pas comme preuve de ce qu'il affirme.

- Un ressenti, individuel ou collectif, n'est jamais un ancrage.
- Une déclaration d'ignorance n'ancre pas INCERTITUDE ; il faut une conduite organisée par
  l'indétermination.
- **Coïncidence lexicale** : quand le nom d'une carte figure dans la description (« mon réseau »),
  le mot ne compte pas, et l'anti-résonance est cherchée du côté de la voisine.
- Un fait vague (sans date, sans nombre, sans acteur identifiable) ne dépasse pas Faible.

**A6 · Force d'ancrage et voisines.**

F/f mesure la **qualité de l'ancrage** (précision du fait, discrimination des voisines), **jamais
l’intensité physique**, ni le statut bibliographique de l'équivalent (A3).
Une nouvelle preuve peut faire passer f à F sans aucun changement du système. Une grandeur réelle
se décrit séparément par mesure, unité, objet, dates et critère observable.

| Force | Condition |
|---|---|
| **Fort** (F) | un fait précis remplit un marqueur de l'équivalent local (Attesté, Documenté ou Proposé), **et** chaque voisine de la carte a été passée (ligne A6 obligatoire, aucun verdict `?`) |
| **Faible** (f) | un fait remplit un marqueur, mais il est vague, ou l'équivalent est Vide, ou une voisine n'est pas tranchée |
| **Nul** | aucun fait → carte inactive |

Passage des voisines : une ligne `A6 · CARTE@strate : VOISINE → (raison) ; …` qui parcourt toute la
liste « À ne pas confondre avec » de la carte dans `cartes.md`, avec l'un de quatre verdicts :
`→` (la question tranche pour cette carte), `+` (la voisine est aussi présente, ancrée par d'autres
faits), `?` (non tranché → au plus Faible), `←` (le fait relève de la voisine et ne compte pas pour
cette carte). La justification entre parenthèses est obligatoire. **Marqueur rempli, définition
contredite** : si un fait remplit le libellé du marqueur local mais contredit la définition de la carte
(`cartes.md`), la carte n'est pas ancrée, ni en F ni en f, et le marqueur est signalé au journal des
lacunes pour correction ; abaisser à f ne règle pas une contradiction de définition (exemple 12). Un mot F n'admet que `→` et `+` :
`?` laisse la question ouverte, `←` attribue son fait à la voisine. Contrôle par `moteur.py valider`
(cas réels) : voisines toutes nommées, verdicts, justifications non vides. Le moteur vérifie la forme ;
la pertinence d'une justification reste un jugement de codeur, mesuré par l'accord A4.

**A7 · Anti-résonance.** Pour chaque carte ancrée, chercher activement la contre-observation la plus
forte **dans la situation** (un contre-exemple pris ailleurs ne compte pas), puis classer sa portée :

| Portée | Critère | Effet |
|---|---|---|
| Marginale | exception, épisode isolé | force inchangée |
| Substantielle | part importante de l'objet, ou mécanisme concurrent aussi explicatif | force baisse d'un cran (F → f ; f → rejet) |
| Dominante | touche le cœur de l'objet, ou les faits relèvent d'une autre carte | rejet |
| Aucune trouvée | dire où l'on a cherché | force inchangée ; statut de lecture plafonné à Spéculatif |

Le rejet est un résultat attendu. Une lecture où toutes les contre-observations sont marginales le
justifie pour chacune.

Dans une fiche, la portée s'écrit dans le champ `portee` (`marginale`, `substantielle`, `dominante`,
`aucune`) et la force notée est la force **après** A7. Une portée substantielle exige la force f et
`force_initiale: "F"` ; sur un mot déjà f, elle impose le rejet. Sur un mot qui persiste,
`force_initiale: "F"` est recoupée avec l'état précédent : le mot devait y être F, ou déjà rétrogradé
depuis F. Une portée dominante interdit le mot.
`moteur.py valider` contrôle cette cohérence depuis 0.4.2, et l'origine F à travers les états depuis
0.4.3. « F maintenu malgré une contre-observation
substantielle » n'existe pas : c'est une sur-affirmation. Le plafond « Spéculatif » d'une portée
`aucune` porte sur le statut de lecture, qui est rédigé par l'analyste (`simulation.md` §2) et non
calculé par le moteur.

**A8 · Résultat nul et hors corpus.** Si aucune carte n'atteint Faible dans aucune strate, l'état est
**nul** (`∅`) : l'outil le déclare, liste les faits disponibles et les faits qui permettraient un
ancrage, et **ne prévoit rien**, sauf demande explicite de prévision ρ4. Si un motif clair organise la
situation sans qu'aucune carte qualifiée ne le décrive, le nommer en clair, sans le rabattre sur la
carte la plus proche, et produire une entrée du journal des lacunes (`validation.md` §6). Ce journal
est la seule entrée vers une nouvelle carte (A2).

---

## Couche 2 · Grammaire

Notation complète, syntaxe formelle et exemples : `grammaire.md`.

**G1 · Le mot.** Un mot est une carte ancrée dans une strate, avec sa force :
`CARTE@strate[F]` ou `CARTE@strate[f]`. Un qualificatif suit le mot entre accolades. Qualificatifs
admis : `{rétroaction amplifiante}`, `{rétroaction stabilisante}`, `{multi-échelle}`, `{délai}`,
`{multi-strate}`. Chacun s'ancre par un fait sur une ligne
`Q · CARTE@strate {qualificatif} : fait ; contre-observation : fait (portée)`. Une contre-observation
substantielle ou dominante retire le qualificatif (il n'a pas de force Faible). Au plus deux par mot.
`{multi-strate}` exige la même carte ancrée dans au moins deux strates par des faits distincts.

**G2 · La phrase (état).** Un état est l'ensemble des mots ancrés à une date, dans une fenêtre
d'observation déclarée : `[2026-09 | 3 mois] SEUIL@7[F] + CONTRAINTE@6[f]`. L'ordre des mots est
sans signification. Un état sans mot s'écrit `[date | fenêtre] ∅`.

**G3 · Les liaisons.** Deux mots d'un même état peuvent être liés.

- **Dans une même strate** — une relation parmi : renforcement, conflit, inclusion, appui,
  reproduction, indépendance, tension (critères observables : `grammaire.md` §4).
- **Entre strates (enchevêtrement)** — *transfert* (deux faits datés, l'un dans la strate source,
  l'autre dans la strate cible, après lui, et un mécanisme nommé), *écho* (même structure, aucun lien
  causal démontré ; verdict par défaut) ou *conflit* (l'ancrage dans une strate entrave l'équivalent
  dans l'autre).

Une liaison non qualifiée est omise, pas devinée.

**G4 · Les positions.** Quand un état compte au moins trois mots, ils peuvent recevoir les positions
*tient* (présent, stable, Fort), *bouge* (présent, en recomposition), *manque* (absent, avec des
effets observables ; l'ancrage porte sur un effet de l'absence). Les configurations Scission,
Reproduction et Lacune contradictoire restent signalables (`grammaire.md` §5). Les positions modulent
l'a priori (T2) : ce qui *bouge* change plus vite, ce qui *manque* est candidat à apparaître.

**G5 · La séquence.** Une séquence relie des états datés par `⇒`, du plus ancien au plus récent :
`[2026-03 | 3 mois] CONTRAINTE@6[F] ⇒ [2026-09 | 3 mois] SEUIL@7[F]`. Les fenêtres d'une même
séquence ont la même durée. Le qualificatif `{délai}` note un intervalle cause-effet daté à
l'intérieur d'un état.

**G6 · Bonne formation.** Une phrase est bien formée si : chaque mot est ancré (A1, A6) ; chaque carte
apparaît au plus une fois par strate ; chaque liaison est qualifiée ; une paire incompatible
(`antagonismes.md` §3) sur le même objet impose de rejeter un des ancrages ;
*indépendance* exige des objets distincts ; chaque
qualificatif a sa ligne Q. Seule une phrase bien formée entre dans la base de cas ou dans un calcul.
Vérification : liste de contrôle de `grammaire.md` §7 ; syntaxe vérifiée par `moteur.py`. Depuis
0.4.1, `moteur.py valider` lit la table de `antagonismes.md` §3 et refuse une paire incompatible dont
les champs `objet` sont identiques (casse et espaces normalisés), ainsi qu'une *indépendance* entre deux
mots de même objet. Limite : deux libellés différents pour la même chose échappent au contrôle ; la
question de `antagonismes.md` §6 reste posée à l'auteur.

---

## Couche 3 · Base de cas

Format de fiche, exemple et procédure de codage : `base-de-cas.md`.

**B1 · Fiche obligatoire.** Identifiant stable, version, strates, fenêtre, séquence, issue,
faits et sources, objet de chaque ancrage, codeur(s), mode, usage, `fictif`, `statut_donnees`.
Chaque état porte `date` et `disponible_le` (date à laquelle les preuves étaient accessibles).
Les dates de fiche et de phrase concordent ; deux états consécutifs sont séparés d’une fenêtre
calendaire exacte. Les données irrégulières sont archivées pour réexamen, pas converties implicitement.
Les nouveaux mots, changements de confiance et retraits sont documentés ; `mots: []` est interdit,
`null` signifie aucun changement à documenter. Le contrôle compare les forces, strates et objets.
Sources réelles non vérifiées : `archive_a_revoir`, avec motif, exclu des calculs. Les quatre anciens
cas transmis sont conservés sous ce statut, sans modification de leurs faits. Le calcul appelle le
même validateur que la commande `valider` ; une fiche active invalide bloque la base.

**B2 · Codage manuel ou déclenché.** Un état est codé à la main à partir d'un récit documenté, ou
déclenché par une **règle sur données** (indicateurs, fenêtre, seuil) rattachée à une carte et une
strate. Chaque règle de déclenchement est versionnée et citée dans la fiche. Le codage déclenché n'est
pas encore outillé automatiquement en v0.4.0.

**B3 · Double codage.** Au moins 20 % des cas de chaque strate sont codés par deux codeurs
indépendants. Un modèle de langage peut être l'un des deux codeurs, jamais les deux : deux passes du
même modèle partagent ses biais. Sous 20 % de cas double-codés, l'outil est en mode solo (A4).

**B4 · Cas sans événement.** La base inclut des situations où la structure était présente et où rien
ne s'est produit, dans une proportion comparable à leur fréquence réelle. Sans eux, toute transition
est surestimée (biais du survivant). Si aucun des cas homologues d'un calcul n'est « sans événement »,
le résultat est plafonné à ρ1. `sans_evenement: true` exige qu'aucune apparition, disparition ni
changement de force ne survienne sur toute la séquence ; `moteur.py valider` le contrôle depuis 0.4.4.

**B5 · Séparation apprentissage / test.** Un cas sert soit à estimer les transitions (couche 4), soit
à valider (couche 6), jamais aux deux. L'usage est fixé à l'entrée du cas par l'empreinte de son
identifiant (`moteur.py partager`, `base-de-cas.md` §5) et ne change plus.

---

## Couche 4 · Graphe de transitions

Dynamiques par carte : `dynamiques.md`. Procédure de calcul et exemple : `graphe.md`.

**T1 · Événements.**

| Type | Condition présente | Résolution |
|---|---|---|
| `X@s apparaît` | X absent | présence de X à la prochaine observation, critère externe figé |
| `X@s persiste` | X présent | présence de X à la prochaine observation |
| `X@s disparaît` | X présent | absence de X à la prochaine observation |
| `X@s se transforme` | X présent, TRANSFORMATION absente | changement de forme de l’objet nommé, invariant conservé et persistance |
| `X@s s'intensifie` | X présent | grandeur mesurée de cet objet augmente selon un critère fixé, avec persistance |
| `se renforce`, `s'affaiblit` (ancien f ↔ F) | révision de confiance du codeur | conservés dans l’historique, **refusés en prévision** |

Pour un composé, P = P(persiste) × P(changement **conditionnel à la persistance**). La fréquence
conditionnelle doit être fournie pour l’objet, l’événement et la fenêtre dans `--references`.
Sans elle : **probabilité non estimée**, aucun 1/3 arbitraire ni produit de probabilités marginales.
La résolution est fournie en JSON ; l’intensification exige une grandeur, une unité, une comparaison
et au moins deux observations numériques datées antérieures à la date d’information. Le moteur
vérifie la structure de ce contrat, pas sa validité scientifique. Les composés à plusieurs pas sont
refusés. Chaque référence a sa clé ; un scalaire `--fref` n’est jamais partagé entre composantes.

**T2 · A priori explicite.** Une fréquence de référence f est modulée, pour les apparitions,
par des **multiplicateurs hypothétiques** λ issus de `dynamiques.md` :

```
p₀ = f × LR / (1 − f + f × LR) ; LR = produit des λ, plafonné à 10
```

Cette forme sur les cotes ne transforme pas des λ choisis en rapports de vraisemblance estimés.
Les effets inhibiteurs ne sont pas encore appris ; ne pas inventer de λ pour les simuler.
Source externe : définition, source consultée, période, fenêtre, date de disponibilité et fréquence
finie entre 0 et 1. Elle est propre à l’événement. La disparition utilise la référence de disparition,
ou le complément d’une référence de persistance, jamais un scalaire ambigu.
Fréquence de base : moyenne pondérée de transitions éligibles, un cas pesant au plus une unité,
lissée par k₀ vers la référence externe ou le défaut. Ancrage sans source externe seulement si
l’effectif **pondéré** atteint n_min. Les fréquences sont calculées après filtrage temporel.
Défauts de probabilité et inerties sont ramenés de 3 mois à la fenêtre à taux constant.
Pour *bouge*, la persistance r devient r^1,5 : accélération du taux de sortie, toujours entre 0 et 1.
0 et 1 sont traités explicitement ; aucune loi bêta impropre n’est fabriquée. Les multiplicateurs
ne constituent ni des mécanismes démontrés ni une validation ; `--sans-cartes` fournit une ablation
sans multiplicateurs ni sélection d’homologues pour mesurer leur apport conjoint.

**T3 · Révision par les cas.** Seuls les cas actifs d’apprentissage disponibles à la date
figée d’information sont éligibles. Pour chaque transition, son état final et les preuves des deux
états doivent être disponibles. Les cas futurs, archives, cas test et données fictives (hors `--demo`)
sont exclus. La même règle s’applique aux homologues et aux fréquences de base.
H1 exige un état structurel complet identique et non vide (cartes, F/f, qualificatifs) ; H1.5 utilise
un Jaccard pondéré sur toutes les cartes (F=1, f=0,5) avec intersection non vide ; H2 exige toutes
les sources de l’événement, non vides. Objets et mécanismes restent à vérifier humainement : ces
proximités ne prouvent pas une identité causale. Liaisons et positions ne sont pas des dimensions
apprises de la similarité ; elles modulent seulement l’a priori aux endroits documentés.
Les transitions d’un cas se partagent un poids maximal de 1, réduit par l’âge ; c_A reste le nombre
de cas distincts. P = (n_E + k p₀)/(n_A + k). L’intervalle bêta est une approximation **conditionnelle**
aux hypothèses et au codage, pas l’incertitude totale. Aucun intervalle sans observation ou lorsque
les paramètres bêta ne sont pas strictement positifs.
ρ0 : ≥30 cas, sous réserve de double codage et cas sans événement ; ρ1 : ≥3 cas ou plafond ;
ρ2 : ≥3 cas empruntés ; sinon ρ3 si référence ancrée, ρ4 sinon. Ces niveaux expriment la provenance,
pas une performance validée. Au niveau ρ0, l’accord de codage doit encore être contrôlé séparément.

**T4 · Emprunt entre strates.** Seulement sans homologue local, par des équivalents
Documentés ou Attestés pour **toutes les cartes sources et la cible**, dans la strate d’origine et
celle d’emprunt. Un seul emprunt par transition ; poids w ; niveau ρ2 à partir de trois cas distincts.
Le partage d’une structure ne démontre pas le transfert de sa dynamique. Avec les équivalents livrés
en 0.4.0 (non sourcés), aucun emprunt empirique n’est autorisé ; documenter et tester un périmètre
avant activation. Les contre-épreuves doivent comparer avec le modèle sans emprunt.

**T5 · Stationnarité.** Les transitions comptent avec un poids qui décroît avec leur âge (demi-vie de
§H). Si la fréquence de l'événement diffère de plus d'un facteur 2 entre les moitiés anciennes et
récentes des transitions homologues (chacune d'au moins 5 transitions), le calcul est déclaré **non
stationnaire** et plafonné à ρ1.

**T6 · L'arbre de la connaissance.** L'arbre est une **vue** du graphe : chaque carte est une branche
portant ses transitions sortantes, chaque strate une sous-branche. Une situation peut avoir plusieurs
parents ; la structure réelle reste un graphe.

---

## Couche 5 · Simulation

Format de sortie complet : `simulation.md`.

**S1 · Prévision.** Une prévision comporte : un énoncé, une **définition de résolution externe**
(source publique, critère, seuil numérique ou fait daté, décidable par un tiers sans recoder la
situation) **qui opérationnalise le marqueur local de la carte visée** (`equivalences/strate-NN.md` ;
le moteur l'affiche), une probabilité et son intervalle, une échéance, un indicateur de bascule, une condition de
réfutation, un niveau ρ et sa source. Deux régimes, à déclarer :

Raison de l'exigence de marqueur : si la résolution mesure autre chose que l'événement calculé (par
exemple « deux attaques en 6 jours » pour « CROISSANCE@7 se renforce », dont le marqueur est « surfaces
contrôlées en série datée »), le score ne dépend plus du modèle mais de la correspondance choisie par
le codeur. Un événement sans marqueur opérationnalisable est reformulé ou abandonné.

- **Prévisions binaires** : chaque événement est une prévision distincte ; aucune somme à 100 %.
- **Partition** : la question énumère des issues incompatibles. Si deux issues calculées séparément
  peuvent se produire ensemble, la question est redécomposée (A seul, B seul, A et B, ni l'un ni
  l'autre) avant toute normalisation. On ne normalise jamais des événements dont la conjonction est
  possible et non modélisée.

**S2 · Pas de temps et horizon.** Le pas est la fenêtre ; un jour est calendaire, un mois
avance au même jour du mois suivant (rabattu au dernier jour si nécessaire), une année conserve le
mois et le jour. L’échéance calculée est `date état + h fenêtres`. Une échéance fournie doit coïncider.
Ne pas arrondir silencieusement une demande : proposer une fenêtre qui atteint l’échéance ou annoncer
l’horizon effectivement calculé. h est un entier de 1 à 20.
Au-delà d’un pas, préciser la sémantique : présence à l’échéance, apparition/disparition au moins une
fois, ou persistance continue. Prévision **et comparateur** sont propagés avec la même sémantique.
Sources supposées fixes ; aucun intervalle multi-pas tant que l’incertitude jointe n’est pas estimée.

**S3 · Proxémie.** `calculer --pas h` utilise une chaîne absent/présent ; les références
d’apparition et de persistance sont distinctes. `--semantique` choisit l’événement temporel.
`trajectoires` est une exploration par risques concurrents : au plus un changement par pas,
faisceau de 300, seuil de pas 5 %, résiduels R1 et R2 distincts. Le risque de **chaque branche** hérite
de toutes les estimations utilisées dans la normalisation. Les liaisons et positions dont les mots
disparaissent sont retirées. La date d’information reste figée pendant la simulation : aucune donnée
future n’est injectée. États affichés + résiduels = 1, vérifié par assertion. Si R2 >30 %, avertissement.
Ce noyau ne représente ni les changements simultanés ni une distribution calibrée des trajectoires.

**S4 · Échelle de risque.** Le niveau dit **d'où vient** une prévision, pas si elle est juste.

| Niveau | Source | Origine |
|---|---|---|
| ρ0 | au moins 30 cas distincts homologues dans la strate | T3, c_A ≥ 30 |
| ρ1 | 3 à 29 cas distincts homologues, ou un plafond T3 | T3 |
| ρ2 | au moins 3 cas distincts empruntés à une autre strate | T4 |
| ρ3 | a priori structurel **ancré** (fréquence de base ou classe de référence citée), aucun cas | T2 |
| ρ4 | a priori non ancré, lecture symbolique, intuition, état nul | hors graphe |

**S5 · Signalement.** Chaque prévision porte la ligne :
`⚠ ρ[n] · [source] · p₀ [x] % · p [y] % [intervalle] · échéance [date] · journal [id]`.
Si l'intervalle est plus large que le seuil de §H, la probabilité s'affiche `~y % (large : a–b)`. Les
probabilités d'une partition sont arrondies par la méthode du plus fort reste ; les valeurs non
arrondies figurent dans la colonne Calcul. Un niveau ou une strate « non validé » (V4) reste
utilisable, avec la mention à côté. Une prévision ρ4 n'est jamais présentée seule : elle accompagne
au moins une prévision de niveau inférieur, ou elle est déclarée comme l'unique hypothèse disponible.
Aucune probabilité n'apparaît dans le bloc symbolique (P9).

---

## Couche 6 · Validation

Journal, score et fiches de diagnostic : `validation.md`.

**V1 · Journal et score.** Une prévision chiffrée est journalisée avant échéance avec
résolution externe, objet, événement temporel, épisode, référence au même horizon, `rejeu`, `fictif`,
versions et empreintes. Une sortie « non estimée » ne devient jamais une probabilité de journal.
Le score est une nouvelle ligne : issue 0/1 selon la source, ou null si non résolue. Aucun doublon
n’est écrasé ; scores orphelins, dates invalides et partitions incohérentes sont refusés.
Les partitions sont scorées comme une question multi-catégories (somme des erreurs quadratiques),
avec probabilités sommant à 1 et exactement une issue réalisée ; un groupe incomplet reste non résolu.
Les rejeux, fictifs, résolutions non contrôlées et prévisions sans preuve de prépublication/empreintes
sont affichés à part et exclus de V4. L’authenticité d’une preuve externe reste à vérifier par un tiers.
Une prédiction manquante de score est comptée, pas oubliée. Les prévisions liées sont regroupées par
`episode_id` : la moyenne comparative donne le même poids à chaque épisode.

**V2 · Diagnostic par couche.** Une prévision manquée est attribuée à la première couche fautive :
1 (ancrage contesté, carte mal choisie), 2 (état mal formé, liaison mal qualifiée), 3 (cas homologues
rares ou biaisés), 4 (transition mal estimée alors que l'état était juste), 5 (propagation, horizon ou
pas de temps). « Imprévisible » n'est pas une couche : c'est une hypothèse, recevable seulement si les
quatre premières ont été examinées.

**V3 · Boucle de révision.** Les diagnostics accumulés révisent : le statut des équivalents (A3),
l'accord entre codeurs (A4), la composition de la base (B4), les valeurs de §H. Toute révision de §H
est datée, motivée par des scores, reportée dans `assets/parametres.json`, et n'est jamais appliquée
aux prévisions déjà journalisées.

**V4 · Jalon de validation.** Au moins 50 épisodes comparables prospectifs, gain de Brier
≥10 % contre le comparateur fixé au même horizon : **jalon interne atteint**, jamais certification
scientifique automatique. Avant : « non encore évalué ». L’indépendance entre épisodes, l’incertitude
du gain, les effets de sélection et la généralisation doivent être étudiés séparément. Réserver une
période future à chaque révision ; ne pas optimiser sur le lot servant à proclamer une performance.
La moyenne p(1−p) décrit la confiance annoncée, pas l’incertitude objective ni l’utilité du test.

## §H · Paramètres

`assets/parametres.json` est la source structurée. Le tableau exhaustif ci-dessous est généré par
`python3 scripts/moteur.py parametres` ; ne pas le modifier à la main. `audit` vérifie toutes ses
valeurs, y compris les tables imbriquées. Les réglages restent des hypothèses non calibrées ; toute
modification impose une version et une nouvelle évaluation, sans réécriture des anciens paris.

<!-- PARAMETRES:BEGIN -->
| Paramètre | Valeur |
|---|---|
| `version` | `"0.5.1"` |
| `nombre_strates` | `13` |
| `cartes.SEU` | `"SEUIL"` |
| `cartes.REC` | `"RÉCIPROCITÉ"` |
| `cartes.PER` | `"PÉRIODICITÉ"` |
| `cartes.RCS` | `"RÉCURSIVITÉ"` |
| `cartes.EME` | `"ÉMERGENCE"` |
| `cartes.HIE` | `"HIÉRARCHIE"` |
| `cartes.RES` | `"RÉSEAU"` |
| `cartes.POL` | `"POLARITÉ"` |
| `cartes.INC` | `"INCERTITUDE"` |
| `cartes.CTR` | `"CONTRAINTE"` |
| `cartes.PRO` | `"PROPORTION"` |
| `cartes.TRA` | `"TRANSFORMATION"` |
| `cartes.TRC` | `"TRACE·MÉMOIRE"` |
| `cartes.CRO` | `"CROISSANCE"` |
| `cartes.COM` | `"COMMUNAUTÉ"` |
| `cartes.RSN` | `"RÉSONANCE"` |
| `lambda.F` | `3.0` |
| `lambda.M` | `1.8` |
| `lambda.f` | `1.2` |
| `f_defaut` | `0.05` |
| `plafond_p0` | `0.95` |
| `plafond_LR` | `10.0` |
| `multiplicateur_bouge` | `1.5` |
| `inertie.SEU` | `0.97` |
| `inertie.TRC` | `0.96` |
| `inertie.PER` | `0.9` |
| `inertie.RES` | `0.9` |
| `inertie.CTR` | `0.9` |
| `inertie.HIE` | `0.88` |
| `inertie.POL` | `0.85` |
| `inertie.PRO` | `0.85` |
| `inertie.RSN` | `0.85` |
| `inertie.REC` | `0.65` |
| `inertie.RCS` | `0.65` |
| `inertie.EME` | `0.65` |
| `inertie.TRA` | `0.65` |
| `inertie.COM` | `0.65` |
| `inertie.CRO` | `0.65` |
| `inertie.INC` | `0.4` |
| `inertie_contrainte_materielle` | `0.65` |
| `k` | `2.0` |
| `seuil_rho0_cas_distincts` | `30` |
| `w_emprunt` | `0.5` |
| `jaccard_H15` | `0.7` |
| `seuil_affichage` | `0.05` |
| `intervalle` | `0.8` |
| `largeur_max_affichage` | `0.3` |
| `demi_vie_ans` | `20` |
| `ratio_non_stationnarite` | `2.0` |
| `min_transitions_par_moitie` | `5` |
| `partage_test` | `"01234"` |
| `double_codage_part` | `0.2` |
| `double_codage_min_cas` | `20` |
| `kappa_min` | `0.6` |
| `v4_gain` | `0.1` |
| `v4_n` | `50` |
| `matrice.SEU.PER` | `"f"` |
| `matrice.SEU.TRA` | `"M"` |
| `matrice.SEU.TRC` | `"F"` |
| `matrice.REC.SEU` | `"f"` |
| `matrice.REC.HIE` | `"M"` |
| `matrice.REC.POL` | `"M"` |
| `matrice.REC.COM` | `"f"` |
| `matrice.PER.SEU` | `"f"` |
| `matrice.PER.RSN` | `"M"` |
| `matrice.RCS.SEU` | `"M"` |
| `matrice.RCS.CTR` | `"f"` |
| `matrice.RCS.CRO` | `"M"` |
| `matrice.EME.HIE` | `"M"` |
| `matrice.EME.CTR` | `"M"` |
| `matrice.EME.TRC` | `"F"` |
| `matrice.EME.CRO` | `"M"` |
| `matrice.EME.COM` | `"f"` |
| `matrice.EME.RES` | `"f"` |
| `matrice.HIE.SEU` | `"f"` |
| `matrice.HIE.POL` | `"M"` |
| `matrice.HIE.TRA` | `"f"` |
| `matrice.HIE.RCS` | `"f"` |
| `matrice.HIE.INC` | `"f"` |
| `matrice.RES.SEU` | `"M"` |
| `matrice.RES.POL` | `"f"` |
| `matrice.RES.PRO` | `"M"` |
| `matrice.RES.EME` | `"f"` |
| `matrice.RES.CRO` | `"f"` |
| `matrice.RES.RSN` | `"f"` |
| `matrice.RES.RCS` | `"f"` |
| `matrice.RES.INC` | `"f"` |
| `matrice.POL.SEU` | `"M"` |
| `matrice.POL.REC` | `"f"` |
| `matrice.POL.HIE` | `"M"` |
| `matrice.POL.CRO` | `"M"` |
| `matrice.POL.CTR` | `"f"` |
| `matrice.INC.SEU` | `"f"` |
| `matrice.INC.EME` | `"M"` |
| `matrice.INC.CTR` | `"M"` |
| `matrice.INC.RCS` | `"f"` |
| `matrice.CTR.SEU` | `"M"` |
| `matrice.CTR.RES` | `"M"` |
| `matrice.CTR.TRA` | `"f"` |
| `matrice.CTR.INC` | `"f"` |
| `matrice.CTR.COM` | `"f"` |
| `matrice.CTR.PER` | `"f"` |
| `matrice.PRO.SEU` | `"f"` |
| `matrice.PRO.POL` | `"f"` |
| `matrice.PRO.TRA` | `"M"` |
| `matrice.TRA.SEU` | `"M"` |
| `matrice.TRA.EME` | `"f"` |
| `matrice.TRA.TRC` | `"M"` |
| `matrice.TRC.SEU` | `"f"` |
| `matrice.TRC.PER` | `"f"` |
| `matrice.TRC.POL` | `"f"` |
| `matrice.CRO.SEU` | `"M"` |
| `matrice.CRO.EME` | `"f"` |
| `matrice.CRO.CTR` | `"F"` |
| `matrice.CRO.RES` | `"f"` |
| `matrice.CRO.PRO` | `"f"` |
| `matrice.COM.SEU` | `"M"` |
| `matrice.COM.REC` | `"f"` |
| `matrice.COM.HIE` | `"M"` |
| `matrice.COM.RES` | `"f"` |
| `matrice.RSN.SEU` | `"M"` |
| `matrice.RSN.CRO` | `"M"` |
| `autre_strate.SEU.SEU` | `"M"` |
| `autre_strate.RES.SEU` | `"M"` |
| `autre_strate.CRO.CTR` | `"F"` |
| `autre_strate.RSN.SEU` | `"M"` |
| `faisceau_max` | `300` |
| `fenetre_reference_jours` | `91.3125` |
| `k0_frequence` | `20` |
| `n_min_frequence` | `10` |
| `c_min_rho1` | `3` |
| `alerte_R2` | `0.3` |
| `pas_max` | `20` |
<!-- PARAMETRES:END -->

