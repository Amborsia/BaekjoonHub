import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        // int 배열을 String 배열로 변환
        String[] strNumbers = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            strNumbers[i] = String.valueOf(numbers[i]);
        }

        // 사용자 정의 Comparator를 이용해 정렬
        Arrays.sort(strNumbers, new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                // (b + a)와 (a + b)를 비교하여 더 큰 순서로 정렬
                return (b + a).compareTo(a + b);
            }
        });

        // 정렬된 배열을 하나의 문자열로 합침
        StringBuilder answer = new StringBuilder();
        for (String str : strNumbers) {
            answer.append(str);
        }

        // "0000..." 같은 경우 "0"으로 반환
        if (strNumbers[0].equals("0")) {
            return "0";
        }

        return answer.toString();
    }
}