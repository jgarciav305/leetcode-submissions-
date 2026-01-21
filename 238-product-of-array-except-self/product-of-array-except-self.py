"""
We must return an array called "answer", answer[i] is equal to the product of all elements of nums except nums[i]
Ex: At index 0, we multiply everything besides what is at index 0, which would be 2x3x4 = 24.
At index 1, we multiply 1x3x4 = 12. So on and so forth.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] # The right side 
        
        # Goes from right to left
        for i in range(len(nums)-1, 0, -1):
            answer.append(answer[-1]*nums[i])
        answer = answer[::-1]
        left = 1
        for i in range(len(nums)):
            answer[i] = answer[i]*left
            left *= nums[i] 
        return answer