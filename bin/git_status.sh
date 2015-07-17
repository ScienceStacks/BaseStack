# Inquire about git status, filtering noise files
git status | grep -v "\.pyc" | grep -v "\.swp"
