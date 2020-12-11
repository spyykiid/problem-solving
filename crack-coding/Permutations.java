import javax.print.event.PrintJobListener;

public class Permutations
{
  
  public static void main(String[] args) {
    int[] copy = new int[0];
    System.out.println(copy.length);
    Permutations p = new Permutations();
    p.permutation("abc");
  }
  
  void permutation(String str)
  {
    permutation(str, "");
  }
  
  void permutation(String str, String prefix)
  {
    if(str.length() == 0)
    {
      System.out.println(prefix);
    }
    else{
      for (int i =0; i< str.length(); i++){
        String rem = str.substring(0,i) + str.substring(i+1);
        this.permutation(rem,prefix+str.charAt(i));
      }
    }

  }

}