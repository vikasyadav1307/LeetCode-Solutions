class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for a in s:
            if a == '(':
                st.append(')')
            elif a == '{':
                st.append('}')
            elif a == '[':
                st.append(']')
            else:
                if not st or st.pop() !=a:
                    return False
        return len(st) == 0