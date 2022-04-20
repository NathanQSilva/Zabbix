#!/usr/bin/python
from basic_discovery import BasicDiscoverer


class Discoverer(BasicDiscoverer):
    def discovery(self, *args):
        response = self.client.describe_load_balancers()
        data = list()
        for balancer in response["LoadBalancers"]:
            tg = self.client.describe_target_groups(LoadBalancerArn=balancer["LoadBalancerArn"])
            for target in tg["TargetGroups"]:

               ldd = {
                       "{#BALANCER_NAME}":      balancer["LoadBalancerName"],
                       "{#BALANCER_ARN}":       "app"+balancer["LoadBalancerArn"].split('app')[1],
                       "{#TARGET_ARN}":    "targetgroup"+target["TargetGroupArn"].split('targetgroup')[1]
               }
               data.append(ldd)
        return data