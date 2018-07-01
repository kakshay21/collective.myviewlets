from plone.app.layout.viewlets import ViewletBase


class MessageViewlet(ViewletBase):

    def render(self):
        return u'Hope to se you there!'
