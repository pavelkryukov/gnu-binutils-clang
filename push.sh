#!/bin/bash
git pull
pushd binutils-gdb
git pull
popd
git commit -a -m "Update GNU Binutils"
git push origin master
