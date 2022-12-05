# aiogram_webhook_template
Aiogram Webhook Bot Template

<p><b>1.	Базовая настройка сервера</b>

<p>apt update && apt upgrade
<p>apt install sudo vim ufw -y
<p>adduser USERNAME
<p>usermod -aG sudo USERNAME
<p>vim /etc/ssh/sshd_config

<p><code>PermitRootLogin no
<p>X11Forwarding no
<p>Port NEWPORT
</code>
<p>Esc - :wq
<p>ufw default deny incoming
<p>ufw default allow outgoing
<p>ufw allow NEWPORT
<p>ufw enable
<p>service sshd restart
<p><b>2.	Установка необходимых модулей и настройка nginx</b>
<p>sudo apt install python3 python3-venv nginx git snapd -y
<p>sudo snap install core
<p>sudo snap refresh core
<p>sudo snap install --classic certbot
<p>sudo ln -s /snap/bin/certbot /usr/bin/certbot
<p>sudo ufw allow ‘Nginx Full’
<p>sudo systemctl stop nginx
<p>sudo vim /etc/nginx/sites-available/DOMAINNAME

<p><code>server {
<p>  server_name DOMAINNAME;
<p>    listen 80;
<p>  location /BOTURL {
<p>        proxy_pass http://127.0.0.1:BOTPORT;
<p>        proxy_set_header Host $http_host;
<p>        proxy_set_header X-Real-IP $remote_addr;
<p>        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
<p>        proxy_set_header realip $remote_addr;
<p>        }
<p>}
</code>
<p>Esc - :wq
<p>sudo ln -s /etc/nginx/sites-available/DOMAINNAME /etc/nginx/sites-enabled/
<p>sudo nginx -t
<p>sudo certbot --nginx -d DOMAINNAME
<p>sudo vim /etc/nginx/sites-available/DOMAINNAME

<p><code><b>*add at the beginning*</b>
<p><b>*disable http://server_ip access*</b>
<p>server {
<p>	listen 80;
<p>	server_name “”;
<p>	return 444;
<p>}
<p><b>*add after “server_name DOMAINNAME”*</b>
<p><b>*disable http://DOMAINNAME access*</b>
<p>location / {
<p>	return 444;
<p>}
<p><b>*add before “listen 443”*</b>
<p>listen 80;
</code>
<p>Esc - :wq
<p>sudo systemctl start nginx
<p>sudo certbot renew --dry-run
<p><b>3.	Установка бота</b>
<p>mkdir FOLDERNAME
<p>cd FOLDERNAME
<p>git clone GIT_BOT_URL .
<p>cp env_template.env
<p>vim .env
<p>Esc - :wq
<p>python3 -m venv venv
<p>. venv/bin/activate
<p>pip install -r requirements.txt
<p><b>4.	Тест работы бота</b>
<p>python3 bot.py
<p>deactivate
<p><b>5.	Настройка автозапуска бота</b>
<p>sudo vim /etc/systemd/system/BOTNAME.service

<p><code>[Unit]
<p>Description=DESCRIPTION
<p>After=syslog.target
<p>After=network.target
<p>
<p>[Service]
<p>Type=simple
<p>User=USERNAME
<p>WorkingDirectory=/path/to/bot
<p>ExecStart=/path/to/bot/venv/bin/python3 /path/to/bot/bot.py
<p>RestartSec=10
<p>Restart=always
<p>
<p>[Install]
<p>WantedBy=multi-user.target
</code>
<p>Ecs - :wq
<p>sudo systemctl daemon-reload
<p>sudo systemctl enable BOTNAME
<p>sudo systemctl start BOTNAME
<p>sudo systemctl status BOTNAME
<p><b>6.	Перезагрука сервера</b>
<p>sudo reboot
<p>после перезагрузки бот должен работать


