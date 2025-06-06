# [Gold IV] 페그 솔리테어 - 9207 

[문제 링크](https://www.acmicpc.net/problem/9207) 

### 성능 요약

메모리: 13720 KB, 시간: 200 ms

### 분류

백트래킹, 브루트포스 알고리즘, 구현

### 제출 일자

2025년 1월 7일 20:38:50

### 문제 설명

<p>페그 솔리테어는 구멍이 뚫려있는 이차원 게임판에서 하는 게임이다. 각 구멍에는 핀을 하나 꽂을 수 있다.</p>

<p>핀은 수평, 수직 방향으로 인접한 핀을 뛰어넘어서 그 핀의 다음 칸으로 이동하는 것만 허용된다. 인접한 핀의 다음 칸은 비어있어야 하고 그 인접한 핀은 제거된다.</p>

<p>현재 게임판에 꽂혀있는 핀의 상태가 주어진다. 이때, 핀을 적절히 움직여서 게임판에 남아있는 핀의 개수를 최소로 하려고 한다. 또, 그렇게 남기기 위해 필요한 최소 이동횟수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 1 ≤ N ≤ 100이 주어진다. 각 테스트 케이스는 게임판의 초기 상태이다.</p>

<p>게임판은 모두 같은 모양을 가진다. (예제 참고) '.'는 빈 칸, 'o'는 핀이 꽂혀있는 칸, '#'는 구멍이 없는 칸이다. 핀의 개수는 최대 8이며, 각 테스트 케이스는 빈 줄로 구분되어져 있다.</p>

### 출력 

 <p>각 테스트 케이스에 대해서, 핀을 움직여서 남길 수 있는 핀의 최소 개수와 그 개수를 만들기 위해 필요한 최소 이동 횟수를 출력한다.</p>

