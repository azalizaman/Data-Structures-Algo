class node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_cycle(head):
    fast, slow = head, head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            cycle_length= cycleLength(slow)
            break

    return findStart(head,cycle_length)

def cycleLength(slow):
    pointer=slow
    length=0
    while True:
        pointer=pointer.next
        length+=1
        if pointer==slow:
            break

    return length

def findStart(head, cycle_length):
    fast,slow=head,head
    cycle_length

    while cycle_length>0:
        fast=fast.next
        cycle_length-=1


    while fast!=slow:
        fast=fast.next
        slow=slow.next
    
    return slow

head = node(5)
head.next = node(6)
head.next.next = node(7)
head.next.next.next = node(8)
head.next.next.next.next = head.next

print(find_cycle(head).value)
