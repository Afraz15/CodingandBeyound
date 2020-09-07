const path = require('path')

var hello = path.parse('foot/ball/play/ground')
var hEllo = path.parse('foot/ball/play/ground/file.html')
var heLlo = path.parse('/foot/ball/play/ground/file.html')

console.log(hello)
console.log(hEllo)
console.log(heLlo)

/*
so this module help us check the type of data inside it's parenthsis 
it works only with this -> '/' type of slash
root: -> the name of the drive/root folder
dir: -> path/directory of the file
base: -> name of the file
ext: -> file type/extension like .jpeg,png,html
name: -> name of the file

*/


