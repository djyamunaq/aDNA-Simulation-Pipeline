rm ./src/temp >> /dev/null 2>&1
echo -e "#!/bin/bash\n\n"\$@" &\nwhile kill -0 \$!; do\n\tprintf '.' > /dev/tty\n\tsleep 1\ndone\nprintf '\\n' > /dev/tty" >> src/temp
echo -n "> Updating packages "
sudo ./src/temp apt update >> /dev/null 2>&1
echo -n "> Installing cmake "
sudo ./src/temp apt install cmake >> /dev/null 2>&1
echo -n "> Installing libgsl "
sudo ./src/temp apt-get install libgsl0-dev >> /dev/null 2>&1
echo -n "> Installing seq-gen "
sudo ./src/temp apt install seq-gen >> /dev/null 2>&1
echo -n "> Updating project modules "
sudo ./src/temp git submodule update --init --recursive >> /dev/null 2>&1
echo -n "> Installing Gargammel and its dependencies "
cd src/gargammel >> /dev/null
sudo ../temp make >> /dev/null 2>&1
cd - >> /dev/null
echo -n "> Installing simpipe "
sudo ./src/temp pip install -e . >> /dev/null 2>&1
GREEN='\033[0;32m'
echo -e "${GREEN}> Successfully installed package simpipe"
rm src/temp

