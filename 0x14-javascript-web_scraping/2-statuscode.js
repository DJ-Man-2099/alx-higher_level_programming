#!/usr/bin/node
const { log } = require('console');
const request = require('request');

request(process.argv[2], (error, response, body) => {
  log('code: ', response.statusCode);
});
