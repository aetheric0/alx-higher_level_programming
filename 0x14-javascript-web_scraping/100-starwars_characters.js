#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const filmData = JSON.parse(body);
  for (const character of filmData.characters) {
    request(character, function (error, response, body) {
      if (error) {
        console.error(error);
      }
      const characterName = JSON.parse(body).name;
      console.log(characterName);
    });
  }
});
