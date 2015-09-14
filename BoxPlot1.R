rm(list=ls())

intertime <- read.csv(file="7hr_NGRID.txt.analysis.csv",sep=",",head=TRUE)

boxplot(intertime$Time_Between_Products.ms., outline=TRUE, ylab="Time Between Products (ms)")
#ylim=c(0,9500)
