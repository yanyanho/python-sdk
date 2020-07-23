# template for codegen
from client.bcosclient import (
    BcosClient
)
from client.datatype_parser import DatatypeParser
import json


class HelloEvent:  # name of abi
    address = None
    contract_abi_string = '''[{"constant": false, "inputs": [{"name": "n", "type": "string"}, {"name": "i", "type": "int256"}, {"name": "key", "type": "string"}], "name": "settwo", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"name": "n", "type": "string"}], "name": "set", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "get", "outputs": [{"name": "", "type": "string"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"name": "n", "type": "string"}, {"name": "i", "type": "bool"}], "name": "setbool", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"name": "n", "type": "string"}, {"name": "i", "type": "int256"}], "name": "setnum", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": false, "inputs": [{"indexed": false, "name": "newname", "type": "string"}], "name": "on_set", "type": "event", "topic": "0xc86dd792cb0df852949fd9d6a7b5a0d8b1cd57ba9066ad4c8da6a1e5c51c9b9a"}, {"anonymous": false, "inputs": [{"indexed": false, "name": "name", "type": "string"}, {"indexed": true, "name": "age", "type": "int256"}], "name": "on_number", "type": "event", "topic": "0x5b6dab5d6200c978aea486370c307cd2e56212d2cd7326b6879fe6a32dd1dc15"}, {"anonymous": false, "inputs": [{"indexed": false, "name": "name", "type": "string"}, {"indexed": true, "name": "age", "type": "int256"}, {"indexed": true, "name": "key", "type": "string"}], "name": "on_two_indexed", "type": "event", "topic": "0x3913a7a6879be541cb82067407c4976bdf08f9243ea1f2da9b552e490484f7d0"}, {"anonymous": false, "inputs": [{"indexed": false, "name": "addr", "type": "address"}], "name": "on_address", "type": "event", "topic": "0x23ec7e97005133e2ecacfedd26b164f27c5b90bc5fe00a552a4c54eeeea8b40c"}]'''
    contract_abi = None
    data_parser = DatatypeParser()
    client = None

    def __init__(self, address):
        self.client = BcosClient()
        self.address = address
        self.contract_abi = json.loads(self.contract_abi_string)
        self.data_parser.set_abi(self.contract_abi)

    def deploy(self, contract_bin_file):
        result = self.client.deployFromFile(contract_bin_file)
        self.address = result["contractAddress"]
        return result

    # ------------------------------------------
    def settwo(self, n, i, key):
        func_name = 'settwo'
        args = [n, i, key]
        receipt = self.client.sendRawTransactionGetReceipt(self.address, self.contract_abi, func_name, args)
        outputresult = self.data_parser.parse_receipt_output(func_name, receipt['output'])
        return outputresult, receipt

    # ------------------------------------------
    def set(self, n):
        func_name = 'set'
        args = [n]
        receipt = self.client.sendRawTransactionGetReceipt(self.address, self.contract_abi, func_name, args)
        outputresult = self.data_parser.parse_receipt_output(func_name, receipt['output'])
        return outputresult, receipt

    # ------------------------------------------
    def get(self):
        func_name = 'get'
        args = []
        result = self.client.call(self.address, self.contract_abi, func_name, args)
        return result

    # ------------------------------------------
    def setbool(self, n, i):
        func_name = 'setbool'
        args = [n, i]
        receipt = self.client.sendRawTransactionGetReceipt(self.address, self.contract_abi, func_name, args)
        outputresult = self.data_parser.parse_receipt_output(func_name, receipt['output'])
        return outputresult, receipt

    # ------------------------------------------
    def setnum(self, n, i):
        func_name = 'setnum'
        args = [n, i]
        receipt = self.client.sendRawTransactionGetReceipt(self.address, self.contract_abi, func_name, args)
        outputresult = self.data_parser.parse_receipt_output(func_name, receipt['output'])
        return outputresult, receipt
