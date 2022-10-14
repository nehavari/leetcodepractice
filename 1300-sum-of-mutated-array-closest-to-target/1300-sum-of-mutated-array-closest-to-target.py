class Solution:
    
    def merge(self, arr, left, mid, right):
        len1 = mid - left + 1
        len2 = right - mid
        
        left_arr = [0] * len1
        right_arr = [0] * len2
        
        for i in range(len1):
            left_arr[i] = arr[left + i]
            
        for i in range(len2):
            right_arr[i] = arr[mid + i + 1]
            
        i, j, k = 0, 0, left
        while i < len1 and j < len2:
            if left_arr[i] > right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len1:
            arr[k] = left_arr[i]
            k += 1
            i += 1
            
        while j < len2:
            arr[k] = right_arr[j]
            j += 1
            k += 1
    
    def mergeSort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            self.mergeSort(arr, left, mid)
            self.mergeSort(arr, mid + 1, right)
            self.merge(arr, left, mid, right)
        
    
    def findBestValue(self, A: List[int], target: int) -> int:
        self.mergeSort(A, 0, len(A) - 1)
        maxA = A[0]
        while A and target >= A[-1] * len(A):
            target -= A.pop()
        return round((target - .0001 )/ len(A)) if A else maxA
    