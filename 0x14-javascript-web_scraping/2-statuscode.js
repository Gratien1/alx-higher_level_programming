#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (!err) console.log('code: ' + res.statusCode);
});
