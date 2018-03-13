import string

class HashTable:

	def __init__(self):
		self.hash_array = [HashNode(i) for i in range(10000)]

	def get_hash(self, word):
		result = 0
		for c in word:
			result = (result * 131 + ord(c)) % 10000
		return result

	def find(self, key):
		key = key.translate(None, string.punctuation).lower()
		key_node = self.search(key)
		if key_node:
			return key_node.count
		else:
			return -1

	def search(self, key):
		# key = key.translate(None, string.punctuation).lower()
		key_hash = self.get_hash(key)
		hash_node = self.hash_array[key_hash]

		key_node = None
		# search if exists
		while hash_node:
			if hash_node.word == key:
				key_node = hash_node
				break
			hash_node = hash_node.next
		return key_node

	def insert(self, key, value = -1, pos = -1):
		key = key.translate(None, string.punctuation).lower()
		key_node = self.search(key)
		key_hash = self.get_hash(key)
		if key_node:
			if value == -1:
				key_node.increase_count(pos)
			else:
				key_node.count = value
		else:
			temp_next = self.hash_array[key_hash].next
			self.hash_array[key_hash].next = HashNode(key, pos)
			self.hash_array[key_hash].next.next = temp_next

	def delete(self,key):
		key = key.translate(None, string.punctuation).lower()
		key_hash = self.get_hash(key)
		hash_node = self.hash_array[key_hash]

		prev_node = hash_node
		main_node = hash_node.next
		# search if exists
		while main_node:
			if main_node.word == key:
				break
			prev_node = main_node
			main_node = main_node.next
		if main_node:
			prev_node.next = main_node.next		
		else:
			print "Key Error"
	
	def increase(self, key):
		key = key.translate(None, string.punctuation).lower()
		key_node = self.search(key)
		if key_node:
			key_node.increase_count()
		else:
			print "Key Error"		

	def list_keys(self):
		key_list = []
		for i in range(10000):
			temp = self.hash_array[i].next
			if temp != None:
				while temp:
					key_list.append(temp.word)
					temp = temp.next
		return key_list

	def print_hash(self):
		for i in range(10000):
			temp = self.hash_array[i].next
			if temp != None:
				while temp:
					print "||", temp.word, ">" , str(temp.count), ">", str(temp.positions), "||\t\t",
					temp = temp.next
				print


class HashNode:

	def __init__(self, word, pos = -1):
		self.word = word
		self.count = 1
		self.next = None
		self.positions = []
		if pos != -1:
			self.positions.append(pos)

	def increase_count(self, pos = -1):
		self.count += 1
		if pos != -1:
			self.positions.append(pos)

H = HashTable()

if __name__ == '__main__':
	wc = 0
	with open('testFile.txt', 'r') as f:
		for line in f:
			B = line.split()
			for i in B:
				wc += 1
				H.insert(i, -1, wc)

	print H.find('soon')
	H.increase('soon')
	print H.find('soon')
	H.delete('soon')
	print H.find('soon')

	H.print_hash()