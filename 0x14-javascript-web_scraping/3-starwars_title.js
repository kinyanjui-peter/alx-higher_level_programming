#!/usr/bin/node
/**
 * A script that prints the title of a Star Wars movie where the episode 
 * number matches a given integer.
 * The first argument is the movie ID
 * You must use the Star wars API with the endpoint 
 * https://swapi-api.alx-tools.com/api/films/:id
 * You must use the module request
 */
const request = require('request');

// Check the number of arguments
if (process.argv.length !== 3) {
  console.error('Usage: node getMovieTitle.js <movie-id>');
  process.exit(1);
}

const numMovie = process.argv[2];
const urlEndpoint = `https://swapi-api.alx-tools.com/api/films/${numMovie}`;

request.get(urlEndpoint, (error, response, body) => {
  if (error) {
    console.error(`Could not connect to the movie API`);
  } else {
    // Parse the response body to JSON
    const movieInfo = JSON.parse(body);

    // Check if the episode number matches the given integer
    if (movieInfo.episode_id == numMovie) {
      console.log(`${movieInfo.title}`);
    } else {
      console.log(`Movie with ID ${numMovie} not found`);
    }
  }
});