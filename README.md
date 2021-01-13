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
v_size- returns the vertex(nodes) size in the graph.
e_size- returns the edges size in the graph.
add edge- Adds an edge to the graph.
add_node-	Adds an node to the graph.
remove_node-	Removes a node from the graph.
remove_edge-	Removes a edge from the graph.
