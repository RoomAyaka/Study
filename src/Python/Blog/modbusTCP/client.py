from pyModbusTCP.client import ModbusClient
from datetime import datetime
import time


class ModbusTCPClient():

    def __init__(self, ipaddress="127.0.0.1", port=12345):
        self.__client = ModbusClient(host=ipaddress, port=port)
        pass

    @property
    def get_nowtime(self):
        """ ログ用のタイムスタンプ """
        return datetime.now()

    @property
    def get_connect_state(self):
        """ サーバーとの接続状態を確認する """
        return self.__client.is_open

    def connect_to_server(self, sec=10):
        """ サーバーとの接続を試みる """
        i = 0
        while i < sec:
            result = self.__client.open()
            print(f"{self.get_nowtime} Connect: Success !!")
            if result:
                break
            else:
                i += 1
                time.sleep(1)

    def disconnect_to_server(self, sec=10):
        """ サーバーとの切断を試みる """
        i = 0
        while i < sec:
            result = self.__client.close()
            if not result:
                print(f"{self.get_nowtime} Disconnect: Success !!")
                break
            else:
                i += 1
                time.sleep(1)

    def read_holding_registers(self, address):
        """ 保持レジスターの値を取得する """
        value = self.__client.read_holding_registers(address)
        print(f"{self.get_nowtime} [client] read_holding_registers[address:{address}]: {value}")

    def write_single_register(self, address, value):
        """ シングルレジスターに値を設定する """
        print(f"{self.get_nowtime} [client] write_single_register[address:{address}]: {value}")
        return self.__client.write_single_register(address, value)

    def write_multiple_registers(self, address, value: list):
        """ マルチレジスターに値を設定する """
        print(f"{self.get_nowtime} [client] write_multiple_registers[address:{address}]: {value}")
        return self.__client.write_multiple_registers(address, value)
