package hackerrank.ds.arrays;

import java.util.Scanner;

public class AlgorithmicCrush{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int Q = scan.nextInt();
        long[] list = new long[N+1];
        long max = 0,x=0;

        for(int i=0;i<Q;i++){
            int a = scan.nextInt();
            int b = scan.nextInt();
            int k = scan.nextInt();
            list[a]+=k;
            if(b+1<=N){
                list[b+1] -= k;
            }
        }

        for(int i=1;i<=N;i++)
        {
            x=x+list[i];
            if(max<x) max=x;
        }
        System.out.println(max);
        scan.close();
    }
}