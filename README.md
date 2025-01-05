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


## Lab 6 Use RESTCONF to Access an IOS XE Device

### Preparation and Implementation
1. **Enable RESTCONF on the router**:
    - Access the router via SSH:
        ```sh
        ssh cisco@192.168.56.101
        ```
    - Enter the following commands to enable RESTCONF:
        ```sh
        config t
        restconf
        exit
        ```

2. **Set up Postman**:
    - Open Postman.
    - Create a new GET request.

3. **Configure Headers in Postman**:
    - In the Headers area, add the following key/value pairs:
        - Key: `Content-Type`, Value: `application/yang-data+json`
        - Key: `Accept`, Value: `application/yang-data+json`

4. **Send the API request to the router**:
    - Set the URL to:
        ```sh
        https://192.168.56.101/restconf/data/ietf-restconf:restconf
        ```
    - Click `Send`.
    - Verify the JSON response from the router.

5. **Gather information for all interfaces on the router**:
    - Duplicate the GET request tab in Postman.
    - Set the URL to:
        ```sh
        https://192.168.56.101/restconf/data/ietf-interfaces:interfaces
        ```
    - Click `Send`.
    - Verify the JSON response from the router.

6. **Gather information for a specific interface on the router**:
    - Duplicate the GET request tab in Postman.
    - Set the URL to:
        ```sh
        https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1
        ```
    - Click `Send`.
    - Verify the JSON response from the router.

7. **Manually configure the interface on the router**:
    - Access the router via SSH:
        ```sh
        ssh cisco@192.168.56.101
        ```
    - Enter the following commands to configure the interface:
        ```sh
        config t
        interface GigabitEthernet1
        ip address 192.168.56.101 255.255.255.0
        end
        ```

8. **Verify the interface configuration**:
    - In Postman, send the GET request again to verify the updated JSON response.

9. **Create a Python script to send a GET request**:
    - Create a new file named `restconf-get.py`.
    - Add the following code to the script:
        ```python
        import json
        import requests
        requests.packages.urllib3.disable_warnings()

        api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces"
        headers = { "Accept": "application/yang-data+json", "Content-type":"application/yang-data+json" }
        basicauth = ("cisco", "cisco123!")

        resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
        print(resp)
        response_json = resp.json()
        print(json.dumps(response_json, indent=4))
        ```

    - Save and run the script:
        ```sh
        python3 restconf-get.py
        ```

10. **Create a Python script to send a PUT request**:
    - Create a new file named `restconf-put.py`.
    - Add the following code to the script:
        ```python
        import json
        import requests
        requests.packages.urllib3.disable_warnings()

        api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback2"
        headers = { "Accept": "application/yang-data+json", "Content-type":"application/yang-data+json" }
        basicauth = ("cisco", "cisco123!")

        yangConfig = {
            "ietf-interfaces:interface": {
                "name": "Loopback2",
                "description": "My second RESTCONF loopback",
                "type": "iana-if-type:softwareLoopback",
                "enabled": True,
                "ietf-ip:ipv4": {
                    "address": [
                        {
                            "ip": "10.2.1.1",
                            "netmask": "255.255.255.0"
                        }
                    ]
                },
                "ietf-ip:ipv6": {}
            }
        }

        resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
        if(resp.status_code >= 200 and resp.status_code <= 299):
            print("STATUS OK: {}".format(resp.status_code))
        else:
            print('Error. Status Code: {} \nError message: {}'.format(resp.status_code, resp.json()))
        ```

    - Save and run the script:
        ```sh
        python3 restconf-put.py
        ```

11. **Verify the new interface configuration**:
    - Access the router via SSH:
        ```sh
        ssh cisco@192.168.56.101
        ```
    - Enter the following command to verify the new interface:
        ```sh
        show ip interface brief
        ```

### Task Troubleshooting
1. If you encounter any issues with the RESTCONF requests, ensure that the router is configured correctly and that the RESTCONF service is enabled.

### Task Verification
1. **Response from the GET request**:
    ```sh
    python restconf-get.py 
    <Response [200]>
    {
        "ietf-interfaces:interfaces": {
            "interface": [
                {
                    "name": "GigabitEthernet1",
                    "description": "Configured by Netmiko",
                    "type": "iana-if-type:ethernetCsmacd",
                    "enabled": true,
                    "ietf-ip:ipv4": {},
                    "ietf-ip:ipv6": {}
                },
                {
                    "name": "GigabitEthernet1.10",
                    "type": "iana-if-type:ethernetCsmacd",
                    "enabled": false,
                    "ietf-ip:ipv4": {
                        "address": [
                            {
                                "ip": "192.168.10.1",
                                "netmask": "255.255.255.0"
                            }
                        ]
                    },
                    "ietf-ip:ipv6": {}
                },
                {
                    "name": "GigabitEthernet1.20",
                    "type": "iana-if-type:ethernetCsmacd",
                    "enabled": true,
                    "ietf-ip:ipv4": {
                        "address": [
                            {
                                "ip": "192.168.20.1",
                                "netmask": "255.255.255.0"
                            }
                        ]
                    },
                    "ietf-ip:ipv6": {}
                }
            ]
        }
    }
    ```

