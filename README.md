# OnBoard-Scripts
Python scripts for raspberry pi

# How to transfer files from raspberry pi to local computer
Software needed:

winSCP 
Alternative 1 -> https://ninite.com/winscp/ (9/4/2019)
Alternative 2 -> https://winscp.net/eng/download.php (9/4/2019)

Note: The pi and the local computer must be connected to the same 
wifi.

1. Open pi terminal 
2. Run the following command -> sudo rasi-config
3. Run the following command -> ifconfig
4. copy the ip from the pi.
5. Open winSCP.
6. Enter on host name the ip from the pi.
7. Enter username and password of the pi.
8. The left contains the local data and the right contains the pi
   data. 
9. Drag and drop to move files.

Reference: https://www.youtube.com/watch?v=WIOpNuQc068&list=WL&index=207&t=0s
