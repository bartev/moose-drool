###R code for: For loops (and how to avoid them)
###January 2013
###Slawa Rokicki srokicki@fas.harvard.edu

##set working directory and load data (Rdata format)
setwd("insert_pathname_here")
load("mydata.Rdata")

##failed code
if(mydata$Age<10) mydata$Agegroup<-2

##super long way to get an old/young indicator - DONT DO THIS
mydata$Agegroup1<-0
for (i in  1:10){
  if(mydata$Age[i]>10 & mydata$Age[i]<20){
    mydata$Agegroup1[i]<-1
  }
  if(mydata$Age[i]>=20){
    mydata$Agegroup1[i]<-2
  }
}


###ifelse basic example
mydata$Old<-ifelse(mydata$Age>40,1,0)

##Faster way to do the agegroup example above
mydata$Agegroup2<-ifelse(mydata$Age>10 & mydata$Age<20,1, ifelse(mydata$Age>20, 2,0))

##Or use cut - remember to change first to character, then to numeric
mydata$Agegroup3<-as.numeric(as.character(cut(mydata$Age, c(0,10,20,100),labels=0:2)))


##other ways to use the ifelse function

##mean by another variable
mydata$meanweight.bysex<-ifelse(mydata$Sex==0, mean(mydata$Weight[mydata$Sex==0], na.rm=TRUE),
                                mean(mydata$Weight[mydata$Sex==1], na.rm=TRUE))

mydata[,c(1:4,14)]

##recoding
mydata$Height<-ifelse(is.na(mydata$Height),9999,mydata$Height)

##new id variable
mydata$year<-c(rep(1990,4),1995,1998, rep(2000,3), 1992)
mydata$ID.long<-ifelse(mydata$ID<10, paste(mydata$year, "-0",mydata$ID,sep=""), 
                       paste(mydata$year, "-", mydata$ID, sep=""))

rstudio::viewData(mydata[,c(1,2,3,16,17)])



