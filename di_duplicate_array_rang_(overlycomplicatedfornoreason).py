
class Solution:
    def getRange(self,arr,target):
        for i in (arr):
            b = arr[i]
            a = arr.count(b)
            if arr[i] == arr[i+1] and arr[i] == target :
                print (i, i+a)
                break
arr = [1,2,2,3,3,3,3,3,3,4,5]
x = 3
print(Solution().getRange(arr,x))
