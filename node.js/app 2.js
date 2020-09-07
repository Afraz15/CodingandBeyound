                                    // TALKING ABOUT OBJECTS

var Hello = function() {
    console.log('hello world');
}

// when we make a variable it automatically become a global and we can acess it anytime.

window.Hello()

// we can call a variable like this but because it is global, It can be overwrited and we don't need that 
// in this case making a module is the best option.

/*
the setTime(),clearTimeout(),setInterval() and clearInterval() are part of window object.
we can acess them just by typing it like this or 'window.setTime()' <- like this
*/

                                