# Visit us at [mun.amb.sch.ae](https://mun.amb.sch.ae)

## Instructions to pull
If you don't use the source control tab in vscode, follow these instructions on how to pull from the terminal
1. Change terminal directory to be at the root of the project, same folder where the `manage.py` file is, use `cd ..` to go to the containing folder
2. Run `git fetch` to update your version of the repo with all the new commits
3. If you already have changes made on your local repo and want to pull, run `git stash`, this will save your changes and revert back to the unmodifed state
4. Run `git pull origin main` to pull all the new changes
5. Run `git stash pop` to bring back your changes to the updated repo, if you didnt have any changes before the pull or didn't do step 3, then you can skip this step

## Instructions to push changes
If you still don't use the source control tab in vscode and the script isn't working, then follow these instructions to push your changes to remote
1. If you have any files bigger than 50MB, you need to use git lfs, run `git lfs track <filename>`, you can also do `*.<file extension>` to add all files that have that file extension, though be aware you only get 1GB of git lfs on the free version so be careful
2. Run `git add -u` to add all changed files for commit, you can run `git add *` to addd all files to commit even if they havent changed
3. Run `git commit -m "<your commit message>` to create a commit, change `<your commit message` to a short description of what changes you made or whatever you want
4. Run `git push origin main` to push changes to remote

If you are using git lfs, first do step 1 to add all large files to git lfs and then you can run follow these instructions or vscode source control or the script

Always know what you are executing to avoid unwanted results