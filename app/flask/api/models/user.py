from api.database import db, ma


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def searchBy(id):
        return db.session.query(User)\
            .filter(User.id == id)\
            .first()

    def searchAll():
        return db.session.query(User).all()

    def create(user):
        user_record = User(
            id=user['id'],
            name=user['name']
        )

        db.session.add(user_record)
        db.session.commit()
        return User.searchBy(user_record.id)

    def update(id, user):
        user_record = db.session.query(User).filter(User.id == id).first()
        user_record.name = user['name']

        db.session.commit()
        return User.searchBy(user_record.id)

    def delete(id):
        user_record = db.session.query(User).filter(User.id == id).first()

        db.session.delete(user_record)
        db.session.commit()
        return

    def __repr__(self):
        return '<Entry id={id} name={name!r}>'.format(
            id=self.id, name=self.name)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


users_schema = UserSchema(many=True)
