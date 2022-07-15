#!/bin/bash

# contains the content for the post-receive script used for testing auto-deployment 
# of the portfolio site using git hooks
# file located in ~/proj/hooks/ on the VPS and not intended to be used in the portfolio folder

while read oldrev newrev ref
do
if [[ $ref =~ .*/main$ ]];
then
echo "Main ref received.  Deploying master branch to production..."

GIT_WORK_TREE=../project-elegant-elephant-myversion GIT_DIR=../project-elegant-elep
hant-myversion/.git git fetch
GIT_WORK_TREE=../project-elegant-elephant-myversion GIT_DIR=../project-elegant-elep
hant-myversion/.git git reset --hard origin/main
cd /root/project-elegant-elephant-myversion
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build

else
echo "Ref $ref successfully received.  Doing nothing: only the main branch may b
e deployed on this server."
fi
done