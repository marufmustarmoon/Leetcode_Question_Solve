def findMaxAverage(nums ,k):

    start = 0
    maxAverage = float('-inf')
    total_k_sum = 0
    for end in range(len(nums)):
        total_k_sum = total_k_sum + nums[end]
        if end-start+1 == k:
            maxAverage = max(maxAverage,total_k_sum/k)
            total_k_sum = total_k_sum - nums[start]
            start = start +1
           
            
        

    return maxAverage


nums = [1,12,-5,-6,50,3]
k = 4

result = findMaxAverage(nums,k)
print(result)