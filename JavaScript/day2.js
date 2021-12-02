const fs = require("fs");
var path = require('path');
var text = fs.readFileSync("./Inputs/day2.txt",
{encoding:'utf8', flag:'r'});
var data = text.split('\r\n')

directions = []
data.forEach(element => {
    directions.push(element.split(' '))
});

horizontal = 0
depth = 0

directions.forEach(element => {
    if(element[0]=='forward'){
        horizontal += Number(element[1])
    }
    else if(element[0]=='down'){
        depth += Number(element[1])
    }
    else if(element[0]=='up'){
        depth -= Number(element[1])
    }
});

console.log('horizontal: ' + horizontal)
console.log('depth: ' + depth)
console.log('first answer: ' + depth*horizontal)

horizontal = 0
depth = 0
aim = 0

directions.forEach(element => {
    if(element[0]=='forward'){
        horizontal += Number(element[1])
        depth += Number(element[1]) * aim
    }
    else if(element[0]=='down'){
        aim += Number(element[1])
    }
    else if(element[0]=='up'){
        aim -= Number(element[1])
    }
});

console.log('horizontal: ' + horizontal)
console.log('depth: ' + depth)
console.log('aim: ' + aim)
console.log('second answer: ' + depth*horizontal)
