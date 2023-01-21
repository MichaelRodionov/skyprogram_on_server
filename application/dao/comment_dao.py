from application.dao.models.models import Comment


class CommentDAO:
    def __init__(self, session):
        self.session = session

    def get_comments_by_post_id(self, post_id):
        return self.session.query(Comment.comment, Comment.commenter_name).\
            filter(Comment.post_id == post_id)
