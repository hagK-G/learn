# ECMA RegExp direct quantity character

|字符|匹配|
|:----:|:----:|
|字母和数字|自身|
|\o|NUL 字符(\u0000)|
|\t| 制表符(\u0009)|
|\n| 换行符(\u000A)|
|\v| 垂直制表符(\u000B)|
|\f| 换页符(\u000C)|
|\r| 回车符(\u000D)|
|\xnn| 十六进制数 nn 指定的拉丁字符，\x0A = \n|
|\uxxxx|  十六进制数 xxxx 指定的 Unicode 字符，\u00009 = \t|