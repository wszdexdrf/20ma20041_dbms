#!/bin/sh

# Get sql user name and password
read -p "SQL username: " username
read -p "SQL password: " pass

sed -i "s/<username>/$username/" ./erp/settings.py 
sed -i "s/<password>/$pass/" ./erp/settings.py 

# Generate random data using scripts
./manage.py shell < mainapp/generate_data/departments.py
./manage.py shell < mainapp/generate_data/faculty.py
./manage.py shell < mainapp/generate_data/students.py
