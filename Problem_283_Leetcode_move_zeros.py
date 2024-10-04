def moveZeroes(nums) -> None:
       
        start = 0
        end = 0
        while(end< len(nums)):
            if not nums[end]== 0:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
            end +=1

        return nums
                  
                  
                  
                  
                  
            
              
        
           
        return nums
            
 

     
nums = [0,1,0,3,12]

result = moveZeroes(nums)
print(result)