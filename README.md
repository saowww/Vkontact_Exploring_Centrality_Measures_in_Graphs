# Centrality Measures in Graphs (VK Mutual Friends)

This project is designed to analyze mutual friends among users on the VK social media platform and compute different centrality measures to identify influential users within the network. VK is a popular social networking platform widely used in Russia and neighboring countries.

Vertex centrality in a graph is a vector that assigns a numerical value (index) to each vertex of the graph.

The most common indices include:

* Degree Centrality
* Closeness Centrality
* Betweenness Centrality
* Eigenvector Centrality
* PageRank Centrality
  
In this project, we will focus on closeness centrality, betweenness centrality, and eigenvector centrality.

Closeness Centrality: A vertex that is closest to all other vertices in the network is considered the most central.
<img width="321" alt="image" src="https://github.com/user-attachments/assets/c9d0985d-bfae-48ed-be0b-09bf7d7aab62" />

<img width="234" alt="image" src="https://github.com/user-attachments/assets/97a7ae23-3cbd-4f14-8e68-46f9714c5ca7" />



Betweenness Centrality: A vertex through which the greatest number of shortest paths pass is considered the most central.
<img width="468" alt="image" src="https://github.com/user-attachments/assets/90115c6a-fa40-4af3-afa5-a8da2fe4bdf6" />

<img width="123" alt="image" src="https://github.com/user-attachments/assets/6f3633f3-a8e3-4c86-82e3-2025e781e7ec" />



Eigenvector Centrality: The centrality of vertex i depends on the centralities of the neighbors of vertex i.
* An eigenvector corresponding to the maximum eigenvalue is selected.
* This centrality takes into account distant interactions.
* Vertices that point to strong vertices themselves are considered the most central.
  
<img width="299" alt="image" src="https://github.com/user-attachments/assets/dde0f1d8-9b00-4baa-b4ed-0f7b42a734f0" />

<img width="228" alt="image" src="https://github.com/user-attachments/assets/bd0583fa-1950-48e4-afe0-07eb04dfc9bd" />


## Results 
<img width="468" alt="image" src="https://github.com/user-attachments/assets/fbcdf723-594d-48a7-94d1-0319b37221c4" />

