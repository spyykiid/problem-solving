// This exercise is just method only no console input or reading necessary.

void Print(Node head) {
    Node n = head;
    if(head == null)
        return;
    while(n != null){
        System.out.println(n.data);
        n= n.next;
    }
  
}