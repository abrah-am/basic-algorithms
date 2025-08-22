
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;



public class StreamPractice {

  static class Person {
    String name;
    Integer age;

    public Person(String name, Integer age) {
      this.name = name;
      this.age = age;
    }

    public Integer getAge() {
      return age;
    }
  }

  private static String findLongestString(List<String> strings) {
    return strings.stream()
        .max(Comparator.comparingInt(String::length))
        .get();
  }

  private static Double getAverageAge(List<Person> people) {
    return people.stream()
        .mapToInt(Person::getAge)
        .average()
        .orElse(0);
  }
  


  public static void main(String args[]) {
    List<String> strings = Arrays
              .asList("apple", "banana", "cherry", "date", "grapefruit");
    System.out.println("Longest String in array: " + findLongestString(strings));

    List<Person> people = Arrays.asList(
      new Person("Alice", 25),
      new Person("Bob", 30),
      new Person("Charlie", 35)
    );
    System.out.println("Average age in list: " + getAverageAge(people));
  }
}