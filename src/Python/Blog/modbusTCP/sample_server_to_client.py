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
# address=0の値が[0]の初期値である事を確認する
modbus_client.read_holding_registers(address=0)
time.sleep(2)
# address=0の値に23をセットします。
modbus_server.set_holding_registers(address=0, value=23)
time.sleep(2)
# address=0の値が23に更新されている事を確認する
modbus_client.read_holding_registers(address=0)

# 書き換えるaddress=1に変更しても同じ動作をするか確認する
modbus_client.read_holding_registers(address=1)
modbus_server.set_holding_registers(address=1, value=25)
time.sleep(2)
modbus_client.read_holding_registers(address=1)

# address=1に別の値を上書きする
modbus_server.set_holding_registers(address=1, value=20)
time.sleep(2)
modbus_client.read_holding_registers(address=1)

print(f"{modbus_client.get_nowtime} from client to server connected state:{modbus_client.get_connect_state}")
modbus_client.disconnect_to_server()
print(f"{modbus_client.get_nowtime} from client to server connected state:{modbus_client.get_connect_state}")
# modbusTCPサーバーを終了させる
modbus_server.stop_server()
