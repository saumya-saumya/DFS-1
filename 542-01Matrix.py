# N is the number of rows and M is the number of columns
# T.C. O(N X M)
# S.C. O(N X M)

# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         if mat is None:
#             return []
        
#         n=len(mat)
#         m=len(mat[0])
        
#         dirs=[[0,1],[1,0],[-1,0],[0,-1]]
#         zero=deque()
#         for i in range(n):
#             for j in range(m):
#                 if mat[i][j]==0:
#                     zero.append([i,j])
#                 else:
#                     mat[i][j]=-1
        
#         dist=1
#         while zero:
#             for level in range(len(zero)):
#                 curr=zero.popleft()
#                 for dir in dirs:
#                     r=curr[0]+dir[0]
#                     c=curr[1]+dir[1]
                    
#                     if (r>=0 and r<n and c>=0 and c<m and mat[r][c]==-1):
#                         mat[r][c]=dist
#                         zero.append([r,c])
                    
                        
#             dist+=1
#         return mat
        
        
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if mat is None:
            return []
        
        n=len(mat)
        m=len(mat[0])
        
        dirs=[[0,1],[1,0],[-1,0],[0,-1]]
        zero=deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    zero.append([i,j])
                else:
                    mat[i][j]=-1

        while zero:
            curr=zero.popleft()
            for dir in dirs:
                r=curr[0]+dir[0]
                c=curr[1]+dir[1]
                
                if (r>=0 and r<n and c>=0 and c<m and mat[r][c]==-1):
                    mat[r][c]=mat[curr[0]][curr[1]]+1
                    zero.append([r,c])
                    
                        
        return mat
