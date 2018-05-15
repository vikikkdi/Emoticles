library(rvest) 
library(syuzhet)
library(dplyr) 
library(data.table)
library(zoo)

args<-commandArgs(TRUE)

h = ""

for(i in unlist(strsplit(args[1],':',fixed=TRUE))){h = paste(h,i,sep=" ")}

get_nrc_sentiment(h, cl = NULL, language = "english")