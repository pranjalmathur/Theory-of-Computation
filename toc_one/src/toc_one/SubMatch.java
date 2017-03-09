/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package toc_one;

//import static java.lang.System.exit;
import java.util.Scanner;

/**
 *
 * @author Pranjal Mathur
 */
public class SubMatch {

    public static String pattern;  // pattern to be searched
    public static int[][] DFA;  // deterministic finite state machine
    public static int lenPattern;  // length of pattern
    public static int total_Input;  //possible number of inputs

    public SubMatch(String substring, int inputs) {

        SubMatch.pattern = substring;
        SubMatch.lenPattern = substring.length();
        SubMatch.total_Input = inputs;
        SubMatch.DFA = new int[inputs][lenPattern];

    }

    public static void makeDFA() {

        DFA[pattern.charAt(0)][0] = 1;  // move to state 1 if 1st character of pattern is found
        for (int X = 0, j = 1; j < lenPattern; j++) {

            // X is the state that is used to get DFA elements from
            // Copy dfa[][X] into dfa[][j]
            for (int c = 0; c < total_Input; c++) {
                DFA[c][j] = DFA[c][X];
            }
            // correct the destination state
            DFA[pattern.charAt(j)][j] = j + 1;
            //Increment the state X
            X = DFA[pattern.charAt(j)][X];

        }
    }

    public static void search(String string) {
        int i, j, m = -1;
        int N = string.length();
        for (i = 0, j = 0; i < N && j < lenPattern; i++) {
            j = DFA[string.charAt(i)][j];

            if (j == lenPattern) {
                // pattern found

                System.out.println("Found at index " + Math.abs(i - lenPattern + 1));
                j = 0;
                m++;

            }
        }
        if (m == -1) // pattern not found
        {
            System.out.println("Not Found");
        }

    }

    public static void main(String[] args) {

        System.out.print("Enter the substring: ");
        String substring;
        Scanner input = new Scanner(System.in);
        substring = input.next();
        SubMatch code = new SubMatch(substring, 256);
        makeDFA();
        int I = 0;
        while (I == 0) {
            System.out.print("Enter the string: ");
            String string;

            string = input.next();
            if (!string.equals("END")) {
                search(string);
            } else {
                I = 1;
            }
            System.out.println();
        }

    }
}
