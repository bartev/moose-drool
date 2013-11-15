###R code for: Extracting information from objects using names()
###March 2013
###Slawa Rokicki srokicki@fas.harvard.edu

##read in Rdata

load("mydata.Rdata")

##column names
names(mydata)
my.col.names<-names(mydata)
class(my.col.names)
length(my.col.names)

##subsetting generally
mydata.subset<-mydata[,c(1:2)]

##use subsetting to get the column name you want

names(mydata)[4]<-"Weight_lbs"
names(mydata)


##1. Summary objects

sum.vec<-summary(mydata$Age)
sum.vec
names(sum.vec)
sum.vec[1]
sum.vec[c(2,3,5)]

tab1<-table(mydata$Race, mydata$Sex)
tab1
summary(tab1)
names(summary(tab1))

summary(tab1)$p.value

###2.  linear regression

##basic liner model object
reg.object<-lm(Weight_lbs~Height+Age, data=mydata)
names(reg.object)
mean(reg.object$residuals)

#summarize lm object
summary(reg.object)
names(summary(reg.object))

##other stats objects
aov.ob<-aov(reg.object)
names(aov.ob)

tt<-t.test(mydata$Age[mydata$Sex==1], mydata$Age[mydata$Sex==0])
names(tt)

names(chisq.test(mydata$Age))

##3. using names on histograms
reg.object$residuals
h<-hist(reg.object$residuals, main="Distribution of Residuals" ,xlab="Residuals")

b<-boxplot(mydata$Weight_lbs~mydata$Race, main="Boxplots by Race", ylab="Weight")
names(b)
b$stats

