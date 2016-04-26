#!/bin/bash
# Database credentials
 user="root"
 password="root"
 host="localhost"
 db_name="raythumithra"


# Other options
 backup_path="/home/ubuntu/raythumithra/backup_scripts/database_backup"
 date=$(date +"%d-%b-%Y")

# Set default file permissions
 umask 177

# Dump database into SQL file
 mysqldump --user=$user --password=$password --host=$host $db_name > $backup_path/$db_name.sql


# Delete files older than 30 days
 find $backup_path/* -mtime +30 -exec rm {} \;

python /home/ubuntu/raythumithra/backup_scripts/backup.py config_file.json database_backup/$db_name.sql

zip -r /home/ubuntu/raythumithra/backup_scripts/backup_bills/bill_images.zip /home/ubuntu/raythumithra/static/static/uploads

python /home/ubuntu/raythumithra/backup_scripts/backup.py config_file2.json backup_bills/bill_images.zip


rm -rf /home/ubuntu/raythumithra/backup_scripts/backup_bills/*

rm -rf /home/ubuntu/raythumithra/backup_scripts//database_backup/*
