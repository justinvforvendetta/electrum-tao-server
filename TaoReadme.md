The Tao Electrum Server "Keep it Simple" Instructions
=============================================

3 things, and you are done. again this is the fast "i dont need a manual" directions. detailed installation is in "INSTALL"

taod
-----------

* tao.conf must have txindex=1 in it. After updating, you'll need to reindex.

electrum-tao-server
---------------------

* Create a directory /var/electrum-tao-server 
	$sudo mkdir /var/electrum-tao-server
* Chown the directory to the user you'll run the electrum-tao-server as. 
	$sudo chown user:user /var/electrum-tao-server
* Install tao_hash located in src/tao_hash 
	$cd src/tao_hash && sudo python setup.py install
*Install electrum-tao-server
	$sudo ./configure
	$sudo python setup.py install 

electrum-tao-server configuration
---------------------------------

*By default, the configuration file is located in /etc/electrum-tao.conf
*By defualt, the logfile is located in /var/log/electrum-tao.log 
*Check for both these files before attempting to run electrum-tao-server.
	If they do not exist, create them and chown them to the user you'll be using.




 


 
