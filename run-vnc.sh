#!/bin/bash
# Start VNC server
x11vnc -display :1 -nopw -forever -shared
echo "VNC server running on :1, port 5900"
