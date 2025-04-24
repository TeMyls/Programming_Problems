#include "iostream"
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <cstdlib>
 
using namespace std;

class Solution {
    public:
        int removeElement(vector<int>& nums, int val) {
            int i = nums.size() - 1;
            int n = 0;
            while (i > -1){
                if (nums[i] == val){
                    nums.erase(nums.begin() + i);
                } else {
                    n++;
                }
                i--;
            }
            return n;
        }
};
int main (){
    Solution s;
    vector <int> nums = {3,2,2,3};
    int val = 3;
    cout << "LOLOLOL" << endl;
    cout << s.removeElement(nums, val) << " elements not equal to " << val << endl;
    //return 0;
}