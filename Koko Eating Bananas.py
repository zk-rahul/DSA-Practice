"Koko Eating Bananas:
ko is given an array arr[], where each element represents a pile of bananas. She has exactly k hours to eat all the bananas.

Each hour, Koko can choose one pile and eat up to s bananas from it.

If the pile has atleast s bananas, she eats exactly s bananas.
If the pile has fewer than s bananas, she eats the entire pile in that hour.

Koko can only eat from one pile per hour.


Your task is to find the minimum value of s (bananas per hour) such that Koko can finish all the piles within k hours.
"

code:

class Solution:
    
    def kokoEat(self, arr, k):
        # Code here
        
        def hour(arr, n, speed):
            h = 0
            
            for i in range(n):
                h += arr[i] // speed
                
                if arr[i] % speed != 0:
                    h += 1
                    
            return h
        
        
        n = len(arr)
        low = 1
        high = max(arr)
        res = -1
        
        while low <= high:
            guess = (low + high) // 2
            
            hours = hour(arr, n, guess)
            
            if hours > k:
                low = guess + 1
            else:
                res = guess
                high = guess - 1
        
        return res