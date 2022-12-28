from server import ModbusTCPServer
from client import ModbusTCPClient
import time

ipaddress = "127.0.0.1"
port = 12345

modbus_server = ModbusTCPServer(ipaddress=ipaddress, port=port)
modbus_client = ModbusTCPClient(ipaddress=ipaddress, port=port)

print(f"{modbus_client.get_nowtime} from client to server connected state:{modbus_client.get_connect_state}")
# modbusTCPサーバーを立ち上げる
modbus_server.start_server()
modbus_client.connect_to_server()
print(f"{modbus_client.get_nowtime} from client to server connected state:{modbus_client.get_connect_state}")

modbus_server.get_holding_registers(address=0)
# address=0の値が[0]の初期値である事を確認する
modbus_client.write_single_register(address=0, value=122)
time.sleep(2)
modbus_server.get_holding_registers(address=0)

modbus_server.get_holding_registers(address=1)
# address=0の値が[0]の初期値である事を確認する
modbus_client.write_multiple_registers(address=1, value=[1, 2, 3])
time.sleep(2)
modbus_server.get_holding_registers(address=1, num=3)

print(f"{modbus_client.get_nowtime} from client to server connected state:{modbus_client.get_connect_state}")
modbus_client.disconnect_to_server()
print(f"{modbus_client.get_nowtime} from client to server connected state:{modbus_client.get_connect_state}")
# modbusTCPサーバーを終了させる
modbus_server.stop_server()
