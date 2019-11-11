class Solution {
    public int bitwiseComplement(int N) {
        if(N==0){return 1;}
        
        int i = 1;
        while(i <= N){
            i *= 2;
        }
        
        return i - N -1;
    }
}
