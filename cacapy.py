# coding:utf-8

import networkx as nx # noeuds = Humains, Excréments, Stations d’épuration, Rivières, Océans, Tomates     arêtes = circulation / flux de pollution
import matplotlib.pyplot as plt # bibliothèque Python pour dessiner des graphiques. Je charge l’outil qui me permet d’afficher des graphiques et des figures.
import matplotlib.animation as animation # c'est pour les animation

def creer_graphe():
    """ 
    Création d'un graphe orienté représentant la circulation mondiale 
    des excréments humains avec boucles écologiques et chemins alternatifs.
    """

    G = nx.DiGraph()

    # NOEUDS – POPULATIONS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    G.add_node("Humains_Afrique", population=1.4e9)
    G.add_node("Humains_Europe", population=0.75e9)
    G.add_node("Humains_Asie", population=4.7e9)
    G.add_node("Humains_Amerique", population=1.0e9)

    G.add_node("Excrements", pollution=1.0)

    # ASSAINISSEMENT !!!!!!!!!!!!!!!!

    G.add_node("Assainissement_faible", efficacite=0.2)
    G.add_node("Assainissement_moyen", efficacite=0.5)
    G.add_node("Assainissement_eleve", efficacite=0.8)

    # MILIEUX AQUATIQUES !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    G.add_node("Rivieres_locales", pollution=0.4)
    G.add_node("Fleuves_majeurs", pollution=0.5)
    G.add_node("Ocean_Atlantique", pollution=0.6)
    G.add_node("Ocean_Pacifique", pollution=0.6)

    # BOUCLE ALIMENTAIRE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    G.add_node("Irrigation_agricole", pollution=0.3)
    G.add_node("Sols_agricoles", pollution=0.2)
    G.add_node("Tomates", contamination=0.1)

    # ARÊTES – PRODUCTION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    G.add_edge("Humains_Afrique", "Excrements", flux=1.0)
    G.add_edge("Humains_Europe", "Excrements", flux=1.0)
    G.add_edge("Humains_Asie", "Excrements", flux=1.0)
    G.add_edge("Humains_Amerique", "Excrements", flux=1.0)

    # ARÊTES – ASSAINISSEMENT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    G.add_edge("Excrements", "Assainissement_faible", flux=0.4)
    G.add_edge("Excrements", "Assainissement_moyen", flux=0.35)
    G.add_edge("Excrements", "Assainissement_eleve", flux=0.25)

    # EAUX CONTINENTALES !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    G.add_edge("Assainissement_faible", "Rivieres_locales", flux=0.9)
    G.add_edge("Assainissement_moyen", "Rivieres_locales", flux=0.6)
    G.add_edge("Assainissement_eleve", "Rivieres_locales", flux=0.3)

    G.add_edge("Rivieres_locales", "Fleuves_majeurs", flux=0.8)

    # Chemins alternatifs vers océans !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    G.add_edge("Rivieres_locales", "Ocean_Atlantique", flux=0.3)
    G.add_edge("Rivieres_locales", "Ocean_Pacifique", flux=0.2)

    # OCEANS !!!!!!!!!!!!!!!!!!!!

    G.add_edge("Fleuves_majeurs", "Ocean_Atlantique", flux=0.5)
    G.add_edge("Fleuves_majeurs", "Ocean_Pacifique", flux=0.5)

    # Pollution transocéanique (cycle océanique) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    G.add_edge("Ocean_Atlantique", "Ocean_Pacifique", flux=0.1)
    G.add_edge("Ocean_Pacifique", "Ocean_Atlantique", flux=0.1)

    # RETOUR AGRICOLE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    G.add_edge("Ocean_Atlantique", "Irrigation_agricole", flux=0.1)
    G.add_edge("Ocean_Pacifique", "Irrigation_agricole", flux=0.1)

    # Retour direct depuis fleuves !!!!!!!!!!!!!!!!
    G.add_edge("Fleuves_majeurs", "Irrigation_agricole", flux=0.15)

    G.add_edge("Irrigation_agricole", "Sols_agricoles", flux=0.7)
    G.add_edge("Sols_agricoles", "Tomates", flux=0.5)

    # BOUCLE ALIMENTAIRE (cycle majeur) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    G.add_edge("Tomates", "Humains_Europe", flux=0.4)
    G.add_edge("Tomates", "Humains_Afrique", flux=0.4)
    G.add_edge("Tomates", "Humains_Asie", flux=0.4)
    G.add_edge("Tomates", "Humains_Amerique", flux=0.4)

    # ÉCHANGES COMMERCIAUX AGRICOLES !!!!!!!!!!!!!!!!

    G.add_edge("Sols_agricoles", "Humains_Europe", flux=0.2)
    G.add_edge("Sols_agricoles", "Humains_Asie", flux=0.2)

    return G


