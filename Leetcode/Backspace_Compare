class Solution {
    public boolean backspaceCompare(String S, String T) {
        return helper(S).equals(helper(T));
    }
    
    public String helper(String S){
        Stack<Character> ans = new Stack();
        
        for(char c :S.toCharArray()){
            if(c != '#'){
                ans.push(c);
            }else if(! ans.empty()){
                ans.pop();
            }
        }
        
        return String.valueOf(ans);   
    }
}
