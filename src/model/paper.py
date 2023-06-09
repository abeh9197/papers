"""
Define papers to object.
"""


from datetime import datetime, timedelta
from process.xml import parse


class Paper:
    """
    All args from xml. Need to parse it.
    """
    def __init__(self, entry: str) -> None:
        self.abstract = parse(entry, "summary")[0].replace('\n', '')
        self.date = parse(entry, "published")[0]
        self.title = parse(entry, "title")[0]
        self.url = parse(entry, "id")[0]

    @property
    def is_todays_entry(self) -> bool:
        """
        Validate entry is todays.
        """
        yesterday = datetime.today() - timedelta(days=1)
        return self.date[0:10] == str(yesterday.strftime('%Y-%m-%d'))
