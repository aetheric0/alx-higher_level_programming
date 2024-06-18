#!/usr/bin/node
const { dict } = require('./101-data');
const newDict = {};
for (const [userId, occurrence] of Object.entries(dict)) {
  if (!newDict[occurrence]) {
    newDict[occurrence] = [];
  }
  newDict[occurrence].push(userId);
}
console.log(newDict);
