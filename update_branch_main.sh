#!/bin/bash
echo '\n'
echo '#########################'
echo 'add and commit all code #\n'
echo '#########################'

git add .; git commit -m '.'; git push; git status

echo '\n'
echo 'update branch main \n'
git checkout main; git merge dev; git push; git checkout dev