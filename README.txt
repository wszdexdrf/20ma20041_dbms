Assuming you have git, python, pip, mySQL and libmysqlclient-dev installed and set-up.
On Ubuntu, run:
`sudo apt-get install python3 pip python-is-python3 git libmysqlclient-dev` 

Then run: `./run_project.sh`
This will ask the SQL username and password. In the CIC Lab, Username: root and Password: passwd. 
If you are getting Permission errors, it means either the username, password is wrong or mysql is 
not set-up. This will take some time because it is generating random data. This will run only once.

After everything returns OK, run `./manage.py runserver`. Then open 127.0.0.1:8000 on any browser.
It will display the required website.

Now if you want to restart the server, only stop/restart the command `./manage.py runserver`.

Randomly generated username and passwords for login are in passwords.txt after starting the server.

Common Errors:
- mysql_config not found
This implies the library could not find the mysql command on the command line. Make sure you can run
mysql on the terminal/powershell.