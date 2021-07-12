Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 

Example 1:

![image](https://user-images.githubusercontent.com/34153546/125229965-71999200-e30a-11eb-84d7-664b0eb2256e.png)


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
![image](https://user-images.githubusercontent.com/34153546/125229982-7a8a6380-e30a-11eb-83e5-d16745282303.png)



Example 2:
![image](https://user-images.githubusercontent.com/34153546/125230001-837b3500-e30a-11eb-832c-6c2f50d3fe2c.png)


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.

 

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in a strictly increasing order.

