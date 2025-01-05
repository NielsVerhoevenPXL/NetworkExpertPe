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

Sure, here is the documentation for Lab 4 using the provided format:

## Lab 4 Explore YANG Models

### Preparation and Implementation
1. **Launch the DEVASC VM**:
    - If you have not already completed the Lab - Install the DEVASC-LAB, do so now.
    - Launch the DEVASC VM.

2. **Explore a YANG Model on GitHub**:
    - Open Chromium and navigate to [Cisco IOS XE YANG models on GitHub](https://github.com/YangModels/yang).
    - Navigate to the YANG models for Cisco IOS XE version 16.9.3: `vendor > cisco > xe > 1693`.
    - Find and click on `ietf-interfaces.yang`.
    - Scroll through the file to explore the container nodes, leaf nodes, and list nodes.
    - Open VS Code.
    - Click `File > Open Folder...` and navigate to the `devnet-src` directory.
    - Click `OK`.
    - Open a terminal window in VS Code: `Terminal > New Terminal`.
    - Create a subdirectory called `pyang` in the `devnet-src` directory:
        ```sh
        mkdir pyang
        ```
    - Return to the Chromium tab with the `ietf-interfaces.yang` model.
    - Click `Raw` to display the raw YANG model data.
    - Copy the URL of the raw YANG model.
    - In the terminal, navigate to the `pyang` folder:
        ```sh
        cd pyang
        ```
    - Use `wget` to save the raw `ietf-interfaces.yang` file:
        ```sh
        wget https://raw.githubusercontent.com/YangModels/yang/master/vendor/cisco/xe/1693/ietf-interfaces.yang
        ```

3. **Explore a YANG Model Using pyang**:
    - In VS Code, open a terminal window.
    - Verify that pyang is installed:
        ```sh
        pyang -v
        ```
    - (Optional) Update pyang to the latest version:
        ```sh
        pip3 install pyang --upgrade
        ```
    - Navigate to the `pyang` directory:
        ```sh
        cd pyang
        ```
    - Explore the options for transforming the YANG model:
        ```sh
        pyang -h | more
        ```
    - Transform the `ietf-interfaces.yang` model into a tree format:
        ```sh
        pyang -f tree ietf-interfaces.yang
        ```

### Task Troubleshooting
1. If you encounter a `ModuleNotFoundError` for `pkg_resources`, install the `setuptools` package:
    ```sh
    pip install setuptools
    ```

### Task Verification
1. Verify that the `ietf-interfaces.yang` model is transformed into a tree format and is easier to read:
    ```sh
    pyang -f tree ietf-interfaces.yang
    ```

    Example output:
    ```plaintext
    module: ietf-interfaces
    +--rw interfaces
    |  +--rw interface* [name]
    |     +--rw name                        string
    |     +--rw description?                string
    |     +--rw type                        identityref
    |     +--rw enabled?                    boolean
    |     +--rw link-up-down-trap-enable?   enumeration {if-mib}?
    +--ro interfaces-state
       +--ro interface* [name]
          +--ro name                        string
          +--ro type                        identityref
          +--ro admin-status                enumeration {if-mib}?
          +--ro oper-status                 enumeration
          +--ro last-change?                yang:date-and-time
          +--ro if-index                    int32 {if-mib}?
          +--ro phys-address?               yang:phys-address
          +--ro higher-layer-if*            interface-state-ref
          +--ro lower-layer-if*             interface-state-ref
          +--ro speed?                      yang:gauge64
          +--ro statistics
             +--ro discontinuity-time       yang:date-and-time
             +--ro in-octets?               yang:counter64
             +--ro in-unicast-pkts?         yang:counter64
             +--ro in-broadcast-pkts?       yang:counter64
             +--ro in-multicast-pkts?       yang:counter64
             +--ro in-discards?             yang:counter32
             +--ro in-errors?               yang:counter32
             +--ro in-unknown-protos?       yang:counter32
             +--ro out-octets?              yang:counter64
             +--ro out-unicast-pkts?        yang:counter64
             +--ro out-broadcast-pkts?      yang:counter64
             +--ro out-multicast-pkts?      yang:counter64
             +--ro out-discards?            yang:counter32
             +--ro out-errors?              yang:counter32
    ```

Sure, here is the documentation for Lab 5 using the same format as the other labs:

## Lab 5 Use NETCONF to Access an IOS XE Device

### Preparation and Implementation
1. **Launch the DEVASC VM**:
    - If you have not already completed the Lab - Install the DEVASC-LAB, do so now.
    - Launch the DEVASC VM.

2. **Verify connectivity between the DEVASC VM and the router**:
    - On your router VM, use the `show ip interface brief` command to verify the IPv4 address.
    - Open a terminal in the DEVASC VM and ping the router to verify connectivity:
        ```sh
        ping -c 5 192.168.56.101
        ```

3. **Verify SSH connectivity to the router VM**:
    - In the terminal for the DEVASC VM, SSH to the router VM:
        ```sh
        ssh cisco@192.168.56.101
        ```
    - Enter the password `cisco123!` to access the router.

4. **Check if NETCONF is running on the router**:
    - Use the following command to check if NETCONF is running:
        ```sh
        show platform software yang-management process
        ```
    - If NETCONF is not running, enable it:
        ```sh
        config t
        netconf-yang
        exit
        ```

5. **Access the NETCONF process through an SSH terminal**:
    - Establish an SSH session with the NETCONF port 830:
        ```sh
        ssh cisco@192.168.56.101 -p 830 -s netconf
        ```
    - The router will respond with a hello message listing its NETCONF capabilities.

6. **Start a NETCONF session by sending a hello message from the client**:
    - Copy and paste the following XML code into the SSH session:
        ```xml
        <hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <capabilities>
        <capability>urn:ietf:params:netconf:base:1.0</capability>
        </capabilities>
        </hello>
        ]]>]]>
        ```

7. **Send RPC messages to the router**:
    - To retrieve interface information, paste the following RPC get message XML code into the terminal:
        ```xml
        <rpc message-id="103" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <get>
        <filter>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
        </filter>
        </get>
        </rpc>
        ]]>]]>
        ```

8. **Close the NETCONF session**:
    - Send the following RPC message to close the NETCONF session:
        ```xml
        <rpc message-id="9999999" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <close-session />
        </rpc>
        ]]>]]>
        ```

9. **Verify that 

ncclient

 is installed**:
    - In a DEVASC-VM terminal, verify that 

ncclient

 is installed:
        ```sh
        pip3 list --format=columns | grep ncclient
        ```
    - If not installed, use the following command to install it:
        ```sh
        pip3 install ncclient
        ```

10. **Create a script to use 

ncclient

 to connect to the NETCONF service**:
    - Create a new file named 

python.py

 in the 

Lab_5_netconfig

 directory.
    - Add the following code to the script:
        ```python
        from ncclient import manager
        import xml.dom.minidom

        m = manager.connect(
            host="192.168.56.101",
            port=830,
            username="cisco",
            password="cisco123!",
            hostkey_verify=False
        )

        print("#Supported Capabilities (YANG models):")
        for capability in m.server_capabilities:
            print(capability)

        netconf_filter = """
        <filter>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
        </filter>
        """
        netconf_reply = m.get_config(source="running", filter=netconf_filter)
        print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
        ```

### Task Troubleshooting
1. If you encounter a `ModuleNotFoundError` for `pkg_resources`, install the `setuptools` package:
    ```sh
    pip install setuptools
    ```

### Task Verification
1. Run the script and verify that it retrieves the configuration from the router:
    ```sh
    python python.py
    ```

    ```xml
    <?xml version="1.0" ?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:bbad003e-0e79-47e9-8849-240e07bdfc77">
        <data>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                        <version>16.9</version>
                        <boot-start-marker/>
                        <boot-end-marker/>
                        <banner>
                                <motd>
                                        <banner>^C</banner>
                                </motd>
                        </banner>
                        <service>
                                <timestamps>
                                        <debug>
                                                <datetime>
                                                        <msec/>
                                                </datetime>
                                        </debug>
                                        <log>
                                                <datetime>
                                                        <msec/>
                                                </datetime>
                                        </log>
                                </timestamps>
                        </service>
                        <platform>
                                <console xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-platform">
                                        <output>virtual</output>
                                </console>
                        </platform>
                        <hostname>CSR1000v</hostname>
                        <username>
                                <name>cisco</name>
                                <privilege>15</privilege>
                                <password>
                                        <encryption>0</encryption>
                                        <password>cisco123</password>
                                </password>
                        </username>
                        <ip>
                                <domain>
                                        <name>example.netacad.com</name>
                                </domain>
                                <forward-protocol>
                                        <protocol>nd</protocol>
                                </forward-protocol>
                                <http xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-http">
                                        <authentication>
                                                <local/>
                                        </authentication>
                                        <server>false</server>
                                        <secure-server>true</secure-server>
                                </http>
                        </ip>
                        <interface>
                                <GigabitEthernet>
                                        <name>1</name>
                                        <description>Configured by Netmiko</description>
                                        <ip>
                                                <address>
                                                        <dhcp/>
                                                </address>
                                        </ip>
                                        <mop>
                                                <enabled>false</enabled>
                                                <sysid>false</sysid>
                                        </mop>
                                        <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
                                                <auto>true</auto>
                                        </negotiation>
                                </GigabitEthernet>
                                <GigabitEthernet>
                                        <name>1.10</name>
                                        <shutdown/>
                                        <encapsulation>
                                                <dot1Q>
                                                        <vlan-id>10</vlan-id>
                                                </dot1Q>
                                        </encapsulation>
                                        <ip>
                                                <address>
                                                        <primary>
                                                                <address>192.168.10.1</address>
                                                                <mask>255.255.255.0</mask>
                                                        </primary>
                                                </address>
                                        </ip>
                                </GigabitEthernet>
                                <GigabitEthernet>
                                        <name>1.20</name>
                                        <encapsulation>
                                                <dot1Q>
                                                        <vlan-id>20</vlan-id>
                                                </dot1Q>
                                        </encapsulation>
                                        <ip>
                                                <address>
                                                        <primary>
                                                                <address>192.168.20.1</address>
                                                                <mask>255.255.255.0</mask>
                                                        </primary>
                                                </address>
                                        </ip>
                                </GigabitEthernet>
                        </interface>
                        <control-plane/>
                        <login>
                                <on-success>
                                        <log/>
                                </on-success>
                        </login>
                        <multilink>
                                <bundle-name xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ppp">authenticated</bundle-name>
                        </multilink>
                        <redundancy/>
                        <spanning-tree>
                                <extend xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-spanning-tree">
                                        <system-id/>
                                </extend>
                        </spanning-tree>
                        <subscriber>
                                <templating/>
                        </subscriber>
                        <license>
                                <udi>
                                        <pid>CSR1000V</pid>
                                        <sn>97EKI7MFNN2</sn>
                                </udi>
                        </license>
                        <line>
                                <console>
                                        <first>0</first>
                                        <logging>
                                                <synchronous/>
                                        </logging>
                                        <stopbits>1</stopbits>
                                </console>
                                <vty>
                                        <first>0</first>
                                        <last>4</last>
                                        <login>
                                                <local/>
                                        </login>
                                        <transport>
                                                <input>
                                                        <input>ssh</input>
                                                </input>
                                        </transport>
                                </vty>
                                <vty>
                                        <first>5</first>
                                        <last>15</last>
                                        <login>
                                                <local/>
                                        </login>
                                        <transport>
                                                <input>
                                                        <input>ssh</input>
                                                </input>
                                        </transport>
                                </vty>
                        </line>
                        <diagnostic xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-diagnostics">
                                <bootup>
                                        <level>minimal</level>
                                </bootup>
                        </diagnostic>
                </native>
        </data>
</rpc-reply>


    ```