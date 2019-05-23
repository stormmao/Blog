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
### 分支管理
- git branch：查看分支
- git branch <name>：创建分支
- git checkout <name>：切换分支
- git checkout -b <name>：创建+切换分支
- git merge <name>：合并某分支到当前分支
- git branch -d <name>：删除分支
### 分支冲突
- 当Git无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并完成。解决冲突就是把Git合并失败的文件手动编辑为我们希望的内容，再提交。
  用git log --graph命令可以看到分支合并图
### 分支管理
- git merge --no-ff -m "merge with no-ff" dev ：合并分支时，加上--no-ff参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而fast forward合并就看不出来曾经做过合并，加上-m参数，把commit描述写进去
### Bug分支
- 修复 bug 时，我们会通过创建新的bug分支进行修复，然后合并，最后删除；当手头工作没有完成时，先把工作现场 git stash 一下，然后去修复bug，修复后，
  再 git stash pop，回到工作现场。
