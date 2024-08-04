def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[x for x in arr[:-1] if x<=pivot] 
    right=[x for x in arr[:-1] if x>pivot]

    return quicksort(left)+[pivot]+quicksort(right)

y=[2,1,3,0,5]
x=quicksort(y)
print(y,x)