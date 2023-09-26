#!/usr/bin/node

// script that gets the contents of a webpage and stores it in a file

const fs = require('fs');
const req = require('request');

const url = process.argv[2];
const filename = process.argv[3];

req(url, (err, res) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    fs.writeFile(filename, res.body, 'utf-8', (e) => {
      if (e) {
        console.log(e);
      }
    });
  } else {
    console.log('code: ' + res.statusCode);
  }
});
