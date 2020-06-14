class binary_search_tree:
    """ Constructor function to define a new node in existing tree.
        The new node will have left and right pointers set to None.
    """
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data
    
    """ Function to insert new data into the tree at a sorted place.
        This function will not balance the tree. If balanced tree is requried then balance_tree() function can be called after adding a node.
    """
    def insert_sorted(self, data = None):
        if data == None:
            return
        
        if self.data == None:
            self.data = data
            return
        
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
    
    """ Function to return the tree nodes in a list object named list_out after parsing tree using inorder traversal method.
    """
    def inorder_traversal(self, list_out):
        if self.left:
            self.left.inorder_traversal(list_out)
        
        list_out.append(self.data)
        
        if self.right:
            self.right.inorder_traversal(list_out)
    
    """ Function to return the tree nodes in a list object named list_out after parsing tree using preorder traversal method.
    """
    def preorder_traversal(self, list_out):
        list_out.append(self.data)
        
        if self.left:
            self.left.preorder_traversal(list_out)
        
        if self.right:
            self.right.preorder_traversal(list_out)
    
    """ Function to return the tree nodes in a list object named list_out after parsing tree using postorder traversal method.
    """
    def postorder_traversal(self, list_out):
        if self.left:
            self.left.postorder_traversal(list_out)
        
        if self.right:
            self.right.postorder_traversal(list_out)
        
        list_out.append(self.data)
    
    """ Function to return the tree nodes in a dictionary object named dict_out after diagonal travesal.
        For example the tree           10                will return the output dict_out[0] = [10, 14, 16]
                                      /  \                                      dict_out[1] = [8, 12]
                                    8     14                                    dict_out[2] = [4]
                                   /     /  \
                                  4    12    16
    """
    def diagonal_traversal(self, dict_out, d):
        if self.left:
            self.left.diagonal_traversal(dict_out, d + 1)
        
        try:
            dict_out[d].append(self.data)
        except KeyError:
            dict_out[d] = [self.data]
        
        if self.right:
            self.right.diagonal_traversal(dict_out, d)

    """ Function to check if this tree is a Binary Search Tree or not
    """
    def check_binary_search_tree(self):
        pass

t1 = binary_search_tree()

t1.insert_sorted(23)
t1.insert_sorted(56)
t1.insert_sorted(67)
t1.insert_sorted(35)
t1.insert_sorted(12)
t1.insert_sorted(90)

list_out = []
t1.inorder_traversal(list_out)
print(list_out)

list_out = []
t1.preorder_traversal(list_out)
print(list_out)

list_out = []
t1.postorder_traversal(list_out)
print(list_out)

dict_out = dict()
t1.diagonal_traversal(dict_out, 0)
print(dict_out)
