class Solution {

    public String encode(List<String> strs) {
        String update = "";
        for(String s : strs){
            update += s.length() + "%" + s;
        }
        return update;
    }

    public List<String> decode(String str) {
        List<String> update = new ArrayList<>();
        int len = 0;
        while(str.length() != 0){
            if(str.substring(len, len + 1).equals("%")){
                Integer num = Integer.valueOf(str.substring(0, len));
                update.add(str.substring(len + 1, len + 1 + num));
                str = str.substring(len + 1 + num);
                len = 0;
            }else{
                len++;
            }
        }
        return update;
    }
}
