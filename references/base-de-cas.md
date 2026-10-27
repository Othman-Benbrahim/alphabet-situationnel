# Alphabet situationnel — Base de cas (couche 3)

> Version : 0.6.15

> Format, codage et contrôles. `valider` et `calculer` appellent le même validateur. Une base valide
> syntaxiquement n'est pas une base factuellement certifiée. Règles : B1–B5.

---

## 1. Rôle et constitution

La base contient des observations datées, sourcées et codées. Choisir les configurations **avant**
de connaître les issues, puis échantillonner les cas dans une population et une période définies,
y compris ceux sans événement. Une sélection de crises saillantes ne représente pas une fréquence.
Commencer par une strate et quelques événements opérationnels ; comparer la référence seule et le
modèle complet. Ne pas remplir artificiellement toutes les cases de l'alphabet.

Trois statuts : `actif`, admissible après contrôles ; `proposition`, recodage complet contrôlé comme
un cas actif mais dont les sources n'ont pas encore été lues (`sources_verifiees: false`,
`motif_proposition` requis), exclu des calculs ; `archive_a_revoir`, conservé mais exclu de tout
calcul et contrôlé seulement comme archive lisible. Une proposition devient active quand l'auteur a
lu ses sources : `sources_verifiees: true`, `statut_donnees: actif`. Les quatre fiches de
`assets/cas-reels.jsonl` sont des archives (0.6.8) : rejeux codés avant les règles courantes, conservés
comme trace ; leur témoignage original est dans `assets/cas-reels-originaux.jsonl` (`feuille-de-route.md`,
étape 2). Les 40 cas d'exemple sont fictifs et demandent `--demo`.

---

## 2. Fiche de cas

Exemple entièrement fictif, au schéma courant (JSONL : une ligne par cas) :

