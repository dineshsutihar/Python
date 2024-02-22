class test:
    print("test 1")
    @staticmethod
    def show(x,y):
        print("test 2")
        return x+y

#d=test()
#test.show=staticmethod(test.show)
print(test.show(10,10))
