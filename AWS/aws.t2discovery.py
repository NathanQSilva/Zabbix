#!/bin/bash
ZABBIX_HOME=/etc/zabbix/scripts
cd $ZABBIX_HOME
if [ $# -gt 3 ]
    then
        ./aws_discovery.py --service $1 --region $2 --account $3 --args ${@:4}
    else
        ./aws_discovery.py --service $1 --region $2 --account $3
fi