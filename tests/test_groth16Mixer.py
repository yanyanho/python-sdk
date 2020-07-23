import sys

from client.bcosclient import BcosClient
from utils.contracts import encode_abi

from client.common.transaction_common import TransactionCommon
from eth_utils import add_0x_prefix, to_checksum_address
from utils.contracts import (
    encode_transaction_data,

)
from contracts.ERC20Mintable import ERC20Mintable
from contracts.Groth16Mixer import Groth16Mixer

si = ERC20Mintable("")

result = si.deploy("contracts/ERC20Mintable.bin")
address = result['contractAddress']
address = to_checksum_address(address)
print("new token address = ", address)


si1 = Groth16Mixer("")
t1 = [16483624808830139117766005204006999845999393770666960505987166774116637665999, 15253936697195453458829704583528307376312090566175390614587367387882742888799]
t2 = [44284375965535255079801546243344002941596092908842750679505529109882140766, 11233183866282701416902842220398187526010682123304678142269318052114672666546]
t3 = [9975131970349417387454290174223382296463371611384079201194338159523411969581, 2836898428783494084355965442200696991005913320682471111065246558592301381311]
t4 = [9012277824718376381708077833555069935024430531058406360274230750681719039405, 18190687865858218001240874594336155036798710042113506844146290795387291588304]
t5 = [17798233959403027396420681547231945946145872783571600213811511589402431785080, 11217575595290996252585082378889649247766308217470417842352099180694760290188]
t6 = [13127546870442545011329176149454856901858462444541631023772933727095126529058, 19404375304354975644607334439648861444889263700940827808535214165647741300489, 7343011947856741308665292820167543015926418084154235912896839265227063475033, 9453663051630548672460758115379738986086323263715023634810574618860824165649, 10496397454998568476919935796689319286841216134974193457788117232365204626258, 11284352140683880343219250416670805942308406063791636940567376665512284052292, 17017594587165963191916060512316029390223787071785433187962067889654085091307, 19758759260873392541342276698014494472625895047987621107563834072318625381206, 8406307591444443375641072935994568035140518660841560151667202202813333885586, 5410830339934220399520427973486934263275622363479939517966013346779825897558, 16445114304315291249248248939147540565726925385944823187367299037813648954755, 3221459929655206232033643211703182348049561169738000403197310192344333897587, 20646682408467610111202194704403498169538806050581274032158885964904048419809, 11513380394743681123603185762855885450188409910128452969151184039101786105503, 16997502938391560880601578169553651092656671673592231136010407878532484008107, 13341125156553104272973835991394926394157444151712334543687551476437070936247, 7657410784579699053919494258956230966569350740250871130025214375144683745585, 15505388359419626992414275582583840166300945266511135060834671458795528295132, 6052746551364842597375684973752628633468284022556264989735303124812075848535, 12662727174561814448494408062186338092403379116204770936971191877512919408352]
fn_args = [32, address, t1, t2, t3, t4, t5, t6]

