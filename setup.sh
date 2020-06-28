#!/bin/bash

# Global variables
ROOT_DIR="/home/pi/arcade1up"
GITHUB_REPO="https://github.com/orlandovald/arcade1up.git"

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
    echo "*** Make sure your power button is connected to pins 5 & 6 ***"
  else
    echo "Skipped power switch configuration"
  fi  
else 
  echo "Power switch script is already configured"
  echo "*** Make sure your power button is connected to pins 5 & 6 ***"
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
  else
    echo "Skipped volume switch configuration"
  fi
else
  echo "Volume switch script is already configured"
  
fi

echo
echo "Now is a good time to reboot, run the below command for that:"
echo "     sudo reboot"
echo
echo "Finished setup"
