class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    prev=dummy=ListNode()

    while list1 and list2:
        if list1.val<list2.val:
            prev.next=list1
            list1=list1.next

        else:
            prev.next=list2
            list2=list2.next

        prev=prev.next

    prev.next=list1 or list2
    return dummy.next



head1=ListNode(1)
head1.next=ListNode(2)
head1.next.next=ListNode(4)

head2=ListNode(1)
head2.next=ListNode(3)
head2.next.next=ListNode(4)

head3=mergeTwoLists(head1,head2)

while head3 is not None:
    print(head3.val)
    head3=head3.next
