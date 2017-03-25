package toc_one;

//import static java.lang.System.exit;
import java.util.Scanner;

/**
 *
 * @author Pranjal Mathur
 */
public class SubMatch {

    /* Variable to be used as input and maintaining the DFA
    and other program variables
    */
    public static String pattern;  // pattern to be searched
    
    public static int[][] DFA;  // deterministic finite state machine
    
    public static int lenPattern;  // length of pattern
    
    public static int total_Input;  //possible number of inputs
    
    
    
    /*Constructor to set up the variables as required
    
    */
    public SubMatch(String substring, int inputs) {

        SubMatch.pattern = substring;
        
        SubMatch.lenPattern = substring.length();
        
        SubMatch.total_Input = inputs;
        
        SubMatch.DFA = new int[inputs][lenPattern];

    }

    public static void makeDFA() {

        DFA[pattern.charAt(0)][0] = 1;  // chanfe the state to state 1 as asson as first match is found
        
        for (int X = 0, j = 1; j < lenPattern; j++) {

            // X maintains the pointer to the match whose elements need to copied
            
            for (int c = 0; c < total_Input; c++) {
                
                // Copy column X to j of the transition table/dfa
                DFA[c][j] = DFA[c][X];
                
            }
            
            // correct the destination state
            DFA[pattern.charAt(j)][j] = j + 1;
            
            
            X = DFA[pattern.charAt(j)][X]; //update X

        }
    }

    /*to search for the required substring
    in the given string
    */
    public static void search(String string) {
        
        int i, j, m = -1;
        
        //calculate string length
        int N = string.length();
        
        for (i = 0, j = 0; i < N && j < lenPattern; i++) {
            
            //keep on calculating the lenght and update as soon as found
            j = DFA[string.charAt(i)][j];

            if (j == lenPattern) {
                
                // print if pattern found
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

    /*drivers program*/
    
    public static void main(String[] args) {

        System.out.print("Enter the substring: ");
        String substring;
        Scanner input = new Scanner(System.in);
        substring = input.next();
        SubMatch code = new SubMatch(substring, 256);
        
        //construct DFA transitions
        makeDFA();
        int I = 0;
        
        //keep the program running until user enters END
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
