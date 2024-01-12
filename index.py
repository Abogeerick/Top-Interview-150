

# Question 1 solution

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Merge nums1 and nums2 into a single array sorted in non-decreasing order.
        Modify nums1 in-place to store the merged result.
        
        :type nums1: List[int] - The first list to merge, with extra space for merging.
        :type m: int - Number of elements in nums1 to be merged.
        :type nums2: List[int] - The second list to merge.
        :type n: int - Number of elements in nums2.
        :rtype: None - Do not return anything, modify nums1 in-place instead.
        """
        
        # Initialize three pointers.
        i = m - 1  # Pointer for the last element in nums1's mergeable part.
        j = n - 1  # Pointer for the last element in nums2.
        k = m + n - 1  # Pointer for the last position in nums1's total space.

        # Iterate over nums1 and nums2 from the end, merging them into nums1.
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]  # Place the larger element at the end of nums1.
                i -= 1  # Move the pointer in nums1 backwards.
            else:
                nums1[k] = nums2[j]  # Place the larger element from nums2 in nums1.
                j -= 1  # Move the pointer in nums2 backwards.
            k -= 1  # Move the merge position backwards.

        # If there are remaining elements in nums2, copy them over to nums1.
        while j >= 0:
            nums1[k] = nums2[j]  # Copy remaining elements from nums2 to nums1.
            j -= 1  # Move the pointer in nums2 backwards.
            k -= 1  # Move the merge position backwards.

    # Question 2
            
    class Solution(object):
        def removeElement(self, nums, val):
            """
            :type nums: List[int]
            :type val: int
            :rtype: int
            """
            insertPosition = 0
            for num in nums:
                if num != val:
                    nums[insertPosition] = num
                    insertPosition += 1
            return insertPosition

