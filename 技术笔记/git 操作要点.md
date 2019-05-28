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
### Bug 分支
- 修复 bug 时，我们会通过创建新的bug分支进行修复，然后合并，最后删除；当手头工作没有完成时，先把工作现场 git stash 一下，然后去修复bug，修复后，
  再 git stash pop，回到工作现场。
### Feature 分支
- 开发一个新 feature，最好新建一个分支；如果要丢弃一个没有被合并过的分支，可以通过 git branch -D <name> 强行删除。
### 多人协作
- 查看远程库信息，使用git remote -v；
- 本地新建的分支如果不推送到远程，对其他人就是不可见的；
- 从本地推送分支，使用git push origin branch-name，如果推送失败，先用git pull抓取远程的新提交；
-  在本地创建和远程分支对应的分支，使用git checkout -b branch-name origin/branch-name，本地和远程分支的名称最好一致；
- 建立本地分支和远程分支的关联，使用git branch --set-upstream branch-name origin/branch-name；
- 从远程抓取分支，使用git pull，如果有冲突，要先处理冲突
### rebase-[变基](http://gitbook.liuhui998.com/4_2.html)
- rebase 操作可以把本地未 push 的分叉提交历史整理成直线；
- rebase 的目的是使得我们在查看历史提交的变化时更容易，因为分叉的提交需要三方对比
  
  
  
参考文献：[廖雪峰Git教程](https://www.liaoxuefeng.com/wiki/896043488029600/1216289527823648)[Git官网](https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%8F%98%E5%9F%BA)
