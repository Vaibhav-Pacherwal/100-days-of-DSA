## Peak Element in 2D Matrix
mat = [
  [1],
  [4],
  [3],
  [5]
]
    
def peakIn2D(mat):
    rows,cols = len(mat),len(mat[0])
    for i in range(rows):
        start,end = 0,cols-1
        while start <= end:
            mid = int(start + (end-start)/2)
            currElement = mat[i][mid]
            up,right,down,left = 0,0,0,0

            if i == 0 and mid == 0:
                right = mat[i][mid+1]
                down = mat[i+1][mid]
                if right < currElement > down:
                    return [i,mid]
                
            elif i == 0 and mid == cols-1:
                left = mat[i][mid-1]
                down = mat[i+1][mid]
                if left < currElement > down:
                    return [i,mid]
            
            elif i == rows-1 and mid == rows-1:
                up = mat[i-1][mid]
                right = mat[i][mid+1]
                if up < currElement > right:
                    return [i,mid]
                
            elif i == rows-1 and mid == cols-1:
                up = mat[i-1][mid]
                left = mat[i][mid-1]
                if up < currElement > left:
                    return [i,mid]
                
            else:
                up = mat[i+1][mid]
                left = mat[i][mid-1]
                down = mat[i+1][mid]
                right = mat[i][mid+1]
                if up < currElement > down and left < currElement > right:
                    return [i,mid]
            
            if mat[i][mid-1] > mat[i][mid]:
                end = mid-1
            else:
                start = mid +1

    return [-1,-1] 

ans = peakIn2D(mat)
print(ans)