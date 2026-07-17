#!/bin/bash -e

## Generate a version from git metadata and print it

fallback_version='0.0.0'
project_file=$1
version="$fallback_version"

if [ -z "$project_file" ]
then
    project_file="pyproject.toml"
fi

## get the latest version tag, trimming the 'v'
latest_tag="$(git describe --abbrev=0 --tags --match 'v*.*.*' 2>/dev/null | sed 's/^v//')"
if [ -z "$latest_tag" ]
then
    latest_tag="$fallback_version"
fi

## See if the current commit is tagged
this_commit_tag="$(git tag -l 'v*.*.*' --points-at HEAD | sed 's/^v//')"
if [ "$this_commit_tag" = "$latest_tag" ]
then
    version="$latest_tag"
else
    ## dev version - append branch, date and commit hash
    branch="$(git rev-parse --abbrev-ref HEAD)"
    timestamp="$(date '+%Y%m%d%H%M%S')"
    hash="$(git rev-parse --short HEAD)"
    version="${latest_tag}-${branch}-${timestamp}-${hash}"
fi

echo "$version"
