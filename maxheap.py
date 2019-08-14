class Maxheap:
	def __init__(self):
		self.heap=[0]
	
	def push(self,data):
		if self.heap==[0]:
			self.heap.append(data)
			
		elif len(self.heap)==2:
			self.heap.append(data)
			if self.heap[1]<self.heap[-1]:
				self.swap(1,len(self.heap)-1)
				
		else:
			self.heap.append(data)
			self.bubble_up(len(self.heap)-1)
		
	def pop(self):
		if len(self.heap)==1:
			print('cannot be popped')
			
		elif len(self.heap)<=3:
			self.heap.pop(0)
		
		else:
			self.swap(1,len(self.heap)-1)
			val=self.heap.pop(-1)
			self.bubble_down(1)
		
	def peek(self):
		print(self.heap[1])
		
	def show(self):
		print(self.heap)
		
	def swap(self,i,j):
		self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
		
	
	def bubble_up(self,index):
		parent=index//2
		if index<=1:
			return
		if self.heap[parent]<self.heap[index]:
			self.swap(parent,index)
			self.bubble_up(parent)
		
	
	def bubble_down(self,index):
		left=index*2
		right=(index*2)+1
		largest=index
		
		if len(self.heap)>left and self.heap[largest]<self.heap[left]:
			largest=left
			
		if len(self.heap)>right and self.heap[largest]<self.heap[right]:
			 largest=right
			 
		if index!=largest:
			self.swap(index,largest)
			self.bubble_down(largest)
			

m=Maxheap()
m.push(5)
m.push(7)
m.push(9)
m.push(2)
m.push(11)
m.peek()
m.pop()
m.peek()
m.push(13)
m.push(1)
m.peek()
m.push(99)
m.show()