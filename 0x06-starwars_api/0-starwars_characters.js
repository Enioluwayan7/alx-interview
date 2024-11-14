#!/usr/bin/node

const axios = require('axios');

// Function to fetch and print characters from the specified movie
async function getMovieCharacters(movieId) {
  try {
    // Fetch movie details
    const response = await axios.get(`https://swapi.dev/api/films/${movieId}/`);
    const filmData = response.data;

    console.log(`Characters in '${filmData.title}':\n`);

    // Iterate over character URLs and fetch each character's name
    for (const characterUrl of filmData.characters) {
      const characterResponse = await axios.get(characterUrl);
      console.log(characterResponse.data.name);
    }
  } catch (error) {
    console.error(`Error fetching data: ${error.message}`);
  }
}

// Ensure a movie ID is provided as a command-line argument
const movieId = process.argv[2];
if (!movieId) {
  console.log('Usage: ./getCharacters.js <movie_id>');
} else {
  getMovieCharacters(movieId);
}
