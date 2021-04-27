class Home {
  constructor(person) {
    this.person = person;
  }
  get sum() {
    return this.person.length;
  }
  add(person) {
    this.person.push(person);
  }
  remove(person) {
    var result = [];
    this.person.map(function (value) {
      if (value !== person) {
        result.push(value);
      }
    });
    this.person = result;
  }
  each(cb) {
    this.person.map(function (value, index, array) {
      cb(value, index, array);
    });
  }
  static staticMethod(a, b) {
    console.log(a + '+' + b);
  }
}

var family = new Home(['a', 'b']);
family.add('c');
family.remove('b');
family.each(function (value) {
  console.log('family method:' + value + ' say hello to you!');
});

console.log(Home.staticMethod(1, 2));

class Community extends Home {
  each(cb) {
    super.each(cb);
    console.log('callback runned');
  }
}

var community = new Community(['x', 'y']);
community.add('z');
community.each(function (value) {
  console.log('community method:' + value + ' say hello to you!');
});
console.log(community);