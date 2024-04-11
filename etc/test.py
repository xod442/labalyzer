import urllib3
from utility.workflow3 import find_version
import time
from utility.write_line import write_line
from utility.workflow3 import get_switches
from utility.workflow3 import lldp
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
switch_list = ['10.250.201.101']
counter = 0
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

line ='======================================================================='
print(line)
write_line(line)
line ="                       Switch LLDP                          "
print(line)
write_line(line)


for switch in switch_list:
    switch_lldp = lldp(switch, version, switch_user, switch_password)
    line ='-------------------------------------------------------------------'
    print(line)
    write_line(line)
    line ="Switch lldp info {}.".format(switch_iidp)
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
