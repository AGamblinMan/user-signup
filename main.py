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

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
    return username and USER_RE.match(username)

def valid_password(password):
    return password and PASS_RE.match(password)

def valid_email(email):
    return not email or EMAIL_RE.match(email)





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
form = """
<h1>Signup</h1>
<form method="post">
    <table>
        <tr>
            <td>
                <label>Username:</label>
            </td>
            <td>
                <input name="username" type="text" value ="%(username)s">
                <span class="error">%(username_error)s</span>
            </td>
        </tr>
        <tr>
            <td>
                <label>Password:</label>
            </td>
            <td>
                <input name="password" type="password">
                <span class="error">%(password_error)s</span>
            </td>
        </tr>
        <tr>
            <td>
                <label>Verify Password:</label>
            </td>
            <td>
                <input name="verify" type="password">
                <span class="error">%(verify_error)s</span>
            </td>
        </tr>
        <tr>
            <td>
                <label>Email (optional):</label>
            </td>
            <td>
                <input name="email" type="text" value="%(email)s">
                <span class="error">%(email_error)s</span>
            </td>
        </tr>
    </table>
    <input type="submit" value="Sign Up">
</form>
"""

html_footer = """
    </body>
</html>
"""
class MainHandler(webapp2.RequestHandler):
    def write_form(self, username="",email="",
    username_error="",password_error="",verify_error="",email_error=""):
        self.response.out.write(html_header + form %{'username':username,
                                                'email':email,
                                                'username_error':username_error,
                                                'password_error':password_error,
                                                'verify_error':verify_error,
                                                'email_error':email_error} + html_footer)

    def get(self):
        self.write_form()

    def post(self):
        error_messages = {}
        errors = []
        user_username = self.request.get('username')
        user_password = self.request.get('password')
        user_verify = self.request.get('verify')
        user_email = self.request.get('email')

        username = valid_username(user_username)
        password = valid_password(user_password)
        verify = valid_password(user_verify)
        email = valid_email(user_email)

        if not username:
            error_messages['username_error']='Please enter a valid Username'
        if not password:
            error_messages['password_error']='Please enter a valid password'
        if user_password != user_verify:
            error_messages['verify_error']='Passwords did not match'
        if not email:
            error_messages['email_error']='Please enter a valid email'

        if error_messages:
            self.write_form(username=escape(user_username),
                            email=escape(user_email),
                            username_error=error_messages.get('username_error',""),
                            password_error=error_messages.get('password_error',""),
                            verify_error=error_messages.get('verify_error',""),
                            email_error=error_messages.get('email_error',""))
        else:
            self.write_form()


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
