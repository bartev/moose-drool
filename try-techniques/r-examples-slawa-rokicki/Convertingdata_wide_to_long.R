###R code for: Converting a dataset from wide to long
###January 2013
###Slawa Rokicki srokicki@fas.harvard.edu

##read in data
births.wide<-read.csv("births_wide.csv")


###using reshape function

########first example
births.long1<-reshape(births.wide, varying=c("b2_01","b2_02","b2_03", "b4_01", "b4_02", "b4_03"), direction="long", idvar="caseid", sep="_")

########cleaned up example
births.long2<-reshape(births.wide, varying=c(3:8), direction="long", idvar="caseid", sep="_", timevar="order")

#reorder by caseid
births.long2<-births.long2[order(births.long2$caseid),]

#rename columns
names(births.long2)<-c("subject","age","order","birthyear","childsex")

#delete all NAs
births.long2<-na.omit(births.long2)






