# Author: Santiago Gil

import time
from pymodbus.client.sync import ModbusTcpClient
unit = 0x41
t_diameter_register = 0x0000
t_speed_register = 0x0002
t_control_register = 0x0003
t_force_register = 0x0004

client = ModbusTcpClient(host='192.168.1.101', port=502)
client.connect()
print(client.is_socket_open())


applied_force = client.read_holding_registers(address=0x0201, unit=unit)
actual_diameter = client.read_holding_registers(address=0x0101, unit=unit)
print(applied_force.registers)
print(actual_diameter.registers)

time.sleep(0.5)
client.write_register(t_diameter_register, 0)
client.write_register(t_speed_register, 10)
client.write_register(t_force_register, 1000)
client.write_register(0x0003, 1)
time.sleep(0.5)
#client.write_register(0x0003, 1)
#time.sleep(0.5)
client.write_register(t_diameter_register, 710)
client.write_register(t_speed_register, 10)
client.write_register(t_force_register, 20)
client.write_register(0x0003, 1)
#time.sleep(0.5)
#client.write_register(0x0003, 1)
