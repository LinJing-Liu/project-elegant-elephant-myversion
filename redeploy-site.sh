#!/bin/bash

tmux kill-server
cd /root/project-elegant-elephant-myversion
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
cd /root

SESSION="redeploy"
tmux new-session -d -s $SESSION
tmux rename-window -t 0 'Main'
tmux send-keys -t 'Main' 'cd /root/project-elegant-elephant-myversion' C-m 'export FLASK_ENV=development' C-m 'flask run --host=0.0.0.0' C-m
