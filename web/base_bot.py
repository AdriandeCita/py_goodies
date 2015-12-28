import urllib
import urllib.request

# Basic class for different operations in web.
class HttpClient:

    def __init__(self, proxy=None, user_agent='Mozilla/5.0'):

        self.http_handler = urllib.request.HTTPHandler()

        if proxy:
            self.proxy_handler = urllib.request.ProxyHandler(proxy)
            self.opener = urllib.request.build_opener(
                self.proxy_handler,
                self.http_handler)
        else:
            self.opener = urllib.request.build_opener(
                self.http_handler)

        self.opener.addheaders = [('User-agent', user_agent)]

        urllib.request.install_opener(self.opener)

    def request(self, url, params={}, timeout=5):
# Returns html responce object as raw bytes

        if params:
            params = urllib.parse.urlencode(params)
            html = self.opener.open(url, params, timeout)

        else:
            req = urllib.request.Request(url)
            html = self.opener.open(req)

        return html.read()
