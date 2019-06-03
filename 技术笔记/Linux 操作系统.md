## 趣谈 Linux 操作系统
### Linux 常用命令
- 用户与密码    
    - adduser name 添加用户 passwd name 设置密码
    - passwd 更改密码
- 浏览文件
    - ls -l
- 安装软件
    - CentOS 下面使用 rpm -i jdk-XXX_linux-x64_bin.rpm 进行安装
    - Ubuntu 下面使用 dpkg -i jdk-XXX_linux-x64_bin.deb。其中 -i 就是 install 的意思。
- 运行程序
    - Linux 执行程序最常用的一种方式,通过 shell 在交互命令行里面运行：./filename 运行这个文件
    - Linux 运行程序的第二种方式,后台运行，最终命令的一般形式为 nohup command >out.file 2>&1 &。这里面,“1”表示文件描述符 1,表示标准输出,“2”表示文件描述符 2,意思是标准错误输出,“2>&1”表示标准输出和错误输出合并到 out.file 里
