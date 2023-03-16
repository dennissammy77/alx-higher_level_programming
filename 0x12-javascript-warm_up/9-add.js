#!/usr/bin/env node

const firstInt = Math.floor(Number(process.argv[2]));
const secondInt = Math.floor(Number(process.argv[3]));

function add (a, b) {
  console.log(a + b);
}

add(firstInt, secondInt);
