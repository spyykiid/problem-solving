package hackerrank.ds.arrays;

import java.util.Scanner;

public class LeftRotation { 
	
	/* Editors solution
    public static int[] rotateArray(int[] arr, int d){
        // Because the constraints state d < n, we need not concern ourselves with shifting > n units.
        int n = arr.length;
        
        // Create a temporary d-element array to store elements shifted to the left of index 0:
        int[] temp_arr = Arrays.copyOfRange(arr, 0, d);
        
        // Shift elements from indices d through n to indices 0 through d - 1:
        for(int i = d; i < n; i++) {
            arr[i - d] = arr[i];
        }
        
        // Copy the d shifted elements from the temporary array back to the original array:
        for(int i = n - d; i < n; i++) {
            arr[i] = temp_arr[i-n+d];
        }
        
        return arr;
    }*/
    	
	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int rotations = scan.nextInt();
		int[] num_array = new int[N];
		int index_0;



		// Print array's elements as a single line of space-separated values:
        
		for (int i=0;i<N;i++) {
		 	num_array[i] = scan.nextInt();
		} 
        for (int i=0; i<rotations;i++) {
        	index_0 = num_array[0];
        	for (int j=1;j<N;j++) {
        		num_array[j-1] = num_array[j];
        	}
        	num_array[N-1] = index_0;
        }
        for(int i : num_array) {
            System.out.print(i + " ");
        }  
	}

}