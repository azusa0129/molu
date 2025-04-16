import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String n = br.readLine();
            int length = 1;
            if (n.equals("0")) {
                break;
            }
            for (int i = 0; i < n.length(); i++) {
                int c = n.charAt(i);
                if (c == '1') {
                    length += 3;
                } else if (c == '0') {
                    length += 5;
                } else {
                    length += 4;
                }
            }
            System.out.println(length);
        }
    }
}