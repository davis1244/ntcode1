class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[m:] = nums2[:n]
        # nums1.sort()

        x, y = m - 1, n - 1
        z = m + n - 1 #len(nums1) - 1

        while x >= 0 and y >= 0:
            if nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x -= 1
            elif nums1[x] < nums2[y]:
                nums1[z] = nums2[y]
                y -= 1
            else:  # nums1[x] == nums2[y]
                nums1[z] = nums2[y]   # or nums1[x], either works
                y -= 1
            z -= 1

        while y >= 0:
            nums1[z] = nums2[z]
            y -= 1
            z -= 1


        
        


        

        




    

