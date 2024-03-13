class TextNode():

  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url
  

  def __repr__(self):
    return f'TextNode({self.text}, {self.text_type}, {self.url})'


  def __eq__(self, other):
    if isinstance(other, TextNode):
      return other == self

    return False



class aluno():
  def __init__(self, name):
    self.name = name


  def __repr__(self):
    return f'this is the student: {self.name}'
