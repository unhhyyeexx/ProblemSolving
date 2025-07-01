function solution(genres, plays) {
    // reduce 함수는 genres 배열의 각 장르를 순회하며, 장르별 총 재생 횟수를 계산하는 데 사용
    // acc는 장르별 총 재생 횟수를 저장하는 객체
    // (acc[genre] || 0) + plays[idx] 는 현재 장르의 재생횟수를 누적해 계산한다.  acc[genre]가 이미 존재하면 기존 값을 가져오고, 없으면 0을 기본값으로 더한다.
    // 최종적으로 genrePlayCnt는 {장르: 총 재생 횟수} 형태의 객체가 된다.
    const genrePlayCnt = genres.reduce((acc, genre, idx) => {
        acc[genre] = (acc[genre] || 0) + plays[idx];
        return acc;
    }, {});
    
    // map 함수를 사용해 각 노래의 정보를 객체 형태로 저장한다.
    // songs 배열에는 {genre, playCnt, idx}형식의 객체가 들어간다.
    // 
    const songs = genres.map((genre, idx) => ({
        genre, // 노래의 장르
        playCnt: plays[idx], // 해당 노래의 재생 횟수
        idx, // 노래의 고유 번호
    }));
    
    const sortedSongs = songs.sort((a, b) => {
        // 1. 장르 총 재생 횟수 내림차순 정렬
        if (genrePlayCnt[b.genre] !== genrePlayCnt[a.genre]) {
            return genrePlayCnt[b.genre] - genrePlayCnt[a.genre];
        }
        // 2. 개별 곡 재생 횟수 내림차순
        if (b.playCnt !== a.playCnt) {
            return b.playCnt - a.playCnt;
        }
        // 3. 고유 번호 오름차순
        return a.idx - b.idx
    });
    
    const selectedSongCnt = {}; // 각 장르별로 이미 선택된 곡의 개수
    const bestAlbum = []; // 최종 결과로 반환할 베스트 앨범의 고유 번호를 담을 배열
    
    for (const song of sortedSongs) {
        // 장르별 최대 두 곡만 선택
        if (selectedSongCnt[song.genre] >= 2) continue;
        bestAlbum.push(song.idx);
        selectedSongCnt[song.genre] = (selectedSongCnt[song.genre] || 0) + 1
    }
    
    return bestAlbum
    
}