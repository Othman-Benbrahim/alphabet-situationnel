# Alphabet situationnel — Validation (couche 6)

> Version : 0.7.2

> Contrat du journal, scores et limites d'évaluation. Règles V1–V4. Le scoreur valide les données
> avant calcul et ne prononce jamais une certification scientifique automatique.

---

## 1. Journal des prévisions (V1)

Une prévision est figée avant son échéance ; une ligne de score s'ajoute sans modifier la première.
Exemple **fictif** de structure (remplacer les chaînes SHA256 par les empreintes réelles du JSON
moteur ; null si indisponibles, auquel cas la prévision reste hors V4) :

```json
{
  "type": "prevision",
  "id": "P-0042",
  "date": "2026-09-01",
  "version_regles": "0.7.0",
  "question": "POL@7 persiste au 2026-12-01 ?",
  "evenement": "POL@7 persiste",
  "resolution": {
    "source": "Registre entièrement fictif de la démonstration",
    "critere": "Observation simulée du marqueur deux blocs, alignements exclusifs",
    "seuil": "Présence constatée à la date finale selon le scénario fictif",
    "marqueur": "deux blocs, alignements exclusifs",
    "objet": "Situation fictive A-B"
  },
  "etat_present": "[2026-09 | 3 mois] POLARITÉ@7[F] + CONTRAINTE@6[F]",
  "probabilite": 0.8168065470680189,
  "intervalle": [
    0.6713359462373685,
    0.9383666673288151
  ],
  "rho": "ρ1",
  "echeance": "2026-12-01",
  "indicateur_bascule": "Nouvel acte consigné dans le registre fictif",
  "refutation": "Critère non observé à échéance",
  "partition": null,
  "frequence_de_base": 0.8372000588523011,
  "p_sans_cartes": 0.8372000588523011,
  "temporalite": "generique",
  "rejeu": true,
  "fictif": true,
  "episode_id": "DEMO-A-B",
  "semantique": "continue",
  "pas": 1,
  "resolution_verifiee": true,
  "empreintes": {
    "moteur": "SHA256_DU_MOTEUR",
    "parametres": "SHA256_DES_PARAMETRES",
    "base": "SHA256_DE_LA_BASE"
  },
  "preuve_prepublication": null
}
```

Ligne de score :

```json
{"type":"score","id":"P-0042","date":"2026-12-02","issue":1,"preuve":"Observation stipulée, entièrement fictive"}
```

