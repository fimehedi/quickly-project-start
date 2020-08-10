#!/bin/bash

function project-create() {
    mkdir $1
    cd $1
    python3 ~/.quick-project-create/project-create.py $1 -$2
}

function project-open() {
    python3 ~/.quick-project-create/project-open.py $1 -$2
}

function project-remove() {
    rm -rf $1
    python3 ~/.quick-project-create/project-remove.py $1 -$2
}