def points_critiques(G):
    """ Détection des points critiques """
    centralite = nx.betweenness_centrality(G) # Calcule la centralité d’intermédiarité. Mesure quels noeuds sont des points de passage obligatoires

    print("___ Points critiques (centralité d'intermédiarité) ___")
    for noeud, score in sorted(centralite.items(), key=lambda x: x[1], reverse=True): # Trie les noeuds par importance (du plus critique au moins critique)
        print(f"{noeud:20s} : {score:.3f}") # Affiche le nom du noeud et son score

    return centralite


def analyse_impact(G):
    """ Analyse d’impact écologique avec plusieurs sources humaines """

    # Initialisation de la pollution reçue par chaque nœud
    pollution = {node: 0.0 for node in G.nodes()}

    # Sources humaines
    sources = [n for n in G.nodes() if n.startswith("Humains")]

    # Pollution initiale produite par chaque source
    for source in sources:
        pollution[source] = 1.0

    # Propagation simple (ordre des arêtes)
    for source, cible in G.edges():
        flux = G.edges[source, cible]["flux"]
        pollution[cible] += pollution[source] * flux

    print("\n___ Impact écologique estimé (multi-sources) ___")
    for noeud, pol in pollution.items():
        print(f"{noeud:25s} pollution estimée : {pol:.3f}")

    return pollution


def parcours_en_largeur(G):
    ''' Le parcours en largeur : exploration “horizontale”
on visite tous ses voisins, puis les voisins de ses voisins, etc.
    '''
    return list(nx.bfs_tree(G, "Humains_Europe"))


def parcours_en_profondeur(G):
    ''' Le parcours en profondeur : exploration “verticale”
on part d'un nœud, on explore un de ses voisins, puis on continue à explorer 
les voisins de ce voisin jusqu'à atteindre un nœud sans voisins non visités, 
puis on revient en arrière pour explorer les autres voisins du nœud précédent 
non encore visités, et ainsi de suite
    '''
    return list(nx.dfs_tree(G, "Humains_Amerique"))




def pagerank_ecologique(G):
    """ Importance globale des nœuds dans la diffusion de la pollution """
    pr = nx.pagerank(G, weight="flux")

    print("\n___ PageRank écologique (influence globale) ___")
    for n, score in sorted(pr.items(), key=lambda x: x[1], reverse=True):
        print(f"{n:25s} : {score:.4f}")

    return pr





def centralite_propre(G):
    """ Centralité propre : influence via des voisins influents """
    ce = nx.eigenvector_centrality_numpy(G, weight="flux")

    print("\n___ Centralité propre (réseau complexe) ___")
    for n, score in sorted(ce.items(), key=lambda x: x[1], reverse=True):
        print(f"{n:25s} : {score:.4f}")

    return ce



def scenario_rupture(G, noeud):
    """ Simulation de rupture d'un nœud clé """
    G2 = G.copy()
    G2.remove_node(noeud)

    print(f"\n___ Scénario de rupture : suppression de {noeud} ___")

    try:
        pr = nx.pagerank(G2, weight="flux")
        for n, score in sorted(pr.items(), key=lambda x: x[1], reverse=True):
            print(f"{n:25s} : {score:.4f}")
    except:
        print("Le graphe n'est plus connexe, diffusion interrompue.")

    return G2



def composantes_fortement_connexes(G):
    """
    Détection des composantes fortement connexes (CFC)
    dans le réseau écologique.
    """

    cfc = list(nx.strongly_connected_components(G))

    print("\n___ Composantes fortement connexes ___")

    for i, composante in enumerate(cfc, start=1):
        print(f"Composante {i} ({len(composante)} nœuds) :")
        for noeud in composante:
            print(f"   - {noeud}")
        print()

    return cfc


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

    # Calcul de l'impact écologique !!!!!!!!!
    pollution = analyse_impact(G)

    # Positions (carte logique, voir section suivante) !!!
    pos = positions_monde(G)

    # Valeurs de pollution pour les couleurs !!
    valeurs = [pollution.get(n, 0.0) for n in G.nodes()]

    plt.figure(figsize=(14, 8))

    nx.draw(
        G, pos,
        with_labels=True,
        arrows=True,
        node_size=2200,
        node_color=valeurs,
        cmap=plt.cm.Reds,
        font_size=9,
        font_weight='bold')

    edge_labels = nx.get_edge_attributes(G, 'flux')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    plt.title("Circulation mondiale des excréments humains et impact écologique")
    plt.colorbar(plt.cm.ScalarMappable(cmap=plt.cm.Reds), label="Niveau de pollution")
    plt.show()





