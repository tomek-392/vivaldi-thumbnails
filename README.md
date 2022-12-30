# vivaldi-thumbnails

## About
It's a very basic implementation of client for speed dial thumbnail/miniatures creation for Vivaldi browser and similar. The idea is to mimic speed dial from mobile version.

It creates png image with solid background color based on dominant color from website favicon, and puts domain name in center of it.

## Limitations
Some websites blocks python requests from accessing it correctly. Also very long domain names will require some default parameters alteration to fit.
