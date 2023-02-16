#!/bin/bash

git add .; git commit -m '.'; git push; git status

git checkout main; git merge dev; git push; git checkout dev