#! /bin/bash

RED="\e[31m"
ENDCOLOR="\e[0m"

echo "************_********************_*"
echo " _ __ _   _| |__   ___ _ __   __| |"
echo "| '__| | | | '_ \ / _ \ '_ \ / _\` |"
echo "| |  | |_| | | | |  __/ | | | (_| |"
echo "|_|   \__,_|_| |_|\___|_| |_|\__,_|"
echo "***********************************"
echo ""
echo " ! Enter your password when prompted !"
echo " > making dir /usr/bin/env-path-gui"
sudo mkdir /usr/bin/env-path-gui
echo " > chmoding logic.py"
sudo chmod +x src/logic.py
echo " > chmoding main.py"
sudo chmod +x src/main.py
echo " > copying logic.py -> /usr/bin/env-path-gui/"
sudo cp -v src/logic.py /usr/bin/env-path-gui/
echo " > copying main.py -> /usr/bin/env-path-gui/"
sudo cp -v src/main.py /usr/bin/env-path-gui/
echo " > copying env-path-gui icon -> /usr/bin/env-path-gui/"
sudo cp -v env-path-gui.png /usr/bin/env-path-gui/
echo " > moving .desktop -> /usr/share/applications/"
sudo cp -v env-path-gui.desktop /usr/share/applications/
echo ""
echo -e "${RED}\e]8;;https://github.com/ruhend/env-path-gui\aRead README.md here\e]8;;\a${ENDCOLOR}"  

echo ""
echo ";)"
