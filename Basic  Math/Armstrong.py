class Solution:

    def __init__(self, num: int):
        self.num = num

    def count_digits(self) -> int:
        count = 0
        while num > 0:
            count += 1
            num //= 10
        return count

    def armstrong(self) -> bool:
        power = self.count_digits(num)
        temp = num
        total = 0

        while temp > 0:
            digit = temp % 10
            total += digit ** power
            temp //= 10

        return total == num


obj = Solution(153)
print(obj.armstrong())  