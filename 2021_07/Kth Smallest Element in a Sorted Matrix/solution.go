import (
	"container/heap"
	"fmt"
)

// An IntHeap is a min-heap of ints.
type Heap [][]int

func (h Heap) Len() int           { return len(h) }
func (h Heap) Less(i, j int) bool { return h[i][0] < h[j][0] }
func (h Heap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *Heap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.([]int))
}

func (h *Heap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func kthSmallest(matrix [][]int, k int) int {
    var window int
    var result int
    n := len(matrix)
    
    if n > k {
        window = k
    } else {
        window = n
    }
    
    h := &Heap{}
    heap.Init(h)
    for i := 0; i < window; i++ {
        heap.Push(h, []int{matrix[i][0], i, 0})
    }
    
    for k > 0 {
        element := heap.Pop(h).([]int)
        result = element[0]
        if element[2] < n - 1 {
            heap.Push(h, []int{matrix[element[1]][element[2] + 1], element[1], element[2] + 1})
        }
        k--
    }
    
    return result
    
}
