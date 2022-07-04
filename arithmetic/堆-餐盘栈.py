"""
我们把无限数量 ∞ 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量 capacity 都相同。

实现一个叫「餐盘」的类 DinnerPlates：

DinnerPlates(int capacity) - 给出栈的最大容量 capacity。
void push(int val) - 将给出的正整数 val 推入 从左往右第一个 没有满的栈。
int pop() - 返回 从右往左第一个 非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回 -1。
int popAtStack(int index) - 返回编号 index 的栈顶部的值，并将其从栈中删除；如果编号 index 的栈是空的，请返回 -1。
 

示例：

输入：
["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
输出：
[null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

解释：
DinnerPlates D = DinnerPlates(2);  // 初始化，栈最大容量 capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // 栈的现状为：    2  4
                                    1  3  5
                                    ﹈ ﹈ ﹈
D.popAtStack(0);   // 返回 2。栈的现状为：      4
                                          1  3  5
                                          ﹈ ﹈ ﹈
D.push(20);        // 栈的现状为：  20  4
                                   1  3  5
                                   ﹈ ﹈ ﹈
D.push(21);        // 栈的现状为：  20  4 21
                                   1  3  5
                                   ﹈ ﹈ ﹈
D.popAtStack(0);   // 返回 20。栈的现状为：       4 21
                                            1  3  5
                                            ﹈ ﹈ ﹈
D.popAtStack(2);   // 返回 21。栈的现状为：       4
                                            1  3  5
                                            ﹈ ﹈ ﹈
D.pop()            // 返回 5。栈的现状为：        4
                                            1  3
                                            ﹈ ﹈
D.pop()            // 返回 4。栈的现状为：    1  3
                                           ﹈ ﹈
D.pop()            // 返回 3。栈的现状为：    1
                                           ﹈
D.pop()            // 返回 1。现在没有栈。
D.pop()            // 返回 -1。仍然没有栈。
 

提示：

1 <= capacity <= 20000
1 <= val <= 20000
0 <= index <= 100000
最多会对 push，pop，和 popAtStack 进行 200000 次调用。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dinner-plate-stacks
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import heapq


class DinnerPlates:
    def __init__(self, capacity: int):
        self.c = capacity
        self.stack = []
        self.heap = []

    def push(self, val: int) -> None:
        if self.heap:
            self.stack[heapq.heappop(self.heap)] += [val]
        elif not self.stack or len(self.stack[-1]) == self.c:
            self.stack += [[val]]
        else:
            self.stack[-1] += [val]

    def pop(self) -> int:
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]:
                return self.stack[i].pop()
            self.stack.pop()
            if self.heap:
                tem = heapq.heappop(self.heap)
                if tem < len(self.stack):
                    heapq.heappush(self.heap, tem)
        return -1

    def popAtStack(self, index: int) -> int:
        if index < len(self.stack) and self.stack[index]:
            heapq.heappush(self.heap, index)
            return self.stack[index].pop()
        return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
