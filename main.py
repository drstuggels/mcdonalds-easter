import re
from sys import argv

from mitmproxy import http, options, proxy
from mitmproxy.addons import core
from mitmproxy.tools.dump import DumpMaster

port = 8080
debug = False

score = int(argv[1])

url = "https://egghunt-prd-mcdfi.mcdapps.com/ajax.php?t=save_game_score"


class ChangeScore:
    def request(self, flow: http.HTTPFlow):
        req = flow.request
        if req.pretty_url == url:
            content = req.get_content()
            modified = modifyScore(content)

            req.set_content(modified)


def start():
    opts = options.Options(listen_port=port)
    pconf = proxy.config.ProxyConfig(opts)

    m = DumpMaster(opts, with_termlog=debug, with_dumper=debug)
    m.server = proxy.server.ProxyServer(pconf)

    m.addons.add(ChangeScore())

    try:
        print("Proxy listening at", port)
        m.run()
    except KeyboardInterrupt:
        m.shutdown()


def modifyScore(content: bytes):
    string = content.decode("utf-8")

    string = re.sub("(?<=score=)(.*?)(?=&)", str(score), string)

    byte = bytes(string, "utf-8")

    return byte


if __name__ == '__main__':
    start()
