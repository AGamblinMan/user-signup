#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re
from cgi import escape

html_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>user-signup</title>
        <style>
            .error{
            color:red
            }
        </style>
    </head>
    <body>
"""
html_footer = """
    </body>
</html>
"""
class MainHandler(webapp2.RequestHandler):
    def get(self):
        form = """
        <h1>Signup</h1>
        <form method="post">
            <table>
                <tr>
                    <td>
                        <label>Username:</label>
                    </td>
                    <td>
                        <input name="username" type="text"/>
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label>Password:</label>
                    </td>
                    <td>
                        <input name="password" type="password"/>
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label>Verify Password:</label>
                    </td>
                    <td>
                        <input name="verify" type="password"/>
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label>Email (optional):</label>
                    </td>
                    <td>
                        <input name="email" type="text"/>
                        <span class="error"></span>
                    </td>
                </tr>
            </table>
            <input type="submit" value="Sign Up"/>
        </form>
        """




        self.response.write(html_header + form + html_footer)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