```json
{
  "id": "C-0041-S07",
  "version_regles": "0.6.0",
  "titre": "Cas fictif 1",
  "strates": [
    6,
    7
  ],
  "fenetre": "3 mois",
  "sequence": [
    {
      "date": "2005-04",
      "etat": "[2005-04 | 3 mois] CONTRAINTE@6[F] + POLARITÉ@7[F]",
      "mots": [
        {
          "carte": "POL",
          "strate": 7,
          "intensite": "F",
          "fait": "Fait fictif n° 1 remplissant un marqueur local de POLARITÉ (strate 7)",
          "source": "Source fictive n° 1 ; source fictive n° 1 bis, indépendante de la première (exemple construit)",
          "corroboration": "independantes",
          "contre_observation": "Contre-observation fictive (marginale)",
          "portee": "marginale",
          "a6": "POLARITÉ@7 : CONTRAINTE → (deux camps nommés, pas une règle qui retire des options) ; SEUIL → (aucun passage irréversible daté)",
          "garantie": {"mecanisme": "les deux blocs se définissent l'un par l'autre et organisent les votes", "attendu": "alignements exclusifs : rejoindre un bloc écarte de l'autre", "contredirait": "une troisième position stable ou des alignements croisés durables"},
          "option": {"acteur": "les États tiers", "avant": "rester non alignés", "apres": "choisir un bloc pour obtenir un soutien"},
          "objet": "objet simulé C-0001-GEO strate 7"
        },
        {
          "carte": "CTR",
          "strate": 6,
          "intensite": "F",
          "fait": "Fait fictif n° 2 remplissant un marqueur local de CONTRAINTE (strate 6)",
          "source": "Source fictive n° 2 (exemple construit)",
          "contre_observation": "Contre-observation fictive (marginale)",
          "portee": "marginale",
          "a6": "CONTRAINTE@6 : SEUIL → (options retirées, aucun nouvel état) ; HIÉRARCHIE → (règle, pas rang) ; POLARITÉ → (règle, pas deux pôles) ; INCERTITUDE → (option fermée, non laissée ouverte) ; TRACE·MÉMOIRE → (plafond décidé, pas héritage)",
          "objet": "objet simulé C-0001-GEO strate 6"
        }
      ],
      "questions": [
        {"question": "Les États tiers forment-ils un troisième groupe stable, hors des deux blocs ?", "si_oui": "RES@7", "si_non": "POL@7"}
      ],
      "liaisons": [],
      "positions": null,
      "disponible_le": "2005-04",
      "retraits": []
    },
    {
      "date": "2005-07",
      "etat": "[2005-07 | 3 mois] CONTRAINTE@6[F] + POLARITÉ@7[F] + RÉSEAU@6[f]",
      "mots": [
        {
          "carte": "RES",
          "strate": 6,
          "intensite": "f",
          "fait": "Fait fictif n° 4 remplissant un marqueur local de RÉSEAU (strate 6)",
          "source": "Source fictive n° 4 (exemple construit)",
          "contre_observation": "Contre-observation fictive (marginale)",
          "portee": "marginale",
          "objet": "objet simulé C-0001-GEO strate 6"
        }
      ],
      "liaisons": [],
      "positions": null,
      "retraits": [],
      "disponible_le": "2005-07"
    },
    {
      "date": "2005-10",
      "etat": "[2005-10 | 3 mois] CONTRAINTE@6[F] + HIÉRARCHIE@7[f] + POLARITÉ@7[F] + RÉSEAU@6[f]",
      "mots": [
        {
          "carte": "HIE",
          "strate": 7,
          "intensite": "f",
          "fait": "Fait fictif n° 6 remplissant un marqueur local de HIÉRARCHIE (strate 7)",
          "source": "Source fictive n° 6 (exemple construit)",
          "contre_observation": "Contre-observation fictive (marginale)",
          "portee": "marginale",
          "objet": "objet simulé C-0001-GEO strate 7"
        }
      ],
      "liaisons": [],
      "positions": null,
      "retraits": [],
      "disponible_le": "2005-10"
    }
  ],
  "issue": {
    "date": "2006-01",
    "etat": "[2006-01 | 3 mois] CONTRAINTE@6[F] + HIÉRARCHIE@7[f] + RÉSEAU@6[f]",
    "mots": null,
    "liaisons": [],
    "positions": null,
    "retraits": [
      {
        "mot": "POLARITÉ@7",
        "fait": "Fait fictif : POLARITÉ n'est plus observé (exemple construit)",
        "source": "Source fictive (exemple construit)"
      }
    ],
    "evenement_cle": "",
    "disponible_le": "2006-01"
  },
  "sans_evenement": false,
  "codage": {
    "mode": "manuel",
    "codeurs": [
      {"id": "codeur-1", "role": "humain"}
    ],
    "regle_declenchement": null,
    "accord": "exemple construit",
    "independants": false,
    "au_moins_un_humain": true
  },
  "usage": "test",
  "notes": "EXEMPLE CONSTRUIT — données fictives, ne pas utiliser pour prévoir",
  "fictif": true,
  "statut_donnees": "actif"
}
```

