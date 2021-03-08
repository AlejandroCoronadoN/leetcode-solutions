class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1_c in-place instead.
        """
        nums1_c = nums1[:m]
        i =0
        c=0
        j=0
        while i <= n+m -1:
          if nums1_c[c]< nums2[j]:
            nums1[i] =  nums1_c[c]
            c+=1
            i+=1
          else:
            nums1[i] = nums2[j] 
            i==1
            j+=1
          if j > n:
            x = i
            while x <= n+m -1:
              nums1[x] = nums1_c[c]
              i+=1
              x+=1
              c+1
          if c>m:
            x = i
            while x <= n+m -1:
              nums1[x] = nums2[j]
              i+=1
              x+=1
              j+=1
              
              
        