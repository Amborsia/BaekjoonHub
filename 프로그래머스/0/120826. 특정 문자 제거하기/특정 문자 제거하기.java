class Solution {
    public String solution(String my_string, String letter) {
        String answer = "";
        char temp = letter.charAt(0);
        for(int i = 0; i<my_string.length(); i++){
            char c = my_string.charAt(i);
            if(c != temp)
            {
                answer+= c;
            }
        }
        return answer;
    }
}