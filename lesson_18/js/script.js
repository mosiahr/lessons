// Строгий режим
"use strict"


// const userName = 20
// userName = "Вася"
// console.log(userName) // Ошибка, так как переменная объявлена с ключевым словом const и не может быть изменена

let numOne = 20
let numTwo = "20"

// let numSum = numOne + numTwo
// console.log(numSum) // string

let numSub = numOne - numTwo
console.log(numSub) // string

let numSum = numOne + Number(numTwo)
console.log("NUMM: ", numSum) // number
