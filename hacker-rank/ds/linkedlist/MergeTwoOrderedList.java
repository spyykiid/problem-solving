/*
  Merge two linked lists
  head pointer input could be NULL as well for empty list
  Node is defined as
  class Node {
     int data;
     Node next;
  }
*/

Node mergeLists(Node headA, Node headB) {
     // This is a "method-only" submission.
     // You only need to complete this method
    Node headC;
    if(headA ==null && headB!=null)
        return headB;
    if(headA !=null && headB==null)
        return headA;
    if(headA.data <= headB.data){
        headC = headA;
        headA = headA.next;
    }else{
        headC = headB;
        headB = headB.next;
    }
    headC.next = mergeLists(headA,headB);
    return headC;
}
