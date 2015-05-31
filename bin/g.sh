# goes to the default path specified by s
echo "cd `cat /tmp/s.out`" > /tmp/g.sh
chmod +x /tmp/g.sh
. /tmp/g.sh
