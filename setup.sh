#!/bin/bash

install_dependencies() {
	sudo pip install -r req.txt
	echo "======= DEPENDENCIES INSTALLED ======="
}

change_name() {
	if [ -a metadata.txt ]; then
		> metadata.txt
	else
		touch metadata.txt
	fi

	read -p "Enter your company name: " name
	echo $name >> metadata.txt
	echo "Thank you, $name!"
}

if [ "$#" -eq 0 ]; then
	install_dependencies
	change_name
elif [ "$1" -ne "1" ]; then
	install_dependencies
elif [ "$1" -ne "0" ]; then
	change_name
else
	install_dependencies
	change_name
fi

echo "You can now run start.sh"
