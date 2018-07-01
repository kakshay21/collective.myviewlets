from plone.app.layout.viewlets import ViewletBase
from datetime import datetime


CONFERENCE_START_DATE = datetime(2018, 11, 5)


class DaysToConferenceViewlet(ViewletBase):

    def get_date(self):
        return CONFERENCE_START_DATE
