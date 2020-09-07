var url = 'http://google.com';

console.log(__filename);
console.log(__dirname)

function hello(message) {
    console.log(message);
}

function hi() {
    console.log('this is the 2nd private file')
}

module.exports.pvt = hello; //this is how we export our file and pvt is a random name
module.exports = hi;
exports.pvt = hello;    // this is a reference/short form of module.exports but we cannot write it like exports = hello;


/* 
so the thing is that we are going to make a module here and remember that each file like app.js is a module
we are going to make a private module here and the modules are changable only in here and when we export it to someother
file then it will only be a read-only file (private)
if we want to see the directory/location of the file then we use __filename,__dirname
*/