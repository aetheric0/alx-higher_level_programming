#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const outputFile = process.argv[3];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  fs.writeFile(outputFile, body, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.error(error);
    }
  });
});
