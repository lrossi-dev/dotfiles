#!/bin/sh

XPROFILE=$HOME/.xprofile

[[ -s "$XPROFILE" ]] && $XPROFILE

exec bspwm
