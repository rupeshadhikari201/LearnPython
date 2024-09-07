def takeinput():
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            current_input = int(input())
            arr[i][j] = current_input
    print(arr)
# takeinput()

def takeInput():
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    ans = []
    for i in range(N):
        j,k,l = map(int, input().split())
        ans.append([j,k,l])
    return ans
ans  = takeInput()

# def main(ans):
    