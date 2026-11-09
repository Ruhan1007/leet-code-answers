class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        clones = {}
        
        current = head
        while current:
            clones[current] = Node(current.val)
            current = current.next
        
        current = head
        while current:
            clone = clones[current]
            clone.next = clones.get(current.next)
            clone.random = clones.get(current.random)
            current = current.next
        
        return clones[head]