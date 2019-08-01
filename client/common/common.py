'''
  bcosliteclientpy is a python client for FISCO BCOS2.0 (https://github.com/FISCO-BCOS/)
  bcosliteclientpy is free software: you can redistribute it and/or modify it under the
  terms of the MIT License as published by the Free Software Foundation. This project is
  distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even
  the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. Thanks for
  authors and contributors of eth-abi, eth-account, eth-hash，eth-keys, eth-typing, eth-utils,
  rlp, eth-rlp , hexbytes ... and relative projects
  @file: consensus_precompile.py
  @function:
  @author: yujiechen
  @date: 2019-07
'''
import shutil
import time
import os
import json
import subprocess
from client_config import client_config
from client.bcosclient import BcosClient
from client.bcoserror import ArgumentsError, BcosException


def backup_file(file_name):
    """
    backup files
    """
    if os.path.isfile(file_name) is False:
        return
    forcewrite = True
    option = "y"
    if client_config.background is False:
        option = input("INFO >> file [{}] exist , continue (y/n): ".format(file_name))
    if (option.lower() == "y"):
        forcewrite = True
    else:
        forcewrite = False
        print("skip write to file: {}".format(file_name))

    # forcewrite ,so do backup job
    if(forcewrite):
        filestat = os.stat(file_name)
        filetime = time.strftime("%Y%m%d%H%M%S", time.localtime(filestat.st_ctime))
        backupfile = "{}.{}".format(file_name, filetime)
        print("backup [{}] to [{}]".format(file_name, backupfile))
        shutil.move(file_name, backupfile)
    return forcewrite


def print_info(level, cmd):
    """
    print information
    """
    print("{} >> {}".format(level, cmd))


def print_result(ret):
    """
    print result
    """
    if isinstance(ret, dict):
        print_info("    ", "{}".format(json.dumps(ret, indent=4)))
    elif isinstance(ret, list):
        if len(ret) > 0:
            for ret_item in ret:
                print_result(ret_item)
        else:
            print_info("    ", "Empty Set")
    else:
        print_info("    ", "{}".format(ret))


def execute_cmd(cmd):
    """
    execute command
    """
    data = subprocess.check_output(cmd.split(), shell=False, universal_newlines=True)
    status = 0
    return (status, data)


def print_error_msg(cmd, e):
    """
    print error msg
    """
    print("ERROR >> execute {} failed\nERROR >> error information: {}\n".format(cmd, e))


def check_int_range(number_str):
    """
    check integer range
    """
    try:
        number = 0
        if number_str.startswith("0x"):
            number = int(number_str, 16)
        else:
            number = int(number_str)
        if number > BcosClient.max_block_number or number < 0:
            raise ArgumentsError(("invalid input: {},"
                                  " must between 0 and {}").
                                 format(number, BcosClient.max_block_number))
        return number
    except Exception as e:
        raise ArgumentsError("invalid input:{}, error info: {}".format(number, e))


def check_hash(hash_str):
    """
    check hash
    """
    min_size = 64
    max_size = 66
    if len(hash_str) < min_size or \
        hash_str.startswith("0x") and len(hash_str) < max_size \
            or len(hash_str) > max_size:
        raise BcosException(("invalid hash: {},"
                             "expected len: {} or {}, real len: {}").
                            format(min_size, max_size,
                                   hash_str, len(hash_str)))


def check_param_num(args, expected, needEqual=False):
    """
    check param num
    """
    if needEqual is False:
        if len(args) < expected:
            raise ArgumentsError(("invalid arguments, expected num >= {},"
                                  "real num: {}").format(expected, len(args)))
    else:
        if len(args) != expected:
            raise ArgumentsError(("invalid arguments, expected num {},"
                                  "real num: {}").format(expected, len(args)))
