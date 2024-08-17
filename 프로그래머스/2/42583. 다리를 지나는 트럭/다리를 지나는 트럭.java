import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> bridge = new LinkedList<>();
        int time = 0;
        int totalWeightOnBridge = 0;
        int currentTruckIndex = 0;

        // 다리 길이만큼 큐를 0으로 채워 초기화
        for (int i = 0; i < bridge_length; i++) {
            bridge.add(0);
        }

        while (!bridge.isEmpty()) {
            time++;

            // 다리에서 트럭 이동 (큐에서 첫 번째 요소 제거)
            totalWeightOnBridge -= bridge.poll();

            // 새로운 트럭이 다리에 올라갈 수 있는지 확인
            if (currentTruckIndex < truck_weights.length) {
                if (totalWeightOnBridge + truck_weights[currentTruckIndex] <= weight) {
                    bridge.add(truck_weights[currentTruckIndex]);
                    totalWeightOnBridge += truck_weights[currentTruckIndex];
                    currentTruckIndex++;
                } else {
                    // 다리에 올릴 수 없으면 0을 추가하여 자리만 차지하게 함
                    bridge.add(0);
                }
            }
        }

        return time;
    }
}
