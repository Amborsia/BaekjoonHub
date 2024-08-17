import java.util.HashMap;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> hash = new HashMap<>();
        for(String[] cloth: clothes)
        {
            String type = cloth[1];
            hash.put(type,hash.getOrDefault(type,0)+1);
        }
        for(int count: hash.values())
        {
            answer *= (count+1);
        }
        return answer-1;
    }
}