class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder s = new StringBuilder();

        int a = 0;
        int b = 0;

        while (a < word1.length() && b < word2.length()) {
            s.append(word1.charAt(a));
            s.append(word2.charAt(b));
            a++;
            b++;
        }

        while (a < word1.length()) {
            s.append(word1.charAt(a));
            a++;
        }

        while (b < word2.length()) {
            s.append(word2.charAt(b));
            b++;
        }

        return s.toString();
    }
}