#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = process.argv[2];
const wedgeAntilles = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const filmsInfo = JSON.parse(body);
    let count = 0;
    for (let i = 0; i < filmsInfo.results.length; i++) {
      if (filmsInfo.results[i].characters.includes(wedgeAntilles)) {
        count++;
      }
    }
    console.log(count);
  }
});
