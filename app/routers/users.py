from fastapi import APIRouter, Query
import json
from fastapi import FastAPI
from starlette.config import Config
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, RedirectResponse
from authlib.integrations.starlette_client import OAuth, OAuthError

r = APIRouter()
config = Config(".env")
oauth = OAuth(config)
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)


@r.get("/user/{user_id}")
async def get_info(request: Request, user_id: int):
    print('Session info?', request.session.get('user'))
    return {"message": f"user info for user: {user_id}"}


@r.route('/login')
async def login(request: Request):
    redirect_uri = request.url_for('logged_in')
    return await oauth.google.authorize_redirect(request, redirect_uri)


@r.get('/auth2')
async def auth2(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
        print("Token", token)
    except OAuthError as error:
        return HTMLResponse(f'<h1>{error.error}</h1>')
    user = token.get('userinfo')
    if user:
        request.session['user'] = dict(user)
    return RedirectResponse(url='/')


@r.get('/logged_in')
async def logged_in(request: Request):
    print("SESSION", request.session)
    return {'status': 'Logged In'}
