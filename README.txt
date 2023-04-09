Assuming you have git, python, pip, mySQL and libmysqlclient-dev installed and set-up
`sudo apt-get install python3 pip python-is-python3 git libmysqlclient-dev` 

Run: `./run_project.sh`
This will ask the SQL username and password. In the CIC Lab, Username: root and Password: passwd. 
If you are getting Permission errors, it means either the username, password is wrong or mysql is 
not set-up.

After everything returns OK, run `./manage.py runserver`. Then open 127.0.0.1:8000 on any browser.
It will display the required website.

Common Errors:
- mysql_config not found
This implies the library could not find the mysql command on the command line. Make sure you can run
mysql on the terminal/powershell.