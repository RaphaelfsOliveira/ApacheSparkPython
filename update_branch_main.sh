#!/bin/bash

echo 'add and commit all code'
git add .; git commit -m '.'; git push; git status

echo 'update branch main'
git checkout main; git merge dev; git push; git checkout dev