#!/bin/sh

spinner() {
  local delay=0.3
  local spinstr='|/-\'
  while [ "$(ps -p $$ -o comm=)" ]; do
    local temp=${spinstr#?}
    printf "[%c]" "$spinstr"
    local spinstr=$temp${spinstr%"$temp"}
    sleep $delay
    printf "\b\b\b"
  done
  printf "    \b\b\b\b"
}

# Get sql user name and password
read -p "SQL username: " username
read -p "SQL password: " pass

sed -i "s/<username>/$username/" ./erp/settings.py 
sed -i "s/<password>/$pass/" ./erp/settings.py 

pip install mysqlclient
pip install django
pip install faker

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
printf "Please be patient " 
# start the spinner in the background
spinner "$0" &
./manage.py shell < mainapp/generate_data/departments.py
./manage.py shell < mainapp/generate_data/faculty.py
./manage.py shell < mainapp/generate_data/students.py
./manage.py shell < mainapp/generate_data/courses.py
./manage.py shell < mainapp/generate_data/enrollments.py
kill $! >/dev/null 2>&1