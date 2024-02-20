#!/usr/bin/node
const { log } = require('console');
const request = require('request');

request(
  'https://swapi-api.alx-tools.com/api/people/18',
  (error, response, body) => {
    if (error) {
      log(error);
    }
    log(JSON.parse(body).films.length);
  }
);
