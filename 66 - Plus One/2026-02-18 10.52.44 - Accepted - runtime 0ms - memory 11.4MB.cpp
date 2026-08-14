#include <vector>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        
        for (int i = digits.size() - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;      // add 1
                return digits;    // done
            }
            digits[i] = 0;        // carry forward
        }

        // if all digits were 9
        digits.insert(digits.begin(), 1);
        return digits;
    }
};