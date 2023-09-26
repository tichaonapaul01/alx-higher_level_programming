#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const dic = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const task = tasks[i];
      if (task.completed === true) {
        if (dic[task.userId] === undefined) {
          dic[task.userId] = 1;
        } else {
          dic[task.userId]++;
        }
      }
    }
    console.log(dic);
  } else {
    console.log('Error ' + response.statusCode);
  }
});
