class Node:
    def __init__(self, data, llink=None, rlink=None):
        self.data = data
        self.ll = llink
        self.rl = rlink

class BST:
    def __init__(self):
        self.root = None
    def is_empty(self):
        '''Return True if empty, False otherwise.'''
        return self.root is None
    def size(self):
        '''Return the number of items in the tree.'''
        return len(self.preorder())
    def height(self):
        '''Return the height of the tree, which is the length of the path from the root to its deepest leaf.'''
        def count(node):
            if node is None:
                return 0
            elif node.ll is None and node.rl is None:
                return 1
            return 1 + max(count(node.ll), count(node.rl)) 
        return count(self.root)
    def add(self, item):
        '''Add item to its proper place in the tree. Return the modified tree.'''
        newNode = Node(item)
        if self.root is None:
            self.root = newNode
        else:
            temp_root = self.root
            follow = None
            while temp_root is not None and temp_root.data != item:
                follow = temp_root
                if item < temp_root.data:
                    temp_root = temp_root.ll
                else:
                    temp_root = temp_root.rl
            if temp_root is not None:
                temp_root.data.count += 1 #.count is because I add class pair from main to the tree
            else:
                if item < follow.data:
                    follow.ll = newNode
                else:
                    follow.rl = newNode
    def remove(self, item):
        '''Remove item from the tree. Return the modified tree.'''
        temp_root = self.root
        parent = None
        right_or_left = 0
        while temp_root is not None and temp_root.data != item:
            parent = temp_root
            if item < temp_root.data:
                temp_root = temp_root.ll
                right_or_left = 0
            else:
                temp_root = temp_root.rl
                right_or_left = 1
        if temp_root is None:
            return ValueError
        elif temp_root.ll is None and temp_root.rl is None: # leaf node
            if right_or_left == 1:
                parent.rl = None
            else:
                parent.ll = None
        elif temp_root.ll is None or temp_root.rl is None: # node has one child
            if right_or_left == 1:
                if temp_root.ll is not None:
                    parent.rl = temp_root.ll
                else:
                    parent.rl = temp_root.rl
            else:
                if temp_root.ll is not None:
                    parent.ll = temp_root.ll
                else:
                    parent.ll = temp_root.rl
        else: # node has two children
            # get the min item of right side (one step right, all the way to the left)
            min_root = temp_root.rl # one step right
            min_parent = None
            while min_root.ll is not None: # all the way to the left
                min_parent = min_root
                min_root = min_root.ll
            # place min data in spot of removal data
            temp_root.data = min_root.data
            # delete min item and deal with its children which will only be one child or none
            if min_root.rl is None: # no children
                min_parent.ll = None
            else: # one child
                min_parent.ll = min_root.rl
    def find(self, item):
        '''Return the matched item. If item is not in the tree, raise a ValueError.'''
        temp_root = self.root
        while temp_root is not None and temp_root.data != item:
            if item < temp_root.data:
                temp_root = temp_root.ll
            else:
                temp_root = temp_root.rl
        if temp_root is not None:
            return temp_root
        else:
            raise ValueError
    def inorder(self):
        '''Return a list with the data items in order of inorder traversal.'''
        in_ord_lyst = []
        stack = []
        temp_root = self.root
        while temp_root is not None or len(stack) != 0:
            while temp_root is not None:
                stack.append(temp_root)
                temp_root = temp_root.ll
            if len(stack) != 0:
                temp_root = stack.pop() #the top of the stack
                in_ord_lyst.append(temp_root.data)
                temp_root = temp_root.rl
        return in_ord_lyst
    def preorder(self):
        '''Return a list with the data items in order of preorder traversal.'''
        pre_ord_lyst = []
        stack = []
        temp_root = self.root
        while temp_root is not None or len(stack) != 0:
            while temp_root is not None:
                pre_ord_lyst.append(temp_root.data)
                stack.append(temp_root)
                temp_root = temp_root.ll
            if len(stack) != 0:
                temp_root = stack.pop() #the top of the stack
                temp_root = temp_root.rl
        return pre_ord_lyst
    def postorder(self):
        '''Return a list with the data items in order of postorder traversal.'''
        post_ord_lyst = []
        def recurse(node):
            if node is not None:
                recurse(node.ll)
                recurse(node.rl)
                post_ord_lyst.append(node.data)
        recurse(self.root)
        return post_ord_lyst
    def rebalance(self):
        '''Rebalance the tree. Return the modified tree.'''          
        # 1.do an inorder traversal of the tree and write the node values out to a list. 
        # If you wish you can use a generator to easily create this list.
        in_ord_lyst = self.inorder()
        # 2.take the middle value as root
        def rebuild(list):
            mid = (len(list) - 1) // 2
            if len(list) != 0:
                #basically took my add function and put it here
                newNode = Node(list[mid])
                if newNode.data == in_ord_lyst[(len(in_ord_lyst) - 1) // 2]:
                    self.root = newNode
                else: 
                    temp_root = self.root
                    follow = None
                    while temp_root is not None and temp_root.data != list[mid]:
                        follow = temp_root
                        if list[mid] < temp_root.data:
                            temp_root = temp_root.ll
                        else:
                            temp_root = temp_root.rl
                    if list[mid] < follow.data:
                        follow.ll = newNode
                    else:
                        follow.rl = newNode
        # 3.split the list in left and right halves, excluding the middle value
                right_lyst = list[mid+1:]
                left_lyst = list[:mid]
        # 4.recursively rebuild the tree, using steps 2 and 3 until done.
                rebuild(left_lyst)
                rebuild(right_lyst)
        rebuild(in_ord_lyst)