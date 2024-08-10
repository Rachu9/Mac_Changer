import subprocess
interface=input("Interface")
new_mac=input("New_mac")
print("Changing Mac address "+interface +"to"+new_mac)

subprocess.run("ifconfig"+interface+"down",shell=True)
subprocess.run("ifconfig"+interface+"hw ether"+new_mac,shell=True)
subprocess.run("ifconfig"+interface+"up",shell=True)
