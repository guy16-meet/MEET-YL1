class Animal() :
	def __init__(self,name,age,color,size):
		self.name=name
		self.age=age
		self.color=color
		self.size=size

	def print_all(self):
		print(self.name)
		print(self.age)
		print(self.color)
		print(self.size)

	def sleep(self,dream):
		print("The animal "+self.name +" is sleeping and dreaming about "+dream)

	def eat(self,food):
		print("The animal "+self.name +" is eating "+food)
dog=Animal("Guy", 15, "brown", "Small") 

dog.print_all()

lion=Animal("Nofar", 5, "orange", "big") 

lion.print_all()

lion.eat("meat")

lion.sleep("flowers")

dog.eat("a steak")

dog.sleep("cats")
