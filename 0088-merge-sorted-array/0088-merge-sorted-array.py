class Solution:
    def merge(self, nums1, m, nums2, n):
        
        p1 = m - 1  # Pointer for nums1's actual elements
        p2 = n - 1  # Pointer for nums2
        p = m + n - 1  # Pointer for placement in nums1

        # Merge in reverse order
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1