2. **Response from the PUT request**:
    ```sh
    python restconf-put.py 
    STATUS OK: 204
    ```

3. **Verify the new interface configuration on the router**:
    ```sh
    CSR1000v#show ip interface brief 
    Interface              IP-Address      OK? Method Status                Protocol
    GigabitEthernet1       192.168.56.101  YES DHCP   up                    up      
    GigabitEthernet1.10    192.168.10.1    YES manual administratively down down    
    GigabitEthernet1.20    192.168.20.1    YES manual up                    up      
    Loopback2              10.2.1.1        YES other  up                    up      
    CSR1000v#
    ```

    Sure, here is the documentation for Lab 7 using the provided format:

## Lab 7 Configure VLAN Membership Using NETCONF/YANG

### Preparation and Implementation
1. **Enable NETCONF/YANG on the router**:
    - Access the router via SSH:
        ```sh
        ssh cisco@192.168.56.101
        ```
    - Enter the following commands to enable NETCONF:
        ```sh
        config t
        netconf-yang
        exit
        ```

2. **Test the Transport**:
    - SSH to the device using the NETCONF port (830):
        ```sh
        ssh -p 830 cisco@192.168.56.101 -s netconf
        ```
    - Enter the password `cisco123!`.
    - Observe the XML response containing a `<hello>` message from the NETCONF device.

3. **Check the Capabilities**:
    - Respond to the hello message by pasting the following XML code into the SSH session:
        ```xml
        <?xml version="1.0" encoding="UTF-8"?>
        <hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <capabilities>
          <capability>urn:ietf:params:netconf:base:1.0</capability>
        </capabilities>
        </hello>]]>]]>
        ```

