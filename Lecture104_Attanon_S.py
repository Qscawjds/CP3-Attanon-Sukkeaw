class Customer:
    name = ""
    lastname = ""
    age = 0
    
    def addCart(self):
        print("Added to ",self.name,self.lastname,"'s cart")

customer1 = Customer()
customer1.name = "John"
customer1.lastname = "Smith"
customer1.age = 20
customer1.addCart()

customer2 = Customer()
customer2.name = "Kaine"
customer2.lastname = "Bruth"
customer2.age = 18
customer2.addCart()

customer3 = Customer()
customer3.name = "Black"
customer3.lastname = "Adam"
customer3.age = 32
customer3.addCart()

customer4 = Customer()
customer4.name = "Luca"
customer4.lastname = "Calson"
customer4.age = 28
customer4.addCart()

