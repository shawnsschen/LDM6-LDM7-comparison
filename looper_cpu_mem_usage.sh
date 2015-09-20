#!/bin/bash

for i in `seq 1 431`; do
        bash /home/ldm7/LDM6-LDM7-comparison/cpu_mem_usage.sh &
        sleep 60
done
