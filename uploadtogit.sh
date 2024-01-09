read -p "Enter commit message: " msg
git add *
git commit -m $msg
git rebase
git push origin main