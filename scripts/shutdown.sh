#!/bin/bash

# Get PID of EmulationStation binary
espid=$( pgrep -f "/opt/retropie/supplementary/.*/emulationstation([^.]|$)" )
if [ "$espid" ]; then
   touch /tmp/es-shutdown && chown pi:pi /tmp/es-shutdown
   kill $espid
   exit
fi

# Regular shutdown if ES binary is not running
shutdown -h now