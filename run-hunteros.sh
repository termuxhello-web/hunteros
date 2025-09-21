#!/bin/bash
# Run X server / framebuffer
Xvfb :1 -screen 0 1024x768x16 &
export DISPLAY=:1

# Start GUI
./gui/run-hunteros-gui &

# Start VNC server
./vnc/run-vnc.sh &

echo "HunterOS Rootless started. Connect via VNC on port 5900."
