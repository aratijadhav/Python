
def rearrangeArray(arr, n) : 

    arr.sort() 
  
    # To store modified array 
    tempArr = [0] * (n + 1) 
  
    # Adding numbers from sorted  
    # array to new array accordingly 
    ArrIndex = 0
  
    # Traverse from begin and end 
    # simultaneously  
    i = 0
    j = n-1
      
    while(i <= n // 2 or j > n // 2 ) : 
      
        tempArr[ArrIndex] = arr[i] 
        ArrIndex = ArrIndex + 1
        tempArr[ArrIndex] = arr[j] 
        ArrIndex = ArrIndex + 1
        i = i + 1
        j = j - 1

    print(tempArr)
  
  
# Driver Code 
arr = [ 5, 8, 1, 4, 2, 9, 3, 7, 6 ] 
n = len(arr) 
rearrangeArray(arr, n) 
  
for i in range(0, n) : 
    print( arr[i], end = " ") 
      
# This code is contributed by Nikita Tiwari. 
