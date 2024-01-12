
// Question 1 solution

class Solution {
    merge(nums1, m, nums2, n) {
        // Initialize three pointers
        let i = m - 1;  // Pointer for the last element in nums1's mergeable part
        let j = n - 1;  // Pointer for the last element in nums2
        let k = m + n - 1;  // Pointer for the last position in nums1's total space

        // Iterate over nums1 and nums2 from the end, merging them into nums1
        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) {
                nums1[k] = nums1[i];  // Place the larger element at the end of nums1
                i--;  // Move the pointer in nums1 backwards
            } else {
                nums1[k] = nums2[j];  // Place the larger element from nums2 in nums1
                j--;  // Move the pointer in nums2 backwards
            }
            k--;  // Move the merge position backwards
        }

        // If there are remaining elements in nums2, copy them over to nums1
        while (j >= 0) {
            nums1[k] = nums2[j];  // Copy remaining elements from nums2 to nums1
            j--;  // Move the pointer in nums2 backwards
            k--;  // Move the merge position backwards
        }
    }
}

// Question 2

class Solution {
    removeElement(nums, val) {
        let insertPosition = 0;

        for (let i = 0; i < nums.length; i++) {
            if (nums[i] !== val) {
                nums[insertPosition] = nums[i];
                insertPosition++;
            }
        }

        return insertPosition;
    }
}

// Question 3

class Solution {
    removeDuplicates(nums) {
        if (nums.length === 0) {
            return 0;
        }

        let insertPosition = 0;

        for (let i = 0; i < nums.length; i++) {
            if (i === nums.length - 1 || nums[i] !== nums[i + 1]) {
                nums[insertPosition] = nums[i];
                insertPosition++;
            }
        }

        return insertPosition;
    }
}

