#!/usr/bin/env python

from pydbus import SessionBus
#string_out = '%{A1:dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause:}%{A2:dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next:}  '
string_out = '%{A1:i3-msg "workspace 10":}  '
try:
    bus = SessionBus()
    spotify_bus= bus.get("org.mpris.MediaPlayer2.spotify","/org/mpris/MediaPlayer2")
    spotify_info = spotify_bus.Get("org.mpris.MediaPlayer2.Player", "Metadata")
    if len(','.join(spotify_info['xesam:artist'])) > 20:
        string_out += ','.join(spotify_info['xesam:artist'])[0:20] + '...'
    else:
        string_out += ','.join(spotify_info['xesam:artist'])

    string_out += ' - '

    if len(spotify_info['xesam:title']) > 20:
        string_out += spotify_info['xesam:title'].rstrip()[0:20] + '...'
    else:
        string_out += spotify_info['xesam:title']

    # Play/Pause
#    if spotify_bus.PlaybackStatus == 'Playing':
#        string_out += '  %{A1:dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause:}%{A}'

#    if spotify_bus.PlaybackStatus == 'Paused':
#        string_out += '  %{A1:dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause:}%{A}'

    # Skip
#    if spotify_bus.CanGoNext is True:
#        string_out += '  %{A1:dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next:}%{A}' 
    string_out += '%{A}'
    if string_out == '%{A1:i3-msg "workspace 10":}   - %{A}':
        string_out = '%{A1:i3-msg "workspace 10":}%{A}'
    if spotify_bus.PlaybackStatus == 'Paused':
        string_out = '%{A1:i3-msg "workspace 10":}%{A}'
    print(string_out)
except BaseException:
    print("%{A1:i3-msg 'workspace 10; exec /usr/bin/spotify':}%{A}")
