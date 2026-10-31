# Alphabet situationnel — Glossaire

> Version : 0.5.1

> Un terme, un sens. Le mot « niveau » est réservé à trois usages, toujours qualifiés : *niveau de
> risque* (ρ), *niveau d'homologie* (H1–H3), *niveau 2* de la taxonomie (disciplines). La force d'un
> ancrage (F / f) ne s'appelle pas « niveau ».

| Terme | Définition | Où |
|---|---|---|
| A priori (p₀) | probabilité d'un événement avant les cas : fréquence de référence modulée par la structure | T2, `graphe.md` §2 |
| Ancrage | fait de la situation qui remplit un marqueur d'une carte dans une strate | A1, A5 |
| Anti-résonance | recherche de la contre-observation la plus forte, qui peut rejeter une carte | A7 |
| Base de cas | fichier `base-de-cas.jsonl` tenu par l'utilisateur, une fiche par ligne | couche 3 |
| Carte | l'une des 16 structures de l'alphabet, inspirée de structures mathématiques, sans universalité prédictive établie | `cartes.md` |
| Cas distincts (c_A) | nombre de cas d'où proviennent les transitions homologues ; fonde le niveau de risque | T3 |
| Classe de référence externe | fréquence publiée d'un phénomène défini de la même façon, citée, qui ancre l'a priori sans base | T2 |
| Couche | l'un des sept étages de l'outil (0 ontologie à 6 validation) | `constitution.md` §4 |
| Enchevêtrement | liaison entre ancrages de strates différentes : transfert, écho, conflit | G3 |
| Équivalent | traduction locale d'une carte dans une strate, avec son marqueur local et son statut | `equivalences/` |
| État | phrase datée : ensemble des mots ancrés dans une fenêtre | G2 |
| Événement | apparition, persistance, disparition, transformation ou intensification mesurée ; f↔F est une révision de confiance ; objet d'une prévision | T1 |
| Fenêtre de référence | 3 mois : durée pour laquelle sont définies la fréquence par défaut, les inerties ; le moteur ramène ces probabilités à la fenêtre de l'état | T2 |
| Force d'ancrage | qualité de l'ancrage : F (Fort), f (Faible) ou Nul ; distincte de l’intensité réelle et du statut de l'équivalent | A6, A3 |
| Fréquence de base | proportion des transitions où l'événement s'est produit, quel que soit l'état de départ ; « concurrent paresseux » du score | T2, V1 |
| Homologie (H1, H1.5, H2, H3) | similarité des cartes (y compris faibles), exacte ou pondérée ; H1 interdit aux états vides | `graphe.md` §3 |
| Inertie | probabilité a priori qu'une carte reste ancrée au pas suivant | `dynamiques.md` |
| Intervalle | intervalle bêta conditionnel approximatif à 80 %, sans incertitude totale de codage/modèle | T3 |
| Liaison | relation qualifiée entre deux mots d'un même état | G3 |
| Marqueur | fait type qui ancre une carte : abstrait (noyau) ou local (équivalent) | `cartes.md`, `equivalences/` |
| Mode solo | moins de 20 % ou moins de 20 cas double-codés dans la strate : ρ0 inaccessible | A4 |
| Mot | carte ancrée dans une strate, avec sa force : `SEUIL@7[F]` | G1 |
| Niveau de risque (ρ0–ρ4) | provenance d'une prévision : cas, emprunt, a priori ancré ou non ; ne mesure pas sa calibration | S4 |
| Noyau à risques concurrents | modèle des trajectoires : statu quo ou un seul changement par pas | S3 |
| Partition | ensemble d'issues incompatibles par construction ; seule situation où l'on somme à 100 % | S1 |
| Pas | durée d'une fenêtre d'état ; unité de l'horizon | S2 |
| Positions | *tient*, *bouge*, *manque*, pour un état d'au moins trois mots | G4 |
| Prévision binaire | événement prévu seul, sans somme à 100 % avec d'autres | S1 |
| Proxémie | déroulé des suites possibles d'un état : événements sur plusieurs pas et trajectoires | S3 |
| Qualificatif | manière dont une structure se déploie : rétroaction, échelle, délai, multi-strate | G1 |
| Scellement | empreinte SHA-256 du journal publiée avant l'échéance, contre la réécriture | `validation.md` §8 |
| Multiplicateur hypothétique (λ, LR) | facteur par lequel une carte source multiplie la cote de l'événement | T2 |
| Résolution externe | source, critère et seuil qui décideront de l'issue d'une prévision sans recoder | S1, V1 |
| Rejeu | prévision calculée alors que l'issue était connue ; exclue de l'évaluation V4 | V1, `validation.md` §8 |
| Résultat nul (∅) | aucune carte ancrée : pas de prévision | A8 |
| Statut d'équivalent | Attesté, Documenté, Proposé, Vide | A3 |
| Statut de lecture | Descriptif, Spéculatif, Nul ; porte sur la lecture, pas sur les prévisions | `simulation.md` §2 |
| Strate | l'un des 13 registres où se rangent les faits (niveaux d'organisation, domaines, longue durée) | `strates.md` |
| Transition | paire d'états consécutifs d'un cas ; unité de comptage | `graphe.md` §3 |

La force F/f, l’intensité F/M/f d’une arête de la matrice et une grandeur physique sont trois notions
distinctes. Les deux premières ne fournissent pas une unité de mesure de la troisième.

