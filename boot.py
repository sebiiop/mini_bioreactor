# Complete project details at https://RandomNerdTutorials.com

import wifimgr              #handles the access point and wifi login
from time import sleep
import machine              #pin library
import network              #handles network connectivity
import os
import ujson as json        #necessary for json file handling
from ota import OTAUpdater  #library for OTA update

try:
  import usocket as socket
except:
  import socket

led = machine.Pin(2, machine.Pin.OUT)

def count():
   count = 0
   while True:
    count += 1
    led.on()
    message = str(count)
    sock.sendall(message.encode())
    print('Sent:', message)
    sleep(5)  # Adjust as needed
    led.off()
    
def read_wifi_credentials_file():
  # Read the wifi credentials from all saved connections from the wifi.dat
  file_path = '/wifi.dat'

  # Open the file in read mode
  try:
      with open(file_path, 'r') as file:
          # Read the contents of the file
          wifi_data = file.read()
          # Print the contents to the console
          return wifi_data
  except OSError:
      print(f"Failed to open or read {file_path}.")


def read_process_parameters():
  #read the process parameters from process_parameter.json
  file_path='/process_parameters.json'
  try:
    with open(file_path, 'r') as file:
      wifi_info = json.load(file)
    return wifi_info
  except OSError:
    print(f"Failed to open or read {file_path}.")
    

############################### Wifi connection setup ###############################
wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D
else:
  print("\n\n\n")
  
# Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
print("ESP OK")

# Get and print the IP address
ip_address = wlan.ifconfig()[0]
print("ESP32 IP address:", ip_address)

#read all saved wifi credentials from wifi.dat file
wifi_file = read_wifi_credentials_file()
print(wifi_file)

#load process_parameters.json
process_parameters = read_process_parameters()
print(process_parameters)

ssid = process_parameters.get("ssid")
print(ssid)
############################### OTA update ###############################
#Github repo page
firmware_url = "https://raw.githubusercontent.com/<username>/<repo_name>/<branch_name>"


#ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "test.py")
#ota_updater.download_and_install_update_if_available()


############################### Main code here ###############################
print("Hello there")
"""
try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind(('', 80))
  s.listen(5)
except OSError as e:
  machine.reset()

# Create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Trying to reach server....")


try:
    # Connect to server
    server_address = ('192.168.68.109', 12345)
    sock.connect(server_address)
    print('Connected to server')

    # Listen for messages from the server
    while True:
        data = sock.recv(1024)
        if data:
            message = data.decode()
            print('Received:', message)
            if message == 'trigger_function':
                #count()

finally:
    sock.close()
    """
