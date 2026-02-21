class DigitCounter:

    def __init__(self, num):
        self.num = num

    def digit_count(self):
        num = abs(self.num)
        count=0
        if num == 0:
            return 1 
        if num > 0:
            while num > 0:
                num = num // 10
                count += 1
            return count   
    

num=int (input("Enter a number:"))
obj = DigitCounter(num)
print("Digit count:", obj.digit_count())         

