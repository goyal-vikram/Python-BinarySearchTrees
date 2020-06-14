class binary_search_tree:
    """ This function is a constructor to define a new node in existing tree.
        The new node will have left and right pointers set to None.
    """
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data
    
    """ This function will insert the new data into the tree at a sorted place.
        This function will not balance the tree. If balanced tree is requried then balance_tree() function can be called.
    """
    def insert_sorted(self, data):
        if data < self.data:
            if self.left:
                self.left.insert_sorted(data)
            else:
                self.left = binary_search_tree(data)
        else:
            if self.right:
                self.right.insert_sorted(data)
            else:
                self.right = binary_search_tree(data)
    
    """ This function will return the tree nodes in a list object named list_out using inorder traversal method.
    """
    def inorder_traversal(self, list_out):
        if self.left:
            self.left.inorder_traversal(list_out)
        
        list_out.append(self.data)
        
        if self.right:
            self.right.inorder_traversal(list_out)
    
    """ This function will return the tree nodes in a list object named list_out using preorder traversal method.
    """
    def preorder_traversal(self, list_out):
        list_out.append(self.data)
        
        if self.left:
            self.left.preorder_traversal(list_out)
        
        if self.right:
            self.right.preorder_traversal(list_out)
    
    """ This function will return the tree nodes in a list object named list_out using postorder traversal method.
    """
    def postorder_traversal(self, list_out):
        if self.left:
            self.left.postorder_traversal(list_out)
        
        if self.right:
            self.right.postorder_traversal(list_out)
    
        list_out.append(self.data)
    
    """
    """
