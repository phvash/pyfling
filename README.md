==========================================================================
Pyfling: A Python script for file sharing
@author: Phvash
version 1.0
==========================================================================

### About

* uses tcp
* written in python 2
* compatible with smartphones through qpython

### Requirements

* based solely on the python standard libray
  (i.e no external libraries or installations required)

### Installation

* Download or clone from https://www.github.com/phvash/pyfling

### How to use:

1. Set up a wireless local area network
   - Procedure varies based on machine
   - Search the web for help on how to do this

2. Set up the server
   - Any device on the network with WiFi hotspot capability can used as the server
   - Copy all files to be sent to the subfolder named 'files'
   - Start up the server from the terminal or cmd
	eg. $ python tcpServer.py

3. Set up the client
   - Get the ip address of the server or host
      a. Open up a terminal on linux and mac or cmd on windows
      b. run ipconfig(windows) or ifconfig(linux)
      c. copy out the ipv4 address of the host
   - Start up the client from the terminal or cmd with the server address as an argument
	eg. $ python tcpClient.py 127.0.0.1

4. Check 'received' subfolder in client folder for received files


### To do:
* Pass HOST as command-line args [DONE]
* Main server displaying current activities [DONE]
* Server multithreading to handle multiple requests simultaneously
* Progress bar
* Client file Unzipping and clearing used files [DONE]
* Clean up broken zip files if transfer doesn't complete breaks
* Don't create zip file until the files have been completely received

### Issues
* Better support for mobile version:
    - Fix write path and persmission issue
