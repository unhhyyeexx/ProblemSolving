function solution(priorities, location) {
  var answer = 0;
  var q = [];
  for ([idx, prior] of Object.entries(priorities)) {
    q.push([prior, Number(idx)]);
  }
  priorities.sort((a, b) => b - a);

  while (q.length > 0) {
    var now = q.shift();
    if (now[0] >= Math.max(...priorities)) {
      answer++;
      if (now[1] === location) return answer;
      else priorities.shift();
    } else {
      q.push(now);
    }
  }
  return answer;
}