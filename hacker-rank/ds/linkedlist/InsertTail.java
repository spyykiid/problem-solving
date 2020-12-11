/*
  Insert Node at the end of a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 
  class Node {
     int data;
     Node next;
  }
*/
Node Insert(Node head,int data) {
// This is a "method-only" submission. 
// You only need to complete this method. 
    Node new_node = new Node();
    new_node.data = data;
    new_node.next = null;
    Node n = head;
    if(head == null){
        head = new_node;
    }else{
        while(n.next !=null){
            n = n.next;
        }
        n.next = new_node;
    }
    return head;
}

