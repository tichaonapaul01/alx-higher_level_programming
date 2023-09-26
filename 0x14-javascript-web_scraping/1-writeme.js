#!/usr/bin/node

// script that reads and prints the content of a file

const filepath = process.argv[2];
const content = process.argv[3];

// import the file storage module
const fs = require('fs');

// use the writeFile function of the fs module

fs.writeFile(filepath, content, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
