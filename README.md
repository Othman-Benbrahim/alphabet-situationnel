# Alphabet situationnel — guide humain

Auteur : Othman Ben Brahim · Licence : MIT (`LICENSE`)

Version 0.7.12 (numéro de `assets/parametres.json`, vérifié par `audit` dans `SKILL.md`, le README, les
20 références, les 13 fichiers d'équivalents et le moteur ; le paquet livré se nomme
`alphabet-situationnel-0.7.12.zip`). **Intégrité du paquet** : `SHA256SUMS` donne l'empreinte de chaque
fichier livré ; `sha256sum -c SHA256SUMS` ou `moteur.py audit` refusent un fichier modifié, ajouté ou
retiré. `audit` valide aussi les JSONL livrés (bases, cas archivés, journal d'exemple). Un zip ne
pouvant contenir sa propre empreinte, son SHA-256 est communiqué à la livraison ; sur GitHub, chaque
version a son étiquette `vX.Y.Z` et sa release, avec `SHA256SUMS` en pièce jointe (`publier-github.ps1`).
Les étiquettes sont signées si une clé est configurée (`git config user.signingkey`, GPG ou SSH ; vérifier par `git tag -v vX.Y.Z`) ; sinon, le niveau d'assurance est celui du compte GitHub de l'auteur. Historique : 0.4.0 a corrigé le calcul et
les contrats, 0.4.1 a rétabli les contrôles perdus (F, G6, renvois, homologie), 0.4.2 a rendu A6 et A7
vérifiables, 0.4.3 recoupe A7 entre états et valide le schéma documenté, 0.4.4 durcit les entrées
(aucune trace Python, erreurs JSON) et l'affichage, 0.4.5 aligne la sortie sur la constitution et
contrôle les chiffres publiés, 0.4.6 détecte les répétitions et réserve `kappa_min`, 0.4.7 recode les cas réels et ajoute la
feuille de route (`references/feuille-de-route.md`, `moteur.py bilan`), 0.4.8 applique les décisions
d'auteur (strate 12 conservée, statut Hors domaine, licence MIT), 0.5.0 ajoute la strate 13
(politique intérieure), les sources françaises issues d'EnVrai? et le comparateur inertiel, 0.5.1
restreint SEUIL@13 et journalise à part les jugements nominatifs, 0.6.0 traduit trois apports théoriques
en contrôles (barreau déclaré, garantie et option des ancrages F, jugement scellé avant le moteur,
bande de sensibilité, questions qui départagent, angles morts ; `references/apports-theoriques.md`),
0.6.1 inscrit la décision 1b (cartes à agents universelles) et propose 16 références pour la strate 7,
0.6.2 à 0.6.4 en documentent treize, sur textes lus, 0.6.5 traite l'audit de la 0.6.4, 0.6.6 retient deux contrôles des apports CIA et *Spiral Semiosis*, 0.6.7 un contrôle de l'apport *Intuition Machine* (QPT), 0.6.8 archive les quatre premiers cas réels, 0.6.9 corrige le plafond (complémentarité, découpage temporel) et lie le journal au calcul entier, 0.6.10 achève ce lien et ajoute la temporalité déclarée, 0.6.11 compte les abstentions, 0.6.12 pose la question de la temporalité avant tout calcul, 0.6.13 traite l'audit de la 0.6.12 (contrôles exécutés pour de vrai, Brier des partitions, temporalité tranchée), 0.6.14 l'audit Manus (provenance des prévisions et des codeurs, manifeste, intégration continue), 0.6.15 les corrections documentaires de l'audit Scira ; 0.7.0 ajoute les tests de preuve du process tracing et la décomposition de Murphy, 0.7.1 corrige la sortie sous Windows (cp1252) et ajoute Windows et macOS à la CI, 0.7.2 exige qu'une question dise ce qui y répondrait et ce que chaque réponse établit, qu'un fait F cite le passage qui le soutient, et décrit le banc d'essai de toute modification du skill, 0.7.3 traite l'audit d'ingénierie : dossier de lecture contrôlé avant tout calcul (`moteur.py dossier`, `calculer --dossier`), bande de sensibilité de la classe de référence, fragilité de niveau d'homologie, sources du calcul affichées, 0.7.4 applique quatre décisions d'auteur sans changer aucune probabilité : sceau de dossier exigé pour V4, partage daté au registre, placebo d'homologie, plancher de recherches A7, 0.7.5 confronte la matrice aux observations (`moteur.py confronter`), teste les écarts de score (tests exacts du signe et de Wilcoxon) et publie les poids des deux a priori, sans changer aucune probabilité, 0.7.6 ajoute la variable sonde sur les paramètres (`moteur.py sonde`), la couverture des arêtes et la taille effective de Kish, 0.7.7 dédouble le seuil d'ancrage, rend V4 absolu, testé et à effectif calculé, ajoute les questions discriminantes et clôt RÉSONANCE@7, 0.7.8 ajoute un comparateur externe aveugle et scellé, la méthode des fréquences externes et l'export du second codeur, 0.7.9 l'accord sous faible prévalence (`accord` : κ, PABAK, taux de manque), l'audit aveugle des rejets et le journal des concessions, 0.7.10 le support du mécanisme et la réfutation qui annule (Toulmin), la répétabilité d'un codeur seul, l'intérêt et le référentiel des références externes, la procédure des jugements et le bras « modèle seul », sans changer aucune probabilité, 0.7.11 scinde « passage insuffisant » en deux diagnostics aux remèdes opposés, exige de nommer ce qui rend deux sources indépendantes et vérifie « aucune probabilité ne change » par clôture complète (`moteur.py conservativite`) au lieu de calculs témoins, 0.7.12 traite l'audit V34 : la paire « sans cartes → avec cartes » en tête tant qu'aucun cas réel n'est actif, une bande d'horizon, l'homologie indiscernable du placebo signalée, une lecture séquentielle de V4 (e-processus), le compte de l'érosion des marqueurs en strate 7 et sept décisions d'auteur ouvertes ; aucune probabilité ne change (clôture identique à la 0.7.9).
Le modèle suit `SKILL.md`. Les anciens faits non revérifiés sont conservés comme archives exclues.

## Ce que fait l'outil

Lire une situation factuelle à l'aide de 16 structures transversales candidates dans 13 strates,
écrire son état, puis calculer des hypothèses conditionnelles quand les entrées sont recevables.
F/f est la confiance du codage ; les grandeurs physiques sont séparées. Les probabilités sont
expérimentales : aucune calibration prospective n'est acquise. Une référence manquante pour un
composé produit « non estimé », sans chiffre de remplacement.

## Organisation

```
SKILL.md                    procédure et chargement par mode
LICENSE                     licence MIT
LICENCES-TIERS.md           notice MIT d'EnVrai?, dont sources-france.md reprend des contenus
README.md                   ce guide
CHANGELOG.md                historique et révisions 0.4.0–0.7.9
references/                 20 références (dont feuille-de-route.md, sources-france.md, angles-morts.md et apports-theoriques.md) et 13 fichiers d'équivalents
scripts/moteur.py           moteur, validateur, scoreur et autotests intégrés
assets/parametres.json      source structurée exhaustive des paramètres
assets/base-de-cas.exemple.jsonl  40 cas fictifs, --demo obligatoire
assets/journal.exemple.jsonl      journal fictif d'archive (règles 0.4.0, calculs non reproductibles sous la version courante), exclu de V4
assets/cas-reels.jsonl            4 premiers cas réels, archivés en 0.6.8 (rejeux d'avant les règles courantes), exclus des calculs
assets/cas-reels-originaux.jsonl  témoignage original de ces 4 cas, archive non réécrite
.github/workflows/ci.yml          contrôles à chaque push : manifeste, audit, autotests, bases, journal (Python 3.8 et 3.12)
SHA256SUMS                        empreinte de chaque fichier livré (moteur.py manifeste)
.gitattributes                    aucune conversion de fin de ligne (les empreintes restent valides)
assets/journal-lacunes.md         pistes historiques à revérifier, ancrages à revoir
assets/rabbits.jsonl              constructions ad hoc d'un codage, avec statut ouvert ou résorbé
.gitignore                        __pycache__/ et *.pyc (sans BOM)
```

## Démarrer

```bash
python3 scripts/moteur.py audit
python3 scripts/moteur.py autotest
python3 scripts/moteur.py valider assets/base-de-cas.exemple.jsonl
python3 scripts/moteur.py calculer --demo --base assets/base-de-cas.exemple.jsonl \
  --etat "[2026-09 | 3 mois] POLARITÉ@7[F] + CONTRAINTE@6[F]" \
  --evenement "SEUIL@7 apparait" --liaison "CONTRAINTE@6 echo POLARITÉ@7" --temporalite generique --json
python3 scripts/moteur.py scorer assets/journal.exemple.jsonl
```

Pour une lecture réelle sans base : F est permis sur un équivalent Proposé si le fait est précis et si
la ligne A6 passe toutes les voisines (signalé « équivalent non vérifié ») ; f sur un équivalent Vide.
Voir les équivalents d'une carte : `python3 scripts/moteur.py equivalences --carte SEUIL`.
Prérequis : Python 3.8 ou plus récent, bibliothèque standard seule.
Pour un événement simple avec fréquence externe, renseigner également source, période et date de
 disponibilité. Les composés exigent des références conditionnelles et une résolution structurée :
voir `references/graphe.md` §2.2 et §7. Les chiffres fictifs ne sont jamais des références empiriques.
Le moteur calcule une échéance exacte ; l'option `--pas` ne peut plus être ignorée silencieusement.

## Pour un second codeur

Lire A1–A8 et la grammaire ; recevoir uniquement les faits et dates de disponibilité, jamais le
premier codage. Coder indépendamment, nommer l'objet de chaque ancrage, documenter les alternatives.
Vérifier les sources des équivalents avant F. Valider la fiche puis examiner l'accord par carte.
Le nombre de codeurs déclaré ne prouve ni leur indépendance ni la valeur de κ ; au moins un humain.
`moteur.py export-codeur --base B --cas ID` produit cette vue : faits, sources et dates, mélangés, sans
mots, cartes, forces, strates ni questions ; les faits restent ceux qu'a retenus le premier codeur, et le
mieux est de partir du dossier de sources complet. Déclarer `signe_suffisant` avant de coder. Mesurer l'accord carte par carte avec `moteur.py accord` : κ seul trompe quand une carte est rare. Un bras
**externe** (prévision produite sans voir l'état ni les cartes, `sceller-comparateur`) peut aussi être
confié à un tiers : il mesure le dispositif entier, pas seulement les cartes.

## Ce que l'outil ne fait pas

Il ne certifie pas la vérité des sources, ne diagnostique pas et ne décide pas sur une personne.
Il ne valide pas scientifiquement ses propres probabilités. Le jalon V4 demande des épisodes
prospectifs comparables, et reste distinct d'une étude de généralisation avec incertitude du gain.
La vérification bibliographique et la collecte prospective ne peuvent pas être remplacées par une
mise à jour du logiciel. Ni universalisme prédictif ni transfert empirique entre strates n'est acquis.
