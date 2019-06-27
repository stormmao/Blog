## 趣谈 Linux 操作系统
### Linux 常用命令
- 用户与密码    
    - adduser name 添加用户 passwd name 设置密码
    - passwd 更改密码
- 浏览文件
    - ls -l
- 搜索字符
    - grep -r "string“ ./
- 安装软件 
    - CentOS 下面使用 rpm -i jdk-XXX_linux-x64_bin.rpm 进行安装
    - Ubuntu 下面使用 dpkg -i jdk-XXX_linux-x64_bin.deb。其中 -i 就是 install 的意思。
- 软件管家
    - CentOS 下面是 yum，搜索 jdk、yum search jdk，安装 yum install java-11-openjdk.x86_64，卸载 yum erase java-11-openjdk.x86_64
    - Ubuntu 下面是 apt-get，搜索 apt-cache search jdk，安装 apt-get install openjdk-9-jdk，卸载 apt-get purge openjdk-9-jdk

    | 操作 | CentOS | Ubuntu  |
    | :-----:| :----: | :----: |
    | 搜索 | yum search jdk | apt-cache search jdk |
    | 安装 |  yum install java-11-openjdk.x86_64 |  apt-get install openjdk-9-jdk |
    | 卸载 | yum erase java-11-openjdk.x86_64 |apt-get purge openjdk-9-jdk |

- 运行程序
    - Linux 执行程序最常用的一种方式,通过 shell 在交互命令行里面运行：./filename 运行这个文件
    - Linux 运行程序的第二种方式,后台运行，最终命令的一般形式为 nohup command >out.file 2>&1 &。这里面,“1”表示文件描述符 1,表示标准输出,“2”表示文件描述符 2,意思是标准错误输出,“2>&1”表示标准输出和错误输出合并到 out.file 里
- 命令别名
    - 添加到 .bash_profile 文件里
    - 解压文件 alias untar='tar -zxvf'
    - 支持断点下载 alias wget='wget -c '
    - 生成一个 20 个字符的随机数密码 alias getpass="openssl rand -base64 20"
    - 校验一下 checksum 值 alias sha='shasum -a 256 '
    - 使用 -c 命令将其限制为 5 次输出 alias ping='ping -c 5'
    - 随时随地启动一个 web 服务器 alias www='python -m SimpleHTTPServer 8000'
    - 网速的测试，借助第三方工具 speedtest-cli ，alias speed='speedtest-cli --server 2406 --simple'
    - 公网 IP alias ipe='curl ipinfo.io/ip'
    - 局域网 IP alias ipi='ipconfig getifaddr en0'
    - 清屏 alias c='clear'
    
- 关机与重启
    - shutdown -h now 是现在就关机
    - reboot 就是重启
### Linux X86 架构
- 计算机工作模式
![alt 硬件与逻辑对应](https://static001.geekbang.org/resource/image/fa/9b/fa6c2b6166d02ac37637d7da4e4b579b.jpeg)
- CPU 和内存是如何配合工作的
    - 运算单元
    - 数据单元
    - 控制单元
- 汇编基本命令
    - move a b :把b值赋给a,使a=b
    - call 和 ret :call调用子程序,子程序以ret结尾
    - jmp :无条件跳
    - int :中断指令
    - add a b : 加法,a=a+b
    - or :或运算
    - xor :异或运算
    - shl :算术左移
    - ahr :算术右移
    - push xxx :压xxx入栈
    - pop xxx: xxx出栈
    - inc: 加1
    - dec: 减1
    - sub a b : a=a-b
    - cmp: 减法比较，修改标志位

![alt ](https://static001.geekbang.org/resource/image/3a/23/3afda18fc38e7e53604e9ebf9cb42023.jpeg)
[W3Cschool linux 教程](https://www.w3cschool.cn/linux/)
[极客时间-趣谈 Linux 系统](https://time.geekbang.org/column/article/89417)
