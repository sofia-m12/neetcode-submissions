class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "");  //removing all non-alphanumeric characters
        s = s.toLowerCase();  //set s to all lowercase to avoid case sensitive
        int p1 = 0;            //1st pointer starts a t the front
        int p2 = s.length() - 1; //2nd pointer starts at the back
        while(p1 < p2){
            if(!(s.charAt(p1) == s.charAt(p2))){
                return false;
            }
            //return s.charAt(p1).equals(s.charAt(p2)); //will return true if elements are the same, false otherwise
            p1++;  //increment by 1
            p2--;  //decrease by 1
        }
        return true;
    }
}
