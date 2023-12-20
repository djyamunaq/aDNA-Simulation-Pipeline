#!/bin/bash

# Stop script if any command fail
set -e

# Force sudo activation
sudo ls >> /dev/null 2>&1

# Remove temporary loading animation file if it exists
if [ -f "simpipe/temp" ] ; then
    sudo rm "simpipe/temp" >> /dev/null 2>&1
fi

# Create temporary loading animation file
echo -e "#!/bin/bash\n\n"\$@" &\nwhile kill -0 \$!; do\n\tprintf '.' > /dev/tty\n\tsleep 1\ndone\nprintf '\\n' > /dev/tty" >> simpipe/temp 

# Update packages
echo -n "> Updating packages "
sudo ./simpipe/temp apt update >> /dev/null 2>&1

# Install cmake
echo -n "> Installing cmake "
sudo ./simpipe/temp apt install cmake >> /dev/null 2>&1

# Install libgsl
echo -n "> Installing libgsl "
sudo ./simpipe/temp apt-get install libgsl0-dev >> /dev/null 2>&1

# Install seq-gen
echo -n "> Installing seq-gen "
sudo ./simpipe/temp apt install seq-gen >> /dev/null 2>&1

# Update git submodules
echo -n "> Updating project modules "
sudo ./simpipe/temp git submodule update --init --recursive >> /dev/null 2>&1

# Install Gargammel and its dependencies
echo -n "> Installing Gargammel and its dependencies "
cd simpipe/gargammel >> /dev/null 2>&1
sudo ../temp make >> /dev/null 2>&1
cd - >> /dev/null 2>&1

# pip install simpipe package
echo "> Installing simpipe\n\n"
if pip install -e .; then
    GREEN='\033[0;32m'
    echo -e "${GREEN}> Successfully installed package simpipe"
else
    RED='\033[0;31m'
    echo -e "${RED}> Failed installing package simpipe"
fi

# Reset terminal colors
WHITE="\033[0;37m"
echo -ne "${WHITE}"

# Remove temporary loading animation file
rm simpipe/temp

