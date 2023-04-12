#!/bin/bash

PROTOCOL=$1

REPOS_HTTPS=(
    "https://github.com/oresat/oresat-olaf.git"
    "https://github.com/oresat/oresat-c3.git"
    "https://github.com/uniclogs/yamcs.git"
)

REPOS_SSH=(
  "git@github.com:oresat/oresat-olaf.git"
  "git@github.com:oresat/oresat-c3.git"
  "git@github.com:uniclogs/yamcs.git"
)

if [ "$PROTOCOL" == "ssh" ]; then
  REPOS=("${REPOS_SSH[@]}")

elif [ "$PROTOCOL" == "https" ]; then
  REPOS=("${REPOS_HTTPS[@]}")
else
  echo "Unrecognized option"
  exit 1
fi

# Iterate through the list and clone each repository
for repo in "${REPOS[@]}"; do
    git clone "$repo"
done
