###R code for: Quick and Easy Subsetting
###October 2012
###Slawa Rokicki srokicki@fas.harvard.edu


##Create some data
mydata<-as.data.frame(cbind(c(1:8),c(26,65,15,7,80,43,28,66),c(1,0,1,1,0,1,1,1), c(132, 122, 184, 145, 143, 137, 128, 154), c(60, 65, 67, 59, 64, 63, 67, 60)))
colnames(mydata)<-c("ID","Age","Sex", "Weight", "Height")

##Subset using subset function, by age
sub.data<-subset(mydata, Age>50)

##Subset by Age and Sex, selecting only ID, Age, and Weight columns
sub.data2<-subset(mydata, Age>50 & Sex==0, select=c(ID, Age, Weight))

##Subset by Age all columns between ID and Sex 
sub.data2<-subset(mydata, Age>50, select=c(ID:Sex))


##Subset using indexing

##Subset all rows, columns 1-3
sub.data3<-mydata[,c(1:3)]

##Subset rows where age>50, sex==0, and columns 1-3
sub.data4<-mydata[mydata$Age>50 & mydata$Sex==0, c(1:3)]

##Other types of subsetting (won't work on this dataset since it's too small)
##Subset rows 1-50 and all rows
sub.data5<-mydata[c(1:50), ]

##Subset all rows and a selection of columns
sub.data6<-mydata[,c(1:5, 8, 12:15, 100:120, 197, 199)]

##Subset all rows and everything EXCEPT columns 190-200
sub.data6<-mydata[,-c(190:200)]







