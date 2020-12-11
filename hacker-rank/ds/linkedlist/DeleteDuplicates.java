/*
Node is defined as
  class Node {
     int data;
     Node next;
  }
*/

Node RemoveDuplicates(Node head) {
  // This is a "method-only" submission.
  // You only need to complete this method.
    if(head.next == null)
        return head;

    Node temp = RemoveDuplicates(head.next);
    if(temp.data == head.data){
        return temp;
    }else{
        head.next = temp;
    }
    return head;

}
