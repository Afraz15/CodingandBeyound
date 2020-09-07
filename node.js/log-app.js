const fun = require('./logger.js')

// var fun = require('./logger.js'); // this is how we import/use the private file

fun.pvt('this is private file');

/*
i was having a bit of problem with the file execution
the problem was that i named the log-app.js -> logger app.js (put space between them) and the terminal was not 
executing the file so NOTE that in programming , never put space in the name of the file

instead of using a var -> cont is more promising because the value of const cannot be changed
*/



