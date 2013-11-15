###R code for: Getting Data in and out of R
###October 2012
###Slawa Rokicki srokicki@fas.harvard.edu


##Set working directory
setwd("/Putyourdirectoryhere")

####CSV files##################
##Read in CSV file
mydata<-read.csv(file="mydata_gettingdatainR.csv")
mydata

##Check out the class of the SBP column and change the periods to missing
class(mydata$SBP)
mydata$SBP<-as.numeric(ifelse(mydata$SBP==".", NA, mydata$SBP))

##Write a CSV file of the updated file
write.csv(mydata, file="mynewdata.csv")

####Stata files##################
##load the foreign library
library(foreign)

##Write a dta file from the mydata file
write.dta(mydata, file="mystatafile.dta")

##Read in a dta file
mystatadata<-read.dta(file="mystatafile.dta")

####SAS files##################
##Load the SASxport library
library(SASxport)

##Read and Write xpt files
write.xport(mydata, file="mysasfile.xpt")
mystatadata<-read.xport(file="mysasfile.xpt")

##Load the sas7bdat library
library(sas7bdat)
mysas7bdat<-read.sas7bdat(file="myothersasfile.sas7bdat")

