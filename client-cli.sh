#!/usr/bin/env bash

echo "You're running ManoucheQL's client CLI"

MODULE_PATH="./src/client_old/modules"

PY_EXTENSION="py"

HTML_EXTENSION="html.jinja2"

CSS_EXTENSION="css"

ROUTER_FILE="router.py"

function generate_py() {
	cat > "$MODULE_PATH/$1/$2.$PY_EXTENSION" << EOF
data = {
	"page_name": "$3"
}

methods = {}

on_open = []
EOF
}

function generate_html() {
	cat > "$MODULE_PATH/$1/$2.$HTML_EXTENSION" << EOF
Welcome to the $3 page
EOF
}

function generate_css() {
	cat > "$MODULE_PATH/$1/$2.$CSS_EXTENSION" << EOF
EOF
}

function generate_module() {
	if [ -d "$MODULE_PATH/$1" ]; then
		echo "Module $1 already exists"
	else
		module_name=`basename "$1"`
		module_upper_name="${module_name^}"
		echo "Creating module $module_name"
		echo "Generating $1 folder in $MODULE_PATH"
		mkdir "$MODULE_PATH/$1"
		echo "Generating $module_name.$PY_EXTENSION"
		generate_py $1 $module_name $module_upper_name
		echo "Generating $module_name.$HTML_EXTENSION"
		generate_html $1 $module_name $module_upper_name
		echo "Generating $module_name.$CSS_EXTENSION"
		generate_css $1 $module_name
		echo "Now, add this route to the $ROUTER_FILE routes array:"
		echo "{\"name\": \"$module_upper_name\", \"path\": \"$1\", \"module\": \"$1\"}"
	fi
}

function show_help() {
	echo "You have to choose between those actions:"
	echo " - new [type]: Create item based on [type]"
	echo "     types:"
	echo "       - module [name]: Generate new module based on [name]"
}

if [[ $1 ]];then
	case $1 in "new")
		if [[ $2 ]]; then
			case $2 in "module")
				if [[ $3 ]]; then
					generate_module $3
				else
					echo "You have to specify a name to your new module:"
					echo " - new module [name]"
				fi
			esac
		else
			echo "You have to specify an option between the followings:"
			echo " - module [name]: Generate new module based on [name]"
		fi
		;;
		*)
		show_help
	esac
else
	show_help
fi

