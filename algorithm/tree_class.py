class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None        

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val: int) -> 'self':
        if self.root is None:
            self.root = TreeNode(val)
            return self
        
        def _insert(val: int, node: TreeNode) -> 'self':
            if val < node.val:
                if node.left: _insert(val, node.left)
                else: node.left = TreeNode(val)
            elif val > node.val:
                if node.right: _insert(val, node.right)
                else: node.right = TreeNode(val)
                
        _insert(val, self.root)
        return self

    def show(self) -> [int]:
        values = []
        def _show(node: TreeNode, height = 0) -> [int]:
            while len(values) <= height:
                values.append([])
            if node is None:
                values[height].append(None)
                return

            values[height].append(node.val)
            _show(node.left, height + 1)
            _show(node.right, height + 1)
            
        _show(self.root)
        return [ val for sublist in values for val in sublist ]

