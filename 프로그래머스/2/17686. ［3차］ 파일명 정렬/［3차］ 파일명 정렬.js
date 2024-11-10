function solution(files) {
    let answer = [];
    let sepFiles = [];
    
    for(let i=0; i<files.length; i++) {
        let head = '', number='', tail='';
        for (let j=0; j<files[i].length; j++) {
            const f = files[i][j];
            if (head.length==00 || ((isNaN(f) || f===' ') && number.length===0)) head += f;
            else if (!isNaN(f) && head.length>0 && tail==='') number += f;
            else if (tail.length>0 || (number.length>0 && (isNaN(f) || f===' '))) tail += f;
        }
        sepFiles.push([head, number, tail]);
    }
    sepFiles
        .sort((a, b) => (a[0].toLowerCase().localeCompare(b[0].toLowerCase())) || Number(a[1]) - Number(b[1]))
        .forEach((file) => answer.push(file.join("")));
    
    return answer;
}