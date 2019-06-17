### shell 的运行
1.作为可执行程序
- chmod +x ./test.sh  #使脚本具有执行权限
- ./test.sh  #执行脚本    

2.作为解释器参数
- /bin/sh test.sh
- /bin/php test.php
### shell 的变量
- 定义变量时，变量名不加美元符号（$，PHP语言中变量需要），如：`your_name="w3cschool.cn"`
- 使用一个定义过的变量，只要在变量名前面加美元符号即可，如：`your_name="qinjx" echo $your_name`
