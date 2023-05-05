package programmers.problems.베스트앨범;

import java.util.*;

class Music implements Comparable<Music>{
    int id;
    int playCnt;
    
    Music(int id, int playCnt) { this.id = id; this.playCnt = playCnt; }
    
    // 재생 횟수 기준 내림차순, 고유번호 기준 오름차순
    public int compareTo(Music m){
        if (this.playCnt - m.playCnt == 0) 
            return this.id - m.id;
        return m.playCnt - this.playCnt;
    }
    
    public String toString(){ return "" + id; }
    
    public int getPlayCnt() { return playCnt; }
}

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, List<Music>> datas = new HashMap<>();
        
        // 장르/음악 담기
        for(int i = 0; i < plays.length; i++){
            List<Music> mList = datas.getOrDefault(genres[i], new ArrayList<Music>());
            mList.add(new Music(i, plays[i]));
            
            datas.put(genres[i], mList);
        }
        
        // List<Music>의 총 playCnt 기준 장르 정렬
        List<String> keys = new ArrayList<>(datas.keySet());
        keys.sort((g1, g2) 
                    -> datas.get(g2).stream().mapToInt(Music::getPlayCnt).sum() - datas.get(g1).stream().mapToInt(Music::getPlayCnt).sum());
        
        // 장르별 조건 만족하는 두곡씩 뽑기
        List<Integer> numbers = new ArrayList<>();
        for (String g : keys){
            List<Music> curM = datas.get(g);
            Collections.sort(curM);
            
            numbers.add(curM.get(0).id);
            if (curM.size() >= 2) numbers.add(curM.get(1).id);
        }
        
        return numbers.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}