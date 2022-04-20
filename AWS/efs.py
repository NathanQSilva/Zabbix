#!/usr/bin/python
from basic_discovery import BasicDiscoverer

class Discoverer(BasicDiscoverer):
    def discovery(self, *args):
        response = self.client.describe_file_systems()
        data = list()
        for instance in response["FileSystems"]:
            ldd_name = {
                    "{#EFS_ID}": instance["FileSystemId"],
                    "{#EFS_NAME}": instance["Name"]
            }
            data.append(ldd_name)
        return data