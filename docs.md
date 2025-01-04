# Networking Expert 
## Lab 1 Install the virtual lab environment

### Preparation and Implementation
1. Installing virtualbox `sudo pacman -S virtualbox` installs the latest version 7.1.4-4
2. I used the files provided to me by the devnet course, these can be found in the resources tab. in this case the VM image
3. Installation of VM image can be achieved by importing the image via the virtualbox UI.


### Task Troubleshooting
1. No need for troubleshooting everything worked fine on the first try.

### Task Verification
1. I booted the VM, pinged to it from my host to see if it was reachable. On the VM itself i used the browser to check if it was able to connect to the internet.

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

### Task Verification
1. I booted the VM, pinged to it from my host to see if it was reachable. On the VM itself i used the browser to check if it was able to connect to the internet.