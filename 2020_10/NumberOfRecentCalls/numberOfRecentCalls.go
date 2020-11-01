type RecentCounter struct {
    pingStore []int
}


func Constructor() RecentCounter {
    return RecentCounter{}
}


func (this *RecentCounter) Ping(t int) int {
    this.pingStore = append(this.pingStore, t)
    lower := t - 3000
    for lower > this.pingStore[0] {
        this.pingStore = this.pingStore[1:]
    }
    return len(this.pingStore)
}


/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */