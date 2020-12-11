/*
  Delete Node at a given position in a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 
  class Node {
     int data;
     Node next;
  }
*/
    // This is a "method-only" submission. 
    // You only need to complete this method. 

Node Delete(Node head, int position) {
    Node cur = head, prev=null;
    int count =0;
    while(cur!=null &&count<position){
        count++;
        prev = cur;
        cur =cur.next;
    }
    if(count!=position){}
    else
        if(head==null){
            return head;
        }else if(prev == null){
            head = head.next;
        }else{
            prev.next = cur.next;
        }

    return head;
}