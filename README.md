# IceBreaker
A Raspberry Pi -powered interpreter device to assist the deaf in communicating with others. For Open Health HACKademy 2019 in Potsdam.

To run on boot:

The project should be checked out to /home/pi/IceBreaker

`$ cd /home/pi`  
`$ mkdir logs`  
`$ sudo crontab -e`  
Add the following line to the bottom of the text:  
`@reboot sh /home/pi/IceBreaker/launcher.sh >/home/pi/logs/cronlog 2>&1`  
Press Ctrl+O, then Enter  
