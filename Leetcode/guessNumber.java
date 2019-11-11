/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int s = 0, e = n;
        while(s <= e){
            int m = s + (e-s)/2;
            if(guess(m) == 1){
                s = m+1;
            }else if(guess(n) == -1){
                e = m-1;
            }else{
                return m;
            }
        }
        return s;
    }
}
