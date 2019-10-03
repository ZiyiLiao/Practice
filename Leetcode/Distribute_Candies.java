class Solution {
    public int[] distributeCandies(int candies, int num_people) {
        int[] ans = new int[num_people];
        
        int count = 0;
        
        while(candies > 0){
            ans[count % num_people] += (count < candies)? (count + 1) : candies;
            count += 1;
            candies -= count;
        }
        
        return ans;
        
    }
}
