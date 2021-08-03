class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        for i in range(row):
            for j in range(col):
                if mat[i][j]!=0:
                    mat[i][j]=float('inf')
                    if i>0:
                        mat[i][j]=min(mat[i][j],mat[i-1][j]+1)
                    if j>0:
                        mat[i][j]=min(mat[i][j],mat[i][j-1]+1)
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                if i<row-1:
                    mat[i][j]=min(mat[i+1][j]+1,mat[i][j])
                if j<col-1:
                    mat[i][j]=min(mat[i][j+1]+1,mat[i][j])
        return mat
