#id1: 207334525
#name1:	Roni Shiri
#username1: ronishiri
#id2: 211325287
#name2: Itai Ben Shahar
#username2: itaib1

"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 
	
	@type key: int
	@param key: key of your node
	@type value: string
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
	
	"""returns whether self is not a virtual node
	 @rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	  """
	def is_real_node(self):
		return self.key is not None and self.value is not None
	
	def __str__(self):
		# print the node's fields
		return (f"Key: {self.key}, value: {self.value}, Height: {self.height}, " \
			f"Left: {self.left.key if self.left else "virt"}, " \
			f"Right: {self.right.key if self.right else "virt"}, "\
            f"Parent: {self.parent.key if self.right else "virt"}")
	
	"""returns whether self is a leaf (real node with no children)
	@rtype: bool
	@returns: True if self is a leaf, False otherwise.
	"""
	def is_leaf(self):
		if self.is_real_node() and not self.right.is_real_node() and not self.left.is_real_node():
			return True
		return False

	"""updates the node's height
	@pre: self.is_real_node() == True
	"""
	def update_height(self):
		self.height = max(self.left.height, self.right.height) + 1

	"""returns the height difference between the current node and its children
	@pre: node is a real node
	@rtype: (int, int)
	"""
	def height_dif(self):
		return (self.height - self.left.height, self.height - self.right.height)
	
	"""returns the height difference between the two children 

	@pre: self.is_real_node() == True
	@rtype: int
	@returns: an int in range(-1, 1)
	"""
	def balance_factor(self):
		if self.is_leaf():
			return 0
		return self.left.height - self.right.height 

	""" converts the node (and its children) to an AVLTree """
	def to_avl_tree(self):
		tree = AVLTree()
		tree.root = self
		curr = self
		curr.update_max()

		return tree

