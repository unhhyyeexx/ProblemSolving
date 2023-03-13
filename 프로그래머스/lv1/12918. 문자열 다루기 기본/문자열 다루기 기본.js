function solution(s) {
    if (![4,6].includes(s.length)) {
        return false;
    }
    for (i of s.split("")) {
        if (isNaN(Number(i))) {
            return false;
        }
    }
    return true;
}