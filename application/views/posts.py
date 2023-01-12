from flask import request
from flask_restx import Resource, Namespace

from application.dao.models.models import PostSchema, CommentSchema
from implemented import post_service, comment_service

# ----------------------------------------------------------------
# create namespace and schemas
post_ns = Namespace('posts')
post_schema = PostSchema()
posts_schema = PostSchema(many=True)
comments_schema = CommentSchema(many=True)


# ----------------------------------------------------------------
# views to handle posts requests
@post_ns.route('/')
class PostsView(Resource):
    @staticmethod
    def get():
        return posts_schema.dump(post_service.get_posts()), 200

    @staticmethod
    def post():
        data = request.json
        post_service.add_post(data)
        return '', 201


@post_ns.route('/<int:post_id>')
class PostView(Resource):
    @staticmethod
    def get(post_id):
        post = post_schema.dump(post_service.get_post(post_id))
        comments = comments_schema.dump(comment_service.get_comments(post_id))
        if not post:
            return 'post not found', 404
        return {'post': post, 'comments': comments, 'comments_count': len(comments)}, 200

    @staticmethod
    def delete(post_id):
        return post_service.delete_post(post_id), 204


