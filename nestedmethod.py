class Test:
    def m1(self):
        def sum(a, b):
            print("first argument ",a)
            print("second argument ",b)
            print("add: ",a+b)
            print("product: ",a*b)
            print("divison: ",a/b)
        sum(100,300)
        sum(100,30880)
        sum(100777,300)
        sum(100,3007654)
        sum(1099999,309)

t = Test().m1()