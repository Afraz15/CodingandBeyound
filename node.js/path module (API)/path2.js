const path = require('path')

var H = path.dirname('C:\Users\Afraz\Downloads') // this built-in module is used to show the name of the directory
var h = path.dirname('C:/Users/Afraz/Downloads')

console.log('unchanged: ' + H)
console.log('changed address: ' + h)

/*
This module is useful if we want to find the name of the directory like dirname(filename) and it will show us
the name of the directory it is in..
It seems like the direction of slash affect the results
*/



