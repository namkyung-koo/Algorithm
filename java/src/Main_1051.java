// 1051 - 숫자 정사각형

import java.util.Scanner;

public class Main_1051 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(), m = sc.nextInt();
        sc.nextLine();

        // 배열로 인자 받기
        int[][] arr = new int[n][m];

        for (int i = 0; i < n; i++) {
            String line = sc.nextLine();
            for (int j = 0; j < m; j++) {
                arr[i][j] = line.charAt(j) - '0';
            }
        }

        int maxSize = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int d = 1; i + d < n && j + d < m; d++) {
                    if (arr[i][j] == arr[i][j + d] &&
                            arr[i][j] == arr[i + d][j] &&
                            arr[i][j] == arr[i + d][j + d]) {
                        int squareSize = d + 1;
                        maxSize = Math.max(maxSize, squareSize);
                    }
                }
            }
        }
        System.out.println(maxSize * maxSize);
        sc.close();
    }
}
