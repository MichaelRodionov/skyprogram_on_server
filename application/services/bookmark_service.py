from sqlalchemy.orm.exc import UnmappedInstanceError

from application.dao.bookmark_dao import BookmarkDAO
from application.dao.models.models import Bookmark


class BookmarkService:
    def __init__(self, bookmark_dao: BookmarkDAO):
        self.bookmark_dao = bookmark_dao

    def get_bookmarks(self):
        return self.bookmark_dao.get_all_bookmarks()

    def add_bookmark(self, post_id):
        bookmark = Bookmark(post_id=post_id)
        self.bookmark_dao.add_new_bookmark(bookmark)

    def delete_bookmark(self, post_id):
        try:
            return self.bookmark_dao.delete_bookmark(post_id)
        except UnmappedInstanceError:
            return 'nothing to delete'
