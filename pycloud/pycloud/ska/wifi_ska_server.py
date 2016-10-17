# KVM-based Discoverable Cloudlet (KD-Cloudlet)
# Copyright (c) 2015 Carnegie Mellon University.
# All Rights Reserved.
#
# THIS SOFTWARE IS PROVIDED "AS IS," WITH NO WARRANTIES WHATSOEVER. CARNEGIE MELLON UNIVERSITY EXPRESSLY DISCLAIMS TO THE FULLEST EXTENT PERMITTEDBY LAW ALL EXPRESS, IMPLIED, AND STATUTORY WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT OF PROPRIETARY RIGHTS.
#
# Released under a modified BSD license, please see license.txt for full terms.
# DM-0002138
#
# KD-Cloudlet includes and/or makes use of the following Third-Party Software subject to their own licenses:
# MiniMongo
# Copyright (c) 2010-2014, Steve Lacy
# All rights reserved. Released under BSD license.
# https://github.com/MiniMongo/minimongo/blob/master/LICENSE
#
# Bootstrap
# Copyright (c) 2011-2015 Twitter, Inc.
# Released under the MIT License
# https://github.com/twbs/bootstrap/blob/master/LICENSE
#
# jQuery JavaScript Library v1.11.0
# http://jquery.com/
# Includes Sizzle.js
# http://sizzlejs.com/
# Copyright 2005, 2014 jQuery Foundation, Inc. and other contributors
# Released under the MIT license
# http://jquery.org/license
import socket

from wifi_ska_comm import WiFiSKACommunicator, WiFiAdapter, TestAdapter


######################################################################################################################
#
######################################################################################################################
class WiFiSKAServer(object):

    ####################################################################################################################
    #
    ####################################################################################################################
    def __init__(self, host, port, secret, files_path, pairing_handler, adapter=WiFiAdapter()):
        self.device_socket = None
        self.host = host
        self.port = port
        self.secret = secret
        self.files_path = files_path
        self.handler = pairing_handler
        self.adapter = adapter

    ####################################################################################################################
    # Listen on a socket and handle commands. Each connection spawns a separate thread
    ####################################################################################################################
    def wait_for_messages(self):
        adapter_name = self.adapter.get_adapter_name()
        if adapter_name is None:
            raise Exception("WiFi adapter not available.")

        self.device_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(self.host + '-' + str(self.port))
        self.device_socket.bind((self.host, self.port))
        self.device_socket.listen(1)

        # Get new data until we get a final command.
        data_socket = None
        try:
            print('Waiting for messages')
            data_socket, addr = self.device_socket.accept()
            print('Device connected')
            comm = WiFiSKACommunicator(data_socket, self.secret)
            self.device_socket.close()

            try:
                while True:
                    command, message = comm.receive_command()
                    print "Received a message."

                    if command == "receive_file":
                        folder_path = self.handler.get_storage_folder_path(self.files_path, message)
                        comm.receive_file(message, folder_path)

                    return_code, return_data = self.handler.handle_incoming(command, message, self.files_path)
                    if return_code == 'send':
                        comm.send_data(return_data)
                    elif return_code == 'ok':
                        comm.send_success_reply()
                    elif return_code == 'transfer_complete':
                        comm.send_success_reply()
                        break
            except Exception as e:
                comm.send_error_reply(e.message)
        finally:
            print('Closing connections...')
            if data_socket is not None:
                data_socket.close()

######################################################################################################################
# Test handler
######################################################################################################################
class TestHandler(object):
    ####################################################################################################################
    # Create path and folders to store the files.
    ####################################################################################################################
    def get_storage_folder_path(self, base_path, message):
        return base_path + '/' + message['cloudlet_name']

    ####################################################################################################################
    # Handle an incoming message.
    ####################################################################################################################
    def handle_incoming(self, command, message, files_path):
        print 'Handling command: ' + command
        if command == 'send_data':
            return 'send', ('device_id', 'pepe')
        elif command == 'transfer_complete':
            return command, ''


######################################################################################################################
# Test method
######################################################################################################################
def test():
    server = WiFiSKAServer(host='127.0.0.1', port=1700, secret='secret',
                           files_path='./data/test', pairing_handler=TestHandler(), adapter=TestAdapter('eth0'))
    server.wait_for_messages()
