var pattern = /s$/; // 正则表达式直接量定义：以 s 结尾的
var pattern = new RegExp('s$'); // RegExp构造函数： 以 s 结尾的


var email = 'dadsaa.da@ddd.com';
var reg = /^[^@]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
console.log(reg.test(email));