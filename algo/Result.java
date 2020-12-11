
import java.util.Stack;


class Result {

/*
* Complete the 'isValid' function below.
*
* The function is expected to return a STRING.
* The function accepts INTEGER_ARRAY a as parameter.
*/

  public static String isValid(List<Integer> a) {
  
    Stack<Integer> treeStack = new Stack<Integer>(); 

    int root = Integer.MIN_VALUE; 

    // Traverse given array 

    for ( Integer i : a) {
      // If we find a node who is on right side 
      // and smaller than root, return false 
      if (i < root) { 
        return "NO"; 
      } 

      // If i is in right subtree of stack top, 
      // Keep removing items smaller than pre[i] 
      // and make the last removed item as new 
      // root. 
      while (!treeStack.empty() && treeStack.peek() < i) { 
          root = treeStack.peek(); 
          treeStack.pop(); 
      }

      // At this point either stack is empty or 
      // i is smaller than root, push i 
      treeStack.push(i);
    }

    return "YES"; 
  }

  public static void main(String[] args) {
    
  }
}