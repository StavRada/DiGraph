from DiGraph.src.GraphAlgo import GraphAlgo
import timeit
import networkx as nx
import json


def my_graph(filename):
    algo =GraphAlgo()
    algo.load_from_json(filename)


    start = timeit.default_timer()
    algo.shortest_path(1,5)
    stop = timeit.default_timer()
    print("my shoetest path ",(stop-start))

    start = timeit.default_timer()
    algo.connected_components()
    stop = timeit.default_timer()
    print("my connected components ",(stop-start))

    start = timeit.default_timer()
    algo.connected_component(0)
    stop = timeit.default_timer()
    print("my connected component ",(stop-start))

def networkx(filename):

    graph=nx.DiGraph()

    with open(filename, 'r') as file:
        file_json = json.load(file)

    for elem in file_json['Nodes']:
        graph.add_node(int(elem.get('id')))

    for elem in file_json['Edges']:
        graph.add_edge(int(elem.get('src')),int(elem.get('dest')),weight= float(elem.get('w')))

    start = timeit.default_timer()
    nx.shortest_path(graph,source=1,target=5,method="dijkstra",weight="weight")
    stop = timeit.default_timer()
    print("networkx shoetest path ",(stop-start))

    start = timeit.default_timer()
    nx.strongly_connected_components(graph)
    stop = timeit.default_timer()
    print("networkx connected components ",(stop-start))


if __name__ == '__main__':
    my_graph('../data/G_10_80_1.json')
    networkx('../data/G_10_80_1.json')