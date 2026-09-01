class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        HashMap<String, List<String>> freq = new HashMap<>();
        for(int i = 0; i < strs.length; i++){
            int[] def = new int[26];
            String str = strs[i];
            StringBuilder sb = new StringBuilder();
            for(int j = 0; j < str.length(); j++){
                def[str.charAt(j) - 'a'] += 1;
            }
            for(int n : def){
                sb.append((char)n);
            }
            if(freq.containsKey(sb.toString())){
                freq.get(sb.toString()).add(str);
            }else{
                List<String> temp = new ArrayList<>();
                temp.add(str);
                freq.put(sb.toString(), temp);
            }
        }
        for(List<String> ls : freq.values()){
            res.add(ls);
        }
        return res;
    }
}
