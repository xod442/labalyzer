
from pyaoscx.session import Session
# Switch details
switch = '10.250.203.203'
version = "10.09"
switch_user = 'admin'
switch_password = 'admin'
# Command to be sent
command = 'show version'

# Initialize the session
switch = str(switch)

s = Session(switch, version)
print(s)
s.open(switch_user, switch_password, use_proxy=False)

'''
session = connect(switch_ip, version, switch_user, switch_password)

try:
    # Open connection to the switch
    session.open()

    # Send command
    response = session.get('/cli', command=command)

    # Print the response
    print(response)

except GenericOperationError as e:
    print("Could not send command: {}".format(e.message))

finally:
    # Close the connection
    switch.close()
'''
