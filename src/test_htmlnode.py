import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLnode(unittest.TestCase):
  def test_prop_eq(self):
    print("running test prop_to_html")
    html = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    result = html.props_to_html()
    expected_return = ' href="https://www.google.com" target="_blank"'
    self.assertEqual(result, expected_return)


class TestLeafNode(unittest.TestCase):
  def test_to_html(self):
    print("testing test_to_html")
    leaf = LeafNode("p", "hello world", children=None, props={"href": "https://www.google.com"})
    html_text = leaf.to_html()
    expected_return = '<p  href="https://www.google.com">hello world</p>'
    self.assertEqual(html_text, expected_return)

  def test_to_html_no_props(self):
    print("testing to html with no props")
    leaf = LeafNode("p", "hello world", None, None) 
    result = leaf.to_html()
    expected_return = '<p>hello world</p>'
    self.assertEqual(result, expected_return)


if __name__ == '__main__':
    unittest.main()
