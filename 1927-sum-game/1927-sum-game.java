class Solution {
    public boolean sumGame(String num) {
        int mid = num.length() / 2;

        int sumLeft = 0;
        int sumRight = 0;
        int questionLeft = 0;
        int questionRight = 0;

        // Left half
        for (int i = 0; i < mid; i++) {
            if (num.charAt(i) == '?') {
                questionLeft++;
            } else {
                sumLeft += num.charAt(i) - '0';
            }
        }

        // Right half
        for (int i = mid; i < num.length(); i++) {
            if (num.charAt(i) == '?') {
                questionRight++;
            } else {
                sumRight += num.charAt(i) - '0';
            }
        }

        int questionDifference = questionLeft - questionRight;
        int sumDifference = sumLeft - sumRight;

        // Odd number of ? difference → Alice wins
        if (questionDifference % 2 != 0) {
            return true;
        }

        // Check if Bob can make both sums equal
        return 2 * sumDifference != -9 * questionDifference;
    }
}