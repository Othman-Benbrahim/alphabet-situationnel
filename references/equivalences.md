# Alphabet situationnel — Équivalents par strate (index, couche 1)

> Version : 0.5.1

> Les équivalents locaux des 16 cartes sont rangés **par strate**, un fichier par strate :
> `equivalences/strate-01.md` à `equivalences/strate-13.md`. Raison : la procédure va des faits vers les
> strates, puis vers les cartes candidates de chaque strate ; on ne charge donc que les strates où se
> trouvent des faits (O1). Vue par carte, pour l'audit :
> `python3 scripts/moteur.py equivalences --carte SEUIL`.

---

## 1. Contenu d'une case

| Colonne | Contenu |
|---|---|
| Équivalent | la traduction locale de la carte |
| Marqueur local | ce qui ancre la carte dans cette strate (A1) ; il précise le marqueur abstrait du noyau (`cartes.md`), il ne le remplace pas |
| Statut | Attesté, Documenté, Proposé ou Vide (§2) |
| Référence | la référence bibliographique qui fonde un statut Documenté, ou l'identifiant du cas qui fonde un statut Attesté |

---

## 2. Statuts (règle A3)

| Statut | Définition | Ce que le statut permet (A3) |
|---|---|---|
| **Attesté** | un cas réel de la base l'ancre avec la force F ; colonne Référence = identifiant du cas | ancrage F ou f ; emprunt T4 |
| **Documenté** | connu de la littérature du champ ; colonne Référence = référence vérifiable | ancrage F ou f ; emprunt T4 |
| **Proposé** | plausible, non vérifié | ancrage F ou f, signalé ; aucun emprunt |
| **Vide** | rien de convaincant trouvé ; l'ancrage passe par le noyau seul | ancrage f ; aucun emprunt |
| **Hors domaine** | la carte ne s'applique pas aux objets de la strate ; décision d'auteur, motif en colonne Référence | aucun ancrage ; aucun emprunt |

**État courant** (recalculé par `audit`) : 0 Attesté, 0 Documenté, 196 Proposé, 12 Vide, 0 Hors domaine. Les 117
anciennes cases Documentées sans référence vérifiée ont été rétrogradées en 0.4.0. Leurs références manquantes sont
conservées comme dette documentaire, jamais comme preuve. Une promotion demande de lire une source
qui soutient la traduction exacte et ses marqueurs. Prioriser quelques événements dans une strate ;
un concept mentionné dans une bibliographie générale ne justifie pas toutes ses transpositions.

---

## 3. Bilan par strate

| Strate | Documenté | Proposé | Vide | Hors domaine |
|---|---|---|---|---|
| 1 Matière | 0 | 13 | 3 | 0 |
| 2 Vivant | 0 | 15 | 1 | 0 |
| 3 Psyché | 0 | 13 | 3 | 0 |
| 4 Relations | 0 | 16 | 0 | 0 |
| 5 Organisations | 0 | 16 | 0 | 0 |
| 6 Économie | 0 | 16 | 0 | 0 |
| 7 Géopolitique | 0 | 16 | 0 | 0 |
| 8 Droit | 0 | 15 | 1 | 0 |
| 9 Culture | 0 | 16 | 0 | 0 |
| 10 Technique | 0 | 16 | 0 | 0 |
| 11 Climat | 0 | 13 | 3 | 0 |
| 12 Histoire longue | 0 | 15 | 1 | 0 |
| 13 Politique intérieure | 0 | 16 | 0 | 0 |

Les 12 cases Vides (carte : strates) : RÉCIPROCITÉ (1, 3, 11) ; RÉCURSIVITÉ (1, 2, 11) ; COMMUNAUTÉ (1, 3) ; ÉMERGENCE (3) ; RÉSONANCE (8, 12) ; HIÉRARCHIE (11). Huit sur douze portent sur
RÉCIPROCITÉ, RÉCURSIVITÉ et COMMUNAUTÉ, cartes qui supposent des agents, et sept sur douze sont dans les
strates sans agents (1, 2, 11). Question ouverte (`CHANGELOG.md`) : ces cartes sont-elles universelles,
ou universelles aux seuls systèmes à agents ?
