#!/bin/zsh

ENV_FILE=$HOME/.config/env
[[ -s "$ENV_FILE" ]] && source $ENV_FILE

# Staring emacs daemon
emacs --daemon &

exec startx
