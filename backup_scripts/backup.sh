#!/bin/bash
# Database credentials
 user="root"
 password="root"
 host="localhost"
 db_name="kranthiagro"


# Other options
 backup_path="/home/ubuntu/xyz/backup_scripts/database_backup"
 date=$(date +"%d-%b-%Y")

# Set default file permissions
 umask 177

# Dump database into SQL file
 mysqldump --user=$user --password=$password --host=$host $db_name > $backup_path/$db_name.sql


# Delete files older than 30 days
 find $backup_path/* -mtime +30 -exec rm {} \;

python /home/ubuntu/xyz/backup_scripts/backup.py config_file.json database_backup/$db_name.sql


rm -rf /home/ubuntu/xyz/backup_scripts/database_backup/*
