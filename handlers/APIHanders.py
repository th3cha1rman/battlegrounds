# -*- coding: utf-8 -*-
"""
Created on Mar 13, 2012

@author: moloch

    Copyright 2012 Root the Box

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
----------------------------------------------------------------------------

This file contains handlers related to the file sharing functionality

"""
import json

from libs.SecurityDecorators import apikey, restrict_ip_address

from .AdminHandlers.AdminGameHandlers import AdminGameHandler
from .BaseHandlers import BaseHandler


class APIActionHandler(BaseHandler):

    @apikey
    @restrict_ip_address
    def post(self, *args, **kwargs):
        actions = AdminGameHandler.admin_actions(self)
        self.write(json.dumps(actions))

    def check_xsrf_cookie(self):
        pass

'''
class UserStatsHandler(BaseHandler):
    """Returns total users and users online"""
    
    def get(self):
        from models import dbsession
        from models.User import User
        
        # Get total users
        total_users = dbsession.query(User).count()
        
        # Get online users (active connections)
        users_online = 0
        try:
            stats = self.memcached.stats().get("127.0.0.1")
            if stats:
                users_online = int(stats.get("curr_connections", 0))
            else:
                users_online = total_users
        except:
            users_online = total_users
        
        self.write({
            'total_users': total_users,
            'users_online': users_online
        })
        self.set_header('Content-Type', 'application/json')
'''