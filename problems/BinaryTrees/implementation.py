from collections import deque
class TreeNode:
    def __init__(self, value, left= None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.value)



    ### Preorder Traversal (root -> left -> right)
    def pre_order(self, node):
        if not node:
            return 
        print(node)
        self.pre_order(node.left)
        self.pre_order(node.right)
    ### Inorder Traversal (left -> root -> right)

    def in_order(self, node):
        if not node:
            return
        self.in_order(node.left)
        print(node)
        self.in_order(node.right)
    ### Postorder Traversal (left -> right -> root)
    def post_order(self, node):
        if not node:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node)

    def pre_order_iterative(self, node):
        stack = [node]

        while stack:
            node = stack.pop()
            print(node)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
    
    ## Level order Traversal - Breadth First Search (BFS)

    def level_order(self, node):
        q = deque()
        q.append(node)

        while q:
            node = q.popleft()
            print(node)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

    def search(self, node, target):
        if not node:
            return False
        
        if node.value == target:
            return True
        return self.search(node.left, target) or self.search(node.right, target)





A = TreeNode(1)
B = TreeNode(2)
c = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F =  TreeNode(10)
A.left = B
A.right = c
B.left = D
B.right = E
c.left = F

print(A.search(A, 13))