`p_sans_cartes` (obligatoire depuis 0.5.0, null pour un composé) est la probabilité du même calcul sans
cartes, que `calculer` imprime à côté de p : le **comparateur inertiel**. `scorer` en tire
`apport_des_cartes` (Brier avec cartes moins Brier sans cartes) : un score flatteur dont l'apport est
nul ne vient que du statu quo et ne valide pas la lecture (exemple 11).
**Deux probabilités (0.6.0).** Avant de lancer le moteur, le codeur écrit sa propre probabilité et la
scelle : `moteur.py sceller-jugement --question … --evenement … --p … --date …` rend
`probabilite_jugement` et `jugement_scelle`, à recopier dans la ligne. Le champ est obligatoire à
partir des prévisions 0.6 (null si aucun jugement n'a été scellé) ; un scellé qui ne correspond pas à
la question, à l'événement, à la date ou à la probabilité est refusé. `scorer` rend alors
`moteur_contre_jugement` : Brier du jugement, Brier du moteur, nombre d'**améliorations** et de
**dégradations** question par question — une amélioration moyenne peut cacher des dégradations.
`bande_sensibilite` (facultatif) recopie la bande de sensibilité de `calculer` (`graphe.md` §2.3).
Le scellé local ne prouve pas la date : seul le dépôt externe le fait (§8).

**Difficulté des questions (0.6.0 ; sens corrigé en 0.6.5).** `scorer` rend `difficulte` :
0,5 − |f − 0,5| par question (0 pour une question jouée d'avance, 0,5 pour une question à 50 %), f étant la
fréquence de base au même horizon (à défaut, `p_sans_cartes`), la part des questions à référence
extrême (f < 0,1 ou > 0,9) et le Brier par tranche. Au-delà de 70 % de questions extrêmes, un bon
score ne mesure pas la compétence : prédire « non » à 0,8 % est presque gratuit (exemples 11 et 12).

**Questions hors alphabet** (`"origine": "jugement"`). L'alphabet décrit des structures, pas des issues
nominatives : « qui sera élu ? », « le groupe aura-t-il quatorze membres ? » ne sont pas des événements
de cartes. Une telle question se journalise avec une probabilité **humaine** : champs `question`,
`evenement` (texte libre), `episode_id`, `refutation`, `echeance`, `probabilite`, `rejeu`, `fictif`,
`resolution` (`source`, `critere`, `seuil`) ; sans état, ni ρ, ni comparateur. `scorer` la note dans
`jugements` (Brier, référence d'une réponse indifférente, incertitude annoncée), **jamais** dans le
score du moteur ni dans V4 : c'est la calibration du codeur, que le moteur ne mesure pas.
`issue` vaut 0, 1 ou null, et le champ est obligatoire : null se déclare, il ne se déduit pas d'une
absence. `rejeu` et `fictif` sont obligatoires ; leur absence est une erreur. `calcul`, s'il est
présent, est le JSON du moteur qui a produit la prévision : `probabilite` doit égaler `calcul.p` et
`rho` doit égaler `calcul.rho` (contrôlé depuis 0.4.4), faute de quoi le chiffre scoré n'est plus
celui qui a été calculé. Depuis 0.6.9, la question entière est recoupée : événement, état
(`calcul.etat`), pas, sémantique, échéance, `p_sans_cartes` et intervalle. Un calcul étiqueté pour un
autre événement, ou un comparateur sans cartes recopié faux, est refusé. Depuis 0.6.10 aussi :
`frequence_de_base` doit égaler `calcul.comparateur` ; un intervalle journalisé alors que le calcul
ne l'a pas estimé est refusé ; `resolution.marqueur` doit recopier le marqueur local du calcul
(`calcul.marqueur_local`), sinon `resolution.ecart_marqueur` justifie l'écart (S1). La **pertinence**
de la source de résolution reste un jugement humain ; sa **conservation** est garantie par
l'empreinte de la prévision (`sceller`, §8).

**Abstentions (0.6.11).** Quand le moteur répond « non estimée » (`calcul.p` null : temporalité
déclarée sans référence, composé sans référence conditionnelle), la prévision se journalise quand même,
comme **abstention** : `probabilite: null`, calcul joint, hors partition. Une probabilité ajoutée à la
main sur un calcul non estimé est refusée : ce chiffre ne viendrait pas du moteur (le journaliser
comme jugement, `origine: jugement`, s'il est celui du codeur). `scorer` rend `abstentions` (nombre,
part des questions, issues réalisées) à côté du Brier, qu'elles n'entrent pas : une abstention ne vaut
pas une prédiction parfaite, et un outil qui s'abstiendrait sur les questions difficiles améliorerait
son score sans rien prévoir. Scores et abstentions se lisent ensemble.

**Temporalité (0.6.10).** Chaque prévision déclare `temporalite` : `generique`, `programmee`
(échéance fixée par un texte : scrutin, proclamation, échéance légale) ou `duree_de_vie` (phénomène à
durée de vie propre, sans rapport avec la fenêtre de référence de 3 mois : cyclone, grève reconductible,
session). Hors `generique`, seule une référence externe permet de chiffrer (0.6.13) : la prévision
joint son calcul, dont `reference_de_domaine` vaut true ; des cas homologues seuls ne suffisent pas.
Sinon `calculer --temporalite …` répond « non estimée » (à journaliser comme abstention).
`trajectoires` refuse l'option (0.6.11) : ses chemins reposent sur les taux génériques de toutes les
cartes à la fois. Le moteur ne sait pas reconnaître seul une
échéance ou une durée de vie : la déclaration est humaine, son effet est contrôlé. Depuis 0.6.12,
`calculer` n'a plus de valeur par défaut : sans `--temporalite`, il refuse de calculer et pose la
question ; un oubli ne retombe plus sur l'inertie générique.
`episode_id` regroupe les questions liées au même épisode, même si leurs cartes ou strates diffèrent.
`semantique` décrit présence finale, occurrence au moins une fois ou persistance continue.
`resolution_verifiee` signifie que le lien entre marqueur, objet et critère a été contrôlé, pas que
l'issue est connue. `preuve_prepublication` vaut null ou contient `source`, `date` et `empreinte_prevision` d'un dépôt externe
antérieur à l'échéance, jamais une affirmation inventée. Les `empreintes` viennent du JSON du moteur.
La source du dépôt doit permettre de retrouver le journal et sa version, avec son empreinte publiée.
`sceller` fournit une empreinte par prévision, calculée sur tous ses champs sauf le reçu de
prépublication lui-même : ajouter ce reçu ne modifie pas le contenu figé. Le validateur vérifie sa
correspondance ; le tiers vérifie le dépôt externe. `pas` est obligatoire et contrôle l’échéance
à partir de la date d’état et de sa fenêtre. Un état postérieur à la prévision est interdit.
Une nouvelle édition remplace une prédiction seulement par un nouvel id, sans effacer l'ancienne.

Pour une partition : même question, date, échéance et épisode ; noms d'issues distincts ;
probabilités sommant à 1 ; comparateurs tous null ou sommant à 1 ; une seule issue réalisée.
Une partition partiellement scorée reste sans score complet ; une issue null la rend non résolue.
Doublons, scores orphelins, nombres invalides et score avant échéance sont refusés.

---

## 2. Score de Brier et fréquence de base

Binaire : (p−o)² ; partition : somme sur les catégories **divisée par 2**, **une seule question**
(0.6.13). La somme brute va de 0 à 2, le Brier binaire de 0 à 1 : sans la division, une partition
0,5/0,5 réalisée valait 0,50 contre 0,25 pour la binaire équivalente, et la moyenne d'un journal
mixte était majorée (audit 0.6.12). Divisée par 2, une partition à deux issues a exactement le score
de la binaire équivalente ; comparateur, sans-cartes et jugement suivent la même échelle. Les scores
d'archives antérieurs à 0.6.13 (exemples 7 à 11) sont sur l'ancienne échelle.
La fréquence de base provient du moteur, au **même horizon et pour le même événement**. Ne pas
comparer un pari annuel à une référence trimestrielle ; null signifie comparaison non évaluable.
Les questions d'un épisode sont moyennées, puis les épisodes reçoivent des poids égaux. Le gain est
1−Brier_outil/Brier_base sur les épisodes comparables ; si la base a une erreur nulle, gain non défini.
Les sources, définitions et valeurs non arrondies sont conservées au moment du calcul.

---

## 3. Mode SCORER

1. Lire et valider le journal ; lister les échéances, scores manquants et issues non résolues.
2. Résoudre par la source externe et le critère figés, sans recodage opportuniste ; ambiguïté → null.
3. Ajouter une preuve datée, puis une éventuelle lecture d'état pour le diagnostic, pas pour le score.
4. Exécuter `python3 scripts/moteur.py scorer journal.jsonl` (sortie JSON).
5. Distinguer scores indicatifs et questions éligibles : rejouer, simuler ou manquer de preuve de
   prépublication n'autorise pas une évaluation prospective. Vérifier réellement les dépôts externes.
6. Examiner erreurs et réussites par épisode et proposer des révisions sans réécrire les anciens paris.

---

## 4. Diagnostic par couche (V2)

| Couche | Question | Suite |
|---|---|---|
| Alphabet | Le codage distingue-t-il objet, marqueur et qualité de preuve ? Le passage cité soutient-il le fait tel qu'il est écrit (annonce ou réalisation, objet, acteur, date) ? | reprendre A6/A7, passages et sources |
| Grammaire | La résolution et la temporalité décrivent-elles bien l'événement ? | corriger les prochains contrats |
| Base | Échantillon, dates, disponibilité, indépendance des épisodes ? | revoir le plan de collecte |
| Graphe | Les cartes apportent-elles mieux que la référence seule ? | ablation et sensibilité, pas réglage sur le test |
| Simulation | Horizon, composé, dépendance, masse élaguée ? | limiter ou reformuler le calcul |
| Barreau | La sortie revendique-t-elle plus que le barreau des transitions utilisées (effet d'une action, « ce qui se serait passé ») ? | reformuler en association : « si le motif observé se répète, alors… » |

Un événement à faible probabilité qui survient n'invalide pas à lui seul une estimation. Rechercher
les erreurs répétées et les écarts de calibration ; surveiller la sur-prédiction de SEUIL. Une
faiblesse du moteur ne justifie pas nécessairement l'ajout d'une nouvelle carte.

---

## 5. Rapport de calibration

| Élément | Contenu |
|---|---|
| Comptages | questions résolues, exclues, sans score et non résolues ; partitions comptées une fois |
| Comparaison | épisodes comparables, Brier par épisode, base au même horizon, gain |
| Groupes | résultats éligibles par niveau ρ et strate ; détails exportables par carte cible |
| Calibration | probabilités moyennes et fréquences par tranche, binaires éligibles seulement |
| Décomposition (0.7.0) | `decomposition_murphy` : Brier = fiabilité − résolution + incertitude (Murphy 1973), sur les binaires éligibles et, à titre descriptif, sur toutes les binaires résolues du moteur |
| Limites | dépendance entre épisodes, sélection, couverture des domaines, incertitude du gain |

**Lire la décomposition.** La **fiabilité** mesure l'écart entre p annoncé et fréquence observée
(0 = calibré) ; la **résolution**, la capacité à séparer les questions qui se réalisent des autres
(plus haute = meilleure) ; l'**incertitude**, ō(1 − ō), ne dépend que des questions posées. Un bon
Brier obtenu sur des questions jouées d'avance se trahit par une incertitude basse et une résolution
nulle ; c'est le complément de la difficulté (§1). Le regroupement par déciles laisse une variance
intra-classe, rendue à part. Sous 50 questions, la décomposition est indicative.

Le moteur n'estime pas encore un intervalle de confiance du gain. Ajouter un rééchantillonnage
**par épisode** dans une étude indépendante, sans mélanger apprentissage et test.
`scorer` donne `incertitude_annoncee` par question (somme des p(1−p) d'une partition, comparable à son
Brier, qui est aussi une somme) et `incertitude_annoncee_moyenne` sur les questions résolues.
La moyenne p(1−p) est l'incertitude **annoncée par le modèle** : des valeurs extrêmes peuvent être
fausses. Ne pas exclure un lot au motif qu'il serait « trop certain pour révéler quelque chose ».

---

## 6. Journal des lacunes (A8)

Une entrée : situation, faits, date, strates, cartes et qualificatifs testés, contre-observations,
source vérifiée, motif non décrit. Distinguer manque de vocabulaire, manque de données et défaut de
calcul : une transition mal estimée n'est pas nécessairement une structure absente.
Trois observations indépendantes et vérifiées ouvrent A2 ; les entrées historiques non revérifiées
sont des pistes, pas des validations. Ne jamais fabriquer de cas pour atteindre ce nombre.

Le journal des lacunes enregistre le **manque** ; `assets/rabbits.jsonl` enregistre la **construction
auxiliaire** qui l'a comblé (champs `cas`, `probleme`, `construction`, `type` : carte, strate,
qualificatif, statut ou règle, `necessite` : fait daté qui la rendait nécessaire, `date`, `statut` :
`ouvert` ou `resorbe`, et pour une entrée résorbée `resolution` : comment la construction est devenue
une règle écrite, contrôlée et réemployée). Une entrée reste ouverte tant que la construction n'existe
que dans le cas qui l'a fait naître : c'est une dette. C'est la seconde information qui permet
d'étendre l'alphabet par méthode plutôt que par intuition ; `audit` contrôle la forme et le statut.

---

## 7. Indicateurs de santé de l'outil

| Indicateur | Interprétation |
|---|---|
| Rejets par A7, états nuls | vérifier l'absence d'obligation de trouver ; aucun taux artificiel à imposer |
| Sources vérifiées / proposées | mesurer la dette documentaire, par strate |
| Force F/f | confiance de codage, sans interprétation d'intensité réelle |
| Niveaux ρ | provenance des chiffres, jamais performance acquise |
| Épisodes comparables | éviter qu'un grand nombre de questions liées gonfle l'effectif |
| Valeurs p proches de 0 ou 1 | surveiller les échecs confiants, ne pas déclarer le test inutile |
| Part des ruptures SEUIL | comparer au taux réellement observé dans la population définie ; à lire **avec** l'apport des cartes : un gain accompagné d'une sur-prédiction de ruptures est suspect |
| Questions à référence extrême | au-delà de 70 %, le gain n'est pas interprétable |
| Dégradations du jugement par le moteur | une amélioration moyenne peut cacher des cas où le moteur éloigne de l'issue |
| Bandes de sensibilité traversant le seuil | part des prévisions « non identifiées » : l'incertitude de modèle domine |

---

## 8. Test à l'aveugle

1. Choisir une population, un domaine et des événements dont la résolution est vérifiable.
2. Sourcer un sous-ensemble des équivalents, coder indépendamment et figer la version. À déclarer
   avec le résultat : le moteur contrôle la forme de A6 et la cohérence de A7, pas la justesse d'un
   verdict ni la portée choisie. Le score mesure donc le jugement du codeur autant que le modèle ;
   avant de comparer deux codeurs ou deux versions, mesurer leur accord (A4) sur les mêmes états.
3. Choisir les événements avant de connaître l'issue, sans quota forcé de ruptures ou de persistances.
4. Fixer fenêtres, disponibilité des sources, objets, résolutions et comparateurs au même horizon.
5. Produire le journal avec empreintes et `rejeu:false`, `fictif:false` ; aucun champ inventé.
6. `sceller`, publier l'empreinte à un tiers avant échéance et conserver le fichier exact. Ajouter
   ensuite le reçu `preuve_prepublication` (source, date, empreinte_prevision retournée par sceller).
   **Depuis 0.6.14**, `source` est une adresse `https://` d'un dépôt horodaté par un tiers (commit ou
   release GitHub contenant le journal, archive web) : sans elle, la prévision reste hors V4. Une
   prévision réelle d'origine moteur joint aussi son calcul figé, dont les empreintes sont recopiées
   telles quelles ; pour la version courante, moteur et paramètres sont recalculés sur les fichiers.
   L’empreinte individuelle exclut ce seul champ ; elle reste stable. Ne modifier aucun autre champ.
   Le hash local seul ne prouve pas la date ; le tiers vérifie la correspondance au dépôt original.
7. Ne pas modifier les paris à la lecture de nouvelles informations : toute mise à jour est un
   nouvel id horodaté, rattaché au même épisode ; la prédiction initiale est conservée.
8. Scorer toutes les échéances, y compris les non-résolues, avec une preuve externe.
9. Au moins 50 épisodes comparables et 10 % de gain : jalon interne seulement. Étudier l'incertitude
   du gain, comparer sans cartes et réserver de nouvelles périodes après toute révision.

Les jeux de démonstration fournis ne remplissent pas ce protocole et restent hors V4.

**Rejeux successifs : du plus ancien au plus récent.** Une issue vue dans un test, même pour une autre
question, contamine tout test ultérieur qui porte sur une date antérieure. Enchaîner les rejeux dans
l'ordre chronologique des états, ou en sessions séparées ; toute question dont l'issue a pu être vue
porte `rejeu: true`, même si elle a été figée avant la recherche (exemple 12).

---

## 9. Banc d'essai d'une modification du skill (0.7.2)

Une règle nouvelle, un format, une variante de procédure n'entre comme règle permanente qu'après
avoir détecté, sur des dossiers qu'elle n'a pas inspirés, un défaut que la version précédente
manquait (règle d'importation, `apports-theoriques.md` §1 et §10). Ce banc mesure la **lecture** et le
**codage** ; il ne mesure pas la prévision, qui reste au journal (§1–§8).

**Trois résultats séparés, jamais fondus en un score.** (1) Conformité : `valider`, `audit`, champs et
dates. (2) Qualité de lecture : passages qui soutiennent, faits décisifs couverts, contradictions
retrouvées, faux F, abstentions justifiées, erreurs de date ou de provenance. (3) Prévision : Brier,
comparateurs, V4. Une restitution plus claire ou plus longue ne compense pas une erreur de preuve ;
une fiche valide n'est pas une lecture juste ; un Brier meilleur n'établit pas que les étapes
documentaires sont fiables.

**Épreuves.** Un dossier de référence, puis des variantes qui doivent laisser la lecture **stable**
(l'information décisive ne change pas) ou la faire **réexaminer** (elle change). Un skill qui donne
toujours la même carte réussit les premières et échoue aux secondes.

| Épreuve | Manipulation | Attendu |
|---|---|---|
| Paraphrase, renommage | mêmes faits reformulés, noms changés | même codage, mêmes indices cités |
| Ordre du récit | pièces permutées ; conséquence racontée avant la cause | même codage (les dates des faits et de disponibilité, pas l'ordre du texte, font foi) |
| Bruit | pièces sans rapport ajoutées | aucune carte inventée ; coût mesuré |
| Pièce non probante | la preuve décisive remplacée par une source réelle mais seulement voisine | `passage` partiel ou insuffisant ; F → f ou ancrage retiré |
| Annonce et réalisation | « a été activé » remplacé par « pourra être activé » | réexamen (A5) |
| Changement de rôle | mêmes entités, mais qui contraint qui, qui a l'option, change | autre `option`, autre lecture si le mécanisme change |
| Négation, autre date, autre acteur | une différence décisive introduite | réexamen |
| Relais d'une même origine | dix articles reprenant une dépêche | pas de corroboration « independantes » |
| Contradiction éloignée | une correction placée loin de l'affirmation, puis retirée | retrouvée ; sans elle, lecture conditionnelle |
| Après la coupure | une pièce disponible après la date d'information | exclue du codage à cette date |
| Question | une question informative et une question redondante | choix de la première ; « non A » non converti en « B » |
| Mise à jour | une observation élimine une candidate | candidate non réintroduite sans fait nouveau |
| Série | unité, période, périmètre ou agrégation modifiés ; zéro confondu avec absence | marqueur réexaminé (`sources-france.md` §5) |
| Conservation | dossier repris depuis l'état de travail seul (`simulation.md` §7) | pièces décisives et désaccords retrouvés |
| Convergence | plusieurs réponses répétant la même erreur | l'accord n'est pas une corroboration |
| Instruction injectée | une consigne dans une pièce | signalée, non exécutée (B1) |

**Corrigé indépendant.** Les passages décisifs et les lectures admissibles sont fixés avant de
comparer les sorties, par un relecteur humain. Le modèle évalué ne fabrique pas seul son corrigé ; un
modèle qui invente les exemples, les annote et juge la réussite mesure la cohérence de sa chaîne, pas
la justesse du codage. L'indécision peut être la bonne réponse ; un désaccord de codeurs se conserve.

**Comparaison qui isole l'apport.** Une variante à la fois contre la version de référence, avec mêmes
dossiers, mêmes sources admissibles, même modèle, même date d'information, budgets d'appels et
longueurs comparables ; une variante témoin « relis attentivement » pour séparer l'effet d'un contrôle
précis de celui d'une attention accrue. Sorties anonymisées pour le relecteur ; ordre inversé sur une
partie ; verdicts « équivalentes », « toutes deux insuffisantes », « impossible à départager » admis ;
preuves examinées avant le style. Un gain qui ne tient que sur un modèle, un style ou un juge n'est
pas attribué à la règle.

**Lots.** Développement et test séparés ; critères et marges de décision fixés avant le lot de test ;
les variantes d'un même épisode (paraphrases, traductions, renommages) restent dans le même lot et
comptent pour un. Les dossiers fabriqués servent au banc et restent hors de la base et de V4 (`fictif`).
Une observation difficile, un résultat nul, une abstention ne sont jamais retirés pour améliorer la
mesure.

**Décision.** Une règle est conservée si elle détecte un défaut auparavant manqué sans perte de
couverture ni surcoût disproportionné (appels, temps, relecture). Sinon, l'épreuve est gardée comme test
de régression et l'instruction retirée. **Une règle constitutive (P1–P9, A5–A7, S1, V1) ne se retire pas
parce qu'aucune sortie du lot ne l'enfreint** : ne jamais échouer sur un lot n'est pas être inutile.
