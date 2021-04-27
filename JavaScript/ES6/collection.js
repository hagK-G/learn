// map
var map = new Map();

var keyObj = {};
var keyFunc = function () {};
var keyString = 'a';
map.set(keyString, 'b');
map.set(keyObj, 'c');
map.set(keyFunc, 'd');

var kvArray = [
  ['key0', 'value0'],
  ['key1', 'value1']
];
var kvMap = new Map(kvArray);


function consoleMapExample() {
  console.log(`kvmap ${kvMap}`);
  for (var [key, value] of map) {
    console.log(`key is ${JSON.stringify(key)}, value is ${value}`);
  }
  console.log(map.size);
  console.log(map.get(keyObj));
  console.log(map); // Map { 'a' => 'b', {} => 'c', [Function] => 'd' }
  console.log(map.values()); //MapIterator { 'b', 'c', 'd' }
  console.log(map.keys()); // MapIterator { 'a', {}, [Function] }
  console.log(map.entries()); // MapIterator { [ 'a', 'b' ], [ {}, 'c' ], [ [Function], 'd' ] }
}

// consoleMapExample();

// set
var set = new Set();
set.add(1);
set.add('a');
set.add(['a', 'b']);
set.add({
  a: 'a',
  b: 'b'
});


console.log(set);
console.log(set.size);