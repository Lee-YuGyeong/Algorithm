import sys

def check(N,arr,d,r,c):
    maximum=1
    row,col,d_cnt=1,1,1
    print("r : ",r,"    c : ",c,"d : ",d)
    print(arr)
    for j in range(N-1):
        if arr[r][j] == arr[r][j+1]:
            row+=1
        else:
            maximum = max(maximum,row)
            print("1 : ",row)
            row=1

        if arr[j][c] == arr[j+1][c]:
            col+=1
        else:
            maximum = max(maximum,col)
            print("2 : ",col)
            col=1
            
        if d=="col":
            if arr[j][r+1] == arr[j+1][r+1]:
                d_cnt+=1
            else:
                maximum = max(maximum,d_cnt)
                print("3 : ",d_cnt)
                d_cnt=1

        elif d=="row":
            if arr[c+1][j] == arr[c+1][j+1]:
                
                d_cnt+=1
            else:
                maximum = max(maximum,d_cnt)
                print("4 : ",d_cnt)
                d_cnt=1
    return maximum

N = int(input())
arr=[]


for i in range(N):
    tmp=[]
    for i in sys.stdin.readline()[:-1]:
        tmp.append(i)
    arr.append(tmp)

maximum=1

for i in range(N):
    for j in range(N-1):
        if arr[i][j]!=arr[i][j+1]:
            arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]
            ##print(i,j,arr)
            maximum = max(maximum,check(N,arr,"row",i,j))
            arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]


for i in range(N-1):
    for j in range(N):
        if arr[i][j]!=arr[i+1][j]:
            arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j]
            print(i,j)
            maximum = max(maximum,check(N,arr,"col",i,j))
            arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j]

print(maximum)