# Port_Scanner
This is a Python Port Scanner program that utilizes Linux cronjob to automatically scan my IP address for vulnerabilities everyday at 12:30pm.
The progam also outputs the open ports and logs them in a text file that is uploaded to Docker and displayed using a flask web application.




Cronjob for linux to run everyday at 12:30
-------------------------------------------
30 12 * * * /usr/bin/python3 /home/king_1up/Documents/port_scan/port_scan.py >>/home/king_1up/Documents/port_Scan_flask/log_file.txt

note: replace the location where python is installed, the location of the python program, and the path to your log file 




Thes commands should be ran on the folder that contains the python progam and docker files to ensure everything runs smoothly
note : to install docker please refer to https://docs.docker.com/engine/install/ubuntu/
also ensure that python is installed on the system https://www.python.org/downloads/
------------------------------------------------------

note : to install docker please refer to https://docs.docker.com/engine/install/ubuntu/

1. to confirm docker is running correctly enter: docker --version

2. docker build -t myflaskapp .

3. to confirm tha the image has been successfully ran:
docker images 

4. docker run -p 5000:5000 myflaskapp




