
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

  def __repr__(self):
    return f'Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}'

  def to_html(self)-> str:
    if self.value is None:
      raise ValueError("Invalid HTML: invalid html")
    if self.tag is None:
      return self.value
    if self.props:
      return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'

    return f'<{self.tag}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
  def __init__(self, tag=None, children=None, props=None):
    super().__init__(tag, children=children, props=props)

  def __repr__(self):
    return f'Tag: {self.tag}, Children: {self.children}, Props: {self.props}'

  def to_html(self):
    if self.tag is None:
        raise ValueError("Invalid HTML: no tag")
    if self.children is None:
        raise ValueError("Invalid HTML: no children")
    children = ''.join(child.to_html() for child in self.children)
    return f'<{self.tag}>{children}</{self.tag}>'





