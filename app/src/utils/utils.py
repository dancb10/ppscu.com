from urllib.parse import urlparse


class Utils:

    @staticmethod
    def extract_domain(url):
        full_domain = urlparse(url).netloc
        return full_domain.split(':')[0]
