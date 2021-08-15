#!/usr/bin/env bash

# Get only utils directory from upstream Buildroot:
# create a shallow and sparse checkout, recipe taken from
# https://stackoverflow.com/a/28039894
temp=$(mktemp --directory $(pwd)/XXXX)
trap 'rm -rf $temp' EXIT

pushd $temp > /dev/null
git init --quiet
git remote add origin https://github.com/buildroot/buildroot.git
git config core.sparsecheckout true

echo 'utils/check-package' >> .git/info/sparse-checkout
echo 'utils/checkpackagelib/*' >> .git/info/sparse-checkout

VERSION=${1:-master}
git pull --quiet --ff-only --depth=1 origin $VERSION

sources="check-package checkpackagelib"
for source in $sources; do
    rm -rf ../$source
    mv utils/$source ..
done
popd > /dev/null

echo Files $sources updated to $VERSION
