class Animal() :
	def __init__(self,name,age,color,size):
		self.name=name
		self.age=age
		self.color=color
		self.size=size

dog=Animal("Sadek", 22, "yellow", "tiny") 
print(dog.name)
print(dog.age)
print(dog.color)
print(dog.size)