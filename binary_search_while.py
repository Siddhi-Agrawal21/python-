n = int(input("Enter no of integers in array:"))
arr = []

for i in range(n):
    a = int(input("Enter the integer:"))
    arr.append(a)

arr.sort()

print(arr)

key = int(input("Enter the integer you want to search:"))

lower = 0
higher = n
mid=0
k=-1


while higher >= lower:
    mid = (lower+higher)//2

    if arr[mid] == key:
        k= mid
        break
    elif arr[mid] > key:
        higher=mid-1
    else:
        lower=mid+1

if k == -1:   
    print("Element not found in array")
else:
    print("Element found at position",str(k))