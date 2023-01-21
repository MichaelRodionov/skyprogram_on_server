from application.dao.models.models import Post


# ----------------------------------------------------------------
# create post dao class to connect with database
class PostDAO:
    def __init__(self, session):
        self.session = session

    def get_all_posts(self):
        return self.session.query(Post).all()

    def get_one_post(self, post_id):
        return self.session.query(Post.pic, Post.poster_name, Post.
                                  poster_avatar, Post.content, Post.views_count,
                                  Post.likes_count).filter(Post.id == post_id).\
            first()

    def add_post(self, new_post):
        self.session.add(new_post)
        self.session.commit()

    def delete_post(self, post_id):
        post = self.session.query(Post).filter(Post.id == post_id).first()
        self.session.delete(post)
        self.session.commit()
        return ''
