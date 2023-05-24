#!/usr/bin/node

const process = require('process');
const fs = require('fs');

fs.readFile(process.argv[2], (err, inputD) => {
  if (err) throw err;
  console.log(inputD.toString());
});
