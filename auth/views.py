import json
from time import time
from bson.objectid import ObjectId
import aiohttp_jinja2
from aiohttp_session import get_session
from aiohttp import web
from auth.models import User


class Login(web.View):
    @aiohttp_jinja2.template('auth/login.html')
    async def get(self):
        session = await get_session(self.request)
        if session.get('user'):
            redirect(self.request, 'main')
        return {'conten': 'Please enter login or email'}

    async def post(self):
        data = await self.request.post()
        user = User(self.request.db, data)