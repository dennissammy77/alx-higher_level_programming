#!/usr/bin/env node

const arr = require('./100-data.js');

const newArr = arr.list.map((element, index) => { return (element * index); });
console.log(arr.list);
console.log(newArr);
