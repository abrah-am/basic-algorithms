
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class OptimizationPractice {
  public static void main(String[] args) {
    printEqualResultsOfPairsIteration1(10);
    printEqualResultsOfPairsIteration2(10);
    printEqualResultsOfPairsIteration3(10);
  }
  
  /**
   * This method will find the first a^3 + b^3 == c^3 + d^3
   * @param n
   */
  static void printEqualResultsOfPairsIteration1(int n) {
    System.err.println("*********** First Iteration **************");
    int count = 0;
    for (int a = 1; a <= n; a++) {
      for (int b = 1; b <= n; b++) {
        for (int c = 1; c <= n; c++) {
          for (int d = 1; d <= n; d++) {
            if ((Math.pow(a, 3) + Math.pow(b, 3)) == (Math.pow(c, 3) + Math.pow(d, 3))) {
              System.out.println("Match: " + (++count) + "> a=" + a + "; b=" + b + "; c=" + c + "; d=" + d);
              break;
            }
          }
        }
      }
    }
    System.err.println("*********** /First Iteration **************");
  }

  static void printEqualResultsOfPairsIteration2(int n) {
    System.err.println("*********** Second Iteration **************");
    int count = 0;
    for (int a = 1; a <= n; a++) {
      for (int b = 1; b <= n; b++) {
        for (int c = 1; c <= n; c++) {
          long d = Math.round(Math.pow(Math.pow(a, 3) + Math.pow(b, 3) - (Math.pow(c, 3)), 1.0 / 3));
          if ((Math.pow(a, 3) + Math.pow(b, 3)) == (Math.pow(c, 3) + Math.pow(d, 3)) && d <= n) {
              System.out.println("Match: " + (++count) + "> a=" + a + "; b=" + b + "; c=" + c + "; d=" + d);
          }
        }
      }
    }
    System.err.println("*********** /Second Iteration **************");
  }  


  static void printEqualResultsOfPairsIteration3(int n) {
    System.err.println("*********** Third Iteration **************");
    int count = 0;
    Map<Double, List<String>> results = new HashMap<>();
    for (int c = 0; c <= n; c++) {
      for (int d = 0; d <= n; d++) {
        double result = (Math.pow(c, 3) + Math.pow(d, 3));
        if (!results.containsKey(result)) {
          results.put(result, new ArrayList<>());
        }
        results.get(result).add("; c=" + c + "; d=" + d);
      }
    }

    for (int a = 1; a <= n; a++) {
      for (int b = 1; b <= n; b++) {
        double result = (Math.pow(a, 3) + Math.pow(b, 3));
        List<String> pairs = results.get(result);
        for (String pair : pairs) {
              System.out.println("Match: " + (++count) + "> a=" + a + "; b=" + b + pair);
        }
      }
    }
    System.err.println("*********** /Third Iteration **************");
  }   
}
