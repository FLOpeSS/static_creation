from textnode import TextNode
from textnode import aluno

text = TextNode("this is a text node", "bold", "https://localhost:8000/")
print(repr(text))

student = aluno("Sebas")
print(repr(student))

# print(repr(text))
# repr(student)
