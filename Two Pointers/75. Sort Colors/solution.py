from collections import defaultdict

class Solution:
  # pointer solution O(n) and O(1)
  def sortColors(self, nums: List[int]) -> None:
      """
      Do not return anything, modify nums in-place instead.
      """

      red, white, blue = 0, 0, len(nums) - 1 

      while white <= blue:
          if nums[white] == 0:
              nums[white], nums[red] = nums[red], nums[white]
              white += 1
              red += 1
          elif nums[white] == 1:
              white += 1
          else:
              nums[blue], nums[white] = nums[white], nums[blue]
              blue -= 1
              
    # counter O(2n) and O(3)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1
        
        idx = 0
        for i in (0 ,1 ,2):
            for _ in range(counter[i]):
                nums[idx] = i
                idx += 1
        
