console.log('hello world')

let age = 25 //let value can be changed anytime

const salary = 25000

console.log(age)
//salary = 5000  //cannot change
console.log(salary)

//Data type:-
//Primitive     //Not primitive


//strings
const str = 'This'
const str2 = `This backticked
multi line possible`


//boolean
const isboolean = true

//numbers - float, decimal, integers

//BigInt type


//symbol type

//undefined
let result

//null
const data = null

console.log(str2)
console.log(result)
console.log(data)

//Non primitive
//Objects

let obj = {
    firstname:'Bruce',
    lastname:'Wayne'
}

console.log(obj.firstname,obj['firstname'],typeof(obj))   //Like python dictionary . 
//Can be any data type . Dot notation can used. Dictionary notation also


//Arrays
const arr = [1,2,3,4]

//Assignment operators
// = symbol

//Arithmetic operators
// +,-,*,/,%,++,--,==,!=, ===(also data type), > <

//Logical opertors ==> will give true/false
//&& , || , !


console.log('Bruce'+'Wayne')
const isEven = 10%2 == 0 ? 'Even':'Odd' //Ternary operator
console.log(isEven)

//Type conversion

//Implicit conversion (Cohersion) automatic
console.log(2+'3') // num + string = string
console.log(true+'3') //bool + string = string
console.log('2'+'3')  //str arithmetic op addition str (str)
console.log('2'-'3')  //str arithmetic op any other result number
console.log('str'-'str')  //result into Nan

// int values : true = 1, false = 0 [ will convert to int when possible]

console.log(5-true) //4
console.log('5'-true) //4

// values for Nan, null, undefined = 0, ',', 0
console.log('5'-NaN) //Nan
console.log('5'* null) //0

//Any opertion with undefined is NaN

//Explicit conversion
console.log(parseInt('5')) //parseFloat, String method

//Conditional statements
//if, else if, switch, else
if (5>0)
{
    console.log('positive')
}
else
{ 
    pass
 }

let color='yellow'
switch (color)
{
    case 'red':
        console.log('red')
        break
    case 'yellow':
        console.log('yelloe')
        break
    default:
        console.log('Not valid color')
}

//loops

//for loop
  
for (i=0;i<arr.length;i++)
{console.log(arr[i])}

//looping over array
for (const num of arr)
{
console.log(num)
}

//functions
function name(a,b)
{
    return a+b
}
console.log(name(2,3))

//arrow functions
const arrfn = (a,b) => {
    return a+b
}
console.log(arrfn(25,45))

//scope

