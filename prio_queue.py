class PriorityQueue:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)
        self._bubble_up()

    def pop(self):
        if len(self.data) == 0:
            return None
        elif len(self.data) == 1:
            return self.data.pop()
        res = self.data[0]
        self.data[0] = self.data.pop()
        self._bubble_down()
        return res

    def peek(self):
        if len(self.data) == 0:
            return None
        else:
            return self.data[0]

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _bubble_up(self, idx=None):
        """
        recursive
        """
        if idx is None:
            idx = len(self.data) - 1
        if idx == 0:
            return
        pidx = self._get_parent_idx(idx)
        pval = self.data[pidx]
        val = self.data[idx]
        if val < pval:
            self._swap(idx, pidx)
            self._bubble_up(pidx)

    def _bubble_down(self, idx=None):
        """
        recursive
        """
        if idx is None:
            idx = 0
        if idx >= len(self.data):
            return
        val = self.data[idx]
        lidx = self._get_left_child_idx(idx)
        if lidx >= len(self.data):
            return
        lval = self.data[lidx]
        ridx = self._get_right_child_idx(idx)
        if ridx >= len(self.data):
            if val > lval:
                self._swap(idx, lidx)
                self._bubble_down(lidx)
            return
        rval = self.data[ridx]
        if lval <= rval and val > lval:
            self._swap(idx, lidx)
            self._bubble_down(lidx)
        elif rval < lval and val > rval:
            self._swap(idx, ridx)
            self._bubble_down(ridx)

    def _get_parent_idx(self, child_idx):
        return (child_idx - 1) // 2

    def _get_left_child_idx(self, parent_idx):
        return 2 * parent_idx + 1

    def _get_right_child_idx(self, parent_idx):
        return self._get_left_child_idx(parent_idx) + 1


if __name__ == "__main__":
    queue = PriorityQueue()

    print(queue.pop())
    print(queue.peek())
    print("adding items...")

    print("push item: 1"), queue.push(1)
    print("push item: 2"), queue.push(2)
    print("push item: 3"), queue.push(3)
    print("push item: 4"), queue.push(4)

    print(f"peek: {queue.peek()}")
    print(f"pop: {queue.pop()}")
    print(f"pop: {queue.pop()}")
    print(f"pop: {queue.pop()}")
    print(f"pop: {queue.pop()}")
