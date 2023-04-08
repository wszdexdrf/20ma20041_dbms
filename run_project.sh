#!/bin/sh

# Get sql user name and password
read -p "SQL username: " username
read -p "SQL password: " pass

sed -i "s/<username>/$username/" ./erp/settings.py 
sed -i "s/<password>/$pass/" ./erp/settings.py 

# Execute MySQL command
mysql -u $username -p$pass -h "localhost" -e "CREATE DATABASE erpdb;"

# Temporarily move urls.py for making migrations
mv erp/urls.py erp/bak_urls.py
cp erp/less_urls.py erp/urls.py
./manage.py makemigrations mainapp
./manage.py migrate

# Move back urls.py
mv erp/bak_urls.py erp/urls.py

# Generate random data using scripts
./manage.py shell < mainapp/generate_data/departments.py
./manage.py shell < mainapp/generate_data/faculty.py
./manage.py shell < mainapp/generate_data/students.py
./manage.py shell < mainapp/generate_data/courses.py
./manage.py shell < mainapp/generate_data/enrollments.py
