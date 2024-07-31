#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const newData = {};
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  const completedTasks = {};
  for (const task of data) {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0
        }
        completedTasks[task.userId]++;
    }
  }
  console.log(completedTasks);
});
