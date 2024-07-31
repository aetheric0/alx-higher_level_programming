#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let characterFilms = [];
let foundCharacter = false;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const films = JSON.parse(body).results;
  for (const film of films) {
    for (const character of film.characters) {
      if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
        request(character, function (error, response, body) {
          if (error) {
            console.error(error);
          }
          const characterData = JSON.parse(body);
          characterFilms = characterData.films;
          console.log(characterFilms.length);
        });
        foundCharacter = true;
        break;
      }
    }
    if (foundCharacter) {
      break;
    }
  }
});