| Champ | Exigence |
|---|---|
| `id` | C-NNNN-SNN ; stable, fixé avant codage ; `id_legacy:true` seulement pour anciens identifiants conservés |
| `version_regles` | même version mineure que la version courante pour un cas actif (0.5.x en 0.5.0) ; un correctif ne force pas le recodage, car `valider` applique les règles courantes à chaque fiche ; ancienne version mineure conservée dans une archive |
| `strates` | entiers uniques 1–13, couvrant les strates de tous les états |
| `fenetre` | durée strictement positive ; même fenêtre dans toutes les phrases |
| `sequence`, `issue` | au moins un état avant l'issue, avec dates de fiche et de phrase identiques |
| `date`, `disponible_le` | date de l'observation, puis date réelle à laquelle ses preuves sont accessibles |
| `mots` | nouveaux mots, changements F/f ; premier état entièrement documenté ; null si aucun changement ; [] interdit |
| `objet` | périmètre concret de chaque mot documenté ; nécessaire au contrôle humain des incompatibilités |
| `intensite` | F/f doit égaler la phrase ; il s'agit de qualité d'ancrage (A6), pas de grandeur physique |
| `fait`, `source`, `contre_observation` | texte renseigné, pertinent ; la contre-observation dit aussi où l'on a cherché |
| `portee` | portée de la contre-observation (A7) : `marginale`, `substantielle`, `dominante` ou `aucune` ; `dominante` interdit le mot ; `substantielle` exige `intensite` f et `force_initiale` F (un mot déjà f est rejeté) |
| `force_initiale` | `"F"` seulement avec une portée substantielle ; sur un mot qui persiste, admis seulement s'il était F, ou déjà rétrogradé depuis F, à l'état précédent |
| `garantie` | requis pour F (cas réel) : `mecanisme`, `attendu`, `contredirait` (A6) ; forme type dans chaque fiche de `cartes.md` |
| `option` | requis pour F (cas réel) : `acteur` (« le système » admis), `avant`, `apres` différents (pertinence, O1) |
| `questions` | requis au premier état non nul d'un cas réel (cas fictif exempté) : liste non vide de `{question, si_oui, si_non}` ; `si_oui` et `si_non` sont deux CARTE@strate **différents**, l'un au moins présent dans l'état. Une question dont les deux réponses mènent à la même carte est décorative et refusée (abduction, `grammaire.md` §7) |
| `corroboration` | requis pour F d'un cas réel **actif** (une proposition le reçoit à son activation) : `"independantes"` si le fait repose sur au moins deux sources indépendantes, nommées dans `source` et séparées par « ; » ; `"unique"` sinon, admis et signalé dans « À vérifier auprès de vous ». Aucun effet sur le calcul (qualité de l'information, 0.6.6) |
| `a6` | requis pour F : chaque voisine de `cartes.md`, verdict `→` ou `+`, justification non vide ; contrôle complet sur cas réel, cas fictif exempté |
| `retraits` | exactement les mots disparus, chacun avec fait et source |
| `liaisons`, `preuves_liaisons` | mots existants, types compatibles avec les strates, une preuve par liaison |
| `preuves_qualificatifs` | dictionnaire CARTE@strate → ligne Q pour chaque mot qualifié |
| `positions`, `preuve_positions` | null ou tient/bouge/manque avec ≥3 mots, contraintes de présence et preuve |
| `sans_evenement` | `true` seulement si aucun mot n'apparaît, ne disparaît ni ne change de force sur toute la séquence (B4) |
| `codage` | `recodage` : qui a proposé le codage quand ce n'est pas le codeur (un modèle, par exemple) ; s'il est renseigné, un cas **actif** exige `recodage_confirme` `{par, date}` : un codeur humain nommé, pas le modèle, a relu ce qui a été proposé (0.6.7). **Codeurs** (0.6.14) : chacun `{id, role}`, `role` = `humain` ou `modele` ; un cas réel actif en
compte au moins un humain, et `recodage_confirme.par` est l'`id` d'un codeur humain de la fiche, pas un
nom libre. Les fiches fictives et les archives gardent la forme courte (chaîne). Puis : mode, codeurs distincts ; `independants` et `au_moins_un_humain` booléens s'ils sont présents ; si deux codeurs : indépendance et au moins un humain explicitement attestés |
| `fictif` | booléen ; tout cas fictif est exclu hors --demo et de V4 |
| `sources_verifiees` | true pour un cas réel actif ; ne pas déclarer sans avoir consulté les sources |
| `statut_donnees` | actif, proposition (exige `motif_proposition` et `sources_verifiees: false`) ou archive_a_revoir (exige `motif_archive`) ; seuls les cas actifs entrent dans les calculs |
| `usage` | partage par empreinte ; les cas test ne contribuent jamais aux estimations |

