#!/usr/bin/node
const { log } = require('console');
const request = require('request');

request(
  process.argv[2],
  (error, response, body) => {
    if (error) {
      log(error);
    }
    let count = 0;
    let movies = (JSON.parse(body)).results;
    for (let index = 0; index < movies.length; index++) {
      let movie = movies[index];
      if (movie.characters &&
        movie.characters.includes("https://swapi-api.alx-tools.com/api/people/18/")) {
        count++;
      }
    }
    log(count);
  }
);
