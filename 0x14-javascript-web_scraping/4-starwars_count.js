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
    const id = 18;
    const movies = (JSON.parse(body)).results;
    for (let index = 0; index < movies.length; index++) {
      const movie = movies[index];
      if (movie.characters &&
        movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${id}/`)) {
        count++;
      }
    }
    log(count);
  }
);
