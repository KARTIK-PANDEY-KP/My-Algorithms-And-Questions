arr = list(map(int,input().split(" ")))
beg = 1
end = len(arr)
mid = (beg+end)//2
value = int(input())
while arr[mid-1]!= value and beg<=end:
    print(mid)
    if value<arr[mid-1]:
        end = mid - 1
    else:
        beg = mid+1
    mid = (beg+end)//2
if arr[mid-1] == value:
    print("Element found at ", mid)
else:
    print("Element not found")
