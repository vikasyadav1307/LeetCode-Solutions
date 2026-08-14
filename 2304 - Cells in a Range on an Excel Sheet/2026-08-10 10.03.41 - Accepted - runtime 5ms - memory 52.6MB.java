class Solution {
    public List<String> cellsInRange(String s) {
        List<String> ans = new ArrayList<>();

        for (char col = s.charAt(0); col <= s.charAt(3); col++) {
            for (int row = s.charAt(1) - '0'; row <= s.charAt(4) - '0'; row++) {
                ans.add("" + col + row);
            }
        }

        return ans;
    }
}