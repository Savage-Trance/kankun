#!/bin/sh
echo "Content-type: text/html"
echo ""

echo "<h2>ON</h2>"
echo 1 > /sys/class/leds/tp-link:blue:relay/brightness

