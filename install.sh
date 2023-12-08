sudo apt update
sudo apt install cmake
sudo apt-get install libgsl0-dev
sudo apt install seq-gen
cd sim/gargammel
make
cd -
pip install -e .