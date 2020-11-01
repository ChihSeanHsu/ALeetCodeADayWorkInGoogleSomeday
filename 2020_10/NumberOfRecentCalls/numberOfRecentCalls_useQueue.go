type RecentCounter struct {
    pingStore Deque
}


func Constructor() RecentCounter {
    return RecentCounter{}
}


func (this *RecentCounter) Ping(t int) int {
    this.pingStore.Inject(t)
    lower := t - 3000
    for lower > this.pingStore.First() {
        this.pingStore.Pop()
    }
    return this.pingStore.Len()
}


func NewDeque() *Deque {
    return &Deque{}
}


type Deque struct {
    Items []int
}


func (q *Deque) Push(item int) {
    tmp := []int{item}
    q.Items = append(tmp, q.Items...)
}

func (q *Deque) Pop() int {
    defer func() {
        q.Items = q.Items[1:] 
    }()
    return q.Items[0]
}

func (q *Deque) Inject(item int) {
    q.Items = append(q.Items, item)
}

func (q *Deque) Eject() int {
    lengthAfterEject := len(q.Items) - 1
    defer func() {
        q.Items = q.Items[:lengthAfterEject]
    }()
    return q.Items[lengthAfterEject]
}

func (q *Deque) Len() int {
    return len(q.Items)
}

func (q *Deque) First() int {
    return q.Items[0]
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */