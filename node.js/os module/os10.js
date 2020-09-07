const os = require('os')

var hello = os.totalmem()
var hi = os.type()
var hey = os.uptime()
var yo = os.version()

console.log('total memory: ' + hello)
console.log('\ntype of os: ' + hi)
console.log('\nuptime of machine: ' + hey)
console.log('\nversion: ' + yo)

/*
they are just like how they appear to be;One tells the total memory of the machine then os,optime and the type of
version it is using 
*/

