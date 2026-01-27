# coding:utf-8

# Dépendances
import networkx as nx # noeuds = Humains, Excréments, Stations d’épuration, Rivières, Océans, Tomates     arêtes = circulation / flux de pollution
import numpy as np
import matplotlib.pyplot as plt # bibliothèque Python pour dessiner des graphiques. Je charge l’outil qui me permet d’afficher des graphiques et des figures.
from PIL import Image


def creer_graphe():
    ''' Création du graphe orienté '''
    G = nx.DiGraph()

    # NOEUDS
    G.add_node("Humains", population=8e9, pollution=0)

    G.add_node("Excrements", pollution=1.0)

    G.add_node("Stations_epuration", efficacite=0.7)

    G.add_node("Rivieres", pollution=0.3)

    G.add_node("Oceans", pollution=0.5)

    G.add_node("Tomates", contamination=0.2)

    # ARÊTES (flux)
    G.add_edge("Humains", "Excrements", flux=1.0)
    G.add_edge("Excrements", "Stations_epuration", flux=0.8)
    G.add_edge("Stations_epuration", "Rivieres", flux=0.6)
    G.add_edge("Rivieres", "Oceans", flux=0.9)
    G.add_edge("Oceans", "Tomates", flux=0.1)

    return G




def points_critiques(G):
    ''' Détection des points critiques '''

    centralite = nx.betweenness_centrality(G) # Calcule la centralité d’intermédiarité. Mesure quels noeuds sont des points de passage obligatoires
    print("=== Points critiques (centralité d'intermédiarité) ===")
    for noeud, score in sorted(centralite.items(), key=lambda x: x[1], reverse=True): # Trie les noeuds par importance (du plus critique au moins critique)
        print(f"{noeud:20s} : {score:.3f}") # Affiche le nom du noeud et son score

    return centralite


def analyse_impact(G):
    ''' Analyse d’impact écologique (Fonction qui simule la propagation de la pollution) '''

    impact = {} # Dictionnaire pour stocker les résultats
    pollution_actuelle = 1.0  # Pollution initiale maximale (des excréments)

    for source, cible in G.edges(): # Parcourt toutes les connexions du graphe
        flux = G.edges[source, cible]["flux"] # Récupère la valeur du flux sur l’arête
        pollution_actuelle = pollution_actuelle * flux # La pollution diminue (ou se propage) selon le flux
        impact[cible] = pollution_actuelle # Stocke la pollution reçue par chaque nœud

    print("\n=== Impact écologique estimé ===")
    for noeud, pol in impact.items():
        print(f"{noeud:20s} pollution estimée : {pol:.3f}")

    return impact



def Parcours_en_Largeur(G):
    ''' Le parcours en largeur : exploration “horizontale”
on visite tous ses voisins, puis les voisins de ses voisins, etc.
    '''
    return list(nx.bfs_tree(G, start_node))



def Parcours_en_Profondeur():
    ''' Le parcours en profondeur : exploration “verticale”
on part d'un nœud, on explore un de ses voisins, puis on continue à explorer 
les voisins de ce voisin jusqu'à atteindre un nœud sans voisins non visités, 
puis on revient en arrière pour explorer les autres voisins du nœud précédent 
non encore visités, et ainsi de suite
    '''
    return list(nx.dfs_tree(G, start_node))


def visualiser_graphe(G):
    ''' Cette fonction permet de visualiser le graphe orienté représentant
la circulation des excréments humains à travers différents milieux
(humains, stations d’épuration, rivières, océans, agriculture).
Elle utilise NetworkX pour calculer la disposition des noeuds
et Matplotlib pour afficher le graphe avec des flèches indiquant
le sens des flux ainsi que des étiquettes pour les noeuds et les arêtes.
L’objectif est de rendre le réseau compréhensible visuellement
et de mettre en évidence les relations entre les différents éléments.
    '''

    pos = nx.spring_layout(G) # Calcule la disposition des nœuds pour une visualisation claire
    nx.draw(G, pos, with_labels=True, arrows=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold') # Dessine le graphe avec des étiquettes et des flèches
    edge_labels = nx.get_edge_attributes(G, 'flux')  # Récupère les étiquettes des arêtes basées sur les flux
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # Affiche les étiquettes des arêtes
    plt.title("Circulation des excréments humains dans l'environnement") # Titre du graphe
    return plt.show() # Affiche le graphe






# Programme principal

if __name__ == "__main__": # Vérifie que le fichier est exécuté directement
    G = creer_graphe() # Crée le graphe
    points_critiques(G) # Analyse les points sensibles
    analyse_impact(G) # Analyse la pollution
    visualiser_graphe(G) # Affiche le graphe

# Stats inquiétantes mais réelles
EXCREMENTS_PAR_PERSONNE_PAR_AN = 50  # kg/an (ordre de grandeur)
MICROPLASTIQUES_PAR_GRAMME = 10




# Évolutions possibles (pour briller)
# Ajouter des continents comme sous-graphes
# Simuler une panne de station d’épuration
# Ajouter des cycles (irrigation agricole)

# Utiliser des données réelles (OMS, FAO)
