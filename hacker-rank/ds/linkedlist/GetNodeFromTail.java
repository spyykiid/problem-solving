/*
  Get Nth element from the end in a linked list of integers
  Number of elements in the list will always be greater than N.
  Node is defined as
  class Node {
     int data;
     Node next;
  }
*/

int GetNode(Node head,int n) {
     // This is a "method-only" submission.
     // You only need to complete this method.
    Node trailingNode = head;
    int len = 0;
    while (head!=null){
        if (len > n)
            trailingNode = trailingNode.next;
        len += 1;
        head = head.next;
    }
  return trailingNode.data;
}
