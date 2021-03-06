# Leetcode 189. Rotate Array
# Easy 1/3/21 

# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Follow up:

#     Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#     Could you do it in-place with O(1) extra space?


# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

 

# Constraints:

#     1 <= nums.length <= 2 * 104
#     -231 <= nums[i] <= 231 - 1
#     0 <= k <= 105



# Solution 1 
# The simplest approach is to 
# rotate all the elements of the array in kkk 
# steps by rotating the elements by 1 unit in each step.


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # speed up the rotation
        k %= len(nums)

        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]



# Time complexity: O(n×k)\mathcal{O}(n \times k)O(n×k). All the numbers
# are shifted by one step(O(n)\mathcal{O}(n)O(n)) k times.
# Space complexity: O(1)\mathcal{O}(1)O(1). No extra space is used.




# Approach 2: Using Extra Array

# Algorithm

# We use an extra array in which we place every element of
# the array at its correct position i.e. the number at index iii 
#in the original array is placed at the index (i+k)% length of 
#array(i + k) \% \text{ length of array}(i+k)% length of array. Then, we copy the new array to the original one.


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
            
        nums[:] = a




# Time complexity: O(n)\mathcal{O}(n)O(n). One pass is used to put the numbers in the new array. And another pass to copy the new array to the original one.
# Space complexity: O(n)\mathcal{O}(n)O(n). Another array of the same size is used.



# Approach 3: Using Cyclic Replacements

# Algorithm

# We can directly place every number of the array at its required correct position. But if we do that, we will destroy the original element. Thus, we need to store the number being replaced in a temptemptemp variable. Then, we can place the replaced number(temp\text{temp}temp) at its correct position and so on, nnn times, where nnn is the length of array. We have chosen nnn to be the number of replacements since we have to shift all the elements of the array(which is nnn). But, there could be a problem with this method, if n%k=0n \% k = 0n%k=0 where k=k%nk = k \% nk=k%n (since a value of kkk larger than nnn eventually leads to a kkk equivalent to k%nk \% nk%n). In this case, while picking up numbers to be placed at the correct position, we will eventually reach the number from which we originally started. Thus, in such a case, when we hit the original number's index again, we start the same process with the number following it.

# Now let's look at the proof of how the above method works. Suppose, we have nnn as the number of elements in the array and kkk is the number of shifts required. Further, assume n%k=0n \%k = 0n%k=0. Now, when we start placing the elements at their correct position, in the first cycle all the numbers with their index iii satisfying i%k=0i \%k = 0i%k=0 get placed at their required position. This happens because when we jump k steps every time, we will only hit the numbers k steps apart. We start with index i=0i = 0i=0, having i%k=0i \% k = 0i%k=0. Thus, we hit all the numbers satisfying the above condition in the first cycle. When we reach back the original index, we have placed nk\frac{n}{k}kn​ elements at their correct position, since we hit only that many elements in the first cycle. Now, we increment the index for replacing the numbers. This time, we place other nk\frac{n}{k}kn​ elements at their correct position, different from the ones placed correctly in the first cycle, because this time we hit all the numbers satisfy the condition i%k=1i \% k = 1i%k=1. When we hit the starting number again, we increment the index and repeat the same process from i=1i = 1i=1 for all the indices satisfying i%k==1i \% k == 1i%k==1. This happens till we reach the number with the index i%k=0i \% k = 0i%k=0 again, which occurs for i=ki=ki=k. We will reach such a number after a total of kkk cycles. Now, the total count of numbers exclusive numbers placed at their correct position will be k×nk=nk \times \frac{n}{k} = nk×kn​=n. Thus, all the numbers will be placed at their correct position.

# Look at the following example to clarify the process:


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                
                if start == current:
                    break
            start += 1



    # Time complexity: O(n)\mathcal{O}(n)O(n). Only one pass is used.

    # Space complexity: O(1)\mathcal{O}(1)O(1). Constant extra space is used.



# Approach 4: Using Reverse

# Algorithm

# This approach is based on the fact that when we rotate the array k times, kk%nk elements from the back end of the array come to the front and the rest of the elements from the front shift backwards.

# In this approach, we firstly reverse all the elements of the array. Then, reversing the first k elements followed by reversing the rest n−kn-kn−k elements gives us the required result.

# Let n=7n = 7n=7 and k=3k = 3k=3.

# Original List                   : 1 2 3 4 5 6 7
# After reversing all numbers     : 7 6 5 4 3 2 1
# After reversing first k numbers : 5 6 7 4 3 2 1
# After revering last n-k numbers : 5 6 7 1 2 3 4 -->


class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
                
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)




    # Time complexity: O(n)\mathcal{O}(n)O(n). nnn elements are reversed a total of three times.

    # Space complexity: O(1)\mathcal{O}(1)O(1). No extra space is used.
