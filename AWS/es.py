#!/usr/bin/python
from basic_discovery import BasicDiscoverer


class Discoverer(BasicDiscoverer):
    def discovery(self, *args):
        response = self.client.list_domain_names()
        data = list()
        for domain in response["DomainNames"]:
            ldd = {
                "{#DOMAIN}": domain['DomainName'],
            }
            data.append(ldd)
        return data