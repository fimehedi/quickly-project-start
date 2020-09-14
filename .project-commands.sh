#!/bin/bash

function project-create() {
    mkdir $1
    cd $1
    python3 ~/.quickly-project-start/project-create.py $1 -$2
}

function project-open() {
    python3 ~/.quickly-project-start/project-open.py $1 -$2
}

function project-remove() {
    rm -rf $1
    python3 ~/.quickly-project-start/project-remove.py $1 -$2
}
