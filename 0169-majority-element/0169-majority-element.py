class Solution(object):
  def majorityElement(self,nums):

    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    # Second pass: verify candidate
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    else:
        return None  # or raise an error if no majority exists
        