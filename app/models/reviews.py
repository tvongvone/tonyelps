from .db import db, environment, SCHEMA, add_prefix_for_prod


class Review(db.Model):
    __tablename__ = 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(1000), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)

    user = db.relationship("User", back_populates="reviews")

    def to_dict(self, add_user=False):
        review = {
            "id": self.id,
            "review": self.review,
            "userId": self.userId
        }

        if(add_user):
            review["user"] = self.user.to_dict()

        return review
