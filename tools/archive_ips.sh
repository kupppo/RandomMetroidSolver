#!/bin/bash

DB_PARAMS=~/RandomMetroidSolver/db_params.py

function get_db_param {
    PARAM="$1"
    sed -e "s+.*${PARAM}='\([^']*\)'.*+\1+" ${DB_PARAMS}
}

function get_pending_seeds {
    SQL="select guid from randomizer where upload_status = 'pending';"
    echo "${SQL}" | mysql --skip-column-names --silent -h ${host} -u ${user} -p${password} ${database}
}

function update_seed_status {
    local KEY="${1}"
    local STATUS="${2}"

    SQL="update randomizer set upload_status = '${STATUS}' where guid = '${KEY}';"
    echo "${SQL}" | mysql --skip-column-names --silent -h ${host} -u ${user} -p${password} ${database}
}

cd ~/varia_repository

# get list of pending upload seeds
export host=$(get_db_param "host")
export user=$(get_db_param "user")
export database=$(get_db_param "database")
export password=$(get_db_param "password")

KEYS=$(get_pending_seeds)

# add them to git
for KEY in ${KEYS}; do
    git add ${KEY}
    update_seed_status "${KEY}" "uploaded"
done
git commit -m "daily commit" .
git push

# delete non git older than retention
RETENTION_DAYS=7
git status . | grep -E '[0-9]+/' | while read KEY; do
    if [ -n "$(find "${KEY}" -mtime +${RETENTION_DAYS})" ]; then
        echo "delete ${KEY}"
        rm -rf "${KEY}"
        KEY=$(echo "${KEY}" | sed -e 's+/$++')
        update_seed_status "${KEY}" "deleted"
    fi
done
