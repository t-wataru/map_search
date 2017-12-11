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

queue = [root]

def func(a, queue):
  if a==None:
    return
  queue+=[a.left, a.right]
  print a.text

root.write()
print map(lambda a:func(a, queue), queue)
