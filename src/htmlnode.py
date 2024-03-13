class HTMLNode():
  def __init__(self, tag=None, value=None, children=None, props={}):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props


  def __repr__(self):
    return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

  def to_html(self):
    raise NotImplementedError()

  def props_to_html(self):
     html_attr = ''.join([f' {key}="{value}"' if i > 0 else f'{key}="{value}"' for i, (key, value) in enumerate(self.props.items())])
     return " " + html_attr
