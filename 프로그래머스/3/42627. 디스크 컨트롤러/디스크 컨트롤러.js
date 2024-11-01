class MinHeap{
    constructor() {
        this.heap = [null];
    }
    
    push(length, time) {
        this.heap.push({length, time});
        let currentIdx = this.heap.length - 1;
        let parentIdx = Math.floor(currentIdx/2);
        
        while (parentIdx !== 0 && this.heap[parentIdx].length >this.heap[currentIdx].length){
            const tmp = this.heap[parentIdx];
            this.heap[parentIdx] = this.heap[currentIdx];
            this.heap[currentIdx] = tmp;
            currentIdx = parentIdx;
            parentIdx = Math.floor(currentIdx/2);
        }
    }
    
    pop() {
        if (this.heap.length <= 2){
            return this.heap.pop();
        }
        
        const returnValue = this.heap[1];
        this.heap[1] = this.heap.pop();
        
        let currentIdx = 1;
        let leftIdx = currentIdx * 2;
        let rightIdx = currentIdx * 2 + 1;
        
        while (leftIdx < this.heap.length && this.heap[leftIdx].length < this.heap[currentIdx].length ||
              rightIdx < this.heap.length && this.heap[rightIdx].length < this.heap[currentIdx].length) {
            if (rightIdx >= this.heap.length || this.heap[leftIdx].length < this.heap[rightIdx].length){
                const tmp = this.heap[leftIdx];
                this.heap[leftIdx] = this.heap[currentIdx];
                this.heap[currentIdx] = tmp;
                currentIdx = leftIdx;
            } else{
                const tmp = this.heap[rightIdx];
                this.heap[rightIdx] = this.heap[currentIdx];
                this.heap[currentIdx] = tmp;
                currentIdx = rightIdx;
            }
            leftIdx = currentIdx * 2;
            rightIdx = currentIdx * 2 + 1;
        }
        return returnValue;
    }
        
    
}

function solution(jobs) {
    let answer = 0; 
    let cnt = 0; //시간
    let complete = 0; // 완료된 작업 개수
    
    const heap = new MinHeap();
    const jobLength = jobs.length;
    
    jobs.sort((a, b) => a[0] - b[0]) // 작업이 들어오는 시간(jobs[0]을 기준으로 정렬)
    
    while (jobs.length || heap.heap.length - 1){
        // jobs 와 heap에 작업이 들어있으면 반복한다.
        while(jobs.length && jobs[0][0] <= cnt) {
            // 시작 시간이 cnt와 일치하면 jobs에서 요소를 빼 heap에 넣어준다.
            const finish = jobs.shift();
            heap.push(finish[1], finish[0]);
        }
        
        if (heap.heap.length - 1 && cnt >= complete){
            // heap에 요소가 있고, 현재 시간(cnt)이 완료시간(complete)과 같거나 크면,
            // 힙에서 가장 시간이 짧은 요소를 꺼내고, 완료 시간에 꺼내온 작업 시간을 더해주고 cnt도 더해준다.
            const task = heap.pop();
            complete = task.length + cnt;
            answer += (complete - task.time);
        }
        cnt++;
    }
    return Math.floor(answer / jobLength);
}