arr = [1,2,2,6,6,6,6,7,10]
arrLength = len(arr)
arr25Percent = arrLength/4
for n in arr:
    numCheck = arr.count(n)
    if numCheck > arr25Percent:
        print(n)