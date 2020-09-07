const path = require('path')

var Pi = path.normalize('foot/ball/play/ground')
var pi = path.normalize('foot\\ball\\play\\ground')
var pI = path.normalize('foot\\\ot-ball\\\play\\\ground')
var PI = path.normalize('foot\ot-ball\play\ground')

console.log(Pi)
console.log(pi)
console.log(pI)
console.log(PI)

/*
this module is used to normalize a path
it seems like it maeks a valid path out of a path which is not from this machine like the Pi-> has a mac address type
*/
