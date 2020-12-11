/*
  Print elements of a linked list in reverse order 
  head pointer input could be NULL as well for empty list
  Node is defined as 
  class Node {
     int data;
     Node next;
  }
*/
    // This is a "method-only" submission. 
    // You only need to complete this method. 

void ReversePrint(Node head) {
  // This is a "method-only" submission. 
  // You only need to complete this method. 
    
    if(head==null)
        return;
    ReversePrint(head.next);
    System.out.println(head.data);
    
    
    /* Using Stack  
    Deque<Integer> stack = new ArrayDeque<Integer>();
    Node cur = head;
    while(cur!=null){
        stack.push(cur.data);
        cur = cur.next;
    }
    
    while(!stack.isEmpty())
    {
        System.out.println(stack.pop());
    } */   
}

