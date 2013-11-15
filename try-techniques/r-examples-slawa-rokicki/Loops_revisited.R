###R code for: Loops revisited: How to rethink macros when using R
###October 2013
###Slawa Rokicki srokicki@fas.harvard.edu

#The R perspective

set.seed(10)
x<-rnorm(100,5,2)
z<-rnorm(100,6,5)
w<-rnorm(100,3,2)
y<-x*2+w*.5+rnorm(100,0,1)
ybin<-as.numeric(y<10)

mydata<-as.data.frame(cbind(x,z,w,y,ybin))


#Use of Maros outside of loops
summary(lm(y~x+z+w, data=mydata))
summary(lm(ybin~x+z+w, data=mydata))
summary(glm(ybin~x+z+w, family=binomial(logit), data=mydata))

#1. 'controlVars' 
xvars<-cbind(x,z,w)
summary(lm(ybin~xvars, data=mydata))
summary(glm(ybin~xvars, family=binomial(logit), data=mydata))

#2. 'if' conditional regression
data.sub<-as.data.frame(mydata[x>2 & z<3,c("x","z","ybin")])
xvars.sub<-as.matrix(data.sub[,c("x","z")])
summary(lm(ybin~xvars.sub, data=data.sub))

#3. looping over variables
apply(mydata[,c("y","ybin")], 2, function(outcome){summary(lm(outcome~x+z))})


#4. looping over parts of variable names
jan<-rnorm(100,3,5)
feb<-rnorm(100,4,8)
march<-rnorm(100,2,5)

months<-as.data.frame(cbind(jan,feb,march))
names(months)
head(months)

for (n in names(months)){
  months[[paste0("HadInc_",n)]] <- as.numeric(months[[n]]>0)
}
head(months)

#came from this: http://stackoverflow.com/questions/14324562/creating-new-named-variable-in-dataframe-using-loop-and-naming-convention

#check out what loop is doing by taking it apart
for (n in names(months)){
  print(n)
  print(months[[n]])
  print(paste0("HadInc_",n))
}

#5. Looping over varlists
names(months)<-toupper(names(months))
head(months)

#6. Looping over numbers
Inc1990<-rnorm(100,5,6)
Inc1991<-rnorm(100,3,8)
Inc1992<-rnorm(100,4,4)

Income<-as.data.frame(cbind(Inc1990, Inc1991, Inc1992))
years<-c(1990:1992)
head(Income)
for (i in seq(along=years)){
  Income[[paste0("hadInc_",years[i])]] <- as.numeric(Income[[i]]>0)
}
head(Income)

#7. Looping over values and levels of
race<-c(rep(1,30),rep(2,30),rep(3,40))
age<-rnorm(100,25,3)
y<-age*10+ifelse(race==1,100, ifelse(race==2, 2000, 0))+rnorm(100,0,1)

racedata<-as.data.frame(cbind(race,age,y))
racedata$race<-as.factor(racedata$race)

#two ways to use lapply
lapply(1:3, function(index) summary(lm(y~age, data=racedata[racedata$race==index,])))
lapply(as.numeric(levels(race)), function(index) summary(lm(y~age, data=racedata[racedata$race==index,])))








