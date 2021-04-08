# McDonalds EasterHack

Run this python script to get a very high score in the easter game in the McDonanald's app.

## Requirements
- Need python
- Need phone
- Need McDonald's app

## Setup
Python virtualenv
```
# create python 3 virtualenv called venv
# example is for mac

virtualenv venv
source venv/bin/activate
```
Install requirements
```
pip install -r requirements.txt
```
Run script
```
# your score can be any number
python main.py 999
```
Set up Proxy
1. Set your phone's wifi to use your computer as a proxy, use port 8080
2. Install SSL certificates to your phone from mitm.it

- You could also follow [this guide on medium](https://medium.com/testvagrant/intercept-ios-android-network-calls-using-mitmproxy-4d3c94831f62), but skip to *Settup up your phone*

## Run
Just go play the easter game and die immediately. Your score will become the score you specified earlier.
