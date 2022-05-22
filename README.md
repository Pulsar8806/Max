[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Pulsar8806/Max)

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
