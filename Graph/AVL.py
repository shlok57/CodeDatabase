# cook your dish here
import time

class Node:
	
	def __init__(self,key):
		self.left = None
		self.right = None
		self.parent = None
		self.val = key
		self.depth = 0
		self.height = 0
	 
	def Get_Height(self, node):
		if(node == None):
			return -1
		else:
			left_height = node.left.height if node.left else -1
			right_height = node.right.height if node.right else -1
			return max(left_height,right_height) + 1

	def Insert(self,key):
		temp = None
		if(key <= self.val):
		  if(self.left == None):
		    temp = Node(key)
		    temp.parent = self
		    temp.depth = self.depth + 1
		    self.left = temp        
		  else:
		    self.left.Insert(key)
		else:
		  if(self.right == None):
		    temp = Node(key)
		    temp.parent = self
		    temp.depth = self.depth + 1
		    self.right = temp
		  else:
		    self.right.Insert(key)
		self.Set_Height(self)    
		global a, root 
		if(temp != None):
		  temp_root = self.Balance_Tree(temp, temp.val)
		  if(root != 0):
		    a = temp_root #-> not always....only when root
		  else:
		    self = temp_root

	def Print_Preorder(self,node):
		print(node.val, node.height, node.depth)
		if(node.left != None):
			self.Print_Preorder(node.left)
		if(node.right != None):
			self.Print_Preorder(node.right)
			
	def Print_Parent(self):
		print(self.parent.val)
	
	def Reduce_Depth(self):
		if(self.left != None):
			self.left.Reduce_Depth()
		if(self.right != None):
			self.right.Reduce_Depth()
		self.depth = self.depth - 1
		
	def Increase_Depth(self):
		if(self.left != None):
			self.left.Increase_Depth()
		if(self.right != None):
			self.right.Increase_Depth()
		self.depth = self.depth + 1
				
	def Delete(self):  
		if(self.left == None and self.right == None):         ### Deletion of leaf node
			if(self.val > self.parent.val):
				self.parent.right = None
			else:
				self.parent.left = None
		elif(self.left == None):                              ### Deletion of node with no left child
			if(self.val > self.parent.val):
				self.parent.right = self.right
			else:
				self.parent.left = self.right
			self.right.Reduce_Depth()
		elif(self.right == None):                             ### Deletion of node with no right child
			if(self.val > self.parent.val):
				self.parent.left = self.left
			else:
				self.parent.right = self.left
			self.left.Reduce_Depth()
		else:                                                 ### Deletion of node with both children
			#find next max
			next_max = self.right
			while(next_max.left != None):
				next_max = next_max.left
			#save
			temp_val = next_max.val
			#delete next max node
			next_max.Delete()
			#replace
			self.val = temp_val
		self.Update_Height(self.parent)                       ### Update Height of its parent

	def Update_Height(self,node):
		node.height = self.Get_Height(node)    
		if(node.parent != None):
			self.Update_Height(node.parent)

	def Search(self,key):
		if(self.val == key):
			print(self.val, self.depth)
		elif(self.val < key):
			if(self.right != None):
				self.right.Search(key)
			else:
				print("Key not found")
				return
		else:
			if(self.left != None):
				self.left.Search(key)
			else:
				print("Key not found")
				return

	def Rotate_Left(self):
		global root,a
		root = 0
		if(self.parent == None):
			root = 1
		if(self.parent != None and self.val > self.parent.val):
			self.parent.right = self.right
		elif(self.parent != None):
			self.parent.left = self.right
		self.right.parent = self.parent
		temp = self.right.left
		self.parent = self.right
		self.right.left = self
		self.right = temp
		self.parent.depth = self.parent.depth - 1
		if(self.parent.right != None):
			self.parent.right.Reduce_Depth()
		self.depth = self.depth + 1
		if(self.left != None):
			self.left.Increase_Depth()
		self.Update_Height(self)
		a = self.parent if root else a

	def Rotate_Right(self):
		global root,a
		root = 0
		if(self.parent == None):
			root = 1
		if(self.parent != None and self.val < self.parent.val):
			self.parent.left = self.left
		elif(self.parent != None):
			self.parent.right = self.left
		self.left.parent = self.parent
		temp = self.left.right
		self.parent = self.left
		self.left.right = self
		self.left = temp
		self.parent.depth = self.parent.depth - 1
		if(self.parent.left != None):
			self.parent.left.Reduce_Depth()
		self.depth = self.depth + 1
		if(self.right != None):
			self.right.Increase_Depth()
		self.Update_Height(self)
		a = self.parent if root else a

	def Balance_Tree(self, node, key):
		global root
		root = 0
		temp_bal = node.Get_Balance() 
		while(abs(temp_bal) <= 1 and node.parent):
			node = node.parent
			temp_bal = node.Get_Balance()
		if(node.parent == None):
			root = 1
		if(temp_bal > 1 and node.left.val > key):
			#just right - left left case
			node.Rotate_Right()
		elif(temp_bal > 1 and node.left.val < key):
			#left right case -
			node.left.Rotate_Left()
			node.Rotate_Right()
		elif(temp_bal < -1 and node.right.val < key):
			#just left - right right case
			node.Rotate_Left()
		elif(temp_bal < -1 and node.right.val > key):
			#left right case - 
			node.right.Rotate_Right()
			node.Rotate_Left()
		else:
			return node
		if(root == 1 and node.parent):
			return node.parent
		else:
			return node

	def Get_Balance(self):
		left_height = self.left.height + 1 if self.left else 0
		right_height = self.right.height + 1 if self.right else 0
		return  left_height - right_height

	def Set_Height(self,node):
		node.height = self.Get_Height(node)
		if(node.parent != None):
			self.Set_Height(node.parent)						

start_time = time.time()	
root = 0  
a = Node(11)
a.Insert(7)
a.Insert(12)
a.Insert(5)
a.Insert(13)
a.Insert(6)
a.Insert(8)
a.Insert(9)
a.Insert(10)
a.Print_Preorder(a)
print()
print("--- %s seconds ---" % (time.time() - start_time))
# a.Insert(10)
# a.Print_Preorder(a)
# print()
# a.Insert(9)
# a.Print_Preorder(a)
# print()