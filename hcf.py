class HCF:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def hcf_cal(self):
        a=abs(self.a)
        b=abs(self.b)
        if  a<b:
            s=a
        else:
            s=b
        hcf=1
        for i  in range(1,s+1):
            if a%i==0 and b%i==0:
                hcf=i    
        return hcf              
    
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
obj = HCF(a,b)      
print("HCF is:", obj.hcf_cal())