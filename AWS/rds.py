#!/usr/bin/python
from basic_discovery import BasicDiscoverer


class Discoverer(BasicDiscoverer):
    def discovery(self, *args):
        response = self.client.describe_db_instances()
        data = list()
        for instance in response["DBInstances"]:
            storage_bytes = int(instance["AllocatedStorage"]) * pow(1024, 3)
            if len(args) >1:
              if len(args)>2:
                 args_group=args[1]+" "+args[2]
              else:
                 args_group=args[1]
              ldd = {
                    "{#SUFIXO}": args[0],
                    "{#GRUPO}": args_group,
                    "{#STORAGE}": storage_bytes,
                    "{#RDS_ID}": instance["DBInstanceIdentifier"],
                    "{#RDS_RESOURCE_ID}": instance["DbiResourceId"]
              }
            else:
              ldd = {
                    "{#STORAGE}": storage_bytes,
                    "{#RDS_ID}": instance["DBInstanceIdentifier"],
                    "{#RDS_RESOURCE_ID}": instance["DbiResourceId"]
              }
            data.append(ldd)
        return data