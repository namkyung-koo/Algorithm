// 1021 - 회전하는 큐

import java.util.LinkedList;
import java.util.Scanner;

public class Main_1021 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LinkedList<Integer> queue = new LinkedList<>();

        int n = sc.nextInt(), m = sc.nextInt();
        sc.nextLine();

        int[] arr = new int[m];
        String[] numbers = sc.nextLine().split(" ");

        for (int i = 0; i < m; i++) {
            arr[i] = Integer.parseInt(numbers[i]);
        }

        for (int i = 1; i <= n; i++) {
            queue.offer(i);
        }

        int count = 0;

        for (int i = 0; i < m; i++) {
            int target = arr[i];
            int index = queue.indexOf(target);
            int half = queue.size() / 2;

            if (index <= half) {
                for (int j = 0; j < index; j++) {
                    queue.offerLast(queue.pollFirst());
                    count++;
                }
            }
            else {
                for (int j = 0; j < queue.size() - index; j++) {
                    queue.offerFirst(queue.pollLast());
                    count++;
                }
            }
            queue.pollFirst();
        }
        System.out.println(count);
        sc.close();
    }
}
