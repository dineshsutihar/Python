'''

class OrganizationAddress:
	def __init__(self,Name,City,state):
		self.Name=Name
		self.City=City
		self.state=state

	def display_organization_address(self):
		print(f"Organization Address:{Name} from {City}, {state}")

class HomeAddress:
	def __init__(self,Nam1,Cit1,stat1):
		self.Name=Nam1
		self.City=Cit1
		self.state=stat1
	
	def display_organization_address(self):
		print(f"Home Address: {Name} from {City}, {state}")


class DeliveryBoy(HomeAddress,OrganizationAddress):
	def __int__(self,Name,City,state,Name,City,state):
		

delivery_boy=DeliveryBoy("Prabhu","Kanakapura","Karnataka","Prabhu","Jain","Karnataka")
delivery_boy.display_organization_address()
delivery_boy.display_home_address()
'''

#Lab Sheet 8 b code is written below:

class OrganizationAddress:
    def __init__(self, Nam1, Cit1, Stat1):
        self.Nam1 = Nam1
        self.Cit1 = Cit1
        self.Stat1 = Stat1

    def display_organization_address(self):
        print(f"Organization Address: {self.Nam1} from {self.Cit1}, {self.Stat1}")


class HomeAddress:
    def __init__(self, Name, City, State):
        self.Name = Name
        self.City = City
        self.State = State

    def display_home_address(self):
        print(f"Home Address: {self.Name} from {self.City}, {self.State}")


class DeliveryBoy(HomeAddress, OrganizationAddress):
    def __init__(self, Name1, City1, State1, Name2, City2, State2):
        HomeAddress.__init__(self, Name1, City1, State1)
        OrganizationAddress.__init__(self, Name2, City2, State2)


delivery_boy = DeliveryBoy("Prabhu", "Kanakapura", "Karnataka", "Prabhu", "Jain", "Karnataka")
delivery_boy.display_organization_address()
delivery_boy.display_home_address()

