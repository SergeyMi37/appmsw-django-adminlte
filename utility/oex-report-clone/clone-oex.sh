#!/bin/bash
# This is a comment
REPOSITORIES=$(curl -s http://django:django-todo-37@iris-test:52774/apptoolsrest/custom-task/user/zapmrepolist-oex-appmsw)
for REPOSITORY in $REPOSITORIES; do
  git clone $REPOSITORY
done
