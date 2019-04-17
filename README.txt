metaquery.py is python script with a GUI based on Tkinter and uses postgresql driver psycopg2 to send a query to the 
shadow database. THIS DOES NOT MODIFY THE DATABASE, it uses the read-only user of the Database. The main purpose of 
this script is to search subscriber gateways based on configured domain name or static ip address. it returns the configured
name of the subscriber gateway(s) so you can find it in metaview web or explorer. It can be modified to search by 
sip binding as well but currently does not. My main use for this is to find gateways that have been "orphaned" and 
do not have a subscriber associated with them(resulting in unusable cable modems). For me the configured domain names (FQDN)
look like this x1-'modem mac address with - instead of :'@domain.net This app searches by the Mac address contained in the FQDN.

INSTRUCTIONS for COMPILING:

1. Install python 2.7 (I used 2.7.15)
2. add environmental Variables to Windows for python and pip
3. In cmd run "pip install psycopg2"
4. in cmd run "pip install cx_Freeze"
5. open metaquery.py in text editor and modify the MetaIP variable on line 7. example MetaIP = '192.168.1.1'
6. (optional) if you have changed any of the other variables on your Meta you must also modify them in this 
file (lines 8-10). It contains the default settings currently.
7. In cmd change directories to the folder that contains the script and run 'python metaquery.py' to test. 
8. (optional) once working I compiled it for distribution by running the setup script by running
'python setup.py bdist_msi' which will build a msi installer (allows others to use without having to install python)
9. Create desktop shortcut by going to install location (C:/Program Files (x86)/MetaSwitch Subscriber Gateway Query/)
is the default and create a shortcut for the metaquery.exe file.

Future: 

I'd like to add to the search by IP address function to be able to query the resolved IP address instead of just by 
the configured static IP address. (something I realized while using the app)

TESTED:

I tested and use this on my Metaswitch running v9.2. 


SIDE NOTE:

This is my first full python app so if you have any pointers or improvements please let me know. 

