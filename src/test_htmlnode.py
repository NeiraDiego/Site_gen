import unittest
from htmlnode import HTMLNode

#self, tag: str|None=None, value: str|None=None, children: list|None=None, props: dict|None=None
class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a","home",None,{"href":"www.kamadi.cl"})
        node2 = HTMLNode("a","home",None,{"href":"www.kamadi.cl"})
        self.assertEqual(node, node2)

    def test_eq_dif_prop(self):
        node = HTMLNode("a","home",None,{"href":"www.kamadi.cl"})
        node2 = HTMLNode("a","home",None,{"href":"www.google.cl"})
        self.assertNotEqual(node, node2)

    def test_eq_dif_tag(self):
        node = HTMLNode("a","home",None,{"href":"www.kamadi.cl"})
        node2 = HTMLNode("p","home",None,{"href":"www.kamadi.cl"})
        self.assertNotEqual(node, node2)

    def test_eq_dif_value(self):
        node = HTMLNode("a","casita",None,{"href":"www.kamadi.cl"})
        node2 = HTMLNode("a","home",None,{"href":"www.kamadi.cl"})
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
