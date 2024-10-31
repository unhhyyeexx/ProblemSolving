class MinHeap {
    constructor() {
        this.heap = [null];
    }
    
    // 왼쪽 자식의 idx = 부모 idx*2
    // 오른쪽 자식의 idx = (부모idx*2) +1
    // 부모의idx = Math.floor(자식의idx / 2)
    push(value) {
        this.heap.push(value); // 힙 배열의 끝에 새 값을 추가
        let currentIdx = this.heap.length -1 // 새로 추가된 요소의 인덱스
        let parentIdx = Math.floor(currentIdx / 2); // 새 요소의 부모 인덱스
        
        // 최소힙이므로 부모 노드가 제일 작아야 한다.
        // 즉 부모 노드가 현재 노드보다 큰 지 검사하며 반복한다.
        while (parentIdx !== 0 && this.heap[parentIdx] > value) {
            // 부모 값이 새로 추가된 값보다 큰 동안만 부모와 위치를 교체
            const tmp = this.heap[parentIdx];
            this.heap[parentIdx] = value;
            this.heap[currentIdx] = tmp;
            currentIdx = parentIdx; // 현재 위치를 부모로 이동
            parentIdx = Math.floor(currentIdx/2); // 새로운 부모 인덱스 갱신
        }
    }
    
    // 루트 노드가 항상 먼저 배출된다.
    // 배출되고 나서 생기는 빈자리는 가장 마지막 노드, 즉 배열에서 제일 뒤에 있는 값을 가져온다.
    // 그리고 다시 루트노드서부터 재정렬을 실행한다.
    pop(){
        // null과 원소 1개가 남았을 경우 나오지 않는 것을 대비
        if(this.heap.length === 2) {
            return this.heap.pop() // 힙에 하나의 요소만 남았을 경우 바로 제거
        }

        const returnValue = this.heap[1]; // 배열의 첫 원소는 비워두므로 root는 heap[1]에 위치
        this.heap[1] = this.heap.pop() // 마지막 요소를 루트로 이동
        
        let currentIdx = 1; // 루트에서 시작
        let leftIdx = currentIdx * 2;
        let rightIdx = currentIdx * 2 + 1;
        
        // 왼쪽과 오른쪽 자식 노드 중 작은 값을 가진 자식과 위치를 교환하면서 힙 구조를 재정렬 한다. 
        while (this.heap[leftIdx] !== undefined &&  this.heap[currentIdx] > this.heap[leftIdx] ||
              this.heap[rightIdx] !== undefined && this.heap[currentIdx] >  this.heap[rightIdx]) {
            // 자식 노드가 없거나, 현재 노드가 자식보다 작을 때 반복문을 종료한다.
            if(this.heap[rightIdx] === undefined || this.heap[leftIdx] <= this.heap[rightIdx]) {
                // 왼쪽 자식이 더 작은 경우 왼쪽 자식과 교환
                const tmp = this.heap[currentIdx];
                this.heap[currentIdx] = this.heap[leftIdx];
                this.heap[leftIdx] = tmp;
                currentIdx = leftIdx;
            } else{
                // 오른쪽 자식이 더 작은 경우 오른쪽 자식과 교환
                const tmp = this.heap[currentIdx];
                this.heap[currentIdx] = this.heap[rightIdx];
                this.heap[rightIdx] = tmp;
                currentIdx = rightIdx;
            }
            // 새로운 자식 노드 인덱스를 갱신
            leftIdx = currentIdx * 2;
            rightIdx = currentIdx * 2 + 1;
        }
        return returnValue;
    }
}


function solution(scoville, K) {
    var answer = 0;
    const heap = new MinHeap();
    scoville.forEach((s) => {
        heap.push(s);
    });
    
    while (heap.heap[1] < K) {
        // 음식의 스코빌 지수를 K이상으로 만들 수 없을 때
        if (heap.heap.length === 2) return -1
        
        const a = heap.pop();
        const b = heap.pop();
        
        const mixed = a + b * 2;
        heap.push(mixed);
        answer ++;
    }
    
    return answer;
}