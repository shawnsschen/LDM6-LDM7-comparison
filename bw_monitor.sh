#!/bin/bash

tcpdump -s 70 -i eth1 -w tmp.pcap
pid=$!
sleep 25200
kill -s SIGINT $pid
