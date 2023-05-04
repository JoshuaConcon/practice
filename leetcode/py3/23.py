import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if(len(lists) == 0):
      return None
    elif((len(lists) == 1)):
      return lists[0]
    else:
      # 2+ lists cases
      heap = []
      for listNode in lists:
        currentListNode = listNode
        while(currentListNode is not None):
          heapq.heappush(heap, currentListNode.val)
          currentListNode = currentListNode.next
      fakeListNodeHead = ListNode(0, None)
      currentNode = fakeListNodeHead
      while(len(heap) != 0):
        nextNumber = heapq.heappop(heap)
        nextNode = ListNode(nextNumber, None)
        currentNode.next = nextNode
        currentNode = currentNode.next
      return fakeListNodeHead.next