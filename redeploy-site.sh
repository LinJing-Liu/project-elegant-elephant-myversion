#!/bin/bash

cd /root/project-elegant-elephant-myversion
#git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
cd /root

systemctl daemon-reload
systemctl restart myportfolio
