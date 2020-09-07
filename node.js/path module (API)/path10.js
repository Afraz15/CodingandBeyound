const path = require('path')

var h = path.resolve('hello/world', 'and/the/people', 'living/on/it')
var H = path.resolve('/hello/world', '/and/the/people', '/living/on/it')
var hi = path.resolve('/hello/world', './and/the/people', './living/on/it')

console.log(h)
console.log(H)
console.log(hi)