def positions_monde(G):
    """ Positionnement logique clair et espacé des nœuds """

    pos = {
        # HUMAIN (ligne haute)
        "Humains_Amerique": (-6, 6),
        "Humains_Afrique":  (-4, 6),
        "Humains_Europe":   (-2, 6),
        "Humains_Asie":     (0, 6),

        # EXCREMENTS
        "Excrements": (-2, 5),

        # ASSAINISSEMENT
        "Assainissement_faible": (-4, 4),
        "Assainissement_moyen":  (-2, 4),
        "Assainissement_eleve":  (0, 4),

        # EAUX CONTINENTALES
        "Rivieres_locales": (2, 3),
        "Fleuves_majeurs":  (4, 3),

        # OCEANS
        "Ocean_Atlantique": (3, 2),
        "Ocean_Pacifique":  (5, 2),

        # AGRICULTURE
        "Irrigation_agricole": (6.5, 1),
        "Sols_agricoles":      (8.5, 1),
        "Tomates":             (10.5, 1),
    }

    return pos




def animer_propagation(G, steps=6):
    """ Animation de la propagation de la pollution dans le temps """

    # Initialisation pollution
    pollution = {node: 0.0 for node in G.nodes()}
    sources = [n for n in G.nodes() if n.startswith("Humains")]

    for s in sources:
        pollution[s] = 1.0

    pos = positions_monde(G)

    fig, ax = plt.subplots(figsize=(14, 8))

    def update(step):
        ax.clear()

        # Propagation d'un pas de temps
        nouvelles_pollutions = pollution.copy()
        for source, cible in G.edges():
            flux = G.edges[source, cible]["flux"]
            nouvelles_pollutions[cible] += pollution[source] * flux / steps

        pollution.update(nouvelles_pollutions)

        valeurs = [pollution[n] for n in G.nodes()]

        # Dessin des nœuds (sans labels)
        nx.draw(
            G, pos,
            ax=ax,
            with_labels=False,
            arrows=True,
            node_size=2200,
            node_color=valeurs,
            cmap=plt.cm.Reds,
            vmin=0,
            vmax=2
        )

        # Labels décalés
        for node, (x, y) in pos.items():
            ax.text(
                x, y - 0.3,
                node,
                fontsize=8,
                ha='center'
            )

        # Labels des arêtes
        edge_labels = nx.get_edge_attributes(G, 'flux')
        nx.draw_networkx_edge_labels(
            G, pos,
            edge_labels=edge_labels,
            font_size=8,
            ax=ax
        )

        ax.set_title(f"Propagation de la pollution – temps t = {step}")

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=steps,
        interval=1200,
        repeat=False
    )

    plt.show()
    return ani





# DIJKSTRA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def plus_court_chemin_ecologique(G, source, cible):
    """
    Calcule le chemin écologique le plus court en utilisant Dijkstra.
    On transforme le flux en coût : coût = 1 / flux
    """

    G_temp = G.copy()

    # Création d'un poids "cout" basé sur l'inverse du flux
    for u, v, data in G_temp.edges(data=True):
        flux = data["flux"]
        if flux > 0:
            data["cout"] = 1 / flux
        else:
            data["cout"] = float("inf")

    try:
        chemin = nx.shortest_path(
            G_temp,
            source=source,
            target=cible,
            weight="cout"
        )

        distance = nx.shortest_path_length(
            G_temp,
            source=source,
            target=cible,
            weight="cout"
        )

        print(f"\n___ Plus court chemin écologique (Dijkstra) ___")
        print(f"De {source} à {cible}")
        print("Chemin :", " -> ".join(chemin))
        print(f"Coût total écologique : {distance:.3f}")

        return chemin, distance

    except nx.NetworkXNoPath:
        print("Aucun chemin trouvé.")
        return None, None





# Programme principal
if __name__ == "__main__": # Vérifie que le fichier est exécuté directement !!!!!!!!!!!!!!!!!!!!!!!!!!!
    G = creer_graphe() # Crée le graphe !
    points_critiques(G) # Analyse les points sensibles
    analyse_impact(G) # Analyse la pollution
    print("Parcours en largeur depuis l'humain Européen :", parcours_en_largeur(G))
    print("Parcours en profondeur depuis l'humain Américain :", parcours_en_profondeur(G))
    pagerank_ecologique(G)
    centralite_propre(G)
    scenario_rupture(G, "Rivieres_locales")
    plus_court_chemin_ecologique(G, "Humains_Europe", "Tomates")
    composantes_fortement_connexes(G)

    # visualiser_graphe(G) # Affiche le graphe
    animer_propagation(G)
