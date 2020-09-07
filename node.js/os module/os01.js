const os = require('os')

var hi = os.cpus()
console.log(hi)

/*
this module is used just like the other modules
It gives complete information about cpu inside the current machine

model: -> the model of your machine copu 
speed: -> MHz ( maybe the speed of ram )
times: -> different modes of cpu

*/