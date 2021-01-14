
from DiGraph.src.GraphInterface import GraphInteface
from typing import Dict
from DiGraph.src.Node import Node_Data
from DiGraph.src.Edge import Edge_Data
class DiGraph(GraphInteface):



    def __init__(self):
        self.__edge_size=0
        self.__mc=0
        self.__nodes : Dict[int,Node_Data]=dict()
        self.__edges : Dict[int,Dict[int,Edge_Data]]=dict()

    """
       returns the vertex(nodes) size in the graph
       """
    def v_size(self) -> int:
        return len(self.__nodes)

    """
        returns the edges size in the graph
        """
    def e_size(self) -> int:
        return self.__edge_size

    def get_mc(self) -> int:
        return self.__mc

    """
           the function adds an edge between two nodes,
           gets the key of the source node, the key of the destination node and
           the weight of this edge.
           the function returns False if the nodes are not exits
           """
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 is not id2 and id1 in self.__nodes and id2 in self.__nodes and id2 not in self.__edges.get(id1):
            edge = Edge_Data(id1,id2,weight)
            self.__edges.get(id1).update({id2:edge})
            self.__nodes.get(id1).out_e+=1
            self.__nodes.get(id2).in_e += 1
            self.__mc+=1
            self.__edge_size+=1
            return True
        else: return False

    """
           the function adds node to the graph
           gets a key of a node and position (x,y,z) to be inserted to the new node
           the function returns False if the node is already exits in this graph
           """
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.__nodes:
            node = Node_Data(node_id,pos)
            self.__nodes.update({node_id: node})
            self.__edges.update({node_id:dict()})
            self.__mc+=1
            return True
        else: return False

    """
            the function gets a key of a node,
            and returns True if the node was deleted
            """
    def remove_node(self, node_id: int) -> bool:
        if node_id in self.__nodes:
            all_out=self.all_out_edges_of_node(node_id)
            all_in = self.all_in_edges_of_node(node_id)
            self.__mc+=len(all_out)+len(all_in)
            self.__edge_size-= len(all_out) + len(all_in)
            for x in all_in:
                self.__edges.get(x).pop(node_id)
            self.__edges.pop(node_id)
            self.__mc+=1
            self.__nodes.pop(node_id)
            return True
        else: return False

    """
            the function gets the key of the source node, the key of the destination node,
            and returns true if the edge was removed else,false
            """
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 is not node_id2 and node_id1 in self.__nodes and node_id2 in self.__nodes and node_id2 in self.__edges.get(node_id1):
            self.__edges.get(node_id1).pop(node_id2)
            self.__nodes.get(node_id1).out_e-=1
            self.__nodes.get(node_id2).in_e -= 1
            self.__mc += 1
            self.__edge_size -= 1
            return True
        else:
            return False

    """ the function returns all the values of node in the graph
    
         """
    def get_all_v(self) -> dict:
        return self.__nodes

    """
       the function gets node and returns a dictionary of edges that get into this node 
    """
    def all_in_edges_of_node(self, id1: int) -> dict:
        ans:Dict[int,Edge_Data]=dict()
        for x in self.__nodes:
            if id1 in self.__edges.get(x):
                ans.update({x:self.__edges.get(x)[id1]})
        return ans

    """
           the function gets node and returns all the edges that come out from this node
        """
    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.__edges.get(id1)

    def __repr__(self):
        return "Graph: |V|=%s , |E|=%s"%(self.v_size(),self.e_size())