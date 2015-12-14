'use strict';


class Client {
  constructor(apiKey) {
    if (!apiKey) throw new Error("API key required.");

    this.apiKey_ = apiKey;
  }
}

module.exports = {Client};
