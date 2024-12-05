import java.nio.file.*; import java.util.regex.*;

public class Day_3 {
    public static void main(String[] args) {
        try {
            var input = Files.readAllLines(Paths.get("Day_3.txt"));
            var p = Pattern.compile("mul\\((\\d+),(\\d+)\\)|(do|don't)\\(\\)");
            boolean enabled = true; int result = 0, filtered = 0;

            for (String s : input) {
                var m = p.matcher(s);
                while (m.find()) {
                    if (m.group().startsWith("mul")) {
                        int prod = Integer.parseInt(m.group(1)) * Integer.parseInt(m.group(2));
                        result += prod; if (enabled) filtered += prod;
                    } else enabled = !m.group().startsWith("don't");
                }
            }
            System.out.printf("Part 1: %d\nPart 2: %d\n", result, filtered);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
