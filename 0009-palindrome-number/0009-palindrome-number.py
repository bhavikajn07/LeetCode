class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_x = list(str(x))
        total = len(list_x)
        mid = total // 2
        
        if x < 0:
            return False
            
        left = list_x[:mid]
        
        if total % 2 != 0:
            right = list_x[mid + 1:]
        else:
            right = list_x[mid:]
        
        if left == right[::-1]:
            return True
        else: 
            return False