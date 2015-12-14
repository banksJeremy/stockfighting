'use strict';
const {await, async} = require('asyncawait');

const main = async (function() {
  console.log("Awaiting async...");
  await (new Promise(resolve => setTimeout(resolve, 2500)));
  console.log("Done.");
});

main();
