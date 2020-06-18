from typing import List
from typing import Optional

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = (len(nums1) + len(nums2)) // 2

        if len(nums1) == 0 or len(nums2) == 0:
            if len(nums1) == 0:
                tmp = nums2
                nums2 = nums1
                nums1 = tmp

            i = k
        else:
            if nums1[-1] <= nums2[0] or nums2[-1] <= nums1[0]:
                if nums2[-1] <= nums1[0]:
                    tmp = nums2
                    nums2 = nums1
                    nums1 = tmp

                if len(nums1) > k:
                    i = k
                else:
                    i = k-len(nums1)
                    tmp = nums2
                    nums2 = nums1
                    nums1 = tmp

            else:
                i = self.findMedianSortedArraysHelper(k, nums1, 0, len(nums1), nums2)
                if i is None:
                    tmp = nums2
                    nums2 = nums1
                    nums1 = tmp
                    i = self.findMedianSortedArraysHelper(k, nums1, 0, len(nums1), nums2)

        if (len(nums1) + len(nums2)) % 2 == 1:
            return nums1[i]
        else:
            if i == 0:
                previous_val = nums2[k-1]
            else:
                if 0 <= k-i-1 and k-i-1 < len(nums2):
                    previous_val = max([nums1[i-1], nums2[k-i-1]])
                else:
                    previous_val = nums1[i-1]

            return (previous_val + nums1[i]) / 2
        
    def findMedianSortedArraysHelper(self, 
            k: int,
            nums1: List[int], 
            i: int, 
            j: int, 
            nums2: List[int]) -> Optional[float]:
        while i < j:
            m = (i + j) // 2
            
            if m > k:
                j = m
                continue

            if k-m-1 >= len(nums2):
                i = m+1
                continue

            if m == k and nums1[m] <= nums2[0]:
                return m

            if m == 0 and k-1 == len(nums2) and nums2[-1] <= nums1[m]:
                return m

            if (k-m >= len(nums2) or nums1[m] <= nums2[k-m]) and (k-m-1 < 0 or nums2[k-m-1] <= nums1[m]):
                return m

            if not (k-m >= len(nums2) or nums1[m] <= nums2[k-m]):
                j = m
                continue
            
            if not (k-m-1 < 0 or nums2[k-m-1] <= nums1[m]):
                i = m+1
                continue

        return None
