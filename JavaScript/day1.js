const fs = require("fs");
var path = require('path');
var text = fs.readFileSync("./Inputs/day1.txt",
{encoding:'utf8', flag:'r'});
var data = text.split('\n').map(Number);
n = 9999999
count = 0
console.log(data.length);
for(const line in data){
    if(n<data[line]){
        count++
    }
    n = data[line]
}
console.log('first answer: '+ count);
count = 0;
for(const line in data){
    num = Number(line)
    a = data[num] + data[num+1] + data[num+2]
    b = data[num+1] + data[num+2] + data[num+3]
    if(a<b){
        count++
    }
}
console.log('second answer: '+ count);