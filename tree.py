class TreeNode:
    def __init__(self, right= None, left=None, parent=None):
        self.right = right
        self.left = left
        self.parent = parent

    def hasLeft(self):
        return self.left

    def hasBouth(self):
        return self.right and self.left

    def hasRight(self):
        return self.right

    def addParent(self, parent):
        if not parent.left:
            parent.left = self
        elif not parent.right:
            parent.right = self
        else:
            return False
        self.parent = parent
        return True

    def __repr__(self):
        return "TreeNode({},{},{})".format("Object" if isinstance(self.right, TreeNode) else self.right, self.left, "None" if not isinstance(self.parent, TreeNode) and self.parent is not None else "Obejct")
