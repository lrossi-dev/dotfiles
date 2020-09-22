#!/bin/sh

XPROFILE=$HOME/.xprofile

[[ -s "$XPROFILE" ]] && $XPROFILE

while true; do
    dwm 2> ~/.local/share/dwm/dwm.log
done
