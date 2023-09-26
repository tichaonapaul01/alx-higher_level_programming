#!/usr/bin/node

// script that display the status code of a GET request.

const id = process.argv[2];

// Used string interpolation so as to pass argument with string
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

// import the request module
const req = require('request');

req(url, (err, res) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const body = JSON.parse(res.body);
    console.log(body.title);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
