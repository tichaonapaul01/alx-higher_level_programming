#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printOrderly(characters, 0);
  }
});

const printOrderly = (characters, index) => {
  request(characters[index], (error, response, body) => {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printOrderly(characters, index + 1);
      }
    }
  });
};
