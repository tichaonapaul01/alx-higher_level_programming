#!/usr/bin/node

// script that display the status code of a GET request.

const url = process.argv[2];

// import the request module
const req = require('request');

req(url, (err, res) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const body = JSON.parse(res.body);
    const result = body.results;
    let count = 0;

    for (let i = 0; i < result.length; i++) {
      const charArr = result[i].characters;
      for (let j = 0; j < charArr.length; j++) {
        if (charArr[j].includes('18')) { count++; }
      }
    }
    console.log(count);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