Deux états consécutifs sont espacés d'une fenêtre **calendaire exacte**. Les mois finissant plus tôt
rabattent le jour au dernier jour du mois. Une transition irrégulière n'est pas un pas régulier ;
la conserver en archive ou la rééchantillonner explicitement avec des observations vérifiables.
Les cas actifs sans mot nouveau peuvent porter `mots:null` ; une archive n'est contrôlée que comme
archive lisible, jamais présentée comme « active recevable ».

---

## 3. Coder un cas historique (mode CODER)

1. Définir configuration, population, fenêtre et règles d'issue avant sélection des exemples.
2. Attribuer l'id ; exécuter `partager` ; conserver ce partage.
3. Réunir les faits avec dates d'événement **et de disponibilité des sources**.
4. Coder chaque état à partir des seules informations alors disponibles ; identifier les objets.
5. Documenter nouveaux mots, révisions de confiance et retraits, puis preuves des liaisons et Q.
6. Un second codeur reçoit les faits, jamais le premier codage ; enregistrer son identité et son rôle.
7. Exécuter `valider`. Toute fiche active invalide bloque le calcul ; ne pas masquer l'erreur.
8. Si source absente, temporalité ambiguë ou règle ancienne non recodée : archiver avec motif.
9. **Traceback (0.6.0).** Nommer ce qui, absent de l'alphabet au départ, a été nécessaire pour rendre
   le cas codable (une carte, une strate, un qualificatif, une règle), ou écrire « rien ». Une
   construction nécessaire s'inscrit dans `assets/rabbits.jsonl`, avec le fait daté qui la rendait
   nécessaire ; une difficulté de lecture n'en est pas une. Trois occurrences indépendantes d'une même
   construction ouvrent A2.

Une validation structurale ne remplace pas A6/A7. Une contre-observation substantielle impose sa
baisse de confiance ; ne pas écrire « substantielle mais F maintenu ». Les observations nouvelles
ne modifient jamais rétroactivement un journal déjà publié.

---

## 4. Cas sans événement (B4)

Inclure les cas sans événement selon un plan représentatif et consigner la population de référence.
Le repère d'un tiers à défaut d'estimation est une alerte de collecte, pas un quota à imposer aux
données. Sans cas sans événement dans les homologues, ρ0 est interdit. Le champ ne remplace pas
les issues explicites des transitions : celles-ci sont calculées depuis les états.

---

## 5. Partage apprentissage / test (B5)

SHA-256 de l'id : premier caractère 0–4 → test (5/16), sinon apprentissage. Le validateur impose
ce partage ; ne pas renuméroter pour changer de lot. Le hasard du partage ne supprime pas les fuites
entre épisodes liés ni les fuites temporelles. Une évaluation doit aussi regrouper les épisodes liés
et réserver une période postérieure. Les fenêtres chevauchantes d'un même événement restent dans
le même ensemble scientifique, même si les identifiants doivent être revus avant toute collecte.

---

## 6. Contrôles de qualité de la base

| Contrôle | Action |
|---|---|
| Sources non consultées | archive, pas apprentissage |
| Date d'issue ou disponibilité après la prévision | transition exclue, y compris de la fréquence de base |
| Plusieurs transitions d'un cas | poids total ≤1 avant décroissance temporelle |
| Double codage | ≥20 cas et ≥20 % dans la strate pour sortir du mode solo ; ne prouve pas κ |
| Accord par carte | mesurer κ et examiner les désaccords ; seuil de travail 0,6 |
| Cas futurs, test, archives | exclus des estimations |
| Cas fictifs | démonstration explicite seulement, jamais validation prospective |
| Référence documentaire absente | équivalent Proposé, confiance f au maximum |

---

## 7. Données personnelles

Appliquer les limites de `constitution.md` §6 : minimisation, pseudonymes des personnes privées,
pas de diagnostic ou décision individuelle à partir du score. Ne conserver que les faits nécessaires
et leur provenance ; ne pas transformer l'accord d'un codeur en consentement d'une personne citée.
