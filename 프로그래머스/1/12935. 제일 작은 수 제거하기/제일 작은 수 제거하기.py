def solution(arr):
    answer = [-1]
    minV = min(arr)
    arr.remove(minV)
    if arr:
        return arr
    return answer