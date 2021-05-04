class Solution {
    private int operate(Character op, Integer n1, Integer n2){
        if ('+' == op){return n1 + n2;}
        if ('-' == op){return n1 - n2;}
        if ('*' == op){return n1 * n2;}
        if ('/' == op){return n1 / n2;}
        return 0;
    }
    public int calculate(String s) {
        Stack<Integer>   nStack= new Stack<Integer>();
        Stack<Character> oStack= new Stack<Character>(); // the operator in front of '('
        Stack<Integer>   lsStack= new Stack<Integer>(); // last see number
        
        int curr = 0;
        int rslt = 0;
        int lastSee = 0;
        Character lastOperator = '+';
        int sign = 1;
        int result = 0;
        for (int i = 0; i < s.length(); i++){
            //System.out.println(curr);
            //System.out.println(result);
            //System.out.println();
            //number
            if (Character.isDigit(s.charAt(i))){
                curr = curr * 10 + (s.charAt(i) - '0');
            }
            //operator
            if ('+' == s.charAt(i)){
                if (lastOperator == '*' || lastOperator == '/'){
                    //curr = operate(lastOperator, lastSee, curr) * sign;
                    curr = operate(lastOperator, lastSee, curr);
                    lastSee = 0;
                }
                lastOperator = '+';
                //System.out.println(curr);
                result += sign * curr;
                curr = 0;
                sign = 1;
                
            }
            if ('-' == s.charAt(i)){
                if (lastOperator == '*' || lastOperator == '/'){
                    curr = operate(lastOperator, lastSee, curr);
                    lastSee = 0;
                }
                lastOperator = '-';
                result += sign * curr;
                curr = 0;
                sign = -1;
            }
            if ('*' == s.charAt(i)){
                if (lastOperator == '*' || lastOperator == '/'){
                    curr = operate(lastOperator, lastSee, curr) * sign;
                    sign = 1;
                }
                lastSee = curr;
                curr = 0;
                lastOperator = '*';
            }
            if ('/' == s.charAt(i)){
                if (lastOperator == '*' || lastOperator == '/'){
                    curr = operate(lastOperator, lastSee, curr) * sign;
                    sign = 1;
                }
                lastSee = curr;
                curr = 0;
                lastOperator = '/';
            }
            if ('(' == s.charAt(i)){
                //System.out.println(lastSee);
                lsStack.push(lastSee*sign);
                sign = 1;
                lastSee = 0;
                oStack.push(lastOperator);
                lastOperator = '+';
                nStack.push(result);
                result = 0;
            }
            if (')' == s.charAt(i)){
                if (lastOperator == '*' || lastOperator == '/'){
                    curr = operate(lastOperator, lastSee, curr);
                    lastOperator = '+';
                }
                result += sign * curr;
                
                sign = 1;
                //System.out.println(oStack.peek());
                //System.out.println(lsStack.peek());
                curr = operate(oStack.pop(), lsStack.pop(), result);
                result = nStack.pop();
                //System.out.println();
                lastSee = 0;
            }
            if (i == s.length() - 1){
                if (lastOperator == '*' || lastOperator == '/'){
                    curr = operate(lastOperator, lastSee, curr);
                    lastOperator = '+';
                }
                result += curr * sign;
            }
        }
        return result;
    }
}
