"""Return the pathname of the KOS root directory."""
# pylint: disable=invalid-name

import pprint

person1 = ['Bob Atlas', 20, 12000, 'software']
person2 = ['Bob Agzz', 22, 20000, 'software']

# print person1[0].split()[-1]
person1[2] *= 1.2
# print person1

personList = [person1, person2]

for person in personList:
    oldPay = person[2]
  # person[2] *= 1.2
  # print 'person first name is %s, person added pay is $d' % person[0].split()[0], person[2] - oldPay

pay = [person[2] for person in personList]
# print sum(pay)

NAME, AGE, WORK, PAY = range(4)
# print person1[NAME]
# print person1[AGE]
# print person1[PAY]
# print person1[WORK]

dictPerson1 = {'name': 'bob atlas', 'age': 20, 'pay': 20000}
key = ['name', 'age', 'pay']
value = ['bbbb', 20, 2000]
dictPerson1 = list(zip(key, value))
# print dictPerson1[0][0]

dictPerson1 = dict.fromkeys(key, '?')
# print dictPerson1

# Bob = {'pay': 20000, 'name': 'Bob'}
Job = {'pay': 30000, 'name': 'Job'}

# personList = [Bob, Job]

# for person in personList:
#     if person['name'] == 'Job':
        # print person['name'], person['pay']

# print [person['pay'] for person in personList if person['pay'] > 20000]

Bob = {
    'name': {'first': 'Bob', 'last': 'Smith'},
    'age': 40,
    'job': 'software',
    'pay': (20000, 40000)
}

# for key in Bob:
#     print Bob[key]

db = {
    'bob': dict(
        name=dict(first='Bob', last='Smith'),
        age=40,
        job=['software', 'hr'],
        pay=(20000, 40000)
        ),
    'job': dict(
        name=dict(first='Job', last='Smith'),
        age=40,
        job=['software', 'hr'],
        pay=(20000, 40000)
    )
}

for key in db:
    print(key, '=>', db[key]['name'])
