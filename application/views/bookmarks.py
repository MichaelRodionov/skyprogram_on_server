from flask_restx import Resource, Namespace

from application.dao.models.models import BookmarkSchema
from implemented import bookmark_service


# ----------------------------------------------------------------
# create namespace and schema
bookmark_ns = Namespace('bookmarks')
bookmarks_schema = BookmarkSchema(many=True)


# ----------------------------------------------------------------
# views to handle bookmarks requests
@bookmark_ns.route('/')
class BookmarksView(Resource):
    @staticmethod
    def get():
        return bookmarks_schema.dump(bookmark_service.get_bookmarks()), 200


@bookmark_ns.route('/add/<int:post_id>')
class BookmarkAdd(Resource):
    @staticmethod
    def post(post_id):
        bookmark_service.add_bookmark(post_id)
        return '', 201


@bookmark_ns.route('/remove/<int:post_id>')
class BookmarkRemove(Resource):
    @staticmethod
    def delete(post_id):
        print(post_id)
        return bookmark_service.delete_bookmark(post_id), 204
