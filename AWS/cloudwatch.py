#!/usr/bin/python
import datetime
from basic_discovery import BasicDiscoverer
now= datetime.datetime.today()
#yesterday = now - datetime.timedelta(1)
class Discoverer(BasicDiscoverer):
    def discovery(self, *args):
        data = list()
        response = self.client.get_metric_statistics(Namespace='AWS/SES',MetricName='Reputation.BounceRate',StartTime=now - datetime.timedelta(days=1), EndTime=now, Period=86400, Statistics=['Maximum'])
        bounce = sorted(response["Datapoints"],key=lambda x: x['Timestamp'])[-1]["Maximum"]
        master_item = {
            "{#BOUNCE_PERCENT}": bounce
            }
        data.append(master_item)
        return data