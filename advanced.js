//nested function scopes

//nested functions have access to variables declared within their scope as well as outer function scope

//---Closure

//A closure is a combination of functions bundled together with reference to its surroundings state. Closures are created every time 
// a function is created , at function creation time

function outer()
{
    let counter = 0
    function inner()
    {
        counter++
        console.log(counter)
    }
    inner()
}

outer() // op:1
outer()  //op again 1 as counter is reinitialized for every function call

function outer()
{
    let counter = 0
    function inner()
    {
        counter++
        console.log(counter)

    }
    return inner   // return the inner function instead of calling

}

const fcn = outer()   // the function along with its scope is returned so that is kept in persistent memory. 
//`thus next time invoked it remembers the value`
fcn()  //op:1
fcn()   //op: 2


//Function currying (Transforms a function)

//This keyword

/* Implicit binding
Explicit binding
New binding
Default binding */

//Functionss can be defined inside of objects



