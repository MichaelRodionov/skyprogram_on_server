from flask import request

from application.dao.post_dao import PostDAO
from application.dao.models.models import Post


# ----------------------------------------------------------------
# post service class
class PostService:
    def __init__(self, post_dao: PostDAO):
        self.post_dao = post_dao

    def get_posts(self):
        return self.post_dao.get_all_posts()

    def get_post(self, post_id):
        return self.post_dao.get_one_post(post_id)

    def add_post(self, data):
        for post in data:
            new_post = Post(**post)
            self.post_dao.add_post(new_post)
        return ""

    def delete_post(self, post_id):
        return self.post_dao.delete_post(post_id)
