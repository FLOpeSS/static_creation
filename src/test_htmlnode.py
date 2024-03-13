import unittest
from htmlnode import HTMLNode

class TestHTMLnode(unittest.TestCase):
  def test_prop_eq(self):
    print("running test prop_to_html")
    html = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    result = html.props_to_html()
    expected_return = ' href="https://www.google.com" target="_blank"'
    self.assertEqual(result, expected_return)


if __name__ == '__main__':
    unittest.main()
