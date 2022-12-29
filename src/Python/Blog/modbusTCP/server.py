from pyModbusTCP.server import ModbusServer
from datetime import datetime


class ModbusTCPServer():

    def __init__(self, ipaddress="127.0.0.1", port=12345):
        self.__ipaddress = ipaddress
        self.__port = port
        self.__server = ModbusServer(ipaddress, port, no_block=True)
        pass

    @property
    def get_nowtime(self):
        """ ログ用のタイムスタンプ """
        return datetime.now()

    @property
    def get_ipaddress(self):
        """ サーバーのIPアドレスを取得する """
        return self.__ipaddress

    @property
    def get_port(self):
        """ サーバーのポートを取得する """
        return self.__port

    def start_server(self):
        """ サーバーを起動する """
        print(f"{self.get_nowtime} Start ModbusTCP Server")
        return self.__server.start()

    def stop_server(self):
        """ サーバーを停止する """
        print(f"{self.get_nowtime} Stop ModbusTCP Server")
        return self.__server.stop()

    def get_holding_registers(self, address, num=1):
        """ 保持レジスターの値を取得する """
        value = self.__server.data_bank.get_holding_registers(address, number=num)
        print(f"{self.get_nowtime} [server] get_holding_registers[address:{address}]: {value}")
        return value

    def set_holding_registers(self, address, value):
        """ 保持レジスターの値を設定する """
        print(f"{self.get_nowtime} [server] set_holding_registers[address:{address}]: {[value]}")
        return self.__server.data_bank.set_holding_registers(address, [value])

