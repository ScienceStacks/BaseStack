# Launches terminal sessions with prescribed positions
# Argument: -w <n> | --windows <n> 
#   <n> is 4 or 6; default is 4

if [ $1 == "-w" ]
then
  WINDOWS=$2
fi
WINDOWS=4

if [ $WINDOWS == "4" ]
then
  gnome-terminal --geometry 87x26+0+0 --hide-menubar
  gnome-terminal --geometry 87x26+1000+0 --hide-menubar
  gnome-terminal --geometry 87x26+0+540 --hide-menubar
  gnome-terminal --geometry 87x26+1000+540 --hide-menubar
else
  gnome-terminal --geometry 62x29+0+0 --hide-menubar
  gnome-terminal --geometry 84x29+645+0 --hide-menubar
  gnome-terminal --geometry 62x29+1290+0 --hide-menubar
  gnome-terminal --geometry 62x29+0+565 --hide-menubar
  gnome-terminal --geometry 84x29+645+565 --hide-menubar
  gnome-terminal --geometry 62x29+1290+565 --hide-menubar
fi
