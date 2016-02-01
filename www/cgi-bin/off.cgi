#!/bin/sh
echo "Content-type: text/html"
echo ""

echo "<h2>OFF</h2>"
echo 0 > /sys/class/leds/tp-link:blue:relay/brightness

