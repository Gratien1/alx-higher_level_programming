#!/usr/bin/node

const process = require('process');
const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const episodeInfo = JSON.parse(body);
    console.log(episodeInfo.title);
  }
});
