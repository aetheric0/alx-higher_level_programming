#!/usr/bin/node
const rawList = require('./100-data').list;
const computedList = rawList.map((number, index) => number * index);
console.log(rawList);
console.log(computedList);
