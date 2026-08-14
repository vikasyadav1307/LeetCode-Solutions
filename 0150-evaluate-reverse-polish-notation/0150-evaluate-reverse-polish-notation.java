class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> s = new Stack<>();

        for (String x : tokens) {
            if (x.equals("+"))
                s.push(s.pop() + s.pop());

            else if (x.equals("-")) {
                int b = s.pop();
                s.push(s.pop() - b);
            }

            else if (x.equals("*"))
                s.push(s.pop() * s.pop());

            else if (x.equals("/")) {
                int b = s.pop();
                s.push(s.pop() / b);
            }

            else
                s.push(Integer.parseInt(x));
        }

        return s.pop();
    }
}