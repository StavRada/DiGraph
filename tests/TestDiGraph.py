import unittest
from DiGraph.src.DiGraph import DiGraph

class TestDiGraph(unittest.TestCase):

    def setUp(self) -> None:
        #before each
        self.graph =DiGraph()

    def test_test1(self):
        self.assertEqual(self.graph.v_size(), 0)
        self.assertTrue(self.graph.add_node(1, (9, 0, 3)))
        self.assertEqual(self.graph.v_size(), 1)
        self.assertEqual(self.graph.get_mc(), 1)

        self.assertFalse(self.graph.add_node(1, (9, 0, 3)))

    def test_test2(self):
        self.assertEqual(self.graph.v_size(), 0)
        self.assertTrue(self.graph.add_node(1, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(2, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(3, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(4, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(5, (9, 0, 3)))
        self.assertTrue(self.graph.add_edge(1, 2, 5))
        self.assertTrue(self.graph.add_edge(2, 3, 1))
        self.assertTrue(self.graph.add_edge(3, 4, 7))
        self.assertTrue(self.graph.add_edge(4, 1, 3))
        self.assertTrue(self.graph.add_edge(4, 5, 10))
        self.assertEqual(self.graph.v_size(), 5)
        self.assertEqual(self.graph.e_size(), 5)
        self.assertEqual(self.graph.get_mc(), 10)

    def test_test3(self):

        self.assertEqual(self.graph.v_size(), 0)
        self.assertTrue(self.graph.add_node(1, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(2, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(3, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(4, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(5, (9, 0, 3)))
        self.assertTrue(self.graph.add_edge(1, 2, 5))
        self.assertTrue(self.graph.add_edge(2, 3, 1))
        self.assertTrue(self.graph.add_edge(3, 4, 7))
        self.assertTrue(self.graph.add_edge(4, 1, 3))
        self.assertTrue(self.graph.add_edge(4, 5, 10))
        self.assertTrue(self.graph.remove_edge(4, 5))

        self.assertEqual(self.graph.v_size(), 5)
        self.assertEqual(self.graph.e_size(), 4)

        self.assertEqual(self.graph.get_mc(), 11)

    def test_test4(self):
        self.assertEqual(self.graph.v_size(), 0)
        self.assertTrue(self.graph.add_node(1, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(2, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(3, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(4, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(5, (9, 0, 3)))
        self.assertTrue(self.graph.add_edge(1, 2, 5))
        self.assertTrue(self.graph.add_edge(2, 3, 1))
        self.assertTrue(self.graph.add_edge(3, 4, 7))
        self.assertTrue(self.graph.add_edge(4, 1, 3))
        self.assertTrue(self.graph.add_edge(4, 5, 10))
        self.assertTrue(self.graph.remove_edge(4, 5))
        self.assertTrue(self.graph.remove_node(5))

        self.assertFalse(self.graph.remove_node(7))
        self.assertEqual(self.graph.v_size(), 4)
        self.assertEqual(self.graph.e_size(), 4)
        self.assertEqual(self.graph.get_mc(), 12)

    def test_test5(self):
        self.assertEqual(self.graph.v_size(), 0)
        self.assertTrue(self.graph.add_node(1, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(2, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(3, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(4, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(5, (9, 0, 3)))
        self.assertTrue(self.graph.add_edge(1, 2, 5))
        self.assertTrue(self.graph.add_edge(2, 3, 1))
        self.assertTrue(self.graph.add_edge(3, 4, 7))
        self.assertTrue(self.graph.add_edge(4, 1, 3))
        self.assertTrue(self.graph.add_edge(4, 5, 10))
        self.assertTrue(self.graph.remove_edge(4, 5))
        self.assertTrue(self.graph.remove_node(5))
        self.assertFalse(self.graph.remove_edge(3, 1))
        self.assertFalse(self.graph.remove_node(7))
        self.assertEqual(self.graph.v_size(), 4)
        self.assertEqual(self.graph.e_size(), 4)
        self.assertEqual(self.graph.get_mc(), 12)
        self.assertEqual(len(self.graph.get_all_v()),4)

    def test_test6(self):   #need to check
       for x in range(10000):
           self.graph.add_node(x,(1,5,3))

       self.assertEqual(self.graph.get_mc(), 10000)

    def test_test7(self):  #need to check
        for x in range(10000):
            self.graph.add_node(x, (1, 5, 3))

        for x in range(0,10000,2):
            self.graph.add_edge(x,x+1,100)

        self.assertEqual(self.graph.get_mc(), 15000)

    def test_test8(self):
        self.assertTrue(self.graph.add_node(1, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(2, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(3, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(4, (9, 0, 3)))
        self.assertTrue(self.graph.add_node(5, (9, 0, 3)))
        self.assertTrue(self.graph.add_edge(1, 2, 5))
        self.assertTrue(self.graph.add_edge(2, 3, 1))
        self.assertTrue(self.graph.add_edge(3, 4, 7))
        self.assertTrue(self.graph.add_edge(4, 1, 3))
        self.assertTrue(self.graph.add_edge(4, 5, 10))
        self.assertEqual(len(self.graph.all_in_edges_of_node(4)),1)
        self.assertEqual(len(self.graph.all_out_edges_of_node(4)), 2)


if __name__ == '__main__':
    unittest.main