def containsDuplicate(nums):

    count = set()
   

    for i in range(len(nums)):

        if nums[i] in count:
            
            return True
        
        count.add(nums[i])
    return False







nums = [1,2,3,5,1]
result = containsDuplicate(nums)
print(result)