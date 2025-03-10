class bst:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

root = bst(10)
print(root.key)
print(root.lchild)
print(root.rchild)