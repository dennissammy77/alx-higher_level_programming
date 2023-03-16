#!/usr/bin/node

let q = 0;

const logMe = (item) => {
  console.log(`${q}: ${item}`);
  q++;
};

module.exports = { logMe };
