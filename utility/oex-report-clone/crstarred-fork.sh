#!/bin/bash
# This is a comment
REPOSITORIES=$(curl -s https://api.github.com/users/SergeyMi37/starred?per_page=1000 | jq -r '.[] | select(.fork == true).clone_url')
for REPOSITORY in $REPOSITORIES; do
  git clone $REPOSITORY
done
