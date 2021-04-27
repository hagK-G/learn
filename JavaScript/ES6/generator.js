function* anotherGenerator(i) {
  yield i + 1;
  yield i + 2;
  yield i + 3;
}

function* generator(i) {
  yield i;
  yield* anotherGenerator(i);
  yield i + 10;
}

var gen = generator(10);

console.log(gen.next()); // { value: 10, done: false }
console.log(gen.next()); // { value: 11, done: false }
console.log(gen.next()); // { value: 12, done: false }
console.log(gen.next()); // { value: 13, done: false }
console.log(gen.next()); // { value: 20, done: false }
console.log(gen.next()); // { value: undefined, done: true }
console.log(gen.next()); // { value: undefined, done: true }

for (let step of generator(1)) {
  console.log(step);
}