#! /bin/sh

. /etc/thinstation.env
. $TS_GLOBAL

header

echo '<pre>'

for filelist in `ls /usr/X11R7/etc/X11/x.config-*`
do
        echo $filelist
	cat $filelist
        echo -e "\n\n"
done

echo '</pre>'

trailer
