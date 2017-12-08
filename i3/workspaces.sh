#!/bin/sh

exec --no-startup-id "i3-msg
    '$workspace1;
    append_layout
    ~/.config/i3/workspaces/ws1.json'"

