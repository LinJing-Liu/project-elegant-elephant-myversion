#!/bin/sh

# curl tests for the mysql database
echo "Input the content for a random timeline post: "
read INPUT
CONTENTS=( "$INPUT" )
echo "Input the content for another random timeline post: "
read INPUT
CONTENTS+=( "$INPUT" )

EMAIL="lin@gmail.com"
NAME="lin"
IDS=()
for entry in "${CONTENTS[@]}"
do
    ID=$(curl -X POST http://127.0.0.1:5000/api/timeline_post -d "name=${NAME}&email=${EMAIL}&content=${entry[@]}" | jq '.id')
    IDS+=( $ID )
done

GETOUTPUT=$( curl http://127.0.0.1:5000/api/timeline_post | jq '.timeline_posts|.[]' )
function checkPostContent () {
    if [[ $1.name = $NAME && $1.email = $EMAIL && $1.content = $0 ]]
    then
        return 0
    else
        return 1
    fi
}
n=0
for i in ${IDS[@]}
do
    SELECTED=$( jq -r 'select(.id=='${i}')' <<< "${GETOUTPUT}")
    if checkPostContent "${CONTENTS[n]}" $SELECTED
    then
        echo "Test failed"
        exit 0
    fi
    curl -X DELETE http://127.0.0.1:5000/api/timeline_post -d "id=${i}"
    n=$(( $n + 1 ))
done
echo "Tests passed"