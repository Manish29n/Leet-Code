class Solution {
public:
    map<int,int> memo;
    int climbStairs(int n) {
        if(memo.count(n))
            return memo[n];
        if(n==1){
            memo[n]=1;
            return memo[n];
        }
        if(n==2){
            memo[n]=2;
            return memo[n];
        }
        int res=climbStairs(n-1)+climbStairs(n-2);
        memo[n]=res;
        return memo[n];
    }
};
