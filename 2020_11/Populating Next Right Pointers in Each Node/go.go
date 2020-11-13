/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */

func connect(root *Node) *Node {
    if root != nil {
        connect_(root.Left, root.Right)
    }
    return root
}

func connect_(left *Node, right *Node) {
    if left == nil {
        return
    }
    left.Next = right
    
    connect_(left.Left, left.Right)
    connect_(right.Left, right.Right)
    connect_(left.Right, right.Left)
    
    
}
