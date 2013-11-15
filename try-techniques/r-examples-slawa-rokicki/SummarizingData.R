###R code for: Getting Data in and out of R
###October 2012
###Slawa Rokicki srokicki@fas.harvard.edu


##Read in Rdata

##Set working directory
# setwd("/Putyourdirectoryhere")

##Load file
##Set working directory
# setwd("/Putyourdirectoryhere")

####CSV files##################
##Read in CSV file and add migrant column
mydata<-read.csv(file="mydata.csv")
mydata$Migrantstatus<-c(1,0,1,1,0,1,1,1,0,0)
mydata$Migrantstatus<-factor(mydata$Migrantstatus, labels=c("Migrant", "Nonmigrant"))

mydata

##Do a summary of all the variables
summary(mydata)

##Table of Sex column, change to proportions using prop.table
table1<-table(mydata$Sex)
table1
prop.table(table1)

##Table of Sex by Marriage, change to proportion across rows and across columns
table2<-table(mydata$Sex, mydata$Married)
table2
prop.table(table2, margin=1)
prop.table(table2, margin=2)

##Table of Sex by Marriage and by Migrant Status
table3<-table(mydata$Sex, mydata$Married, mydata$Migrantstatus)
table3
table3[,,1]

##Aggregation Table of Mean Weight by Sex
aggtable<-aggregate(mydata$Weight, by=list(mydata$Sex), FUN=mean)
aggtable

##Take out the NAs
aggtable.narm<-aggregate(mydata$Weight, by=list(mydata$Sex), FUN=mean, na.rm=TRUE )
aggtable.narm

##Aggregation table of Mean Weight by Sex and Marital Status, add column names
aggtable.3<-aggregate(mydata$Weight, by=list(mydata$Sex, mydata$Married), FUN=mean, na.rm=TRUE )
names(aggtable.3)<-c("Sex","Married","Meanweight")
aggtable.3



