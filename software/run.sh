#!/bin/bash

xhost +local:
DIR="$(dirname "$(realpath "$0")")"
$DIR/main.py
