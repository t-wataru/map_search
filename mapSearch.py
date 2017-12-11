class Node:
  def __init__(self, left, right, text):
    self.text = text
    self.left = left
    self.right = right

  def write(self):
    print "[", self.text,
    if self.left != None: self.left.write(),
    if self.right != None: self.right.write(),
    print "]",

root = Node( Node ( Node( None, None, "aiu"), None, "fjal;"), Node(None, None, "qwer"), "root")

stack = [root]

def func(a, stack):
  if a==None:
    return
  stack+=[a.left, a.right]
  print a.text

root.write()
print map(lambda a:func(a, stack), stack)
