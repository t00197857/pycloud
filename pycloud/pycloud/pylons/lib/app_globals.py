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

"""The application's Globals object"""

import pycloud.pycloud.cloudlet as cloudlet

from pycloud.pycloud.pylons.lib.tm import TemplateManager

class Globals(object):

    # Globals acts as a container for objects available throughout the
    # life of the application.

    def __init__(self, config):
        # One instance of Globals is created during application
        # initialization and is available during requests via the
        # 'pylons.app_globals' variable.

        # Create or get instance of the singleton Cloudlet object.
        self.cloudlet = cloudlet.get_cloudlet_instance(config)

        # Set up the global template manager.
        self.tm = TemplateManager()
