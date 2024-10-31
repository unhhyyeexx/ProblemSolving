function solution(genres, plays) {
    var dic = {};
    genres.forEach((g, i) => {
        dic[g] = dic[g] ? dic[g]+plays[i] : plays[i];
    });
    console.log(genres)
    console.log(dic)
    var dic2 = {}; // 장르별 최대 두 곡을 거르는 용도
    return genres
        .map((g, i) => ({genre:g, cnt: plays[i], idx: i}))
        .sort((a, b) => {
            // 1. 장르가 다르면 dic 객체에서 장르별로 총 재생 횟수를 기준으로 내림차순 정렬한다.
            // 2. 장르가 같다면 cnt 값을 비교해 재생 횟수가 많은 순서로 정렬한다.
            // 3. 재생 횟수까지 같다면 idx 로 오름차순 정렬한다(고유번호가 작은순)
            if( a.genre !== b.genre) return dic[b.genre] - dic[a.genre];
            if (a.cnt !== b.cnt) return b.cnt - a.cnt
            return a.idx - b.idx
    })
        .filter(g => {
            // 각 장르당 최대 두 곡까지만 유지하도록 필터링
            // dupDic[t.genre] >= 2인 경우 return false;로 필터링에서 제외
            //그렇지 않으면 해당 장르의 곡을 추가하고 dupDic[t.genre] 값을 1 증가
            if(dic2[g.genre] >= 2) return false;
            dic2[g.genre] = dic2[g.genre] ? dic2[g.genre]+1 : 1;
            return true;
    })
        .map(g => g.idx) // 각 노래 객체의 idx 값을 추출해 배열로 반환
    
}