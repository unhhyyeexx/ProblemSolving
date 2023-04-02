from collections import defaultdict

def solution(atoms):
    answer = 0

    while len(atoms) >= 2:
        for i in range(len(atoms)):
            atoms[i][0] += dirs[atoms[i][2]][0]
            atoms[i][1] += dirs[atoms[i][2]][1]
        
        location = defaultdict(list)
        for atom in atoms:
            location[(atom[0], atom[1])].append(atom)
        
        natoms = []
        for l in location:
            if len(location[l]) >= 2:
                for ll in location[l]:
                    answer += ll[3]
            else:
                if -1000<=location[l][0][0] <= 1000 and -1000<=location[l][0][1]<=1000:
                    natoms.append(location[l][0])
        
        atoms = natoms

    return answer

T = int(input().strip())
for t in range(1, T+1):
    n = int(input())
    atoms = [list(map(int, input().split())) for _ in range(n)]
    dirs = [[0, 0.5], [0, -0.5], [-0.5, 0], [0.5, 0]]

    print(f'#{t} {solution(atoms)}')