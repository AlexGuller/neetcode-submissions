class Solution {

    public String encode(List<String> strs) {
        StringBuilder str = new StringBuilder();
        for(String curr : strs){
            str.append(curr.length());
            str.append("#");
            str.append(curr);
        }
        return str.toString();
    }


    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int cntr = 0;
        while(cntr < str.length()){
            int j = cntr;
            while(str.charAt(j) != '#'){
                j++;
            }
            int len = Integer.parseInt(str.substring(cntr, j));
            res.add(str.substring(j + 1, j + 1 + len));
            cntr = j + 1 + len;
        }
        return res;
    }
}
