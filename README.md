# TalkNow

Contributors:
- Justin Wong


This is starting out from the Cisco Hack@Home Hackathon 2021

## Starting the Virtual Environment

Follow this as a reference: https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/


To get started with running the venv for TalkNow, run the following command:
```
virtualenv talknow
source talknow/bin/activate
pip install -r requirements.txt
chmod +x start_local.sh
./start_local.sh
```


## Starting the app

### Locally
```
source talknow/bin/activate
ls
  README.md		app.py			requirements.txt	talknow
pip install requirements.txt

flask run
```
