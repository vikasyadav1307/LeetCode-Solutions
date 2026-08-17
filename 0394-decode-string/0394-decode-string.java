class Solution {
    public String decodeString(String s) {
        Stack<Integer> countStack = new Stack<>();
        Stack<StringBuilder> stringStack = new Stack<>();
        StringBuilder currentString = new StringBuilder();
        int k = 0;
        for (char ch : s.toCharArray()) {
            if (Character.isDigit(ch)) {
                k = k * 10 + (ch - '0');
            } else if (ch == '[') {
                countStack.push(k);
                stringStack.push(currentString);
                currentString = new StringBuilder();
                k = 0;
            } else if (ch == ']') {
                StringBuilder prevString = stringStack.pop();
                int repeatCount = countStack.pop();
                for (int i = 0; i < repeatCount; i++) {
                    prevString.append(currentString);
                }
                currentString = prevString;
            } else {
                currentString.append(ch);
            }
        }
        return currentString.toString();
    }
}