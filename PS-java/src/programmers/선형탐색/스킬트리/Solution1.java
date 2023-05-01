package programmers.선형탐색.스킬트리;

class Solution1 {
    boolean check(boolean[] checked, int idx){
        for (int i = 0; i < idx; i++){
            if (!checked[i]) return false;
        }
        return true;
    }
    
    public int solution(String skill, String[] skill_trees) {
        int cnt = 0;
        
        for (String skill_tree : skill_trees){
            boolean[] checked = new boolean[skill.length()];
            boolean success = true;
            for (char x : skill_tree.toCharArray()){
                int idx = skill.indexOf(x);
                if (idx < 0) continue;
                if (check(checked, idx)) {
                    checked[idx] = true;
                }
                else{
                    success = false;
                    break;
                }
            }
            if (success) cnt++;
        }
        
        return cnt;
    }
}