abi = [
                   {"inputs":
                        [
                   {"internalType": "uint256", "name": "mk_depth", "type": "uint256"},
                   {"internalType": "address", "name": "token", "type": "address"},
                   {"internalType": "uint256[2]", "name": "Alpha", "type": "uint256[2]"},
                   {"internalType": "uint256[2]", "name": "Beta1", "type": "uint256[2]"},
                   {"internalType": "uint256[2]", "name": "Beta2", "type": "uint256[2]"},
                   {"internalType": "uint256[2]", "name": "Delta1", "type": "uint256[2]"},
                   {"internalType": "uint256[2]", "name": "Delta2", "type": "uint256[2]"},
                   {"internalType": "uint256[]", "name": "ABC_coords", "type": "uint256[]"}],
        "payable": False, "stateMutability": "nonpayable", "type": "constructor"},
       {"anonymous": False, "inputs": [{"indexed": False, "internalType": "string", "name": "message", "type": "string"}], "name": "LogDebug", "type": "event"},
      {"anonymous": False, "inputs": [{"indexed": False, "internalType": "bytes32", "name": "message", "type": "bytes32"}], "name": "LogDebug", "type": "event"},
      {"anonymous": False, "inputs": [{"indexed": False, "internalType": "bytes32", "name": "root", "type": "bytes32"},
                                      {"indexed": False, "internalType": "bytes32[2]", "name": "nullifiers", "type": "bytes32[2]"},
                                      {"indexed": False, "internalType": "bytes32[2]", "name": "commitments", "type": "bytes32[2]"},
                                      {"indexed": False, "internalType": "bytes[2]", "name": "ciphertexts", "type": "bytes[2]"}], "name": "LogMix", "type": "event"},
    {"constant": True, "inputs": [{"internalType": "uint256[9]", "name": "primary_inputs", "type": "uint256[9]"}], "name": "assemble_hsig", "outputs": [{"internalType": "bytes32", "name": "hsig", "type": "bytes32"}], "payable": False, "stateMutability": "pure", "type": "function"},
    {"constant": True, "inputs": [{"internalType": "uint256", "name": "index", "type": "uint256"}, {"internalType": "uint256[9]", "name": "primary_inputs", "type": "uint256[9]"}], "name": "assemble_nullifier", "outputs": [{"internalType": "bytes32", "name": "nf", "type": "bytes32"}], "payable": False, "stateMutability": "pure", "type": "function"},
    {"constant": True, "inputs": [{"internalType": "uint256[9]", "name": "primary_inputs", "type": "uint256[9]"}], "name": "assemble_public_values", "outputs": [{"internalType": "uint256", "name": "vpub_in", "type": "uint256"},
                                                                                                                                                                 {"internalType": "uint256", "name": "vpub_out", "type": "uint256"}], "payable": False, "stateMutability": "pure", "type": "function"}, {"constant": True, "inputs": [], "name": "get_constants", "outputs": [{"internalType": "uint256", "name": "js_in", "type": "uint256"}, {"internalType": "uint256", "name": "js_out", "type": "uint256"}, {"internalType": "uint256", "name": "num_inputs", "type": "uint256"}], "payable": False, "stateMutability": "pure", "type": "function"}, {"constant": False, "inputs": [{"internalType": "bytes32", "name": "commitment", "type": "bytes32"}], "name": "insert", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": False, "inputs": [{"internalType": "uint256[2]", "name": "a", "type": "uint256[2]"}, {"internalType": "uint256[4]", "name": "b", "type": "uint256[4]"}, {"internalType": "uint256[2]", "name": "c", "type": "uint256[2]"}, {"internalType": "uint256[4]", "name": "vk", "type": "uint256[4]"}, {"internalType": "uint256", "name": "sigma", "type": "uint256"}, {"internalType": "uint256[9]", "name": "input", "type": "uint256[9]"}, {"internalType": "bytes[2]", "name": "ciphertexts", "type": "bytes[2]"}], "name": "mix", "outputs": [], "payable": True, "stateMutability": "payable", "type": "function"}, {"constant": True, "inputs": [], "name": "token", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [{"internalType": "address", "name": "from", "type": "address"}, {"internalType": "uint256", "name": "value", "type": "uint256"}, {"internalType": "bytes", "name": "data", "type": "bytes"}], "name": "tokenFallback", "outputs": [], "payable": False, "stateMutability": "pure", "type": "function"}]
#argbin  = TransactionCommon.format_args_by_abi(fn_args, abi[0]['inputs'] )
#argbin  = encode_transaction_data(None, abi, None, fn_args)

fn_abi = {"inputs":
                        [
                   {"internalType": "uint256", "name": "mk_depth", "type": "uint256"},
                   {"internalType": "address", "name": "token", "type": "address"},
                   {"internalType": "uint[2]", "name": "Alpha", "type": "uint256[2]"},
                   {"internalType": "uint256[2]", "name": "Beta1", "type": "uint256[2]"},
                   {"internalType": "uint256[2]", "name": "Beta2", "type": "uint256[2]"},
                   {"internalType": "uint256[2]", "name": "Delta1", "type": "uint256[2]"},
                   {"internalType": "uint256[2]", "name": "Delta2", "type": "uint256[2]"},
                   {"internalType": "uint256[]", "name": "ABC_coords", "type": "uint256[]"}],
        "payable": False, "stateMutability": "nonpayable", "type": "constructor"}

bin = '0x60806040523480156200001157600080fd5b50604051620025a4380380620025a4833981016040819052620000349162000479565b8787818060208114620000645760405162461bcd60e51b81526004016200005b9062000590565b60405180910390fd5b50620000786001600160e01b036200025a16565b50600080800154600081815264020000000060205260409020805460ff1916600117905564020000000280546001600160a01b0385166001600160a01b03199091161790559050505050604051806040016040528087600060028110620000db57fe5b6020020151815260200187600160028110620000f357fe5b602090810291909101519091528151640200000003559081015164020000000455604080516080808201835288518083528985015183860181905289518486018190528a87015160609586018190526402000000059390935564020000000691909155640200000007556402000000085582519081018352865180825287850151828601819052875194830185905294870151919092018190526402000000099190915564020000000a9290925564020000000b5564020000000c5560005b6002825181620001be57fe5b64020000000d54919004146200024b57640200000003600a016040518060400160405280848481518110620001ef57fe5b602002602001015181526020018484600101815181106200020c57fe5b602090810291909101810151909152825460018181018555600094855293829020835160029283029091019081559290910151919092015501620001b2565b5050505050505050506200064b565b60006401fffffffe81905563800000005b8015620002b357620002898283620002b760201b62000ef41760201c565b91506001196002820201826000826401ffffffff8110620002a657fe5b015550600290046200026b565b5050565b60007fdec937b7fa8db3de380427a8cc947bfab68514522c3439cfa2e99655098368146000527f30644e72e131a029b85045b68181585d2833e84879b9709143e1f593f00000018284828282088381820984858383098683840909925060005b605a8112156200034f57602060002080600052868688838808089350868485099250868488858a878809090994505060010162000317565b508484868a88888808080898975050505050505050565b8051620003738162000626565b92915050565b600082601f8301126200038b57600080fd5b6002620003a26200039c82620005c9565b620005a2565b91508183856020840282011115620003b957600080fd5b60005b83811015620003e95781620003d288826200046c565b8452506020928301929190910190600101620003bc565b5050505092915050565b600082601f8301126200040557600080fd5b8151620004166200039c82620005e7565b915081818352602084019350602081019050838560208402820111156200043c57600080fd5b60005b83811015620003e957816200045588826200046c565b84525060209283019291909101906001016200043f565b8051620003738162000640565b6000806000806000806000806101a0898b0312156200049757600080fd5b6000620004a58b8b6200046c565b9850506020620004b88b828c0162000366565b9750506040620004cb8b828c0162000379565b9650506080620004de8b828c0162000379565b95505060c0620004f18b828c0162000379565b945050610100620005058b828c0162000379565b935050610140620005198b828c0162000379565b9250506101808901516001600160401b038111156200053757600080fd5b620005458b828c01620003f3565b9150509295985092959890939650565b600062000564601f8362000608565b7f496e76616c696420646570746820696e20426173654d65726b6c655472656500815260200192915050565b60208082528101620003738162000555565b6040518181016001600160401b0381118282101715620005c157600080fd5b604052919050565b60006001600160401b03821115620005e057600080fd5b5060200290565b60006001600160401b03821115620005fe57600080fd5b5060209081020190565b90815260200190565b60006001600160a01b03821662000373565b90565b620006318162000611565b81146200063d57600080fd5b50565b620006318162000623565b611f49806200065b6000396000f3fe60806040526004361061007b5760003560e01c806397e004891161004e57806397e0048914610126578063c0ee0b8a14610139578063f9eb943f14610159578063fc0c546a1461017d5761007b565b806305ceb93c146100805780631f40927c146100b65780632d287e43146100e4578063354d06fd14610106575b600080fd5b34801561008c57600080fd5b506100a061009b3660046113e9565b61019f565b6040516100ad9190611c7d565b60405180910390f35b3480156100c257600080fd5b506100d66100d136600461138e565b61022d565b6040516100ad929190611dbf565b3480156100f057600080fd5b506101046100ff3660046113ad565b610256565b005b34801561011257600080fd5b506100a061012136600461138e565b6102ad565b6101046101343660046112d5565b6102cc565b34801561014557600080fd5b50610104610154366004611270565b61043f565b34801561016557600080fd5b5061016e610526565b6040516100ad93929190611dcd565b34801561018957600080fd5b50610192610530565b6040516100ad9190611c2c565b6000600283106101ca5760405162461bcd60e51b81526004016101c190611ccf565b60405180910390fd5b60036001840102608081019060830160fd10156101f95760405162461bcd60e51b81526004016101c190611d1f565b610100830151607182011b60fd1c60006003858782016009811061021957fe5b6020020151901b9190910195945050505050565b610100015164e8d4a5100067ffffffffffffffff604f83901c8116820293600f9390931c160290565b6401ffffffff54640100000000116102805760405162461bcd60e51b81526004016101c190611d0f565b6401ffffffff80546001810182559063ffffffff8201908390600090839081106102a657fe5b0155505050565b61010081015160a09091015160031b6007600c9290921c919091160190565b6102d4610fa1565b6102df858483610543565b815160208084015160405160009360029361030693339390918f918f918f918d9101611bb8565b60408051601f198184030181529082905261032091611ba1565b602060405180830381855afa15801561033d573d6000803e3d6000fd5b5050506040513d601f19601f8201168201806040525061036091908101906113cb565b86516020880151604089015160608a015193945061037f9389866106a4565b61039b5760405162461bcd60e51b81526004016101c190611d8f565b6103a789898987610743565b6103c35760405162461bcd60e51b81526004016101c190611d5f565b6103cb610fa1565b6103d58582610860565b60006103e160026108ad565b90506103ec816108ee565b7f36ed7c3f2ecfb5a5226c478b034d33144c060afe361be291e948f861dcddc618818584886040516104219493929190611c8b565b60405180910390a16104328661090d565b5050505050505050505050565b610447610fbf565b6001600160a01b0384168152602081018390526040810182905281516000906018908490600390811061047657fe5b016020015184516001600160f81b031990911690911c60e01c90601090859060029081106104a057fe5b016020015185516001600160f81b031990911690911c60e01c90600890869060019081106104ca57fe5b016020015186516001600160f81b031990911690911c60e01c9086906000906104ef57fe5b01602001516001600160e01b031963ff00000060e092831c16929092019290920192909201901b1660609092019190915250505050565b6002908190600990565b640200000002546001600160a01b031681565b81516000908152640200000000602052604090205460ff166105775760405162461bcd60e51b81526004016101c190611d2f565b60005b60028110156105fd57600061058f828561019f565b6000818152640200000001602052604090205490915060ff16156105c55760405162461bcd60e51b81526004016101c190611cdf565b600081815264020000000160205260409020805460ff19166001179055808383600281106105ef57fe5b60200201525060010161057a565b50600060028285604051602001610615929190611b7b565b60408051601f198184030181529082905261062f91611ba1565b602060405180830381855afa15801561064c573d6000803e3d6000fd5b5050506040513d601f19601f8201168201806040525061066f91908101906113cb565b9050600061067c846102ad565b905080821461069d5760405162461bcd60e51b81526004016101c190611d3f565b5050505050565b60006106ae610ffa565b6107d05a038682528560208301528360408301526020608083016060846000600286f150604082018981528860208201526040816060836000600787f1506040836080856000600687f15060016040840152600260608401528560808401526040816060836000600787f150505060408101518151148015610737575060608101516020820151145b98975050505050505050565b60007f30644e72e131a029b85045b68181585d2833e84879b9709143e1f593f000000161076e611018565b86518152602080880151828201528651604080840191909152878201516060808501919091528189015160808501528089015160a0850152875160c08501528783015160e0850152815160098082526101408201909352909290919082016101208038833901905050905060005b600981101561084457838682600981106107f257fe5b6020020151106108145760405162461bcd60e51b81526004016101c190611d7f565b85816009811061082057fe5b602002015182828151811061083157fe5b60209081029190910101526001016107dc565b5061084f8183610b60565b60011493505050505b949350505050565b60005b60028110156108a857600083826001016009811061087d57fe5b602002015190508083836002811061089157fe5b602002015261089f81610256565b50600101610863565b505050565b6401ffffffff546000908281036401000000005b60018111156108e2576108d5818385610e2b565b93509150600290046108c1565b50506000549392505050565b600090815264020000000060205260409020805460ff19166001179055565b6000806109198361022d565b909250905081156109cf57640200000002546001600160a01b0316156109ab57640200000002546040516323b872dd60e01b81526001600160a01b039091169081906323b872dd9061097390339030908890600401611c3a565b600060405180830381600087803b15801561098d57600080fd5b505af11580156109a1573d6000803e3d6000fd5b50505050506109ca565b8134146109ca5760405162461bcd60e51b81526004016101c190611d6f565b610a53565b3415610a53576000336001600160a01b0316346040516109ee90611bad565b60006040518083038185875af1925050503d8060008114610a2b576040519150601f19603f3d011682016040523d82523d6000602084013e610a30565b606091505b5050905080610a515760405162461bcd60e51b81526004016101c190611cef565b505b80156108a857640200000002546001600160a01b031615610ade576402000000025460405163a9059cbb60e01b81526001600160a01b0390911690819063a9059cbb90610aa69033908690600401611c62565b600060405180830381600087803b158015610ac057600080fd5b505af1158015610ad4573d6000803e3d6000fd5b50505050506108a8565b6000336001600160a01b031682604051610af790611bad565b60006040518083038185875af1925050503d8060008114610b34576040519150601f19603f3d011682016040523d82523d6000602084013e610b39565b606091505b5050905080610b5a5760405162461bcd60e51b81526004016101c190611cff565b50505050565b64020000000d548251600091600190910114610b8e5760405162461bcd60e51b81526004016101c190611d4f565b610b9661105d565b60016107d05a03600a6402000000030183526020832060208701875160200281018254865260018301546020870152600283019250604086015b81831015610c1e57835481526001840154602082015282516040820152604081606083600060078af160408860808a600060068bf11695909516946002939093019260209290920191610bd0565b505050505080610c405760405162461bcd60e51b81526004016101c190611daf565b7f198e9393920d483a7260bfb731fb5d25f1aa493335a9e71297e485b7aef312c260408301527f1800deef121f1e76426a00665e5c4479674322d4f75edadd46debd5cd992f6ed60608301527f090689d0585ff075ec9e99ad690c3395bc4b313370b38ef355acdadcd122975b60808301527f12c85ea5db8c6deb4aab71808dcb408fe3d1e7690c43d37b4ce6cc0166fa7daa60a08301526402000000035460c08301526001640200000003015460e08301526002640200000003015461010083015260036402000000030154610120830152600464020000000301546101408301526005640200000003015461016083015283516101808301527f30644e72e131a029b85045b68181585d97816a916871ca8d3c208c16d87cfd47602085015181810682036101a085015260408601516101c085015260608601516101e0850152608086015161020085015260a086015161022085015260c086015161024085015260e086015161026085015260066402000000030154610280850152600764020000000301546102a0850152600864020000000301546102c0850152600964020000000301546102e085015260208461030086600060086107d05a03f19250505080610e205760405162461bcd60e51b81526004016101c190611d9f565b505190505b92915050565b600080600019808601906001198616870101826001861615610e9f575060001982860101610e806000826401ffffffff8110610e6357fe5b01546000856002026401ffffffff8110610e7957fe5b0154610ef4565b600060026000198401046401ffffffff8110610e9857fe5b0155610ea4565b508185015b81811115610eda5760011901610e806000826401ffffffff8110610ec457fe5b01546000836001016401ffffffff8110610e7957fe5b600287046002600188010494509450505050935093915050565b60007fdec937b7fa8db3de380427a8cc947bfab68514522c3439cfa2e99655098368146000527f30644e72e131a029b85045b68181585d2833e84879b9709143e1f593f00000018284828282088381820984858383098683840909925060005b605a811215610f8a57602060002080600052868688838808089350868485099250868488858a8788090909945050600101610f54565b508484868a88888808080898975050505050505050565b60405180604001604052806002906020820280388339509192915050565b604051806080016040528060006001600160a01b03168152602001600081526020016060815260200160006001600160e01b03191681525090565b6040518060a001604052806005906020820280388339509192915050565b60405180610100016040528060008152602001600081526020016000815260200160008152602001600081526020016000815260200160008152602001600081525090565b6040518061030001604052806018906020820280388339509192915050565b8035610e2581611ee6565b600082601f83011261109857600080fd5b60026110ab6110a682611e0f565b611de8565b9150818360005b838110156110de57813586016110c88882611221565b84525060209283019291909101906001016110b2565b5050505092915050565b600082601f8301126110f957600080fd5b60026111076110a682611e0f565b9150818385602084028201111561111d57600080fd5b60005b838110156110de5781611133888261120b565b8452506020928301929190910190600101611120565b600082601f83011261115a57600080fd5b60046111686110a682611e0f565b9150818385602084028201111561117e57600080fd5b60005b838110156110de5781611194888261120b565b8452506020928301929190910190600101611181565b600082601f8301126111bb57600080fd5b60096111c96110a682611e0f565b915081838560208402820111156111df57600080fd5b60005b838110156110de57816111f5888261120b565b84525060209283019291909101906001016111e2565b8035610e2581611efd565b8051610e2581611efd565b600082601f83011261123257600080fd5b81356112406110a682611e2d565b9150808252602083016020830185838301111561125c57600080fd5b611267838284611ea4565b50505092915050565b60008060006060848603121561128557600080fd5b6000611291868661107c565b93505060206112a28682870161120b565b925050604084013567ffffffffffffffff8111156112bf57600080fd5b6112cb86828701611221565b9150509250925092565b60008060008060008060006102e0888a0312156112f157600080fd5b60006112fd8a8a6110e8565b975050604061130e8a828b01611149565b96505060c061131f8a828b016110e8565b9550506101006113318a828b01611149565b9450506101806113438a828b0161120b565b9350506101a06113558a828b016111aa565b9250506102c088013567ffffffffffffffff81111561137357600080fd5b61137f8a828b01611087565b91505092959891949750929550565b600061012082840312156113a157600080fd5b600061085884846111aa565b6000602082840312156113bf57600080fd5b6000610858848461120b565b6000602082840312156113dd57600080fd5b60006108588484611216565b60008061014083850312156113fd57600080fd5b6000611409858561120b565b925050602061141a858286016111aa565b9150509250929050565b60006114308383611655565b505060200190565b6000611444838361168d565b9392505050565b61145481611e93565b82525050565b61145481611e82565b61146c81611e58565b6114768184611e74565b925061148182611e55565b8060005b838110156114af5781516114998782611424565b96506114a483611e6e565b925050600101611485565b505050505050565b6114c081611e58565b6114ca8184611e74565b92506114d582611e55565b8060005b838110156114af5781516114ed8782611424565b96506114f883611e6e565b9250506001016114d9565b600061150e82611e58565b6115188185611e74565b93508360208202850161152a85611e55565b8060005b8581101561156457848403895281516115478582611438565b945061155283611e6e565b60209a909a019992505060010161152e565b5091979650505050505050565b61157a81611e58565b6115848184611e74565b925061158f82611e55565b8060005b838110156114af5781516115a78782611424565b96506115b283611e6e565b925050600101611593565b6115c681611e5e565b6115d08184611e74565b92506115db82611e55565b8060005b838110156114af5781516115f38782611424565b96506115fe83611e6e565b9250506001016115df565b61161281611e64565b61161c8184611e74565b925061162782611e55565b8060005b838110156114af57815161163f8782611424565b965061164a83611e6e565b92505060010161162b565b61145481611e55565b600061166982611e6a565b6116738185611e74565b9350611683818560208601611eb0565b9290920192915050565b600061169882611e6a565b6116a28185611e79565b93506116b2818560208601611eb0565b6116bb81611edc565b9093019392505050565b60006116d2601883611e79565b7f6e756c6c696669657220696e646578206f766572666c6f770000000000000000815260200192915050565b600061170b603783611e79565b7f496e76616c6964206e756c6c69666965723a2054686973206e756c6c6966696581527f722068617320616c7265616479206265656e2075736564000000000000000000602082015260400192915050565b600061176a601e83611e79565b7f767075625f696e2072657475726e207472616e73666572206661696c65640000815260200192915050565b60006117a3601883611e79565b7f767075625f6f7574207472616e73666572206661696c65640000000000000000815260200192915050565b60006117dc602783611e79565b7f4d65726b6c6520747265652066756c6c3a2043616e6e6f7420617070656e6420815266616e796d6f726560c81b602082015260400192915050565b6000611825603083611e79565b7f6e756c6c6966696572207772697474656e20696e20646966666572656e74207281526f32b9b4b23ab0b6103134ba103317329760811b602082015260400192915050565b6000611877602583611e79565b7f496e76616c696420726f6f743a205468697320726f6f7420646f65736e277420815264195e1a5cdd60da1b602082015260400192915050565b60006118be604983611e79565b7f496e76616c696420687369673a2054686973206873696720646f6573206e6f7481527f20636f72726573706f6e6420746f207468652068617368206f6620766b20616e6020820152686420746865206e667360b81b604082015260600192915050565b600061192f602283611e79565b7f496e707574206c656e67746820646966666572732066726f6d20657870656374815261195960f21b602082015260400192915050565b6000611973603383611e79565b7f496e76616c69642070726f6f663a20556e61626c6520746f20766572696679208152727468652070726f6f6620636f72726563746c7960681b602082015260400192915050565b60006119c8602a83611e79565b7f57726f6e67206d73672e76616c75653a2056616c75652070616964206973206e8152691bdd0818dbdc9c9958dd60b21b602082015260400192915050565b6000611a14601c83611e79565b7f496e707574206973206e6f7420696e207363616c6172206669656c6400000000815260200192915050565b6000611a4d603b83611e79565b7f496e76616c6964207369676e61747572653a20556e61626c6520746f2076657281527f69667920746865207369676e617475726520636f72726563746c790000000000602082015260400192915050565b6000610e25600083611e74565b6000611ab9603783611e79565b7f43616c6c20746f20626e3235364164642c20626e3235365363616c61724d756c81527f206f7220626e32353650616972696e67206661696c6564000000000000000000602082015260400192915050565b6000611b18603983611e79565b7f43616c6c20746f2074686520626e323536416464206f7220626e32353653636181527f6c61724d756c20707265636f6d70696c6564206661696c656400000000000000602082015260400192915050565b611454611b7682611e55565b611e55565b6000611b8782856114b7565b604082019150611b9782846115bd565b5060800192915050565b6000611444828461165e565b6000610e2582611a9f565b6000611bc4828a611b6a565b602082019150611bd4828961165e565b9150611be0828861165e565b9150611bec8287611571565b604082019150611bfc82866115bd565b608082019150611c0c8285611571565b604082019150611c1c8284611609565b5061012001979650505050505050565b60208101610e25828461145a565b60608101611c48828661144b565b611c55602083018561145a565b6108586040830184611655565b60408101611c70828561144b565b6114446020830184611655565b60208101610e258284611655565b60c08101611c998287611655565b611ca66020830186611463565b611cb36060830185611463565b81810360a0830152611cc58184611503565b9695505050505050565b60208082528101610e25816116c5565b60208082528101610e25816116fe565b60208082528101610e258161175d565b60208082528101610e2581611796565b60208082528101610e25816117cf565b60208082528101610e2581611818565b60208082528101610e258161186a565b60208082528101610e25816118b1565b60208082528101610e2581611922565b60208082528101610e2581611966565b60208082528101610e25816119bb565b60208082528101610e2581611a07565b60208082528101610e2581611a40565b60208082528101610e2581611aac565b60208082528101610e2581611b0b565b60408101611c708285611655565b60608101611ddb8286611655565b611c556020830185611655565b60405181810167ffffffffffffffff81118282101715611e0757600080fd5b604052919050565b600067ffffffffffffffff821115611e2657600080fd5b5060200290565b600067ffffffffffffffff821115611e4457600080fd5b506020601f91909101601f19160190565b90565b50600290565b50600490565b50600990565b5190565b60200190565b919050565b90815260200190565b60006001600160a01b038216610e25565b6000610e25826000610e2582611e82565b82818337506000910152565b60005b83811015611ecb578181015183820152602001611eb3565b83811115610b5a5750506000910152565b601f01601f191690565b611eef81611e82565b8114611efa57600080fd5b50565b611eef81611e5556fea365627a7a72315820e42326a4694c17436c7722fd4a82ac810b74162de26e7fd1035ac3ef5d5a29d16c6578706572696d656e74616cf564736f6c63430005110040'
argbin = (encode_abi(fn_abi, fn_args))
totalbin = bin + argbin
fo = open("./temp.bin", "w")

fo.write(bin)
fo.close()

print("totalbin: ", totalbin)



# Greeter = eth.contract(abi, bin)
# si1.constructor
# result1 = si1.deploy("./temp.bin")

client = BcosClient()
info = client.init()
print(info)

result1 = client.sendRawTransactionGetReceipt("", abi, None, fn_args, bin, 30000000, 15)

address = result1['contractAddress']
si1 = Groth16Mixer(address)
print("token address: ", si1.token())
print("new address = ", address)
