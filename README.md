# Networking Expert 
## Lab 1 Install the virtual lab environment

### Preparation and Implementation
1. Installing virtualbox `sudo pacman -S virtualbox` installs the latest version 7.1.4-4
2. I used the files provided to me by the devnet course, these can be found in the resources tab. in this case the VM image
3. Installation of VM image can be achieved by importing the image via the virtualbox UI.


### Task Troubleshooting
1. No need for troubleshooting everything worked fine on the first try.

### Task Verification
1. On the VM itself i used the browser to check if it was able to connect to the internet.

## Lab 2 Install the CSR1000v VM

### Preparation and Implementation
1. I download the provided files from the file share 
2. I read the instructions of the corresponding lab
3. I created a new network interface in virtualbox, as mentioned in the guide. 
4. Now that the preparation was done, I started by importing the router into virtualbox.
5. Next I changed the iso file in the first cd drive to the one mentioned in the guide.
6. wait for success 
7. success


### Task Troubleshooting
1. I spend quet a bit of time on troubleshooting. mainly because the provided files on the fileshare didn't work. my guess is that the iso file for the installation was the cullprit.
2. I tried the install on both my machine (windows, linux) but the results were the same. I even tried downgrading the version of virtualbox because most resources that i found where pretty outdated.
3. Finally I used the iso file that was provided by devnet itself, this fixed the problem.
4. I saved the state of VM but when i tried to boot it again it gave me an out of memory error. when i checked my resources with the free command, i could see that i had 15GB ram in use. I used this command `echo 3 > /proc/sys/vm/drop_caches` now i had just enough memory. 

### Task Verification
1. I booted the VM and i was able to login to the router.
2. I pinged it from my host with success
3. I pinged the router from the VM i have created in lab 1
4. I used to ssh command to connect to router from my VM.
5. I logged in to webui for the router from the VM and did the same from my host

![alt text](images/image.png)

## Lab 3 Python Network automation with NETMIKO

### Preparation and Implementation
1. First I looked at the script that was mentioned in the assigment. It all seemed pretty self explanetorie. Create a router dictionary import the netmiko module, create ConnectHandler object based of the dict and send a command to the router and print the response.
2. I created a venv `python -m venv NetworkingExpertPeVenv`
3. I activated the venv `source NetworkingExpertPeVenv/bin/activate` 
4. I installed pip and installed the netmiko module
5. I adjusted the values of the router dictionarie to the correspond to my router.
6. added show commands and a config command and saved the output to a file
7.


### Task Troubleshooting
1. I first created the venv via vscode, the problem here was that it was installed in some location managed by vscode, and I wanted it to be part of my PE directory. 
2. I created the venv via my cli now it was available in my directory and I knew the location.

### Task Verification
1. I ran the script and recieved the desired output, showing a succesfull connection.
``` sh
python Lab3_netmiko.py 


Interface Configuration:

('Building configuration...\n'
 '\n'
 'Current configuration : 117 bytes\n'
 '!\n'
 'interface GigabitEthernet1\n'
 ' description VBox\n'
 ' ip address dhcp\n'
 ' negotiation auto\n'
 ' no mop enabled\n'
 ' no mop sysid\n'
 'end\n')

==================================================
```
2. This is the output of the final form of the script
```bash
python Lab3_netmiko.py 
Configuration Output for 192.168.56.101:

('configure terminal\n'
 'Enter configuration commands, one per line.  End with CNTL/Z.\n'
 'CSR1000v(config)#hostname CSR1000v_Local\n'
 'CSR1000v_Local(config)#hostname CSR1000v\n'
 'CSR1000v(config)#interface GigabitEthernet1\n'
 'CSR1000v(config-if)# description Configured by Netmiko\n'
 'CSR1000v(config-if)# ip address dhcp\n'
 'CSR1000v(config-if)# no shutdown\n'
 'CSR1000v(config-if)#end\n'
 'CSR1000v#')

==================================================

Subinterfaces are already configured. Skipping configuration.
Backup completed successfully for 192.168.56.101.
Configuration Output for 192.168.56.102:

('configure terminal\n'
 'Enter configuration commands, one per line.  End with CNTL/Z.\n'
 'CSR1000v(config)#hostname CSR1000v_Local\n'
 'CSR1000v_Local(config)#hostname CSR1000v\n'
 'CSR1000v(config)#interface GigabitEthernet1\n'
 'CSR1000v(config-if)# description Configured by Netmiko\n'
 'CSR1000v(config-if)# ip address dhcp\n'
 'CSR1000v(config-if)# no shutdown\n'
 'CSR1000v(config-if)#end\n'
 'CSR1000v#')

==================================================

Configuring subinterfaces...
Subinterface Configuration Output:

('configure terminal\n'
 'Enter configuration commands, one per line.  End with CNTL/Z.\n'
 'CSR1000v(config)#interface GigabitEthernet1.10\n'
 'CSR1000v(config-subif)#encapsulation dot1Q 10\n'
 'CSR1000v(config-subif)#ip address 192.168.10.1 255.255.255.0\n'
 'CSR1000v(config-subif)#no shutdown\n'
 'CSR1000v(config-subif)#interface GigabitEthernet1.20\n'
 'CSR1000v(config-subif)#encapsulation dot1Q 20\n'
 'CSR1000v(config-subif)#ip address 192.168.20.1 255.255.255.0\n'
 'CSR1000v(config-subif)#no shutdown\n'
 'CSR1000v(config-subif)#end\n'
 'CSR1000v#')

==================================================

Backup completed successfully for 192.168.56.102.
```
3. I created an exciting and challenging script that monitors interface status and bandwidth utilization, logs the information to a file, and sends alerts if any interface goes down or if bandwidth utilization exceeds a certain threshold.
    ```sh
    python Lab3b_netmiko.py
    ```

The script continuously checks the interface status and bandwidth utilization every 5 minutes, logs the information, and prints alerts to the console.

4. to verify the script i have manually shutdown one of the sub interfaces and this imediately results in a message to the console, the outputs can also be viewed in the outputs folder under interface_status_log.txt

`❯ python Lab3b_netmiko.py 
ALERT: GigabitEthernet1.10 is down (Status: administratively, Protocol: down)
`

## Lab 4