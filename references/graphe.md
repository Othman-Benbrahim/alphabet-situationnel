# Alphabet situationnel — Graphe de transitions (couche 4)

> Version : 0.6.15

> Procédure expérimentale. Le moteur produit les chiffres et le JSON ; l'interprétation des sources
> et des objets reste à vérifier. Règles : T1–T6 ; paramètres : `protocole.md` §H.

---

## 1. Événements (T1)

| Type | Commande | Sens |
|---|---|---|
| Apparition | `X@s apparait` | absent maintenant, présent à la prochaine observation |
| Persistance | `X@s persiste` | présent maintenant et à la prochaine observation |
| Disparition | `X@s disparait` | présent maintenant, absent à la prochaine observation |
| Transformation | `X@s se transforme` | même objet qui change de forme et persiste ; référence conditionnelle nécessaire |
| Intensification | `X@s s'intensifie` | grandeur mesurée augmente et objet persiste ; référence conditionnelle nécessaire |
| Ancien f ↔ F | `se renforce`, `s'affaiblit` | refusé en prévision : révision de la qualité d'ancrage |

Les critères de résolution sont définis avant calcul et mesurent l'objet et le marqueur concernés.
Ils ne sont pas choisis après avoir vu l'issue ou pour rendre la prévision plus favorable.

---

## 2. A priori p₀ (T2)

### 2.1 Sources et multiplicateurs hypothétiques

Les sources viennent de la matrice de `dynamiques.md`. Les λ 3 / 1,8 / 1,2 sont des hypothèses de
travail, non des rapports de vraisemblance mesurés. Même strate : valeur de la table. Autre strate :
abaissement d'un cran, sauf propagation explicitement admise ou transfert ancré. Sources liées par
inclusion, renforcement ou transfert : garder la plus forte, pour limiter le double comptage.
*Bouge* multiplie le λ de la source par 1,5 ; *manque* ajoute une source moyenne. Le produit est
plafonné à 10. Ces règles ne démontrent ni causalité ni indépendance ; elles sont à comparer au
modèle `--sans-cartes`. Ce dernier désactive également les homologues : il mesure l'apport conjoint
de la modulation et de la sélection structurelle, pas l'effet isolé d'un seul mécanisme.
Les effets inhibiteurs ne sont pas estimés dans cette version ; ne pas en inventer.

**Portée des cartes.** Les multiplicateurs ne s'appliquent qu'aux **apparitions**. Sans base de cas,
la probabilité d'une persistance ou d'une disparition ne dépend que de l'inertie de la carte : une
telle question ne teste pas la lecture structurelle, quel que soit son score. `calculer` imprime donc
à côté de p la probabilité sans cartes, et le journal la conserve (`p_sans_cartes`, `validation.md`
§1). Pour éprouver la lecture, préférer des apparitions, ou des persistances sur une base où les
homologues diffèrent des transitions non homologues.

### 2.2 Fréquence de référence f

La fréquence est spécifique à **un événement et une fenêtre**. Une référence externe comporte source
consultée, définition, période, fenêtre, date de disponibilité. Exemple de fichier de références
externes, fourni par l'utilisateur et passé à `--references` (aucun fichier de ce nom n'est livré ;
ne pas le confondre avec `assets/parametres.json`) :

```json
{
 "POL@7 persiste": {"frequence": 0.85, "source": "SOURCE À REMPLACER PAR UNE RÉFÉRENCE VÉRIFIÉE", "definition": "les deux blocs restent présents", "periode": "période de la série", "fenetre": "3 mois", "disponible_le": "2026-10-01"},
 "POL@7 hausse|persiste": {"frequence": 0.2, "source": "SOURCE À REMPLACER PAR UNE RÉFÉRENCE VÉRIFIÉE", "definition": "hausse de la mesure parmi les épisodes où la polarité persiste", "periode": "période de la série", "fenetre": "3 mois", "disponible_le": "2026-10-01"}
}
```

Ces nombres sont **fictifs**, pas des références prêtes à l'emploi. Les clés utilisent les
abréviations canoniques. Pour la transformation : `RES@7 transformation|persiste` par exemple.
Aucune fréquence scalaire n'est partagée entre deux composantes. Pour un événement simple seulement,
`--fref` est un raccourci avec `--source-ref`, `--periode-ref`, `--disponible-ref` obligatoires.
Le moteur contrôle les champs et dates ; l'existence et la pertinence de la source sont humaines.

Base disponible : chaque cas se partage un poids total ≤1 entre ses transitions éligibles, puis
pondération par l'âge. f = (succès pondérés + k₀ × référence) / (poids total + k₀).
Référence : externe si fournie ; sinon défaut de 5 % sur 3 mois pour une apparition ou inertie pour
une persistance. Sans source externe, l'ancrage demande un effectif pondéré ≥ n_min (10).
Les dates d'issue **et de disponibilité des preuves** sont antérieures ou égales à la date d'information.

