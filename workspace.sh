#!/usr/bin/env bash

# Script to open frequently used programs on their designed workspaces

## Workspace 1
i3-msg 'workspace 1 ; exec firefox https://calendar.google.com/calendar/r'
i3-msg 'workspace 1 ; exec firefox https://todoist.com/app?lang=en#agenda%2Foverdue%2C%20today'

## Workspace 2
i3-msg 'workspace 2 ; exec firefox'
sleep 1

## Workspace 3
i3-msg 'workspace 3 ; exec subl'

## Workspace 4
i3-msg 'workspace 4; exec mendeleydesktop'
sleep 2
i3-msg 'workspace 4; exec evince ~/masterarbeit/main.pdf'
sleep 1

## Workspace 5
i3-msg 'workspace 5 ; exec thunderbird'