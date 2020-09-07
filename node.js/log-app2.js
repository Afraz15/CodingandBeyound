const fun = require('./logger.js')

fun()

/*
we replace the mocule.exports.name = hi by removing '.hi' in it because we don't need that 
that mathod is used if we have many properties/methods so we make it an object but since this only has one function 
we just type it like that and instead of calling it fun.name() -> fun() because it's a single function
*/



