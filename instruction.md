# Installing the urinterface


* Clone urinterface repo from: https://gitlab.au.dk/clagms/urinterface
* Open "Git bash" in the folder where urinterface is cloned, then change the branch from 'master' to 'data_publisher', by typing 'git checkout data_publisher'
* Install the urinterface, by typing 'pip install -e .'
* Check that all necessary python packages are installed



# Installing the non blocking tcp server for the kuka robot

* Download the nonBlockingtcpserver.py file from the repo
* install all the necessary python packages



# Connect through an ethernet cable to the switch setup in the Flexcell

* connect ethernet cable to PC and switch
* change computer's IP address to a static IP address of '192.168.1.14' with a subnet mask of '255.255.255.0'

# Running

## UR robot

* run 'python run_experiment.py'
* 


## Unity

* ensure both the kuka server and ur server are running before starting the Unity live stream application