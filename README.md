# Caca
Graphe représentant la circulation de caca !!!



Expliquer en quoi le graphe est nécéssaire et quel est son but ?



---

# Modélisation de la circulation mondiale des excréments humains

## Présentation du projet

Ce projet propose une **modélisation simplifiée de la circulation mondiale des excréments humains** à travers différents systèmes environnementaux et socio-écologiques.

L'objectif est de représenter comment les déchets humains peuvent circuler entre plusieurs milieux :

* les **populations humaines**
* les **systèmes d’assainissement**
* les **milieux aquatiques** (rivières, fleuves, océans)
* les **systèmes agricoles**
* la **boucle alimentaire**

Pour cela, le projet utilise un **graphe orienté** construit avec la bibliothèque **NetworkX**. Dans ce graphe :

* les **nœuds** représentent des éléments du système écologique (humains, excréments, rivières, océans, sols agricoles, etc.)
* les **arêtes** représentent les **flux de matière ou de pollution** entre ces éléments.

Chaque arête possède un **poids appelé flux**, qui représente l'intensité de la circulation de pollution entre deux éléments.

Ce modèle permet d’explorer plusieurs questions :

* Quels sont les **points critiques** dans la diffusion de pollution ?
* Comment la pollution **se propage** dans le réseau écologique ?
* Quels sont les **chemins principaux** reliant la production de déchets humains à la contamination alimentaire ?
* Que se passe-t-il si un **élément du système disparaît** (ex : une rivière ou un système d'assainissement) ?

Le projet combine donc :

* **théorie des graphes**
* **modélisation environnementale**
* **analyse de réseaux complexes**
* **visualisation scientifique**

---

# Justification des fonctions

## `creer_graphe()`

Cette fonction construit le **graphe principal du modèle écologique**.

Elle définit :

* les **nœuds du système** (humains, excréments, stations d’assainissement, rivières, océans, agriculture)
* les **flux entre ces éléments**

Le graphe est orienté afin de représenter **le sens réel de circulation de la pollution**.

Cette fonction constitue **la base du modèle**, car toutes les analyses reposent sur cette structure.

---

## `points_critiques(G)`

Cette fonction calcule la **centralité d’intermédiarité** des nœuds.

Cela permet d’identifier les **points de passage essentiels** dans le réseau :
les éléments qui contrôlent une grande partie des flux.

Dans un système écologique réel, ces points critiques peuvent correspondre par exemple à :

* des fleuves majeurs
* des infrastructures d’assainissement
* des zones de redistribution de pollution

---

## `analyse_impact(G)`

Cette fonction simule la **propagation de la pollution** à partir des populations humaines.

Elle initialise une pollution de départ puis la **propage dans le graphe en fonction des flux**.

L'objectif est d'obtenir une **estimation du niveau de pollution reçu par chaque élément du système**.

Cette analyse permet de comprendre :

* où la pollution **s'accumule**
* quels milieux sont **les plus exposés**

---

## `parcours_en_largeur(G)`

Cette fonction applique un **parcours en largeur (BFS)**.

Elle permet d’explorer le réseau **niveau par niveau** à partir d'une source humaine.

Dans le contexte du modèle, cela permet d'observer **comment la pollution peut se diffuser progressivement dans le système écologique**.

---

## `parcours_en_profondeur(G)`

Cette fonction applique un **parcours en profondeur (DFS)**.

Contrairement au parcours en largeur, il explore **une chaîne complète de propagation** avant de revenir en arrière.

Cela permet d’identifier des **trajectoires complètes de circulation de la pollution** dans le système.

---

## `pagerank_ecologique(G)`

Cette fonction applique l’algorithme **PageRank** au réseau écologique.

Elle permet de mesurer **l’importance globale des nœuds dans la diffusion de la pollution**.

Un nœud aura un score élevé s'il :

* reçoit beaucoup de flux
* est connecté à d'autres nœuds influents.

---

## `centralite_propre(G)`

Cette fonction calcule la **centralité propre (eigenvector centrality)**.

Elle mesure l’influence d’un nœud **en fonction de l’importance de ses voisins**.

Dans un système environnemental, cela permet d’identifier les **zones structurantes du réseau écologique**.

---

## `scenario_rupture(G, noeud)`

Cette fonction simule la **disparition d’un élément du système**.

Elle supprime un nœud (par exemple une rivière) puis recalcul les équilibres du réseau.

Cela permet d'étudier :

* la **résilience du système**
* les **changements dans la diffusion de la pollution**

---

## `composantes_fortement_connexes(G)`

Cette fonction détecte les **composantes fortement connexes du graphe**.

Une composante fortement connexe est un groupe de nœuds où **chaque nœud peut atteindre les autres**.

Dans ce modèle, cela peut révéler **des cycles écologiques** ou des **boucles de pollution**.

---

## `visualiser_graphe(G)`

Cette fonction permet de **visualiser le réseau écologique**.

Elle utilise **Matplotlib** et **NetworkX** pour afficher :

* les nœuds
* les flux
* le niveau de pollution

La couleur des nœuds représente **l’intensité de la pollution estimée**.

---

## `positions_monde(G)`

Cette fonction définit une **disposition spatiale logique des nœuds**.

Les nœuds sont organisés selon la logique du système :

1. humains
2. excréments
3. assainissement
4. rivières et fleuves
5. océans
6. agriculture
7. retour alimentaire

Cette organisation facilite la **lecture du graphe**.

---

## `animer_propagation(G)`

Cette fonction crée une **animation de la propagation de la pollution dans le temps**.

Elle montre visuellement :

* comment la pollution se diffuse
* comment certains milieux deviennent progressivement plus contaminés.

Cette visualisation rend le modèle **plus intuitif et pédagogique**.

---

## `plus_court_chemin_ecologique(G, source, cible)`

Cette fonction utilise **l’algorithme de Dijkstra** pour calculer le chemin écologique le plus court.

Le flux est transformé en **coût écologique (1 / flux)** afin de modéliser la facilité de propagation.

Cela permet d’identifier **les trajectoires les plus probables de circulation de pollution** entre deux éléments du système.



En résumé, ce projet montre comment la **théorie des graphes peut être utilisée pour modéliser un système écologique complexe**, en représentant la circulation des polluants dans les interactions entre humains, environnement et agriculture.






---

# Pourquoi utiliser un graphe ?

Le système étudié dans ce projet est **complexe et interconnecté**. Les excréments humains ne restent pas dans un seul endroit : ils circulent entre plusieurs milieux :

* les **populations humaines**
* les **systèmes d’assainissement**
* les **rivières et fleuves**
* les **océans**
* les **systèmes agricoles**
* la **boucle alimentaire**

Ces éléments forment un **réseau d’interactions** où la pollution peut suivre différents chemins.

Pour représenter correctement ces relations, l'utilisation d’un **graphe orienté** est particulièrement adaptée.

Dans ce modèle :

* les **nœuds** représentent les éléments du système (humains, excréments, rivières, sols agricoles, etc.)
* les **arêtes** représentent les **flux de circulation de la pollution**
* le **poids des arêtes** représente l’intensité du flux.

Ainsi, le graphe permet de **modéliser les relations et les trajectoires possibles de la pollution dans l’environnement**.

---

# But du graphe

Le graphe sert principalement à **analyser la circulation et l’impact écologique des excréments humains à l’échelle globale**.

Grâce à cette représentation, il devient possible de :

### Comprendre la propagation de la pollution

Le graphe permet de suivre **comment la pollution se déplace dans les différents milieux** :
des populations humaines vers les systèmes d’assainissement, puis vers les rivières, les océans et finalement l’agriculture.

---

### Identifier les points critiques du système

Certaines parties du réseau peuvent jouer un rôle central dans la circulation de la pollution.

Par exemple :

* les **rivières locales**
* les **fleuves majeurs**
* les **systèmes d’assainissement**

Les algorithmes de **centralité** permettent d’identifier ces points sensibles.

---

### Étudier les cycles écologiques

Le graphe met en évidence des **boucles de circulation**, notamment la boucle alimentaire :

humains → excréments → eau → agriculture → nourriture → humains.

Cela montre comment certains polluants peuvent **revenir indirectement vers les populations humaines**.

---

### Simuler des scénarios

Grâce au graphe, il est possible de tester différents scénarios :

* suppression d’un nœud (ex : disparition d’une rivière)
* modification des flux de pollution
* évolution de l’assainissement

Ces simulations permettent d’observer **l’impact sur l’ensemble du système**.

---

**En résumé :**

Le graphe est nécessaire car il permet de **représenter un système environnemental complexe sous forme de réseau**, ce qui rend possible l’analyse de la propagation de la pollution, l’identification des points critiques et la simulation de différents scénarios écologiques.

---




<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/21a7e2ac-2b4c-44a2-8e3e-d8f877a119c2" />
