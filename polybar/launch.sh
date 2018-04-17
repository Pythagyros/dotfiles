#!/usr/bin/env sh

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null;
	do sleep 1;
done

# Get all monitor names to display multiple polybars https://github.com/jaagr/polybar/issues/763
if type "xrandr"; then
  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
    MONITOR=$m polybar --reload davidarrieta &
  done
else
  polybar --reload davidarrieta &
fi

# Launch bar1 and bar2
# polybar davidarrieta 


echo "Bars launched..."

