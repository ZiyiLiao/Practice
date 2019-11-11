class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int dist = 99;
        char ans = letters[0];
        for(int i = 0; i < letters.length; i++){
            int temp = letters[i] - target;
            if(temp > 0 && temp < dist){
                ans = letters[i];
                dist = temp;
            }
        }
        return ans;
    }
}
