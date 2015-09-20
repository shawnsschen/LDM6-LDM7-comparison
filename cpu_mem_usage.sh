#!/bin/bash

date '+%X' >> log_cpu_mem_usage.txt
ps -eo pcpu,pmem,rss,pid,args | grep "ldmd" >> log_cpu_mem_usage.txt
