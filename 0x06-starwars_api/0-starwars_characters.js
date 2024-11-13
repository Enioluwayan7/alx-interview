#!/usr/bin/node

const https = require('https');

// Helper function to perform an HTTPS GET request and parse JSON
function fetchJson(url) {
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';
      res.on('data', (chunk) => {
        data += chunk;
      });
      res.on('end', () => {
        try {
          const jsonData = JSON.parse(data);
          resolve(jsonData);
        } catch (error) {
          reject(new Error('Error parsing JSON'));
        }
      });
    }).on('error', (err) => {
      reject(err);
    });
  });
}

// Function to fetch and print characters from the specified movie
async function getMovieCharacters(movieId) {
  try {
    const filmUrl = `https://swapi.dev/api/films/${movieId}/`;
    const filmData = await fetchJson(filmUrl);

    console.log(`Characters in '${filmData.title}':\n`);

    // Fetch each character using the new API endpoint
    const characterPromises = filmData.characters.map((characterUrl) => {
      // Extract character ID from the URL and use the new API endpoint
      const characterId = characterUrl.split('/').filter(Boolean).pop();
      const newCharacterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}`;
      return fetchJson(newCharacterUrl);
    });

    // Wait for all character data to be fetched and print names in order
    const characters = await Promise.all(characterPromises);
    characters.forEach((character) => {
      console.log(character.name);
    });

  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

// Ensure a movie ID is provided as a command-line argument
const movieId = process.argv[2];
if (!movieId) {
  console.log('Usage: ./getCharacters.js <movie_id>');
} else {
  getMovieCharacters(movieId);
}
