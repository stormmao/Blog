### shell 的运行
1.作为可执行程序
- chmod +x ./test.sh  #使脚本具有执行权限
- ./test.sh  #执行脚本    

2.作为解释器参数
- /bin/sh test.sh
- /bin/php test.php
### shell 的变量
- 定义变量时，变量名不加美元符号（$，PHP语言中变量需要），如：`your_name="w3cschool.cn"`
- 使用一个定义过的变量，只要在变量名前面加美元符号即可，如：
```
your_name="qinjx" 
echo $your_name
```  
- 推荐给所有变量加上花括号，这是个好的编程习惯，如：
```
for skill in Ada Coffe Action Java do 
    echo "I am good at ${skill}Script" 
done
```
- 已定义的变量，可以被重新定义，如：
```
your_name="tom" 
echo $your_name 
your_name="alibaba" 
echo $your_nam
```
### Shell 传递参数
- 我们可以在执行 Shell 脚本时，向脚本传递参数，脚本内获取参数的格式为：$n。n 代表一个数字，1 为执行脚本的第一个参数，2 为执行脚本的第二个参数，以此类推
```
#!/bin/bash
# author:W3Cschool教程
# url:www.w3cschool.cn

echo "Shell 传递参数实例！";
echo "执行的文件名：$0";
echo "第一个参数为：$1";
echo "第二个参数为：$2";
echo "第三个参数为：$3";
```
- 为脚本设置可执行权限，并执行脚本，输出结果如下所示：
```
$ chmod +x test.sh 
$ ./test.sh 1 2 3
Shell 传递参数实例！
执行的文件名：test.sh
第一个参数为：1
第二个参数为：2
第三个参数为：3
```
### Shell 数组
- 数组中可以存放多个值。Bash Shell 只支持一维数组（不支持多维数组），初始化时不需要定义数组大小（与 PHP 类似）。与大部分编程语言类似，数组元素的下标由0开始。Shell 数组用括号来表示，元素用"空格"符号分割开。
- 读取数组读取数组元素值的一般格式是：`${array_name[index]}`
- 获取数组中的所有元素使用@ 或 * 可以获取数组中的所有元素:`echo "数组的元素为: ${my_array[*]}" echo "数组的元素为: ${my_array[@]}"`
### Shell echo命令
- 显示普通字符串：echo "It is a test"
- 显示转义字符：echo "\"It is a test\""
- 显示变量：
    - read 命令从标准输入中读取一行,并把输入行的每个字段的值指定给 shell 变量
     ```
     #!/bin/sh
     read name 
     echo "$name It is a test"
     ```
