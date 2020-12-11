import java.util.ArrayList;
import java.util.List;

public class Solution{
  public static int cost(List<Integer> nums) 
  { 
        
      // find the minimum using 
      // for loop 
      int prevSum = 0;

      while(nums.size() > 1){ 
           
        int sum = nums.get(0) + nums.get(1);
        prevSum = nums.get(nums.size()-1);
        
        nums.add(sum);
        nums.remove(0);
        nums.remove(0);

      }

      return nums.get(0) + prevSum;

    
  } 
    
  static public void main (String[] args) 
  { 
        
      List<Integer> a = new ArrayList();
      a.add(1);
      a.add(2);
      a.add(3);
      a.add(4); 
      // int n = a.length; 
        
      System.out.println(cost(a)); 
  } 
}