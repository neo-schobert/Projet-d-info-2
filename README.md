# README: Projet de Recherche des Racines d'un Polynôme avec la Méthode de Durand-Kerner

## Introduction

Ce projet vise à déterminer les racines d'un polynôme unitaire en utilisant la méthode de Durand-Kerner. Cette méthode repose sur une itération sur des nombres complexes afin de trouver les racines du polynôme. Le projet est également accompagné d'analyses de complexité des différentes fonctions implémentées.

## Structure du Projet

### Fichiers

- **Projet d'info 2.py : Contient l'implémentation des algorithmes et les fonctions principales.**
- **README.md** : Ce fichier, qui explique le fonctionnement global du projet.

### Présentation de la Méthode

1. Limitation du rayon de recherche des racines en utilisant une borne calculée :

2. Utilisation de l'algorithme de Durand-Kerner :

   - Initialisation de \$deg(P)\$ nombres complexes distincts.
   - Construction de suites par récurrence qui convergent (sous certaines conditions) vers les racines du polynôme.
   - Gestion des cas de convergence et de non-convergence.

### Représentation du Polynôme

Le polynôme est représenté sous forme d'un tableau contenant ses coefficients exprimés en notation complexe, facilitant les calculs numériques et évitant les conversions inutiles entre types de données.

## Fonctionnalités

### Calcul du Rayon de Recherche

- **Fonction : calcul\_R(tab)**
- Entrée : Un tableau contenant les coefficients du polynôme.
- Sortie : La valeur \$1 + \max\_{0 \leq i \leq p-1} |a\_i|\$, limitant le rayon de recherche des racines.
- Complexité : \$\mathcal{O}(deg(P))\$

### Algorithme de Durand-Kerner

L'algorithme est divisé en trois fonctions principales :

1. **P\_el** : Calcule \$P(x\_n^k)\$ pour un polynôme donné et une valeur complexe.
   - Complexité : \$\mathcal{O}(deg(P))\$
2. **random\_complex\_de\_D** : Génère un nombre complexe aléatoire dans le disque de recherche.
   - Complexité : \$\mathcal{O}(1)\$
3. **suite\_Durand\_Kerner1** : Implémente le reste de l'algorithme.
   - Complexité globale : \$\mathcal{O}(deg(P)^2)\$ dans le cas moyen, en raison des boucles imbriquées.

## Utilisation

1. Assurez-vous que **Python 3** est installé sur votre système.
2. Clonez ce répertoire ou téléchargez les fichiers.
3. Placez les coefficients de votre polynôme dans un tableau sous la forme de nombres complexes. Exemple pour \$P(x) = x^2 + 2x + 1\$ :
   ```python
   tab = [1+0j, 2+0j, 1+0j]
   ```
4. Modifiez les paramètres d'initialisation et de précision dans le fichier principal selon vos besoins.
5. Lancez le programme :
   ```bash
   python "Projet d'info 2.py"
   ```
6. Les racines seront affichées dans la console.

## Visualisation

Les résultats peuvent être visualisés à l'aide d'un graphe représentant les racines dans le plan complexe (fonctionnalité à implémenter ou à connecter).

## Limitations

- La méthode ne garantit pas toujours la convergence, bien qu'elle fonctionne dans la plupart des cas pratiques.
- Les performances peuvent diminuer avec des polynômes de très haut degré.

## Conclusion

Ce projet offre une implémentation efficace de la méthode de Durand-Kerner, tout en mettant l'accent sur les aspects théoriques et pratiques du calcul des racines de polynômes. N'hésitez pas à adapter et étendre le code pour répondre à vos besoins spécifiques.

---

**Auteur :** Néo Schobert

