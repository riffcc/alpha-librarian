#!/bin/bash
pip3 install virtualenv
python3 -m venv venv
source venv/bin/activate
pip3 install internetarchive
pip3 install json
pip3 install tqdm
pip3 install requests
pip3 install torrentool
pip3 install fnmatch