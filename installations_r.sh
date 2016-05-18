sudo apt-get install python-pip
sudo pip install django==1.8.5
sudo pip install djangorestframework
sudo pip install django-cors-headers
sudo pip install django-cron

sudo apt-get update
sudo apt-get install mysql-server
sudo pip install MySQL-python
sudo pip install PyJwt
sudo pip install --upgrade google-api-python-client

sudo apt-get install nginx

sudo apt-get install  zip

sudo pip install google-api-python-client==1.4.2
sudo pip install oauth2client==1.4.12

echo "create database raythumithra" | mysql -u root -p

# steps to follow automatic google drive upload after above installation

# step1: In developer google console goto google drive and enable it

#step2  create service account

# After google drive project is created, You go to API & Auth tab and click on Credentials.
#From here, click on button with label Create new Client ID and select service account and click on Create Client ID button ,
#after created service account, you download the private key to somewhere such as I put at path "configs/74214843aee8aba9f11b7825e0a22ef1f06533b7-privatekey.p12"
#and copy service account id such as "xxxxx-5kfab22qfu82uub2887gi0c9e6eincmu@developer.gserviceaccount.com"


#step3: You come back to your google drive drive.google.com
#and create share folder( you create an empty folder and right click on the folder and share to user xxxxx-5kfab22qfu82uub2887gi0c9e6eincmu@developer.gserviceaccount.com )
#and copy the folder id ( You can look at the url after visit folder and the id is there )
#and in my case the backup folder url is https://drive.google.com/#folders/0B0XTTQmH9aXreFdxS0txVU5Xb1U so that the id is 0B0XTTQmH9aXreFdxS0txVU5Xb1U

#step5
#Create config file( such as config_file.json ) and input into this file with json format such as

#{
#    "service_account":"xxxxx-5kfab22qfu82uub2887gi0c9e6eincmu@developer.gserviceaccount.com",
#    "private_key12_path":"configs/74214843aee8aba9f11b7825e0a22ef1f06533b7-privatekey.p12",
#    "backup_folder_id":"0B0XTTQmH9aXreFdxS0txVU5Xb1U",
#    "description" : "Description for backup file",
#    "max_file_in_folder": 5
#}

#usage: python backup.py path/configs/config_file.json /path/backup_file.tar.gz


#-----------creation cron tab
#ubuntu contains crontab service in which you can add following code
#crontab -e
#30 2 * * * /home/ubuntu/raythumithra/backup_scripts/backup.sh  > /home/ubuntu/raythumithra/cron_error.log 2>&1



#---------------nginx
# in /etc/nginx/site-enable/default code
server {
        listen  80;
        server_name raythumithrafertilizers.in 52.36.255.74;
        location /static/static/ {
            root /home/ubuntu/raythumithra;
        }
        location / {
                proxy_set_header Host $host;
                proxy_pass http://127.0.0.1:8000/;
                proxy_http_version 1.1;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
        }
}


#----------/etc/init/ray.conf code

description "new Repository Deamon upstart script"
start on runlevel [235]
stop on runlevel [016]
respawn
script
        cd /home/ubuntu/raythumithra
        PORT=8000 python manage.py runserver >> /var/log/ray_log.log 2>&1
end script

