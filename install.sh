sudo apt update
sudo apt install cmake
sudo apt-get install libgsl0-dev
sudo apt install seq-gen
cd src/gargammel
make
cd -
pip install -e .