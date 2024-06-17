#!/usr/bin/node
let result = 1;
const number = Math.floor(Number(process.argv[2]));
function factorial (number) {
  if (isNaN(number)) {
    console.log(1);
    return;
  }
  if (number === 0) {
    console.log(result);
    return;
  }
  result *= number;
  return factorial(number - 1);
}
factorial(number);
