from application.dao.post_dao import PostDAO
from application.dao.comment_dao import CommentDAO
from application.dao.bookmark_dao import BookmarkDAO
from application.services.post_service import PostService
from application.services.comment_service import CommentService
from application.services.bookmark_service import BookmarkService
from database.setup_db import db


# ----------------------------------------------------------------
# creating objects of dao
post_dao = PostDAO(db.session)
comment_dao = CommentDAO(db.session)
bookmark_dao = BookmarkDAO(db.session)


# ----------------------------------------------------------------
# creating objects of services
post_service = PostService(post_dao)
comment_service = CommentService(comment_dao)
bookmark_service = BookmarkService(bookmark_dao)
