class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for(int i = s.length() - 1; i >= 0; i--){
            if(s.charAt(i) == '('){
                if(stack.isEmpty() || stack.pop() != ')'){
                    return false;
                }
            }else if(s.charAt(i) == '{'){
                if(stack.isEmpty() || stack.pop() != '}'){
                    return false;
                }
            }else if(s.charAt(i) == '['){
                if(stack.isEmpty() || stack.pop() != ']'){
                    return false;
                }
            }else{
                stack.push(s.charAt(i));
            }
        }
        return stack.isEmpty();
    }
}
