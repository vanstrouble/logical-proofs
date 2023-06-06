def findMedian(arr):
    n = len(arr)
    arr.sort()
    if n % 2 == 0:
        median = (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        median = arr[n//2]
    return median

if __name__ == '__main__':
    n = int(input())
    values = list(map(int, input().split()))
    median = findMedian(values)
    print(median)