4. **Use a NETCONF Tool**:
    - Download and set up netconf-console from [GitHub](https://github.com/OpenNetworkingFoundation/configuration/tree/master/netconf-console).
    - Rename the file to `netconf-console.py`.
    - Edit the file to change the default username, password, and port if needed.
    - Run the hello operation:
        ```sh
        ./netconf-console.py --host=192.168.56.101 -u cisco -p cisco123! --port 830 --hello
        ```
    - Run the get-config command:
        ```sh
        ./netconf-console.py --host=192.168.56.101 -u cisco -p cisco123! --port 830 --get-config
        ```

5. **Customize Responses Using Pretty-Print**:
    - Use an XML formatter to get a structured view of the response. You can use online tools like [XML Formatter](https://www.freeformatter.com/xml-formatter.html) or local tools like `xmllint`:
        ```sh
        echo '<your-xml-response>' | xmllint --format -
        ```

6. **Understand RPC Calls**:
    - Send an RPC get-config command by pasting the following XML code into the SSH session:
        ```xml
        <?xml version="1.0"?>
        <rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101">
        <get-config>
        <source>
        <running/>
        </source>
        </get-config>
        </rpc>]]>]]>
        ```

7. **Grasp the Concept of Structured Data**:
    - Use filters to specify a subset of the configuration:
        ```sh
        ./netconf-console.py --host=192.168.56.101 -u cisco -p cisco123! --port 830 --get-config -x "interfaces"
        ```
    - Use filters to get the configuration of a specific interface:
        ```sh
        ./netconf-console.py --host=192.168.56.101 -u cisco -p cisco123! --port 830 --get-config -x "interfaces/interface[name='GigabitEthernet1']"
        ```
    - Use filters to get the description attribute for a specific interface:
        ```sh
        ./netconf-console.py --host=192.168.56.101 -u cisco -p cisco123! --port 830 --get-config -x "interfaces/interface[name='GigabitEthernet1']/description"
        ```
    - Use filters to get the description for all interfaces:
        ```sh
        ./netconf-console.py --host=192.168.56.101 -u cisco -p cisco123! --port 830 --get-config -x "interfaces/interface/description"
        ```

8. **Configure VLAN Membership**:
    - Get the configuration of a specific interface using the native model:
        ```sh
        ./netconf-console.py --host=192.168.56.101 -u cisco -p cisco123! --port 830 --get-config -x "native/interface/GigabitEthernet[name='1']"
        ```

    - Create a file with the changes to be made:
        ```xml
        <!-- filepath: /home/cow/school/networking/pe/Lab_7/edit -->
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
          <interface>
            <GigabitEthernet>
              <name>1</name>
              <description>Configured by NETCONF</description>
              <ip>
                <address>
                  <primary>
                    <address>192.168.56.101</address>
                    <mask>255.255.255.0</mask>
                  </primary>
                </address>
              </ip>
            </GigabitEthernet>
          </interface>
        </native>
        ```

    - Apply the changes using the edit-config RPC:
        ```sh
        netconf-console2 --host=192.168.56.101 -u cisco -p cisco123! --port 830 --edit-config=edit
        ```

    - Verify the VLAN configuration:
        ```sh
        netconf-console2 --host=192.168.56.101 -u cisco -p cisco123! --port 830 --get-config -x "native/interface/GigabitEthernet[name='1']"
        ```

### Task Troubleshooting
1. **Verify NETCONF is Enabled**:
    - Ensure NETCONF is enabled on the router:
        ```sh
        show running-config | include netconf
        ```
    - If NETCONF is not enabled, enable it:
        ```sh
        config t
        netconf-yang
        exit
        ```

2. **Check Network Connectivity**:
    - Ensure that the DEVASC VM can reach the router on the NETCONF port (830):
        ```sh
        nc -zv 192.168.56.101 830
        ```

3. **Restart the NETCONF Service**:
    - Restart the NETCONF service if needed:
        ```sh
        config t
        no netconf-yang
        netconf-yang
        exit
        ```

### Task Verification
1. **Response from the Hello Command**:
    ```sh
    netconf-console2 --host=192.168.56.101 -u cisco -p cisco123! --port 830 --hello | tail
    ```

    Example output:
    ```xml
    <nc:capability>urn:ietf:params:xml:ns:yang:smiv2:TUNNEL-MIB?module=TUNNEL-MIB&amp;revision=2005-05-16</nc:capability>
    <nc:capability>urn:ietf:params:xml:ns:yang:smiv2:UDP-MIB?module=UDP-MIB&amp;revision=2005-05-20</nc:capability>
    <nc:capability>urn:ietf:params:xml:ns:yang:smiv2:VPN-TC-STD-MIB?module=VPN-TC-STD-MIB&amp;revision=2005-11-15</nc:capability>
    <nc:capability>urn:ietf:params:xml:ns:netconf:base:1.0?module=ietf-netconf&amp;revision=2011-06-01</nc:capability>
    <nc:capability>urn:ietf:params:xml:ns:yang:ietf-netconf-with-defaults?module=ietf-netconf-with-defaults&amp;revision=2011-06-01</nc:capability>
    <nc:capability>
        urn:ietf:params:netconf:capability:notification:1.1
      </nc:capability>
    </nc:capabilities>
    </nc:hello>
    ```

2. **Response from the Get-Config Command**:
    ```sh
    netconf-console2 --host=192.168.56.101 -u cisco -p cisco123! --port 830 --get-config | head
    ```

    Example output:
    ```xml
    <?xml version='1.0' encoding='UTF-8'?>
    <data xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <version>16.9</version>
        <boot-start-marker/>
        <boot-end-marker/>
        <banner>
          <motd>
            <banner>^C</banner>
          </motd>
        </banner>
    ```

3. **Response from the Filtered Get-Config Command**:
    ```sh
    netconf-console2 --host=192.168.56.101 -u cisco -p cisco123! --port 830 --get-config -x "interfaces" | tail
    ```

    Example output:
    ```xml
      <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
          <ip>10.2.1.1</ip>
          <netmask>255.255.255.0</netmask>
        </address>
      </ipv4>
      <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
    </interface>
  </interfaces>
</data>
    ```

4. **Response from the Specific Interface Get-Config Command**:
    ```sh
    netconf-console2 --host=192.168.56.101 -u cisco -p cisco123! --port 830 --get-config -x "interfaces/interface[name='GigabitEthernet1']" | head
    ```

    Example output:
    ```xml
    <?xml version='1.0' encoding='UTF-8'?>
    <data xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
      <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
          <name>GigabitEthernet1</name>
          <config>
            <name>GigabitEthernet1</name>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
            <description>Configured by Netmiko</description>
            <enabled>true</enabled>
    ```

5. **Response from the Description Get-Config Command**:
    ```sh
    netconf-console2 --host=192.168.56.101 -u cisco -p cisco123! --port 830 --get-config -x "interfaces/interface[name='GigabitEthernet1']/description"
    ```

    Example output:
    ```xml
    <?xml version='1.0' encoding='UTF-8'?>
    <data xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <name>GigabitEthernet1</name>
          <description>Configured by Netmiko</description>
        </interface>
      </interfaces>
    </data>
    ```

6. **Response from the All Descriptions Get-Config Command**:
    ```sh
    netconf-console2 --host=192.168.56.101 -u cisco -p cisco123! --port 830 --get-config -x "interfaces/interface/description"
    ```

    Example output:
    ```xml
    <?xml version='1.0' encoding='UTF-8'?>
    <data xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <name>GigabitEthernet1</name>
          <description>Configured by Netmiko</description>
        </interface>
        <interface>
          <name>Loopback2</name>
          <description>My second RESTCONF loopback</description>
        </interface>
      </interfaces>
    </data>
    ```

7. **Response from the Native Model Get-Config Command**:
    ```sh
    netconf-console2 --host=192.168.56.101 -u cisco -p cisco123! --port 830 --get-config -x "native/interface/GigabitEthernet[name='1']"
    ```

    Example output:
    ```xml
    <?xml version='1.0' encoding='UTF-8'?>
    <data xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
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
        </interface>
      </native>
    </data>
    ```

8. **Response from the Edit-Config Command**:
    ```sh
    netconf-console2 --host=192.168.56.101 -u cisco -p cisco123! --port 830 --edit-config=edit
    ```

    Example output:
    ```xml
    <rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101">
      <ok/>
    </rpc-reply>
    ```

# Networking Expert
## Lab 8 NETCONF/YANG

### Preparation and Implementation
1. **Create a Python Virtual Environment**  
   - From your project directory, create and activate a virtual environment:  
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Install any required libraries (e.g., ncclient):  
     ```sh
     pip install ncclient
     ```

2. **Use NCC (NETCONF Client) to Connect to the Router**  
   - Clone or download the NCC script (e.g., ncc.py).  
   - Make it executable and run a basic get-config command:
     ```sh
     chmod +x ncc.py
     ./ncc.py --host 192.168.56.101 --get-running
     ```
   - Observe the XML `<data>` returned by the router.

3. **Understand and Apply Structured Data**  
   - Explore how YANG models map to XML. Look for containers (single-instance data structures) and lists (multi-instance data structures).  
   - Example command to filter interface data:
     ```sh
     ./ncc.py --host 192.168.56.101 --get-running -x '/interfaces/interface'
     ```

4. **Use Filters, RPC Calls, and Actions**  
   - Apply an XPath filter to retrieve a single interface:
     ```sh
     ./ncc.py --host 192.168.56.101 --get-running -x '/native/interface/GigabitEthernet[name="1"]'
     ```
   - Note how the response focuses on just the requested interface.

5. **Differentiate Between Operational and Configuration Data**  
   - Operational data (statistics or status) is read-only. Example:
     ```sh
     ./ncc.py --host 192.168.56.101 --get-operational -x '/interfaces-state/interface[name="GigabitEthernet1"]'
     ```
   - Configuration data can be changed. Example:
     ```sh
     ./ncc.py --host 192.168.56.101 --get-running -x '/native/interface'
     ```

6. **Make Configuration Changes Using the NCC Client**  
   - Create or edit an XML file (e.g., edit-vlan.xml) to configure a VLAN:
     ```xml
     <!-- filepath: /home/user/networking/lab8/edit-vlan.xml -->
     <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
       <interface>
         <GigabitEthernet>
           <name>1/0/9</name>
           <switchport>
             <access>
               <vlan>
                 <vlan>20</vlan>
               </vlan>
             </access>
           </switchport>
         </GigabitEthernet>
       </interface>
     </native>
     ```
   - Apply the changes:
     ```sh
     ./ncc.py --host 192.168.56.101 --edit-config -f edit-vlan.xml
     ```

### Task Troubleshooting
1. **Connection Issues**  
   - If you see “Could not open socket,” verify NETCONF is enabled on port 830 and check firewall settings:
     ```sh
     nc -zv 192.168.56.101 830
     ```
   - Confirm your router config:
     ```sh
     show running-config | include netconf
     ```

2. **XML Namespace or Unknown Element Errors**  
   - Verify the correct namespace in your XML payload.  
   - Retrieve capabilities:
     ```sh
     ./ncc.py --host 192.168.56.101 --hello
     ```
   - Adjust your XML namespaces to match the advertised capabilities.

### Task Verification
1. **Review Filtered Output**  
   - Run a filtered get-config:
     ```sh
     ./ncc.py --host 192.168.56.101 --get-running -x '/native/interface/GigabitEthernet[name="1/0/9"]'
     ```
   - Confirm the interface is configured with VLAN 20:
     ```xml
     <GigabitEthernet>
       <name>1/0/9</name>
       <switchport>
         <access>
           <vlan>
             <vlan>20</vlan>
           </vlan>
         </access>
       </switchport>
     </GigabitEthernet>
     ```

2. **Check Operational Data**  
   - Retrieve interface state to ensure it is up:
     ```sh
     ./ncc.py --host 192.168.56.101 --get-operational -x '/interfaces-state/interface[name="GigabitEthernet1/0/9"]'
     ```
   - Confirm it returns status and statistics, indicating the interface is operational.