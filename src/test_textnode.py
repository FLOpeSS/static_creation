import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("this is a text node", "bold", "https://localhost:8000/")
    node2 = TextNode("this is a text node", "bold", "https://localhost:8000/")

    self.assertEqual(node, node2)

  def strig_repr(self):
    node = TextNode("this is a text node", "bold", "https://localhost:8000/")
    expected_str = "TextNode(this is a text node, bold, https://localhost:8000/)"
    self.assertEqual(str(node), expected_str)



if __name__ == "__main__":
  unittest.main()



