class Solution {
    public boolean isPalindrome(String s) {
        if(s.length() == 0){
            return true;
        }
        String[] wordArr = s.trim().split("[^a-zA-Z0-9]+");
        String str = "";
        for(int i = 0; i < wordArr.length; i++){
            str += wordArr[i].trim().toLowerCase();
        }
        char[] backwards = str.toCharArray();
        int front = 0;
        int back = backwards.length - 1;
        while(front < backwards.length - 1 && back > 0){
            if(backwards[front] != backwards[back]){
                return false;
            }
            front++;
            back--;
        }
        return true;
    }
}
