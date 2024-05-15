from fastapi import FastAPI
from fastapi import Request
from mongo import Mongo

db=Mongo()

app=FastAPI()

@app.get('/')
async def home():

    return "This is the home route, please acces api endpoints via '/api/<endpoint>' "

@app.get('/api/post')
async def get_post(id: str):
    
    #params=dict(req.query_params)
    return db.get_post(id)

@app.post('/api/post')
async def add_post(blog: str):
    
    return db.add_post(blog)

@app.put('/api/post')
async def edit_post(id: str,blog: str):
    
    return db.update_post(id,blog)

@app.delete('/api/post')
async def delete_post(id: str):
    
    return db.delete_post(id)


@app.post('/api/post/like')
async def like_post(id: str):
    
    return db.rate_post(id,1)

@app.post('/api/post/dislike')
async def dislike_post(id: str):

    return db.rate_post(id,-1)

@app.post('/api/post/comment')
async def comment_post(id: str, comment: str):
    
    return db.comment_post(id,comment)