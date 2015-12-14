'use strict';
const {await, async} = require('asyncawait');

const Client = require('./stockfighter/trades-exec').Client;


const main = async (function() {
  const API_KEY = process.env['STOCKFIGHTER_API_KEY'];
  const client = new Client(API_KEY);

  console.log("Awaiting async...");
  await (new Promise(resolve => setTimeout(resolve, 2500)));
  console.log("Done. Now let's run some imaginary code:");

  const levels = client.levels();
  const nextLevel = levels[levels.length - 1];
  const instance = nextLevel.getOrCreateInstance();

  console.log(instance);
});

main();
