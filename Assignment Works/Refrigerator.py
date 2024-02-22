class Refrigerator:
   #Asking User the Name and Price
    def get_data(self):
        print("\t****BOSCH INDIA Pvt Limited******")
        self.customer_name = input("Enter the Customer Name:")
        self.price = int(input("Enter the Total amount Purchase:"))
   

    #Calculating Discoutn
    def compute_discount(self):
        if self.price <= 25000:
            return 2000
        elif 25000 < self.price <= 50000:
            return 5000
        else:
            return 10000
        
    #Printing the Details of the Customer
    
    def display_details(self):
        discount = self.compute_discount()
        final_price = self.price - discount
        print("\t****Bill******")
        print(f"Name of the Customer: {self.customer_name}")
        print(f"Total Amount Purchased: {self.price}")
        print(f"Discount Amount: {discount}")
        print(f"Total Bill Amount: {final_price}")



# Create an object of the class and call its members and methods
fridge = Refrigerator()
fridge.get_data()
fridge.display_details()



#Final One

'''class Refrigerator:
    #Constructor
    def __init__(self, customer_name, price):
        self.customer_name = customer_name
        self.price = price

    #Calculating Discoutn
    def compute_discount(self):
        if self.price <= 25000:
            return 2000
        elif 25000 < self.price <= 50000:
            return 5000
        else:
            return 10000
        
    #Printing the Details of the Customer
    
    def display_details(self):
        discount = self.compute_discount()
        final_price = self.price - discount
        print("\t****Bill******")
        print(f"Name of the Customer: {self.customer_name}")
        print(f"Total Amount Purchased: {self.price}")
        print(f"Discount Amount: {discount}")
        print(f"Total Bill Amount: {final_price}")

#Asking User the Name and Price
print("\t****BOSCH INDIA Pvt Limited******")
customer_name = input("Enter the Customer Name:")
price = int(input("Enter the Total amount Purchase:"))

# Create an object of the class and call its members and methods
fridge = Refrigerator(customer_name, price)
fridge.display_details()
'''
