# Global variables
ROOT_DIR="/home/pi/arcade1up"
GITHUB_REPO="https://github.com/orlandovald/arcade1up.git"

echo "Installing prerequisites"

sudo apt-get update
sudo apt-get -y install git python-pip
pip install RPi.GPIO

# Create root directory
mkdir -p "${ROOT_DIR}"

# Clone repo
git clone "${GITHUB_REPO}" "${ROOT_DIR}"

echo "prerequisites have been installed"