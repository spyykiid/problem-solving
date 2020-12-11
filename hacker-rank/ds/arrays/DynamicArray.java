package hackerrank.ds.arrays;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.io.*;

public class DynamicArray{ 
  /*Editor's solution
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int numQueries = scan.nextInt();
        
        // Initialize Empty Sequences
        Vector< Vector<Integer> > seqN = new Vector< Vector<Integer> >(n);
        for(int i = 0; i < n; i++){
            seqN.add(new Vector<Integer>());
        }
        
        // Process Queries
        int lastAns = 0;
        for(int i = 0; i < numQueries; i++){
            int queryType = scan.nextInt();
            int x = scan.nextInt();
            int y = scan.nextInt();
            int seqIndex = ((x ^ lastAns ) % n);
            Vector<Integer> currSeq = seqN.get(seqIndex);
            
            if(queryType == 1){
                currSeq.add(y);
            }
            else{ // Query type 2
                lastAns = currSeq.get(y % currSeq.size());
                System.out.println(lastAns);
            }
        }
        scan.close();
    }
  */
	public static void main(String[] args) {
	Scanner in = new Scanner(System.in);
	int N = in.nextInt();
	int Q = in.nextInt();
	int lastAns = 0;

    /* Create 2-D ArrayList */
    ArrayList<ArrayList<Integer>> lists = new ArrayList<>();
    for (int i = 0; i < N; i++) {
        lists.add(new ArrayList<Integer>());
    }

    for(int i=0;i<Q;i++){
      	int q = in.nextInt();
        int x = in.nextInt();
        int y = in.nextInt();
  		ArrayList<Integer> seq = lists.get((x ^ lastAns) % N);
  		if(q==1)
  		{
  			seq.add(y);
  		}else{
  			lastAns = seq.get(y%seq.size());
  			System.out.println(lastAns);
  		}
  	}
  	}
}
