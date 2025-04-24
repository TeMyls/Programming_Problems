#include "iostream"
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <cstdlib>
 
using namespace std;

void printVectorInt(vector<int> v){
    for(int i = 0; i < v.size(); i++){
        cout << "Index: " << i << " Value: " << v[i] << endl;
    }
 
}

class Solution {
    public:
        int removeDuplicates(vector<int>& nums) {
            int i = nums.size() - 1;
            int n = 1;
            while (i > 0){
                if (nums[i - 1] == nums[i]){
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
    vector <int> nums = {0,0,1,1,1,2,2,3,3,4};
    printVectorInt(nums);
    cout << s.removeDuplicates(nums) << endl;
    printVectorInt(nums);
    
    //return 0;
}