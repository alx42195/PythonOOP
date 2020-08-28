class LinksMaster:
    def __init__(self, url_full, url_short):
        self.url_full = url_full
        self.url_short = url_short

    @property
    def short_link(self):
        return self.url_short

    @short_link.setter
    def short_link(self, new_name):
        self.url_short = new_name

    @property
    def long_link(self):
        return self.url_full

    @long_link.setter
    def long_link(self, new_name):
        self.url_full = new_name

    def __repr__(self):
        return f"{self.url_full} | {self.url_short}"

    def __str__(self):
        return f"Short link: {self.url_short}, long link: {self.url_full}"