'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        que = []  # curs存K个链表滑动的头指针
        for index, node in enumerate(lists):
            if node is not None:
                heapq.heappush(que, (node.val, index))

        dummy_node = ListNode(-1)
        cur = dummy_node
        while que:
            val, index = heapq.heappop(que)
            cur.next = lists[index]
            cur = cur.next
            lists[index] = lists[index].next
            if lists[index] is not None:
                heapq.heappush(que, (lists[index].val, index))
        return dummy_node.next