"""
A class implementing an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.
	"""
	def __init__(self):
		self.root = AVLNode(None, None) # sentinel
		self.max = self.root # pointer to node with max key
		self.t_size = 0 

	"""------------------ help functions ------------------"""

	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.t_size
	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		if self.root.is_real_node():
			return self.root
		else:
			return None
	"""returns the node with the maximal key in the dictionary

	@rtype: AVLNode
	@returns: the maximal node, None if the dictionary is empty
	"""
	def max_node(self):
		if self.max.is_real_node():
			return self.max
		else:
			return None
	"""returns the node with the minimal key in the dictionary

	@rtype: AVLNode
	@returns: the minimal node, None if the dictionary is empty
	"""
	def min_node(self):
		node = self.get_root()
		if node is None:
			return None
		while node.left.is_real_node():
			node = node.left
		return node
	"""updates the node with the maximal key in the dictionary 
	@rtype: AVLNode
	@returns: -
	"""
	def update_max(self):
		node = self.get_root()
		if node is None:
			self.max = self.root
			return
		while node.right.is_real_node():
			node = node.right
		self.max = node
	"""returns the successor of a given node in the dictionary

	@rtype: AVLNode
	@returns: the successor of node, None if node is the max
	"""
	def succsessor(self,node):
		## edge case - node is max
		if node == self.max:
			return None     
		if node.right.is_real_node():
			node = node.right
			while node.left.is_real_node():
				node = node.left
			return node
		else:
			## node is right child
			while node.parent.is_real_node() and node.parent.right == node:
				node = node.parent
			return node.parent if node.parent.is_real_node() else None
	
	"""------------------ rebalances and rotations functions------------------ """

	"""rebalancing the tree after inserting a new node so it maintain the AVLTree properties
    @type node: AVLNode
    @rtype: int
    @returns: an int indicating the number of promotes
    """
	def rebalance_insertion(self, node):
		node.update_height()
        # if it's the root
		if node is self.get_root():
			return 1
		bf = node.parent.balance_factor()
		if bf == 0: # both children are a single step from the father
			return 0
		if abs(bf) == 1:
			return self.rebalance_insertion(node.parent) + 1
		else: # abs(bf) == 2 so we rotate
			curr_bf = node.balance_factor()
			# determine the type of rotation needed according to the balance factors
			if bf == 2:
				if curr_bf > 0:
					self.single_rotation_right_ins(node) 
				else:
					self.double_rotation_right_ins(node) 
			else:
				if curr_bf < 0: 
					self.single_rotation_left_ins(node) 
				else:
					self.double_rotation_left_ins(node)
				return 0
	
	"""rotates the sub-tree a single rotation right to keep form of an AVLtree
    @type node: AVLNode
    @returns: None
    """
	def single_rotation_right_ins(self, node):
		## save pointers
		son = node.right
		old_par = node.parent
		node.right = old_par
		new_par = old_par.parent
		node.parent = new_par
		old_par.left = son
		old_par.parent = node
		son.parent = old_par

		# updates heights due to rotation
		old_par.update_height()
		node.update_height()
		# updating the root pointer if needed
		if self.get_root() == old_par:
			self.root = node
		# assigning the sub-tree's head pointers
		elif new_par.key < node.key:
			new_par.right = node
		else:
			new_par.left = node
	"""rotates the sub-tree a single rotation left to keep form of an AVLtree
    @type node: AVLNode
    @returns: None
    """
	def single_rotation_left_ins(self, node):
		## save pointers
		son = node.left
		old_par = node.parent
		node.left = old_par
		new_par = old_par.parent
		node.parent = new_par
		old_par.right = son
		old_par.parent = node
		son.parent = old_par
		# updates heights due to rotation
		old_par.update_height()
		node.update_height()
		# updating the root pointer if needed
		if self.get_root() == old_par:
			self.root = node
		# assigning the sub-tree's head pointers
		elif new_par.key < node.key:
			new_par.right = node
		else:
			new_par.left = node
	"""rotates the sub-tree a double rotation right to keep form of an AVLtree
    @type node: AVLNode
    @returns: None
    """
	def double_rotation_right_ins(self, node):
		#change pointers
		old_par = node.parent
		new_grandpar = node.right
		new_grandpar.parent = old_par.parent
		# original leaves
		right_grandson = new_grandpar.right 
		left_grandson = new_grandpar.left
		# construction of new right sub-tree
		new_grandpar.right = old_par
		old_par.parent = new_grandpar
		old_par.left = right_grandson
		# construction of new left sub-tree
		new_grandpar.left = node
		right_grandson.parent = old_par
		left_grandson.parent = node
		# modifications for originial nodes
		node.right = left_grandson  
		node.parent = new_grandpar
		# updates height due to rotation
		old_par.update_height()
		node.update_height()
		new_grandpar.update_height()
		# updating the root pointer if needed
		if self.get_root() == old_par:
			self.root = new_grandpar
		# assigning the sub-tree's head pointers
		elif new_grandpar.parent.key < new_grandpar.key:
			new_grandpar.parent.right = new_grandpar
		else:
			new_grandpar.parent.left = new_grandpar
	"""rotates the sub-tree a double rotation left to keep form of an AVLtree
    @type node: AVLNode
    @returns: None
    """
	def double_rotation_left_ins(self, node):
		# change pointers
		old_par = node.parent
		new_grandpar = node.left
		new_grandpar.parent = old_par.parent
		# original leaves
		right_grandson = new_grandpar.right 
		left_grandson = new_grandpar.left
		# construction of new left sub-tree
		new_grandpar.left = old_par
		old_par.parent = new_grandpar
		old_par.right = left_grandson
		# construction of new right sub-tree
		new_grandpar.right = node
		left_grandson.parent = old_par
		right_grandson.parent = node
		# modifications for originial nodes
		node.left = right_grandson  
		node.parent = new_grandpar
		# updates height due to rotation
		old_par.update_height()
		node.update_height()
		new_grandpar.update_height()
		# updating the root pointer if needed
		if self.get_root() == old_par:
			self.root = new_grandpar
		# assigning the sub-tree's head pointers
		elif new_grandpar.parent.key < new_grandpar.key:
			new_grandpar.parent.right = new_grandpar
		else:
			new_grandpar.parent.left = new_grandpar
    
	"""rebalancing the the tree after deletion a node so it maintain the AVLTree properties
    @type node: AVLNode
    """
	def rebalance_deletion(self, node):
		# edge case of empty tree
		if not node.is_real_node():
			return 
		dif = node.height_dif()
		## if the node is balanced
		if (dif == (2, 1)) or (dif==(1, 2)): ## balanced
			return 
		elif dif == (2, 2): ## up to parent
			node.update_height()
			self.rebalance_deletion(node.parent)
			return
		# determine the type of rotation needed according to the balance factors
		if dif == (3, 1):
			child_dif = node.right.height_dif() 
			if child_dif == (1, 1): ## R and L - same hight
				self.single_rotation_left_del(node)
			elif child_dif == (2, 1): 
				self.single_rotation_left_del(node)
				self.rebalance_deletion(node.parent.parent)
			else: # child_dif == (1, 2)
				self.double_rotation_left_del(node)
				self.rebalance_deletion(node.parent.parent)
		else: # dif == (1, 3)
			child_dif = node.left.height_dif()
			if child_dif == (1, 1):
				self.single_rotation_right_del(node)
			elif child_dif == (1, 2):
				self.single_rotation_right_del(node)
				self.rebalance_deletion(node.parent.parent)
			else: # child_dif == (2, 1)
				self.double_rotation_right_del(node)
				self.rebalance_deletion(node.parent.parent)
		return 		
			
	"""rotates the sub-tree a single rotation left to keep form of an AVLtree
    @type node: AVLNode
    @returns: None
    """
	def single_rotation_left_del(self, node):
		# establish pointers
		right_child = node.right
		left_grandchild = right_child.left
		# the original sub-tree root's parent
		right_child.parent = node.parent        
		if node is not self.root: # address sentinal 
			if node.parent.key < node.key:
				node.parent.right = right_child
			else:
				node.parent.left = right_child
		# modify pointers
		right_child.left = node
		node.parent = right_child
		node.right = left_grandchild
		left_grandchild.parent = node
		# updating height
		node.update_height()
		right_child.update_height()
		# updating the root pointer if needed
		if self.get_root() == node:
			self.root = right_child
	"""rotates the sub-tree a single rotation right to keep form of an AVLtree
	@type node: AVLNode
	@returns: None
	"""
	def single_rotation_right_del(self, node):
		# establish pointers
		left_child = node.left
		right_grandchild = left_child.right
		# the original sub-tree root's parent
		left_child.parent = node.parent
		if node is not self.root: 
			if node.parent.key < node.key:
				node.parent.right = left_child
			else:
				node.parent.left = left_child
		# modify pointers
		left_child.right = node
		node.parent = left_child
		node.left = right_grandchild
		right_grandchild.parent = node
		# update height
		node.update_height()
		left_child.update_height()
		# updating the root pointer if needed
		if self.get_root() == node:
			self.root = left_child
	"""rotates the sub-tree a double rotation left to keep form of an AVLtree
	@type node: AVLNode
	@returns: None
	"""
	def double_rotation_left_del(self, node):
		# establish pointers
		y=node.right
		a=y.left
		c=a.left
		d=a.right
		a.parent = node.parent
		if node is not self.root: # address sentinal 
			if node.parent.key < node.key:
				node.parent.right = a
			else:
				node.parent.left = a
		# establish right sub-tree
		y.left=d
		d.parent=y
		y.parent=a
		a.right=y
		# establish left sub-tree
		node.right=c
		c.parent=node
		a.left=node
		node.parent=a       
		# update height
		node.update_height()
		y.update_height()
		a.update_height()
		# updating the root pointer if needed
		if self.get_root() == node:
			self.root = a
	"""rotates the sub-tree a double rotation right to keep form of an AVLtree
	@type node: AVLNode
	@returns: None
	"""
	def double_rotation_right_del(self, node):
		# establish pointers
		y=node.left
		a=y.right
		c=a.right
		d=a.left
		a.parent = node.parent
		if node is not self.root: # address sentinal 
			if node.parent.key < node.key:
				node.parent.right = a
			else:
				node.parent.left = a
		# establish left sub-tree
		y.right=d
		d.parent=y
		y.parent=a
		a.left=y
		# establish right sub-tree
		node.left=c
		c.parent=node
		a.right=node
		node.parent=a       
		# update height
		node.update_height()
		y.update_height()
		a.update_height()
		# updating the root pointer if needed
		if self.get_root() == node:
			self.root = a
	

	"""------------------ main functions ------------------"""

	"""searches for a node in the dictionary corresponding to the key (starting at the root)
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
	def search(self, key):
		node = self.get_root()
		edges = 1
		while node.is_real_node():
			if node.key == key:
				return node, edges
			elif key < node.key:
				node = node.left if node.left.is_real_node() else None
			else:
				node = node.right if node.right.is_real_node() else None
			edges += 1
		return None, -1

	"""searches for a node in the dictionary corresponding to the key, starting at the max
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
	def finger_search(self, key):
		node = self.max_node()
		edges = 0
		if node is None:
			return None
		##up the tree
		while node.parent.is_real_node() and node.key > node.parent.key: 
			node = node.parent
			edges += 1

		t = node.to_avl_tree()
		if t.root.key == self.root.key:
			t = self
		ans = t.search(key)

		if ans == (None, 0):
			return None
		else:
			return (ans[0], ans[1] + edges)

	"""inserts a new node into the dictionary with corresponding key and value (starting at the root)

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing
	"""
	def insert(self, key, val):
		## update size && create new node
		self.t_size += 1
		new_n = AVLNode(key, val)
		new_n.left = AVLNode(None, None)
		new_n.right = AVLNode(None, None)
		new_n.update_height()
		rt = self.get_root()
		## empty tree case
		if rt is None:
			self.root = new_n
			self.max = new_n
			return (new_n, 0, 1)

		## insetion
		curr = rt
		edges = 0
		while curr.is_real_node():
			edges += 1
			curr = curr.left if key < curr.key else curr.right
		curr = curr.parent ## one step back
		new_n.parent = curr
		if key < curr.key:
			curr.left = new_n
		else:
			curr.right = new_n

		## update max
		if self.max_node() == None or curr.key >= self.max.key: 
			self.max = new_n
		## rebalance
		promote_count = self.rebalance_insertion(new_node)

		return (new_n, edges, promote_count)
		
	"""inserts a new node into the dictionary with corresponding key and value, starting at the max

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing
	"""
	def finger_insert(self, key, val):
		return None, -1, -1

	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	"""
	def delete(self, node):
		# decrease the tree's size by 1
		self.t_size -= 1
		# initialize variables
		prnt = node.parent
		if node == self.get_root():
			right_son = True
		else: ##i'm a right or left child
			right_son = True if prnt.key < node.key else False
		# if node has two children
		if node.right.is_real_node() and node.left.is_real_node():
			suc = self.successor(node)
			if right_son:
				prnt.right = suc
			else:
				prnt.left = suc           
			if node.right != suc: # the sucsessor is not a direct child of node
				suc.parent.left = suc.right # terminate the original parent of suc from suc 
				suc.right.parent = suc.parent 
				suc.right = node.right
				suc.left.parent = suc.parent
				node.right.parent = suc 	
			# replace node's left pointers with its sucsessor             
			suc.left = node.left
			node.left.parent = suc    
			if suc.parent == node:
				start_balance_node = suc
			else:
				start_balance_node = suc.parent
			suc.parent = prnt
			if node == self.get_root():
				self.root = suc 
			suc.update_height() # suc location changed to be as the deleted node
		# node has one or less children
		elif node.right.is_real_node(): # has only a right child
			if right_son:
				prnt.right = node.right
			else:
				prnt.left = node.right  
			node.right.parent = prnt
			start_balance_node = prnt
			if node == self.get_root():
				self.root = node.right
		# node has a left child, or is a leaf
		else: 
			if right_son:
				prnt.right = node.left
			else:
				prnt.left = node.left   
			node.left.parent = prnt
			start_balance_node = prnt
			# updating the max and root fields if needed            
			if node == self.get_root():
				self.root = node.left
				self.update_max() # find new max
			elif node == self.max_node():
				self.max = prnt

		# rebalancing
		self.rebalance_deletion(start_balance_node)

	"""joins self with item and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: the key separting self and tree2
	@type val: string
	@param val: the value corresponding to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key,
	or the opposite way
	"""
	def join(self, tree2, key, val):
		 # initialize variables
		x = AVLNode(key, val)
		tall, short = (self, tree2) if self.root.height >= tree2.root.height else (tree2 ,self)
		h = short.root.height
		if h == -1: # one of the trees is empty
			tall.insert(x.key, x.value)
			self.root = tall.root
			self.max = tall.max
			self.t_size = tall.size()
			return
		
		curr = tall.root
		if short.root.key < key:
			# short tree has smaller keys
			while curr.height > h: 
				curr = curr.left
			## update pointers
			x.left = short.root
			short.root.parent = x
			origin_par = curr.parent 
			x.right = curr
			curr.parent = x
			origin_par.left = x
			x.parent = origin_par
			## update max
			if tall.max.is_real_node():
				self.max = tall.max
			else:
				self.max = self.root
		else:
			# short tree has larger keys
			while curr.height > h: 
				curr = curr.right
			## update pointers
			x.right = short.root
			short.root.parent = x
			origin_par = curr.parent 
			x.left = curr
			curr.parent = x
			origin_par.right = x
			x.parent = origin_par

			## update max
			if short.max.is_real_node():
				self.max = short.max
			else:
				self.max = self.root

		## epdate root and size
		self.root = x if tall.root.height == short.root.height else tall.root
		self.t_size = tall.size() + short.size() + 1

		self.rebalance_insertion(x)
		return
	
	"""splits the dictionary at a given node

	@type node: AVLNode
	@pre: node is in self
	@param node: the node in the dictionary to be used for the split
	@rtype: (AVLTree, AVLTree)
	@returns: a tuple (left, right), where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, and right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		t_left = node.left.to_avl_tree() if node.left.is_real_node() else AVLTree()
		t_right = node.right.to_avl_tree() if node.right.is_real_node() else AVLTree() 


		while node is not self.root:
			par = node.parent
			curr_t = AVLTree()
			curr_t.max = AVLNode(None, None)
			if node == par.left:  
				## node is left child
				curr_t.root = par.right
				t_right.join(curr_t, par.key, par.value)
			else:
				## node is right child
				curr_t.root = par.left
				t_left.join(curr_t, par.key, par.value)

			t_left.update_max()
			t_right.update_max()
			
		return(t_left, t_right)

	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		node = self.min_node()
		if node is None:
			return []
		arr = []
		while node.is_real_node():
			arr.append((node.key, node.value))
			node = self.succsessor(node)
		return arr
		
