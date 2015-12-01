# Inquire about git status, filtering noise files
clear; git status | grep -v "\.pyc" | grep -v "\.swp"
