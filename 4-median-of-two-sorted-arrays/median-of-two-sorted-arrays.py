class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Step 1: Ensure nums1 is the shorter array
        # This keeps the binary search range [0, m] as small as possible
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            # Partition index for nums1
            partition1 = (low + high) // 2
            # Partition index for nums2 (ensures equal elements on left/right)
            partition2 = (m + n + 1) // 2 - partition1
            
            # Boundary values for nums1
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            # Boundary values for nums2
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we have found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Total elements is even
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                # Total elements is odd
                else:
                    return max(maxLeft1, maxLeft2)
            
            elif maxLeft1 > minRight2:
                # Move left in nums1
                high = partition1 - 1
            else:
                # Move right in nums1
                low = partition1 + 1
        
        return 0.0