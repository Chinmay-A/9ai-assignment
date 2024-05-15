class Mongo:

    def __init__(self):

        import pymongo  as pym

        self.client=pym.MongoClient('mongodb+srv://chinmayaons1:0pMEiNALChGMgUYm@testcluster.mdjjc1i.mongodb.net/assign_nineAI?retryWrites=true&w=majority&appName=TestCluster')
        self.db=self.client['assign_nineAI']
        self.posts=self.db['posts']
    
    def get_obj(self,id):

        from bson.objectid import ObjectId

        return ObjectId(id)
    
    def add_post(self,data):

        new_post=self.posts.insert_one({'blog': data,'likes':0,'comments':[]})

        print(f'Created post with id: {new_post.inserted_id}')

        return {'id':str(new_post.inserted_id)}
    
    def get_post(self,id):

        matching_post=self.posts.find_one({'_id': self.get_obj(id)})


        if(matching_post):
            matching_post['_id']=str(matching_post['_id'])

        #print(matching_post)
        
        return matching_post
    
    def rate_post(self,id,update):

        #update=1 for like and -1 for dislike
        
        updated_doc=self.posts.find_one_and_update({'_id':self.get_obj(id)},{'$inc':{'likes':update}},new=True)

        updated_doc['_id']=str(updated_doc['_id'])

        return updated_doc
    
    def comment_post(self,id,comment):

        updated_doc=self.posts.find_one_and_update({'_id':self.get_obj(id)},{'$push':{'comments':comment}},new=True)

        updated_doc['_id']=str(updated_doc['_id'])

        return updated_doc
    
    def update_post(self,id,update):

        updated_doc=self.posts.find_one_and_update({'_id':self.get_obj(id)},{'$set':{'blog':update}},new=True)

        updated_doc['_id']=str(updated_doc['_id'])

        return updated_doc
    
    def delete_post(self,id):

        self.posts.delete_one({'_id':self.get_obj(id)})

