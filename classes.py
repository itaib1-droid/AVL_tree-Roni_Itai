#id1:
#name1:
#username1:
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
	def toAVLTree(self):
		tree = AVLTree()
		tree.root = self
		curr = self
		curr.update_max()

		return tree

	#########################################################################
	''' /* note : 1 more func used by them */ '''
	#########################################################################
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

	""" help functions """

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

		t = node.toAVLTree()
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
		return None, -1, -1

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
		return	

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

		self.rebalance_insertion(node)
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
		t_left = node.left.toAVLTree() if node.left.is_real_node() else AVLTree()
		t_right = node.right.toAVLTree() if node.right.is_real_node() else AVLTree() 


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
		
