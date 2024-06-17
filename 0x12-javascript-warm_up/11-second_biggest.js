#!/usr/bin/node
let values = [];
let result;
process.argv.slice(2).forEach(val => {
  values.push(Math.floor(Number(val)));
});
function biggestValue() {
  result = values[0];
  for (let i = 0; i < values.length; i++) {
    if (values[i] > result) {
      result = values[i]
    }
  }
}
biggestValue();
values = values.filter(value => value !== result);
biggestValue();
console.log(result);
