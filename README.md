# DiGraph
## about the project
In this project we dealt with the development of data structures of directed weighted graph,We created a system of building the graph, creating the node vertices and even in the previous project it was divided into two parts, the first building the graph and the second building a game. In addition we implemented a number of algorithms on the graph such as: connected, shortest path distance and more…
this is the last project of implemented directed weighted graph and now it is in the Python programming language.

## The classes of the project :
### node:
In this class we have implemented operations at a node (vertex) in a weighted graph (directional). key, location(position), weight, tag and info of each node.

### edge:
In this class there are edge thst consists of 2 nodes - src and dest and each edge has a weight.

## DiGraph:
In this class there is edges size, mode counter (mc) and graph, I used hash map for the nodes and hash map for the edges.
the functions in this class are:
* v_size- returns the vertex(nodes) size in the graph.
* e_size- returns the edges size in the graph.
* add edge- Adds an edge to the graph.
* add_node-	Adds an node to the graph.
* remove_node-	Removes a node from the graph.
* remove_edge-	Removes a edge from the graph.
* get_all_v- returns a dictionary of all the nodes in the Graph, each node is represented using a pair (node_id, node_data).
* all_in_edges_of_node- returns	a dictionary of all nodes connected to (to) node_id.
* all_out_edges_of_node- returns a dictionary of all nodes connected from node_id. 

## GraphAlgo
In this class there are algorithms that we used to the graph, 
### Is connected :
I used algorithms to check if all nodes in graph are connected for that I used Tarjan(strongly connected components) algorithm and Dfs (depth first search) algorithm.
* Tarjan-Tarjan strongly connected components is an algorithm in graph theory for finding the strongly connected components (SCCs) of a directed graph.
* Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures in our case is graph. the dfs algorithm checks the node on which it was activated, and then runs itself recursively on each of the nodes linked to the node to which it was activated, if it has not yet visited them, In order to remember which nodes the algorithm has already visited I used stack to put all the visited nodes.

### Shortest path :
I used algorithm to check the shortest path between 2 nodes in graph -dijkstra is algorithm that we maintain two sets one set contains vertices included in shortest path tree, other set includes vertices not yet included in shortest path tree At every step of the algorithm, we find a vertex which is in the other set (set of not yet included) and has a minimum distance from the source. my implementation requires Priority Queue to access in distance order.
* Dijkstra - to find the shortest route in the graph, and to return the list of sides in the shortest route in the graph. In methods: shortestpathDist, shortestpath
### more function in this class:
* load_from_json	Loads a graph from a json file.
* save_to_json	Saves the graph in JSON format to a file


