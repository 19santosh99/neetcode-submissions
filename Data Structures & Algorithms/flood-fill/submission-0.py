class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROW_LEN = len(image)
        COL_LEN = len(image[0])

        def dfs(grid_val, sr, sc, image):

            if sc < 0 or sr < 0 or sc == COL_LEN or sr == ROW_LEN or image[sr][sc] == color:
                return image

            if image[sr][sc] != grid_val:
                return image

            # if the image has the grid val
            if image[sr][sc] == grid_val:
                image[sr][sc] = color

            image = dfs(grid_val, sr - 1, sc, image)
            image = dfs(grid_val, sr + 1, sc, image)
            image = dfs(grid_val, sr, sc + 1, image)
            image = dfs(grid_val, sr, sc - 1, image)

            return image

            

        
        return dfs(image[sr][sc], sr, sc, image)




        