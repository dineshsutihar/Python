# 17-05-2023
class Banner:
    
    @staticmethod
    def get_banner():
        return input("Enter the University Name: ")
    
    @staticmethod
    def display_banner(name):
        print(f"University name is {name}")

name=Banner.get_banner()
Banner.display_banner(name)