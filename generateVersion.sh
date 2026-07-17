#!/bin/bash -x

## Generate a version from git metadata and print it

fallback_version='0.0.0'
project_file=$1
version="$fallback_version"

## get the latest version tag, trimming the 'v'
latest_version="$(git describe --abbrev=0 --tags --match 'v*.*.*' 2>/dev/null | sed 's/^v//')"
if [ -z "$latest_version" ]
then
    latest_version="$fallback_version"
fi

## See if the current commit is tagged
this_commit_tag="$(git tag -l 'v*.*.*' --points-at HEAD | sed 's/^v//')"
if [ "$this_commit_tag" = "$latest_version" ]
then
    version="$latest_version"
else
    ## auto-increment patch number from latest_version
    latest_major="$(echo $latest_version | sed -r 's/([[:digit:]]+)\.([[:digit:]]+)\.([[:digit:]]+)/\1/')"
    latest_minor="$(echo $latest_version | sed -r 's/([[:digit:]]+)\.([[:digit:]]+)\.([[:digit:]]+)/\2/')"
    latest_patch="$(echo $latest_version | sed -r 's/([[:digit:]]+)\.([[:digit:]]+)\.([[:digit:]]+)/\3/')"
    next_patch=$((latest_patch + 1))

    dev_count="$(git rev-list vx${latest_version}..HEAD --count 2>/dev/null)"

    next_version="${latest_major}.${latest_minor}.${next_patch}"
    ## dev version - append branch, date and commit hash
    branch="$(git rev-parse --abbrev-ref HEAD | sed 's/[^0-9A-Za-z-]/-/g' | sed 's/--*/-/g')"
    timestamp="$(date '+%Y%m%d%H%M%S')"
    hash="$(git rev-parse --short HEAD)"
    version="${next_version}.dev${dev_count}+${branch}-${timestamp}-${hash}"
fi

echo "$version"

## write the new version to the project file, if specified
if [ ! -z "$project_file" ]
then
    echo "writing new version"
    sed "s/^version =.*$/version = \"${version}\"/" $project_file > proj.tmp
    mv proj.tmp $project_file
fi
