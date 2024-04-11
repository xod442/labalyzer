import urllib3
from utility.workflow3 import find_version
import time
from utility.write_line import write_line
from utility.workflow3 import get_switches
from utility.workflow3 import get_lldp
import utility.nic2dvs as nic
from pyVmomi import vim
from pyVim.task import WaitForTask
from pyVim.connect import SmartConnect, Disconnect
import ssl
from utility.vm_watcher import vm_watcher


# There are two approaches to workflows, both using the session.
version = "10.09"
switch_user = 'admin'
switch_password = 'admin'

switch_list = [\
'10.250.201.101','10.250.201.102','10.250.201.103'\
,'10.250.202.101','10.250.202.102','10.250.202.103'\
,'10.250.203.101','10.250.203.102','10.250.203.103'\
,'10.250.204.101','10.250.204.102','10.250.204.103'\
,'10.250.205.101','10.250.205.102','10.250.205.103'\

,'10.250.206.101','10.250.206.102','10.250.206.103'\
,'10.250.207.101','10.250.207.102','10.250.207.103'\
,'10.250.208.101','10.250.208.102','10.250.208.103'\
,'10.250.209.101','10.250.209.102','10.250.209.103'\
,'10.250.210.101','10.250.210.102','10.250.210.103'\
]

counter = 0
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

line ='======================================================================='
print(line)
write_line(line)
line ="                       Switch Up and Version                           "
print(line)
write_line(line)


for switch in switch_list:
    switch_version = find_version(switch, version, switch_user, switch_password)
    line ='-------------------------------------------------------------------'
    print(line)
    write_line(line)
    line ="{} Switch is up and alive, running version {}.".format(switch, switch_version)
    print(line)
    write_line(line)
    counter = counter + 1
    time.sleep(1)
line ="Total number of switches processed {}.".format(counter)
print(line)
write_line(line)
line ='======================================================================='
print(line)
write_line(line)

#                AFC SECTION

# There are two approaches to workflows, both using the session.
version = "10.09"
afc_user = 'admin'
afc_password = 'admin'
serno = open('serial.txt','w')
cr = '\n'

afc_list = ['10.250.201.11','10.250.202.11','10.250.203.11','10.250.204.11','10.250.205.11',\
'10.250.206.11','10.250.207.11','10.250.208.11','10.250.209.11','10.250.210.11']
# afc_list = ['10.250.201.11']
counter = 0
c = ','
line = '======================================================================='
print(line)
write_line(line)
line = "                       AFC / Switch Check                              "
print(line)
write_line(line)

counter = 0
for afc_ip in afc_list:
    base_url = "https://{0}/api/v1/".format(afc_ip)
    line = "======------------AFC INFO -------------================================="
    print(line)
    write_line(line)

    line = "{} is the baseurl.".format(base_url)
    print(line)
    write_line(line)

    switches = get_switches(base_url, afc_user, afc_password)
    for s in switches:
        line = "{} Switch is discovered, and it's status is {}.".format(s['ip_address'], s['status'])
        print(line)
        write_line(line)
        inventory = str(s['name'])+c+str(s['description'])+c+str(s['mac_address'])+c+str(s['ip_address'])+c+str(s['sw_version'])+c+str(s['serial_number'])
        serno.write(inventory)
        serno.write(cr)
    #print('-------------------------------------------------------------------')
    #print("{} Switch is up and alive, running version {}.".format(switch, switch_version))
    counter = counter + 1
    #time.sleep(1)
#print("Total number of switches processed {}.".format(counter))
line = '=======================  END AFC CHECK  ==============================='
print(line)
write_line(line)
serno.close()

#     VMWARE Section


 #There are two approaches to workflows, both using the session.
version = "10.09"
switch_user = 'admin'
switch_password = 'admin'
vsphere_ip = '10.250.0.50'
vsphere_user = 'administrator@vsphere.local'
vsphere_pass = 'Aruba123!@#'

