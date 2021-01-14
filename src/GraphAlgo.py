from typing import List
from DiGraph.src.DiGraph import DiGraph
from DiGraph.src.GraphAlgoInterface import GraphAlgoInterface
from DiGraph.src import GraphInterface
import json
import math
from queue import PriorityQueue
from DiGraph.src.Node import *
import random
import matplotlib.pyplot as plots

#global variables
path = []
list_path=[]


class GraphAlgo(GraphAlgoInterface):



    def __init__(self, graph: GraphInterface =DiGraph()):
        self.g=graph

    """
           this function gets graph
          """
    def get_graph(self) -> GraphInterface:
        return self.g

    """
         this function loads a graph from a json file.
         It deserialize it from a JSON file, by loading it from the given path.
          """
    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name,'r') as file:
                file_json= json.load(file)

            for n in file_json['Nodes']:
                if n.get('pos') is None:
                    self.g.add_node(n.get('id'))
                else:
                    position= tuple(map(float, n.get('pos').split(",")))
                    self.g.add_node(n.get('id'),position)

            for e in file_json['Edges']:
                self.g.add_edge(e.get('src'),e.get('dest'),e.get('w'))

            return True
        except :
            return False

    """
             this function gets file and save it  to json file.
              """
    def save_to_json(self, file_name: str) -> bool:

        Nodes = []

        for node in self.g.get_all_v().values():
            if node.getPos() is not None:
                postion = str(node.getPos()[0])+","+str(node.getPos()[1])
                Nodes.append({'pos': postion,'id': node.getk()})
            else:
                Nodes.append({'id': node.getk()})

        Edges=[]
        for n in self.g.get_all_v().keys():
            for edge in self.g.all_out_edges_of_node(n).values():
                #Dict[int,Dict[int,Edge_Data]]
                Edges.append({"src":edge.getSrc(),"w":edge.getW(),"dest":edge.getDest()})

        graph_json={'Edges': Edges,'Nodes':Nodes}
        try:
            with open(file_name,'w') as file:
                json.dump(graph_json,file)
            return True
        except FileNotFoundError:
            return False

    """
        this function initializing the nodes to infinity
        """
    def __infinity_nodes(self):
        for node in self.g.get_all_v().values():
            node.w=math.inf
            node.tag=0
            node.info=""

    """
         This function returns list of nodes we went and returns the path.
	     we used dijkstra algorithm to check the shortest path between 2 nodes in graph, src and dest.
	     my implementation requires PriorityQueue to access in distance order.
         """
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 not in self.g.get_all_v() or id2 not in self.g.get_all_v():
            return math.inf,[]

        self.__infinity_nodes()

        queue = PriorityQueue()

        node_data = self.g.get_all_v().get(id1)
        node_data.w=0
        queue.put(node_data)
        while not queue.empty():
            vertex = queue.get()
            for edge in self.g.all_out_edges_of_node(vertex.getk()).values():
                neigbur=self.g.get_all_v().get(edge.getDest())
                dist = vertex.w+edge.getW()
                if dist < neigbur.w:
                    neigbur.w=dist
                    neigbur.info=vertex.getk()
                    queue.put(neigbur)

        dest = self.g.get_all_v().get(id2)
        if dest.w is math.inf:
            return math.inf,[]

        list_path=[]
        list_path.insert(0,dest.getk())

        info = dest.info
        while info != "":
            node = self.g.get_all_v().get(info)
            list_path.insert(0, node.getk())
            info = node.info

        return dest.w,list_path

    """
        we used the tarjan algorithm to find the strongly connected components in the graph
	    if we have 1 components graph is connected else is not connected
        """

    def connected_component(self, id1: int) -> list:
        if self.g is None and id1 not in self.g.get_all_v():
            return []

        global path, list_path
        path=[]
        list_path=[]

        self.__infinity_nodes()

        self.__dfs(id1)

        return path

    """
        dfs (depth first search) algorithm
        """
    def __dfs(self,at:int):
        global path,list_path
        id=0
        stack=[]
        # index - > tag lowlink -> weight  onstack ->info
        work =[(at,0)]

        while work:
            at,i = work[-1]
            del work[-1]
            at_node: Node_Data = self.g.get_all_v().get(at)
            if i == 0:
                stack.append(at)
                id+=1
                # index - > tag lowlink -> weight  onstack ->info
                at_node.tag = id
                at_node.w = id
                at_node.info = "true"
            recurse = False
            j=0
            for to in self.g.all_out_edges_of_node(at).keys():
                to_node:Node_Data = self.g.get_all_v().get(to)
                w=to_node.getk()
                if to_node.tag == 0:
                    work.append((at, j + 1))
                    work.append((w, 0))
                    recurse = True
                    j += 1
                    break
                elif to_node.info == "true":
                    j += 1
                    at_node.w = min(at_node.w, to_node.w)
            if recurse: continue
            if at_node.tag == at_node.w:
                path = []
                while stack:
                    node = stack.pop()
                    path.insert(0,node)
                    node_: Node_Data = self.g.get_all_v().get(node)
                    node_.info = ""
                    node_.w = at_node.tag
                    if node == at: break
                list_path.insert(0,path)
            if work: # NEW: v was recursively visited.
                w = at
                at, _ = work[-1]
                to_node: Node_Data = self.g.get_all_v().get(w)
                at_node.w = min(at_node.w, to_node.w)


    def connected_components(self) -> List[list]:
        if self.g is None:
            return []
        global path, list_path,stack,id
        path=[]
        list_path=[]
        stack = []
        id = 0
        self.__infinity_nodes()


        for x in self.g.get_all_v().values():
            if x.tag == 0:
                self.__dfs(x.getk())

        return list_path

    """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        each directed edge is represented as an arrow, which points the dest, starting from src.
        each node is represented as a red dot with it's key above it's location.
        """
    def plot_graph(self) -> None:

        array_x=[]
        array_y=[]
        nodes= []
        for x in self.g.get_all_v().values():
            node:Node_Data = x
            if node.getPos() is None:
                node.setPos((random.uniform(35.18, 35.2),random.uniform(32.1, 32.2)))
            array_x.append(node.getPos()[0])
            array_y.append(node.getPos()[1])
            nodes.append(node.getk())

        fig,ax = plots.subplots()
        for p, txt in enumerate(nodes):
            ax.annotate(nodes[p], (array_x[p], array_y[p]))
        plots.plot(array_x,array_y,".",color = "blue")


        for s in self.g.get_all_v().keys():
             for d in self.g.all_out_edges_of_node(s).keys():
                x1=self.g.get_all_v().get(s).getPos()[0]
                y1=self.g.get_all_v().get(s).getPos()[1]
                x2=self.g.get_all_v().get(d).getPos()[0]
                y2=self.g.get_all_v().get(d).getPos()[1]

                plots.arrow(x1,y1,(x2-x1),(y2-y1),length_includes_head=True,width = 0.00003,
                            head_width=0.00022 , color = 'black')
        plots.show()