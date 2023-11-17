#!/bin/bash
# This is a comment
REPOSITORIES=$(curl -s https://appadmin.demo.community.intersystems.com/apptoolsrest/custom-task/user/zapmrepolist-$1-$2)
for REPOSITORY in $REPOSITORIES; do
  git clone $REPOSITORY
done
