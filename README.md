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
![image](https://github.com/saowww/Vkontact_Exploring_Centrality_Measures_in_Graphs/assets/66699311/f63315d1-6585-46c4-ac0a-07799f6d5dc9)
![image](https://github.com/saowww/Vkontact_Exploring_Centrality_Measures_in_Graphs/assets/66699311/2817456d-afdd-4e05-a5cc-94109b478371)


Betweenness Centrality: A vertex through which the greatest number of shortest paths pass is considered the most central.
![image](https://github.com/saowww/Vkontact_Exploring_Centrality_Measures_in_Graphs/assets/66699311/bf6218f2-e966-4528-b735-cc2c8a42dbef)
![image](https://github.com/saowww/Vkontact_Exploring_Centrality_Measures_in_Graphs/assets/66699311/6704605d-2e9a-4aac-9806-29fce13b5cb0)


Eigenvector Centrality: The centrality of vertex i depends on the centralities of the neighbors of vertex i.
* An eigenvector corresponding to the maximum eigenvalue is selected.
* This centrality takes into account distant interactions.
* Vertices that point to strong vertices themselves are considered the most central.
  
![image](https://github.com/saowww/Vkontact_Exploring_Centrality_Measures_in_Graphs/assets/66699311/d3a4d39d-766c-4308-9e89-00af77f3c05f)
![image](https://github.com/saowww/Vkontact_Exploring_Centrality_Measures_in_Graphs/assets/66699311/d14ba907-9aa4-4452-bf36-da641deb20a1)

## Results 
![image](https://github.com/saowww/Vkontact_Exploring_Centrality_Measures_in_Graphs/assets/66699311/6936dc07-8ab3-489c-aee6-bc3886f599d4)
