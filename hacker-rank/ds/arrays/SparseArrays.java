package hackerrank.ds.arrays;

import java.util.Map;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Scanner;
import java.lang.System;
public class SparseArrays {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        // Implementation using Sparse Array
        String[] sparse_string = new String[1001];
        int N = scan.nextInt();
        int[] cnt = new int[1001];
        int cnt_i=0;
        for(int i=0;i<N;i++){
            String s = scan.next();
            for(int j=0; j < cnt_i ; j++){
                if(sparse_string[j] == s){
                    cnt[j]+=1;
                    continue;
                }
            }
            cnt[cnt_i] = 1;
            sparse_string[cnt_i++] = s;    
        }
        
        int Q = scan.nextInt();
        for (int i=0;i<Q;i++) {
            String s = scan.next();
            for(int j=0;j<cnt_i;j++){
                if(sparse_string[j]==s)
                    System.out.println(cnt[j]);
            }
        }
        
        /* Implementation using HashMap
        Map<String,Integer> string_dict = new HashMap<>();

        // Reading collection of string to a HashSet 
        int N = scan.nextInt();
        for(int i=0;i<N;i++){
            String s = scan.next();
            //int rsult = string_dict.get(s) == null ? string_dict.put(s,string_dict.get(s)+1) : string_dict.put(s,1); 
            if(string_dict.get(s)==null){
                string_dict.put(s,1);
            }else{
                string_dict.put(s,string_dict.get(s)+1);    
            }
        }

        // Perform Queries
        int Q = scan.nextInt();
        int[] result = new int[Q];
        for (int i=0;i<Q;i++) {
            String s = scan.next();
            result[i] = 0;
            if(string_dict.get(s) != null)
                result[i] = string_dict.get(s);
        }
        
        //Print result
        for (int r : result) {
            System.out.println(r);
        }*/
    }
}