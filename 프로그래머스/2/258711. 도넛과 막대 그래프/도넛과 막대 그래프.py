from collections import defaultdict

def solution(edges):
    answer = [0,0,0,0]
    
    graph_in = defaultdict(int)
    graph_out = defaultdict(int)
    nodes = set()
    for a, b in edges:
        graph_in[b] += 1
        graph_out[a] += 1
        nodes.add(a)
        nodes.add(b)
        
    for node in nodes:
        # 생성한 정점의 번호: 나가는 간선 2개 이상(그래프 합이 2 이상), 들어오는 간선 없음
        if graph_out[node] and graph_out[node] >=2 and not graph_in[node]:
            answer[0] = node
        # 막대모양 그래프: 나가는 간선만 있고 들어오는 간선이 없는 노드의 개수와 같음
        elif not graph_out[node] and graph_in[node] and graph_in[node] > 0:
            answer[2] += 1
        # 8자 모양 그래프: 나가는 간선과 들어오는 간선의 수가 2개로 같은 노드의 개수와 같음, 들어오는 간선중 생성점에서 들어오는 것도 있으므로 2이상으로 탐색
        elif  graph_in[node] and graph_in[node] >= 2 and graph_out[node] and graph_out[node] == 2:
            answer[3] += 1
    
    # 도넛 모양 그래프: 생성된 정점의 나가는 간선 수에서 막대, 8자 그래프의 개수를 빼면 나옴.
    answer[1] = graph_out[answer[0]] - answer[2] - answer[3]
    
    
    return answer