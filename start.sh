#!/bin/bash

if [ -a metadata.txt ]; then
	python main.py
else
	echo "Sorry, please set up your application first by running setup.sh"
	read -p "Would you like us to do this for you? Y/N:" ans
	if [ "$ans" == "Y" ] || [ "$ans" == "y" ]; then
		sudo ./setup.sh
	fi
fi
