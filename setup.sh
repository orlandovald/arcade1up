#!/bin/bash

# Global variables
ROOT_DIR="/home/pi/arcade1up"
GITHUB_REPO="https://github.com/orlandovald/arcade1up.git"
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

echo "*** Installing prerequisites ***"
echo

sudo apt-get update
sudo apt-get -y install git python-pip
pip install RPi.GPIO

# Create root directory
mkdir -p "${ROOT_DIR}"

# Clone repo
git clone "${GITHUB_REPO}" "${ROOT_DIR}"

echo
echo "*** Prerequisites have been installed ***"
echo

RC_LOCAL_FILE="/etc/rc.local"
POWER_SCRIPT_CMD="sudo python $ROOT_DIR/power.py &"
VOLUME_SCRIPT_CMD="python $ROOT_DIR/volume.py &"

grep -q -F "$POWER_SCRIPT_CMD" "$RC_LOCAL_FILE"
if [ $? -ne 0 ]; 
then
  read -p "Press 'Y' to configure the power switch script: " -n 1 -r
  echo
  if [[ $REPLY =~ ^[Yy]$ ]]
  then
    sudo sed -i.bakp "/^exit 0/i $POWER_SCRIPT_CMD" "$RC_LOCAL_FILE"
    echo "Power switch script has been configured"
    echo -e "${RED}*** Make sure your power button is connected to pins 5 & 6 ***${NC}"
  else
    echo "Skipped power switch configuration"
  fi  
else 
  echo "Power switch script is already configured"
  echo -e "${RED}*** Make sure your power button is connected to pins 5 & 6 ***${NC}"
fi

echo

grep -q -F "$VOLUME_SCRIPT_CMD" "$RC_LOCAL_FILE"
if [ $? -ne 0 ]; 
then
  read -p "Press 'Y' to configure the power switch script: " -n 1 -r
  echo
  if [[ $REPLY =~ ^[Yy]$ ]]
  then
    sudo sed -i.bakv "/^exit 0/i $VOLUME_SCRIPT_CMD" "$RC_LOCAL_FILE"
    echo "Volume switch script has been configured"
    echo -e "${RED} *** Default pin configuration is LOW=18 and MAX=16 ***"
    echo -e "${RED} *** Edit config.ini file to change pin and volume level defaults ***${NC}"
  else
    echo "Skipped volume switch configuration"
  fi
else
  echo "Volume switch script is already configured"
  echo -e "${RED} *** Default pin configuration is LOW=18 and MAX=16 ***"
  echo -e "${RED} *** Edit config.ini file to change pin and volume level defaults ***${NC}"
  
fi

echo
echo "If you need to change defult pin values in config.ini do that now. Otherwise, reboot."
echo
echo -e "${GREEN}     sudo reboot${NC}"
echo
echo "Finished setup"
