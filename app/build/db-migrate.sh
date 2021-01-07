#!/usr/bin/env bash
set -e
set -x
export MIGRATIONS_DIR='/var/lib/db-migrate/work'
[[ -d /var/lib/db-migrate/work ]] && rm -rf /var/lib/db-migrate/work
mkdir -p /var/lib/db-migrate/work
if [[ -f "/var/lib/db-migrate/lock" ]]
then
  echo "lock exists do nothing"
else
  echo "lock file does not exist, performing migration"
  cd /home/app
  python migrations.py db init
  python migrations.py db migrate
  python migrations.py db upgrade
  touch /var/lib/db-migrate/lock
fi
