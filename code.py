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
    def check_binary_search_tree(self, list_out, x):
        if self.left:
            x = self.left.check_binary_search_tree(list_out, x)
        
        list_out.append(self.data)
        
        if len(list_out) > 1:
            if list_out[-1] < list_out[-2]:
                x = 'The tree is not a Binary Search Tree'
                return x
        
        if self.right:
            x = self.right.check_binary_search_tree(list_out, x)
        
        return x

    """ Function to balance the tree. The function balance_tree writes the node of tree into a list object named list_out.
        That object is passed to another function tree_balancer, which splits the input list recursively into two halves and
        saves the middle list item as the current sub-tree's data.
    """
    def balance_tree(self):
        list_out = []
        self.inorder_traversal(list_out)
        tree_temp = binary_search_tree(None)
        tree_temp.tree_balancer(list_out)
        return tree_temp
    
    def tree_balancer(self, list_out):
        if len(list_out) == 0:
            return
        
        if len(list_out) == 1:
            self.data = list_out[0]
            return
        
        self.data = list_out[int(len(list_out)/2)]
        left_list = list_out[:int(len(list_out)/2)]
        right_list = list_out[int(len(list_out)/2+1):]
        
        if len(left_list):
            self.left = binary_search_tree(None)
            self.left.tree_balancer(left_list)
        
        if len(right_list):
            self.right = binary_search_tree(None)
            self.right.tree_balancer(right_list)
    
    """ Function to create mirror image of the tree. Note that the resultant tree will not be a Binary Search Tree,
        but it will be return elements in reverse order if done inorder traversal.
        For example the tree           10       will return the output          10
                                      /  \                                     /  \
                                    8     14                                 14    8
                                   /     /  \                               /  \    \
                                  4    12    16                           16    12   4
    """
    def tree_mirror(self):
        if self.left:
            self.left.tree_mirror()
        
        if self.right:
            self.right.tree_mirror()
        
        self.left, self.right = self.right, self.left
    
    """ Function to count the number of leaf nodes in a tree i.e. nodes with no child nodes.
    """
    def leaf_count(self):
        if self.left == None and self.right == None:
            return 1
        
        x = y = 0
        
        if self.left:
            x = self.left.leaf_count()
        
        if self.right:
            y = self.right.leaf_count()
        
        return x + y

""" Test script for various functions
"""
t1 = binary_search_tree(1)
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

x = 'The tree is Binary Search Tree'
list_out = []
x = t1.check_binary_search_tree(list_out, x)
print(x)

t1 = t1.balance_tree()
list_out = []
t1.preorder_traversal(list_out)
print(list_out)

dict_out = dict()
t1.diagonal_traversal(dict_out, 0)
print(dict_out)

t1.tree_mirror()
dict_out = dict()
t1.diagonal_traversal(dict_out, 0)
print(dict_out)

x = t1.leaf_count()
print(x)
