#!/usr/bin/node

// script that prints all characters of a Star Wars movie:

const req = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

req(url, (err, res) => {
  if (err) { console.log(err); } else if (res.statusCode === 200) {
    const body = JSON.parse(res.body);
    const charArr = body.characters;

    for (let i = 0; i < charArr.length; i++) {
      req(charArr[i], (e, r) => {
        if (e) { console.log(e); } else if (r.statusCode === 200) {
          const body = JSON.parse(r.body);
          console.log(body.name);
        } else { console.log('code: ' + r.statusCode); }
      });
    }
  } else { console.log('code: ' + res.statusCode); }
});
