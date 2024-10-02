def missingNumber(nums):
   
    n = len(nums)
    sum_expected = (n * (n+1))//2

    sum_of_list = sum(nums)

    return sum_expected - sum_of_list






nums = [0,1]
result = missingNumber(nums)
print(result)