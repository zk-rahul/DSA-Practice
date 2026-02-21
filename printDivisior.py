class printDivisior:

    def __init__(self, num):
        self.num = num

    def divisors(self):
        num = abs(self.num)
        div=set()
        for i in range(1,num+1):
            if num % i ==0:
                div.add(i)
        return div

num=int (input("Enter a number:"))
obj = printDivisior(num)   
print("Divisors:", obj.divisors())