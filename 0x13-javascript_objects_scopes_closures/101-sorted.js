#!/usr/bin/node
const dict = require('./101-data').dict;

const totalList = Object.entries(dict);
const values = Object.values(dict);
const valuesUnique = [...new set(values)];
const newDict = {};
for (const i in valuesUnique) {
  const list = [];
  for (const j in totalList) {
    if (totalList[j][1] === valuesUnique[i]) {
      list.unshift(totalList[j][0]);
    }
  }
  newDict[valuesUnique[i]] = list;
}
console.log(newDict);