workload_list = ['LG01-WL01-V10-101','LG01-WL02-V10-102','LG01-WL03-V20-101','LG02-WL01-V10-101','LG02-WL02-V10-102',\
'LG02-WL03-V20-101','LG03-WL01-V10-101','LG03-WL02-V10-102','LG03-WL03-V20-101','LG04-WL01-V10-101',\
'LG04-WL02-V10-102','LG04-WL03-V20-101','LG05-WL01-V10-101','LG05-WL02-V10-102','LG05-WL03-V20-101',\
'LG06-WL01-V10-101','LG06-WL02-V10-102','LG06-WL03-V20-101','LG07-WL01-V10-101','LG07-WL02-V10-102',\
'LG07-WL03-V20-101','LG08-WL01-V10-101','LG08-WL02-V10-102','LG08-WL03-V20-101','LG09-WL01-V10-101',\
'LG09-WL02-V10-102','LG09-WL03-V20-101','LG10-WL01-V10-101','LG10-WL02-V10-102','LG10-WL03-V20-101']
#workload_list = ['LG01-WL01-V10-101']
dvs_list = ['LG01-dvs-1','LG01-dvs-2','LG02-dvs-1','LG02-dvs-2','LG03-dvs-1','LG03-dvs-2','LG04-dvs-1','LG04-dvs-2',\
'LG05-dvs-1','LG05-dvs-2','LG06-dvs-1','LG06-dvs-2','LG07-dvs-1','LG07-dvs-2','LG08-dvs-1','LG08-dvs-2','LG09-dvs-1','LG09-dvs-2',\
'LG10-dvs-1','LG10-dvs-2']

afc_name_list = ['LG01-AFC','LG02-AFC','LG03-AFC','LG04-AFC','LG05-AFC','LG06-AFC','LG07-AFC','LG08-AFC','LG09-AFC','LG10-AFC']
# afc_name_list = ['LG01-AFC']
psm_name_list = ['LG01-PSM','LG02-PSM','LG03-PSM','LG04-PSM','LG05-PSM','LG06-PSM','LG07-PSM','LG08-PSM','LG09-PSM','LG10-PSM',]
# psm_name_list = ['LG01-PSM']
sslContext = ssl._create_unverified_context()

port="443"
# Create a connector to vsphere
service_instance = SmartConnect(
                    host=vsphere_ip,
                    user=vsphere_user,
                    pwd=vsphere_pass,
                    port=port,
                    sslContext=sslContext
)
content = service_instance.RetrieveContent()

counter = 0
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#========================================================
# Process Workloads
#=========================================================

line = '======================================================================='
print(line)
write_line(line)
line = "                       VMware / Virtual Health                         "
print(line)
write_line(line)
line = '======================================================================='
print(line)
write_line(line)

for load in workload_list:
    response = vm_watcher(content, load)
    counter = counter + 1
print("automation has detected {} workloads!.".format(counter))



#========================================================
# Process DVSwitches
#=========================================================
counter = 0
line = '======================================================================='
print(line)
write_line(line)
line = "            VMware / Distributed Virtual Switches                        "
print(line)
write_line(line)
line = '======================================================================'
print(line)
write_line(line)

for dvs in dvs_list:
    dvs_switch = nic.find_dvs_by_name(content,dvs)
    line = "Distributed Virtual Switch has been found: {}.".format(dvs_switch.name)
    print(line)
    write_line(line)
    counter = counter + 1
    line = "automation has detected {} healthy DVswitches!.".format(counter)
line = '======================================================================='
print(line)
write_line(line)

#========================================================
# Process AFC
#=========================================================
counter = 0
for afc in afc_name_list:
    response = vm_watcher(content, afc)
    counter = counter + 1

line = "automation has detected {} AFC workloads!.".format(counter)
print(line)
write_line(line)
line = '======================================================================='
print(line)
write_line(line)

#========================================================
# Process PSM
#=========================================================
counter = 0
for psm in psm_name_list:
    response = vm_watcher(content, psm)
    counter = counter + 1

line = "automation has detected {} psm workloads!.".format(counter)
print(line)
write_line(line)
line = '======================================================================='
print(line)
write_line(line)
