#!/bin/sh

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -x polybar >/dev/null; do sleep 1; done

# Launch
polybar main &
if [[ "$(xrandr -q | grep -w connected | wc -l)" -eq 2 ]]; then
    polybar second &
fi

echo "Bar launched..."
