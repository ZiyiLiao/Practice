class Solution {
    public int addDigits(int num) {
        if(num < 10){return num;}
        else{return addDigits(helper(num));}
       
    }
    
    private int helper(int num){
        int digit = 0;
        while(num > 0){
            digit += num % 10;
            num /= 10;
        }
        return digit;
    }
    
}
