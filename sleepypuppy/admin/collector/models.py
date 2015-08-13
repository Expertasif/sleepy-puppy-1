from sleepypuppy import db
import datetime


class GenericCollector(db.Model):
    """
    Javascript model contains the following parameters:

    name = name of javascriopt file.
    code = code that will be executed when a sleepy puppy payload is executed
    notes = notes

    Javascript is many to many with payload.
    """
    __tablename__ = 'generic_collector'

    id = db.Column(db.Integer, primary_key=True)
    payload_id = db.Column(db.Integer, db.ForeignKey('payloads.id'))
    javascript_name = db.Column(db.String(500), nullable=False)
    data = db.Column(db.Text())
    url = db.Column(db.Text(), unique=False)
    referrer = db.Column(db.Text(), unique=False)
    pub_date = db.Column(db.String(512), unique=False)

    def as_dict(self):
        """Return Capture model as JSON object"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, payload_id, javascript_name, url, referrer, data, pub_date=None):
        self.payload_id = payload_id
        self.javascript_name = javascript_name
        self.url = url
        self.referrer = referrer
        self.data = data
        # Set datetime when a capture is recieved
        if pub_date is None:
            pub_date = str(datetime.datetime.now())
        self.pub_date = pub_date

    def __repr__(self):
        return str(self.payload_id)