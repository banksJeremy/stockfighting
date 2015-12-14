'use strict';


class Client {
  constructor(apiKey) {
    if (!apiKey) throw new Error("API key required.");

    this.apiKey_ = apiKey;
  }
}


class Level {
  constructor(client, name) {
    this.client = client;
    this.name = name;
  }
}


class Instance {
  constructor(level, id) {
    this.client = client;
    this.id = id;
  }
}


class Stock {
  constructor(instance, symbol) {
    this.instance = instance;
    this.symbol = symbol;
  }
}


class Venue {
  constructor(instance, name) {
    this.instance = instance;
    this.name = name;
  }
}


class Ticker {
  constructor(venue, stock) {
    this.venue = venue;
    this.stock = stock;
  }
}


class OwnOrder {
  constructor(ticker, id) {
    this.ticker = ticker;
    this.id = id;
  }
}


class AnOrder {
  constructor(ticker) {
    this.ticker = ticker;
    // TODO: all properties should be required here.
  }
}


class Quote {
  constructor(ticker) {
    this.ticker = ticker;
  }
}


class Execution {
  constructor(ticker) {
    this.ticker = ticker;
  }
}


module.exports = {Client};
