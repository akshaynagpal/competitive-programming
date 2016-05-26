//https://www.hackerrank.com/challenges/the-time-in-words

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        HashMap <Integer,String> hm = new HashMap<Integer,String>();
        
        hm.put(1,"one");
        hm.put(2,"two");
        hm.put(3,"three");
        hm.put(4,"four");
        hm.put(5,"five");
        hm.put(6,"six");
        hm.put(7,"seven");
        hm.put(8,"eight");
        hm.put(9,"nine");
        hm.put(10,"ten");
        hm.put(11,"eleven");
        hm.put(12,"twelve");
        hm.put(13,"thirteen");
        hm.put(14,"fourteen");
        hm.put(15,"fifteen");
        hm.put(16,"sixteen");
        hm.put(17,"seventeen");
        hm.put(18,"eighteen");
        hm.put(19,"nineteen");
        hm.put(20,"twenty");
        hm.put(21,"twenty one");
        hm.put(22,"twenty two");
        hm.put(23,"twenty three");
        hm.put(24,"twenty four");
        hm.put(25,"twenty five");
        hm.put(26,"twenty six");
        hm.put(27,"twenty seven");
        hm.put(28,"twenty eight");
        hm.put(29,"twenty nine");
        
        Scanner in = new Scanner(System.in);
        int h = in.nextInt();
        int m = in.nextInt();
        if(m==30){
            System.out.println("half past "+hm.get(h));
        }
        else if(m<30){
            if(m==0)
                System.out.println(hm.get(h)+" o' clock");
            else if(m==15)
                System.out.println("quarter past "+hm.get(h));
            else
                System.out.println(hm.get(m)+" minutes past "+hm.get(h));      
        }
        else{
            if(m==45)
                System.out.println("quarter to "+hm.get(h+1));
            else
                System.out.println(hm.get(60-m)+" minutes to "+hm.get(h+1));
        }      
    }
}