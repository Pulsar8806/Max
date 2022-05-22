<p align='left'>
 <a href="https://www.supun.ml/deploy.html"><img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy on Heroku"></a></br></br>
</p>


<h3>Features</h3> 
<ul>
    <li>Playlist features</li>
    <li>Multi Language</li>
    <li>Maintained</li>
    <li>Less environment variables</li>
</ul>

<h3>Telegram</h3>
<ul>
    <a href="https://t.me/solidprojects"><img alt="SolidProject Channel" src="https://img.shields.io/badge/SolidProject-Channel-blue.svg?logo=telegram"></a> <br/>
    <a href="https://t.me/solidprojects_chat"><img alt="SolidProject Support" src="https://img.shields.io/badge/SolidProject-Support-blue.svg?logo=telegram"></a> <br/>
</ul>


### Deploy to VPS
```
$ sudo su
# apt-get update && apt-get upgrade -y
# apt-get install curl
# curl -sL https://deb.nodesource.com/setup_16.x | bash - 
# apt-get install ffmpeg python3-pip python3-virtualenv nodejs -y 
# git clone https://github.com/doellbarr/solidmusic && cd solidmusic 
# virtualenv venv && . venv/bin/activate 
# pip3 install --no-cache-dir -r requirements.txt 
# cp sample.env .env 
# nano .env # fill it with your env 
# python3 main.py
```
