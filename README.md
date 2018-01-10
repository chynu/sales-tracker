# Sales Tracker
### Very Simple Sales Tracker for Amazon Sellers

This was originally created for Boenmo. This is a Flask application.

## Setup

Install all requirements by running

```
sudo ./setup.sh
```

Log in if the terminal asks for your credentials. If you are having trouble
running the file, try changing access settings on the file by running

```
chmod u+x setup.sh
```

to give yourself execution access to the bash file.

Running this file does two things: (1) it installs necessary Python dependencies and (2) it asks you for your company name to personalize the sales tracker. If you wish to do one and not the other, run `./setup.sh 0` to only install dependencies and `.setup.sh 1` to only change the company name.

## Run the Application

You can run the application by typing

```
./start.sh
```
