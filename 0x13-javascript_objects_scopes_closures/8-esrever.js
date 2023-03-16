#!/usr/bin/env node

const esrever = (list) => {
  return list.map((item, idx) => list[list.length - 1 - idx]);
};

module.exports = { esrever };
