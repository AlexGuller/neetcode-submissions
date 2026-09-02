class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer, Set<Character>> box = new HashMap<>();
        HashMap<Integer, Set<Character>> column = new HashMap<>();
        HashMap<Integer, Set<Character>> row = new HashMap<>();
        for(int i = 0; i < 9; i++){
            row.put(i, row.getOrDefault(i, new HashSet<>()));
            for(int j = 0; j < 9; j++){
                column.put(j, column.getOrDefault(j, new HashSet<>()));
                int boxIdx = (int)(i / 3) * 3 + (int)(j / 3);
                box.put(boxIdx, box.getOrDefault(boxIdx, new HashSet<>()));

                char currVal = board[i][j];
                if(currVal == '.'){
                    continue;
                }
                if(row.get(i).contains(currVal) || column.get(j).contains(currVal) || box.get(boxIdx).contains(currVal)){
                    return false;
                }else{
                    box.get(boxIdx).add(currVal);
                    row.get(i).add(currVal);
                    column.get(j).add(currVal);
                }
            }
        }
        return true;
    }
}
