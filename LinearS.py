def linear_search(list,n,key):
    for i in range(0,n):
       if (list1[i] == key):  
            return i  
    return -1  
         
list1= [1,3,5,4,7,9]
key=7
    
n = len(list1)
res=linear_search(list,n,key)
if(res==-1):
    print("Element not Found")
else:
    print("Element found at index:",res)