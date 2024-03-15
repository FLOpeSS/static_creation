class HTMLNode():
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props


  def __repr__(self):
    return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

  def to_html(self):
    raise NotImplementedError()

  def props_to_html(self):
     if self.props is None:
       return ""

     props_html = ""
     for prop in self.props:
       props_html += f' {prop}="{self.props[prop]}"'

     return props_html



class LeafNode(HTMLNode):
  def __init__(self, tag=None, value=None, children=None, props=None):
    super().__init__(tag, value, children, props)

  def to_html(self)-> str:
    if self.value == None or self.value == "":
      raise ValueError

    if self.tag == None or self.tag == "":
      return str(self.value)

    if bool(self.props) != False:
      return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'

    return f'<{self.tag}>{self.value}</{self.tag}>'

