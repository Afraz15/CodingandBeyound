const path = require('path')

var hi = path.isAbsolute('C:/Users/Afraz/Downloads')
var hI = path.isAbsolute('Users/Afraz/Downloads')
var Hi = path.isAbsolute('/Users/Afraz/Downloads')
var HI = path.isAbsolute('C:\Users\Afraz\Downloads')
var last = path.isAbsolute('C:\\Users\\Afraz\\Downloads')

console.log(hi)
console.log(hI)
console.log(Hi)
console.log(HI)
console.log(last)

/*
This module help us check if the address of the file is in it's correct rules or not
*/


