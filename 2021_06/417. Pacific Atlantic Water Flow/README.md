You are given an m x n integer matrix heights representing the height of each unit cell in a continent. The Pacific ocean touches the continent's left and top edges, and the Atlantic ocean touches the continent's right and bottom edges.

Water can only flow in four directions: up, down, left, and right. Water flows from a cell to an adjacent one with an equal or lower height.

Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.

![image](https://github.com/ChihSeanHsu/ALeetCodeADayWorkInGoogleSomeday/blob/master/2021_06/417.%20Pacific%20Atlantic%20Water%20Flow/ocean-grid.jpg)

Example 1:

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]

 

Constraints:

    m == heights.length
    n == heights[i].length
    1 <= m, n <= 200
    0 <= heights[i][j] <= 105

