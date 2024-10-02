
def findDisappearedNumbers(nums):
    for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])  

       
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i + 1)
    
    return result
    
    







nums = [4,3,2,7,8,2,3,1]

result = findDisappearedNumbers(nums)
print(result)