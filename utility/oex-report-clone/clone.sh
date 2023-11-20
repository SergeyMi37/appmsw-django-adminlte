#!/bin/bash
# $1 - pm or oex  $2 - context repos
REPOSITORIES=$(curl -s https://appadmin.demo.community.intersystems.com/apptoolsrest/custom-task/user/zapmrepolist-$1-$2)
for REPOSITORY in $REPOSITORIES; do
  echo '  --- ' $REPOSITORY
  git clone $REPOSITORY
done
