###R code for: From Continuous to Categorical
###October 2012
###Slawa Rokicki srokicki@fas.harvard.edu


##Create some data
mydata<-as.data.frame(cbind(c(1,2,3,4),c(26,12,15,7),c(1,0,1,1)))
colnames(mydata)<-c("ID","Age","Sex")

##Cut Age into categorical using various techniques
mydata$Agecat1<-cut(mydata$Age, c(0,5,10,15,20,25,30))
mydata$Agecat2<-cut(mydata$Age, seq(0,30,5))
mydata$Agecat3<-cut(mydata$Age, seq(0,30,5), right=FALSE)
mydata$Agecat4<-cut(mydata$Age, seq(0,30,5), right=FALSE, labels=c(1:6))

##Do a table of this age category against sex
table(mydata$Agecat1, mydata$Sex)

##Summarize the age categorical variables
summary(mydata$Agecat1)



