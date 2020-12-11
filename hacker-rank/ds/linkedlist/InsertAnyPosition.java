/*
  Insert Node at a given position in a linked list 
  head can be NULL 
  First element in the linked list is at position 0
  Node is defined as 
  class Node {
     int data;
     Node next;
  }
*/
    

Node InsertNth(Node head, int data, int position) {
    // This is a "method-only" submission. 
    // You only need to complete this method. 
    // Better solution
    Node tmp = new Node();
    tmp.data = data;
    tmp.next = null;
    Node prev=null,cur=head;
    int count = 0;
    
    while(cur != null && count<position){
        count+=1;
        prev = cur;
        cur = cur.next;
    }
    if(count!=position){
        // Not enough nodes in the list
    }
    else
        if(prev == null){
            tmp.next = head;
            head = tmp;
        }else{
            tmp.next= cur;
            prev.next = tmp;
        }
    return head;
    /* First thought solution
    Node tmp = new Node();
    tmp.data = data;
    tmp.next = null;
    Node node=head,before_node=null, after_node=null;
    if(head==null){
        head = tmp;
        return head;
    }
    if(position==0){
        tmp.next = head;
        head = tmp;
        
    }else{
        while(position>0){
            before_node = node; 
            after_node = node.next;
            node = node.next;
            position--;
        }
        tmp.next = after_node;
        before_node.next = tmp;    
    } 
    return head;*/
}

