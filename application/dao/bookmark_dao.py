from application.dao.models.models import Bookmark


class BookmarkDAO:
    def __init__(self, session):
        self.session = session

    def get_all_bookmarks(self):
        return self.session.query(Bookmark).all()

    def add_new_bookmark(self, bookmark):
        self.session.add(bookmark)
        self.session.commit()

    def delete_bookmark(self, post_id):
        bookmark = self.session.query(Bookmark).filter(post_id == Bookmark.post_id).first()
        self.session.delete(bookmark)
        self.session.commit()
        return ""
