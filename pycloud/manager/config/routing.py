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

"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    mapper = Mapper()
    connect = mapper.connect

    # For backwards compatibility with 0.9.7.
    mapper.explicit = False

    # Note that all of these paths are relative to the base path, /manager. 
    connect('/', controller='services', action='index')
    connect('/home', controller='home', action='index')
    connect('/home/state', controller='home', action='state')

    connect('/auth/signin', controller='auth', action='signin')
    connect('/auth/signin_form', controller='auth', action='signin_form')
    connect('/auth/signout', controller='auth', action='signout')
    
    connect('/services', controller='services', action='listServices')
    connect('/services/removeService/{id}', controller='services', action='removeService')
    
    connect('/instances', controller='instances', action='index')
    connect('/instances/startInstance/{id}', controller='instances', action='startInstance')
    connect('/instances/stopInstance/{id}', controller='instances', action='stopInstance')
    connect('/instances/migrate/{id}', controller='instances', action='migrateInstance')
    connect('/instances/receiveMigratedSVMMetadata', controller='instances', action='receiveMigratedSVMMetadata')
    connect('/instances/receiveMigratedSVMDiskFile', controller='instances', action='receiveMigratedSVMDiskFile')
    connect('/instances/resumeMigratedSVM', controller='instances', action='resumeMigratedSVM')
    connect('/instances/getMigrationInfo/{id}', controller='instances', action='getMigrationInfo')
    connect('/instances/svmList', controller='instances', action='svmList')

    connect('add_service', '/service/add', controller='modify', action='index')
    connect('/service/createSVM', controller='modify', action='createSVM')
    connect('/service/saveNewSVM', controller='modify', action='saveNewSVM')
    connect('/service/openSVM/{id}', controller='modify', action='openSVM')
    connect('/service/edit/{id}', controller='modify', action='index')
    connect('/service/saveSVM', controller='modify', action='saveInstanceToRoot')
    connect('/service/getImageInfo', controller='modify', action='getImageInfo')

    connect('/apps', controller='apps', action='index')
    connect('/apps/list', controller='apps', action='list')
    connect('/apps/get', controller='apps', action='get_data')
    connect('/apps/add', controller='apps', action='add')
    connect('/apps/edit', controller='apps', action='edit')
    connect('/apps/remove', controller='apps', action='remove')

    connect('export_service', '/service/exportsvm/{sid}', controller='export', action='export_svm')
    connect('import_service', '/service/importsvm', controller='import', action='import')

    connect('list_devices', '/devices', controller='devices', action='list')
    connect('clear', '/devices/clear', controller='devices', action='clear')
    connect('bootrstrap', '/devices/bootstrap', controller='devices', action='bootstrap')
    connect('available_devices', '/devices/available', controller='pairing', action='available')
    connect('pair_device', '/devices/pair/{id}', controller='pairing', action='pair')
    connect('authorize_device', '/devices/authorize/{did}', controller='devices', action='authorize')
    connect('unpair_device', '/devices/unpair/{id}', controller='devices', action='unpair')
    connect('revoke_auth', '/devices/revoke/{id}', controller='devices', action='revoke')
    connect('reauthorize', '/devices/reauthorize/{id}', controller='devices', action='reauthorize')

    return mapper
