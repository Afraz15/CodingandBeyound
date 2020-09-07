const path = require('path')

var hello = path.relative('foot/ball/play/ground', '/hello/world')

console.log(hello)

/*
this module joins two addresses but hide their names so we can tell how many directories are...
*/