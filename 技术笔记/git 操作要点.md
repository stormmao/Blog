### 初始化仓库
- git init 把当前目录转化为仓库
- git add 文件名 添加文件到仓库
- git commit -m "fisrt commit" 提交到仓库
### 版本回退
- git reset --hard HEAD^ 退回到上一版本，HEAD^ 也可以是版本提交编号
- git log 显示提交历史
- git reflog 查看命令历史
### 撤销修改
- 工作区修改 git checkout -- file 让这个文件回到最近一次 git commit 或 git add 时的状态
- git add 之后，使用 git reset HEAD <file>，撤销缓存区的修改，修改只在工作区，再使用  git checkout -- file 就回到解放前了
- git commit 之后，使用版本回退
### 撤销删除
- 1.如果你用的 rm 删除文件，那就相当于只删除了工作区的文件，如果想要恢复，直接用 git checkout -- <file> 就可以 
- 2.如果你用的是 git rm 删除文件，那就相当于不仅删除了文件，而且还添加到了暂存区，需要先 git reset HEAD <file>，然后再 git checkout -- <file> 
- 3.如果你想彻底把版本库的删除掉，先 git rm，再 git commit 就 ok 了
### 远端仓库
- 创建一个仓库，然后使用 git remote add origin https://github.com/stormmao/ex.git 关联远端仓库
- git push -u origin master 推送本地仓库与远端仓库同步
