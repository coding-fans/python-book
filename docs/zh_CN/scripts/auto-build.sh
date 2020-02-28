#!/bin/bash
# FileName:   auto-build.sh
# Author:     Fasion Chan
# @contact:   fasionchan@gmail.com
# @version:   $Id$
#
# Description:
#
# Changelog:
#
#

SELF_PATH=`realpath "$0"`
SCRIPT_DIR_PATH=`dirname "$SELF_PATH"`
DOC_ROOT_PATH=`dirname "$SCRIPT_DIR_PATH"`
PYENV_PATH="$DOC_ROOT_PATH/opt/pyenv"
BUILD_PATH="$DOC_ROOT_PATH/_build"

BIND_ADDR=python.local
sudo ifconfig lo0 alias $BIND_ADDR up

rm -rf "$BUILD_PATH"
(
    cd "$DOC_ROOT_PATH"
    PATH="$PYENV_PATH/bin:$PATH" "$PYENV_PATH/bin/sphinx-autobuild" \
        --ignore "*.swp" \
        -H $BIND_ADDR \
        -p 58000 \
        . "$BUILD_PATH/html"
)
