from contracts.ERC20Mintable import ERC20Mintable
import sys

print(sys.path)
si = ERC20Mintable("")
result = si.deploy("contracts/ERC20Mintable.bin")
address = result['contractAddress']
print("new address = ", address)

#address = "0x7b6cb85c667c6ec8a4d81be837270ddfcf1838d5"
erc20mintable = ERC20Mintable(address)
(outputresult, receipt) = erc20mintable.mint("0xF0109fC8DF283027b6285cc889F5aA624EaC1F55",1000)
# outputresult  = si.data_parser.parse_receipt_output("set", receipt['output'])
print("receipt output :", outputresult)
logresult = erc20mintable.data_parser.parse_event_logs(receipt["logs"])
i = 0
for log in logresult:
    if 'eventname' in log:
        i = i + 1
        print("{}): log name: {} , data: {}".format(i, log['eventname'], log['eventdata']))
print(erc20mintable.balanceOf("0xF0109fC8DF283027b6285cc889F5aA624EaC1F55"))
