---

# 💩 Global Human Excrement Circulation Graph

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![NetworkX](https://img.shields.io/badge/NetworkX-Graph%20analysis-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Status](https://img.shields.io/badge/status-Experimental-purple)

</p>

---

# Project Overview

This project models the **global circulation of human excrement and its ecological consequences** using **graph theory**.

Human waste does not disappear after disposal. It moves through several interconnected environmental systems:

* human populations
* sanitation infrastructures
* rivers and major waterways
* oceans
* agricultural systems
* food consumption cycles

This project represents these interactions using a **directed ecological network**.

The objective is to **study the propagation of pollution through interconnected environmental systems**.

---

# Scientific Motivation

Human waste can contribute to several environmental processes:

* **water pollution**
* **nutrient cycling**
* **agricultural contamination**
* **global pollutant redistribution**

Understanding these dynamics requires modeling **complex networks of interactions**.

Graph theory provides a powerful framework to:

* represent environmental interactions
* identify critical nodes
* analyze diffusion pathways
* simulate ecological disruptions.

---

# Graph Model

The system is modeled as a **directed weighted graph**.

### Nodes represent:

* Human populations
* Excrement production
* Sanitation systems
* Rivers
* Major rivers
* Oceans
* Irrigation systems
* Agricultural soils
* Food products

### Edges represent:

**pollution fluxes** between system components.

Each edge has a **weight (`flux`)** representing the intensity of pollutant transfer.

---

# Ecological Circulation Cycle

The model highlights a major ecological feedback loop:

```
Humans
  ↓
Excrement
  ↓
Sanitation systems
  ↓
Rivers
  ↓
Oceans
  ↓
Agricultural irrigation
  ↓
Crops (tomatoes)
  ↓
Humans
```

This illustrates how pollutants may **indirectly return to human populations** through the food system.

---

# Graph Diagram

Simplified structure of the ecological network:

```
        Humans
          │
          ▼
      Excrement
          │
          ▼
    Sanitation Systems
   ┌────────┼────────┐
   ▼        ▼        ▼
Weak     Medium     High
   │        │        │
   ▼        ▼        ▼
     Local Rivers
          │
          ▼
     Major Rivers
      ┌────┴────┐
      ▼         ▼
 Atlantic     Pacific
   Ocean        Ocean
      │           │
      └────┬──────┘
           ▼
   Agricultural Irrigation
           │
           ▼
     Agricultural Soil
           │
           ▼
        Tomatoes
           │
           ▼
         Humans
```

---

# Algorithms Used

The project applies several **network science algorithms**.

| Algorithm                     | Purpose                              |
| ----------------------------- | ------------------------------------ |
| Betweenness Centrality        | Detect critical ecological nodes     |
| PageRank                      | Measure global node influence        |
| Eigenvector Centrality        | Identify influential ecological hubs |
| BFS                           | Explore pollution propagation        |
| DFS                           | Explore deep circulation paths       |
| Dijkstra                      | Compute shortest ecological paths    |
| Strongly Connected Components | Detect ecological cycles             |

---

# Example Analyses

The model can answer questions such as:

* Which nodes are **critical pollution hubs**?
* How does pollution **propagate through ecosystems**?
* What happens if a **river system collapses**?
* Which paths connect **human waste to food contamination**?

---

# Pollution Propagation Animation

The project includes a **dynamic simulation of pollution propagation**.

You can generate the animation using:

```
animer_propagation(G)
```

---

# Graph Visualization

The network can also be visualized:

```python
visualiser_graphe(G)
```

Nodes are colored according to **pollution intensity**.

---

# Running the Project

Execute the main script:

```bash
python cacapy.py
```

This will run:

* graph construction
* pollution propagation analysis
* centrality analysis
* shortest ecological path
* strongly connected components detection
* pollution propagation animation

---

# Example Output

Example console output:

```
___ Points critiques ___
Rivieres_locales : 0.452
Fleuves_majeurs  : 0.318
Excrements       : 0.211
```

---

# Future Improvements

Possible extensions:

* integrate **real-world pollution datasets**
* add **geographical mapping**
* simulate **policy scenarios**
* integrate **wastewater treatment efficiency models**
* build **interactive dashboards**

---

# References

Concepts used in this project:

* Graph Theory
* Network Science
* Environmental Systems Modeling
* Pollution Diffusion Models

---

# Author

Project exploring **ecological network modeling using Python and graph theory**.

---






<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/21a7e2ac-2b4c-44a2-8e3e-d8f877a119c2" />