### 2.3 Combinaison

**Sensibilité (0.6.0).** Le moteur compte une centaine de paramètres non calibrés pour quelques cas :
le système est sous-déterminé, une infinité de jeux de paramètres reproduisent les cas connus et
divergent sur le suivant. `calculer` relance donc chaque calcul sous six variantes (multiplicateurs
d'un cran plus bas et plus haut, inerties − 0,05 et + 0,05, fréquence par défaut × ½ et × 2) et
imprime la bande obtenue. Elle mesure l'incertitude de **modèle**, que l'intervalle bêta (bruit
d'échantillonnage) ne couvre pas. Si la bande traverse `seuil_decision` (§H, 50 %), la ligne S5
écrit « non identifié » : le sens de la réponse dépend d'hypothèses non calibrées. **Bande large
(0.6.5)** : indépendamment de tout seuil, une bande plus large que `largeur_max_affichage` (§H, 30
points) est signalée (`bande_large`) ; une bande de 10 à 45 % ne traverse pas 50 % mais ne permet
aucune lecture. **Portée** : les six variantes déplacent tous les paramètres d'un même type ensemble.
C'est une sensibilité *paramétrique globale*, pas une incertitude *structurelle* : une seule transition
fausse parmi les 66 de la matrice déplacerait à peine la bande, et le modèle serait faux quand même.
Une bande étroite ne dit donc pas que la matrice est juste. Sur l'exemple 1,
la bande (19–28 %) est plus étroite que l'intervalle bêta (5–43 %) : pour ce calcul, l'incertitude
d'échantillonnage domine celle des hypothèses.

```
p₀ = f × LR / (1 − f + f × LR)
```

0 et 1 sont traités sans division par zéro ; aucune entrée hors [0,1] ou non finie.
Persistance à défaut : r = inertie^(durée / 91,3125 jours). En position *bouge* : r^1,5.
Disparition : complément de la persistance, sauf référence explicitement propre à la disparition.
Le moteur distingue ces événements ; il ne réinterprète pas une fréquence de disparition comme une
fréquence de persistance. L'échelle de risque décrit la provenance et n'atteste aucune calibration.

**Plafond (0.6.9).** `plafond_p0` (§H, 95 %) borne l'effet des cartes, pas la fréquence : il ne
s'applique que si les multiplicateurs élèvent p au-dessus de la fréquence f, et jamais sous f. Avant
0.6.9, il s'appliquait à toute probabilité : une persistance d'inertie à 99,5 % sur 7 jours tombait à
95 % sans que son complément bouge (somme 96,2 %), et 7 pas quotidiens plafonnés donnaient 0,95⁷ ≈ 70 %
pour la même question (audit du test brésilien, octobre 2026). Propriétés désormais vérifiées par
autotest : persistance et disparition somment à 1 ; la persistance et l'apparition sans
multiplicateur ne dépendent pas du découpage temporel. **Limite connue** : avec multiplicateurs,
l'apparition dépend légèrement du découpage (SEUIL@7 sur 3 mois : 10,2 % en un pas, 10,4 % en 13 pas
hebdomadaires), parce que λ multiplie la cote et non le taux ; avec une base de cas, dont les fréquences
sont observées à la fenêtre des cas, l'invariance ne peut pas tenir. Calculer à la fenêtre de la question.

### 2.4 Un événement sur plusieurs pas

Soient a l'apparition par pas et r la persistance par pas. Sources et paramètres supposés fixes.

| Question temporelle | Calcul |
|---|---|
| Absent au départ, présent à h | q₀=0 ; qₜ₊₁=qₜr+(1−qₜ)a |
| Présent au départ, présent à h | même chaîne avec q₀=1 |
| Apparition au moins une fois | 1−(1−a)^h |
| Persistance continue | r^h |
| Disparition au moins une fois | 1−r^h |
| Absence à l'échéance depuis un état présent | 1−q_h |

`--semantique presence`, `continue` ou `au-moins-une-fois`, selon l'événement. Défauts : presence
pour apparition, continue pour persistance, au-moins-une-fois pour disparition. À un pas, le modèle
observe les états aux bornes ; il ne détecte pas un changement transitoire à l'intérieur de la fenêtre.
La fréquence de base est propagée avec **la même formule** ; si une composante de référence manque,
le comparateur est non évaluable. Le niveau ρ hérite des composantes réellement utilisées.
Aucun intervalle multi-pas : propager seulement les bornes d'une composante ignorerait les autres.
Composés : un pas seulement, sinon erreur explicite.

---

## 3. Cas homologues (T3)

### 3.1 Unité de comptage

Une transition relie deux états espacés d'une fenêtre calendaire exacte. Un cas avec dix transitions
ne pèse pas dix cas : poids de chaque transition = pondération d'âge / nombre de transitions
éligibles de ce cas dans le lot. n_A et n_E sont les sommes pondérées ; c_A est le nombre de cas.
Cela limite la pseudo-réplication mais ne prouve pas l'indépendance entre cas ; des épisodes liés
peuvent nécessiter un regroupement supplémentaire. Dates et preuves futures sont exclues aussi de f.

### 3.2 Échelle de similarité

| Niveau | Condition |
|---|---|
| H1 | mêmes cartes, mêmes F/f, mêmes qualificatifs ; état non vide |
| H1.5 | Jaccard pondéré de toutes les cartes (F=1 ; f=0,5), ≥0,7 et intersection non vide |
| H2 | toutes les sources non vides de l'événement présentes |
| H3 | sources et cible traduites dans une autre strate, tous équivalents vérifiés |

Retenir le niveau le plus strict qui atteint 3 cas distincts (`c_min_rho1`) ; sinon le plus strict
non vide. Raison : H1 ⊆ H1.5, si bien que la règle de 0.4.0 (« le niveau qui offre le plus de cas »)
ne retenait jamais H1 sous 30 cas et échangeait la comparabilité contre l'effectif sans le dire. Le prix
est un intervalle plus large ; il est affiché. Une pondération continue par la similarité (le Jaccard
pondéré est déjà calculé) serait plus cohérente encore ; elle est différée faute de données pour en
fixer la forme. H3 seulement sans homologue local. Deux ensembles de mots forts vides ne créent plus H1.
Cette similarité ne code pas l'identité des objets, les positions ou les liaisons ; l'utilisateur doit
examiner la pertinence des cas retenus. Les transitions, dates, issues et poids figurent dans le JSON.

---

## 4. Révision (T3)

P = (n_E + k × p₀)/(n_A + k), k=2. La loi bêta de paramètres n_E+k p₀ et n_A−n_E+k(1−p₀)
fournit des quantiles 10–90 % seulement si les deux paramètres sont positifs et n_A>0.
Intervalle **conditionnel approximatif** : ni le codage, ni les λ, ni le choix de modèle n'y sont
incertains. Le nombre de cas n'est pas une preuve de calibration. Sans cas ou loi dégénérée : null.
Les seuils ρ sont définis par T3 ; double codage insuffisant, absence de cas sans événement et
non-stationnarité empêchent ρ0. Les sources de référence et les cas sont versionnés.

---

## 5. Emprunt entre strates (T4)

Exiger des équivalents Documentés/Attestés des cartes sources **et de la cible** dans les deux
strates. Les équivalents non sourcés livrés en 0.4.0 ne permettent aucun emprunt. Après documentation,
le poids w=0,5 reste une hypothèse à tester, et non une garantie de transportabilité. Un emprunt ne
remplace pas une observation du domaine cible ; le signalement ρ2 est obligatoire.

---

## 6. Plusieurs événements pour une même question (S1)

Les événements binaires séparés ne somment pas nécessairement à 1. Une partition comporte des issues
exclusives et exhaustives ; sa somme et celle de son comparateur doivent valoir 1, avec exactement
une issue réalisée. Le scoreur compte la partition comme **une question**. Ne pas fabriquer une
partition par multiplication de marginales : la dépendance doit être modélisée ou une distribution
jointe externe justifiée doit être fournie. En l'absence de modèle joint, conserver les binaires.
Le moteur ne propose pas de génération automatique de partitions arbitraires. Tous les résultats
et leur comparateur doivent porter sur le même horizon et la même définition de résolution.

---

## 7. Exemple chiffré, reproductible

```bash
python3 scripts/moteur.py calculer --demo --base assets/base-de-cas.exemple.jsonl \
  --etat "[2026-09 | 3 mois] POLARITÉ@7[F] + CONTRAINTE@6[F]" \
  --evenement "SEUIL@7 apparait" --liaison "CONTRAINTE@6 echo POLARITÉ@7" --temporalite generique --json
```

Base entièrement fictive. Les sorties courantes, régénérées avec le moteur livré, figurent dans
`exemples.md`. Pour une comparaison à quatre pas : ajouter `--pas 4 --semantique presence` ; le
comparateur est lui aussi porté à quatre pas, ou null s'il n'est pas estimable. Aucun ancien chiffre
0.3.x n'est présenté comme une sortie de la nouvelle version.

Pour un composé, fournir également `--resolution resolution.json` : objet, source, critère, seuil,
marqueur ; pour l'intensification, grandeur, unité, comparaison et `observations` sous la forme
`[{"date":"2026-08-01","valeur":10},{"date":"2026-09-01","valeur":12}]`. Ce sont les observations
connues au départ, pas les valeurs futures de résolution. La comparaison future est figée en texte.
