#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, data1) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.readFile(process.argv[3], 'utf8', (err, data2) => {
    if (err) {
      console.error(err);
      return;
    }
    const concatData = data1 + data2;
    fs.writeFile(process.argv[4], concatData, (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
});
