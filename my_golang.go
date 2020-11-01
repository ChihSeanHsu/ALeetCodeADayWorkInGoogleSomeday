/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
import (
    "strconv"
)

func getDecimalValue(head *ListNode) int {
    tmp := head
    values := ""
    for tmp != nil {
        values += strconv.Itoa(tmp.Val)
        tmp = tmp.Next
    }
    result64, _ := strconv.ParseInt(values, 2, 32)
    result := int(result64)
    return result
}