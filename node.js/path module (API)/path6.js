path = require('path')

var p = path.join('foot', 'ball', 'play', 'ground')
var P = path.join('\\games', 'are', 'good', 'to', '..', 'play', 'when', 'your', '..')

console.log(p)
console.log(P)


/*
this module is used to join the paths/make an address out of it
NOTE: the values inside of join brackets must be strings/'hello'
if we put '..' in the join then it will skip 1 string from the left side
*/

