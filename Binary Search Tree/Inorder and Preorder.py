class bst:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = bst(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = bst(data)

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
            print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()
            print(self.key, end=" ")

root = bst(10)
list1 = [20,4,30,4,1,5,6]
for i in list1:
    root.insert(i)
print('In order')
root.inorder()

