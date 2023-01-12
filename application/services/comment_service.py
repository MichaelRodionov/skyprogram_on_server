from application.dao.comment_dao import CommentDAO


class CommentService:
    def __init__(self, comment_dao: CommentDAO):
        self.comment_dao = comment_dao

    def get_comments(self, post_id):
        return self.comment_dao.get_comments_by_post_id(post_id)
