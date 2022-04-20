#!/usr/bin/python
from basic_discovery import BasicDiscoverer


class Discoverer(BasicDiscoverer):
    def discovery(self, *args):
        response = self.client.get_send_statistics()
        #print response
        data = list()
        b_count = 0
        d_count = 0
        t_count = 0
        for ses in response["SendDataPoints"]:
           b_count += int(ses["Bounces"])
           d_count += int(ses["DeliveryAttempts"])
        t_count += (b_count * 100.0) / d_count
        master_item = {
            "{#BOUNCE_PERCENT}": t_count,
            "{#DELIVERY_ATTEMPTS}": d_count,
            "{#BOUNCE}": b_count
            }
        data.append(master_item)
        return data