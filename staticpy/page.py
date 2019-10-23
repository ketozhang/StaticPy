class Page(dict):

    def __init__(self, url, subpages=[], title=None, **kwargs):
        self.update({
            'url': url,
            'title': title,
            'subpages':  subpages,
            **kwargs})

        if self['title'] == None:
            self['title'] = self['url'].split('/')[-1]

    def __getitem__(self, key):
        return self.get(key)