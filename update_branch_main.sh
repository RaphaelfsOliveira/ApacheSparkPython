#!/bin/bash
echo '\n'
echo '#########################'
echo 'add and commit all code #'
echo '#########################\n'

git add .; git commit -m '.'; git push; git status

echo '\n'
echo '####################'
echo 'update branch main #'
echo '####################\n'

git checkout main; git merge dev; git push; git checkout dev