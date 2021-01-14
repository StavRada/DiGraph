import unittest
from DiGraph.src.DiGraph import DiGraph
from DiGraph.src.GraphAlgo import GraphAlgo


class TestGraphAlgo(unittest.TestCase):
    def setUp(self) -> None:
        self.graph =DiGraph()

    def test_load_save(self):

        algo = GraphAlgo()
        self.assertFalse(algo.load_from_json("../data/sadasasdas.json"))
        self.assertTrue(algo.load_from_json("../data/T0.json"))
        self.assertTrue(algo.save_to_json("../data/Test.json"))

        graph = algo.get_graph()

        self.assertEqual(graph.v_size(),4)
        self.assertEqual(graph.e_size(),5)


    def test_shortest_path1(self):

        self.assertTrue(self.graph.add_node(0))
        self.assertTrue(self.graph.add_node(1))
        self.assertTrue(self.graph.add_node(2))

        self.assertTrue(self.graph.add_edge(0,1,1))
        self.assertTrue(self.graph.add_edge(1, 2, 1))
        self.assertTrue(self.graph.add_edge(0, 2, 3))


        algo=GraphAlgo(self.graph)

        p=algo.shortest_path(0,2)
        self.assertEqual(p[0],2)
        self.assertEqual(p[1], [0, 1, 2])

    def test_shortest_path2(self):

        self.assertTrue(self.graph.add_node(0))
        self.assertTrue(self.graph.add_node(1))
        self.assertTrue(self.graph.add_node(2))

        self.assertTrue(self.graph.add_edge(0,1,1))
        self.assertTrue(self.graph.add_edge(1, 2, 1))
        self.assertTrue(self.graph.add_edge(0, 2, 0.5))


        algo=GraphAlgo(self.graph)

        p=algo.shortest_path(0,2)
        self.assertEqual(p[0],0.5)
        self.assertEqual(p[1], [0,2])


    def test_component_s(self):
        self.assertTrue(self.graph.add_node(0))
        self.assertTrue(self.graph.add_node(1))
        self.assertTrue(self.graph.add_node(2))
        self.assertTrue(self.graph.add_node(3))

        self.assertTrue(self.graph.add_edge(0,1,1))
        self.assertTrue(self.graph.add_edge(1, 2, 1))
        self.assertTrue(self.graph.add_edge(2,0, 0.5))
        self.assertTrue(self.graph.add_edge(2, 3, 0.5))

        algo = GraphAlgo(self.graph)
        p=algo.connected_components()
        self.assertEqual(p,[[0,1,2],[3]])
        p=algo.connected_component(3)
        p1 = algo.connected_component(1)
        self.assertEqual(p, [3])
        self.assertEqual(p1, [1, 2, 0])


    def test_plot(self):
        algo = GraphAlgo()
        self.assertTrue(algo.load_from_json("../data/A5"))
        algo.plot_graph()



    def test_connected_components(self):
        g = DiGraph()
        for i in range(1000):
            g6.add_node(i)
            g6.add_edge(i - 1, i, 1)
            if i % 100 != 0:
                g6.add_edge(i, i - 1, 1)
        ga6 = GraphAlgo(g6)
        self.assertEqual(len(ga6.connected_components()), 10)
        ga6.get_graph().add_edge(100, 99, 1)
        self.assertEqual(len(ga6.connected_components()), 9)





if __name__ == '__main__':
    unittest.main