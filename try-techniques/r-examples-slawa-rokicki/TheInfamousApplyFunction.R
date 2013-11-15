###R code for: The Infamous Apply Function
###September 2012
###Slawa Rokicki srokicki@fas.harvard.edu


###Example 1
##Create some births data
births<-as.data.frame(cbind(c(2,1,1,1,1),c(NA,1,1,2,1), c(NA,1,1,NA,3),c(NA,1,NA,NA,1),c(NA,1,NA,NA,NA)))
colnames(births)<-c("outcome_01", "outcome_02","outcome_03","outcome_04","outcome_05")
for(i in 1:5){births[,i]<-factor(births[,i], levels=c(1,2,3),labels=c("live birth","lost","still birth"))}

##use Apply to get the sum of the live births by counting over a row the number of times it sees "live birth"
births$childcount<-apply(births[,1:5], MARGIN=1, function(x) {sum(x=="live birth", na.rm=TRUE)}) 

###Example 2
##Create some data
originaldata<-cbind(c(1,2,3,4),c(99,12,15,-99),c(1,2,1,1),c(1,2,99,1),c(1,2,3,1),c(-99,99,1,1))
colnames(originaldata)<-c("ID","Age","Sex","Var1","Var2","Var3")

##Apply to this original data, across the columns, the function where it takes the columns and replaces it with NA if it equals 99 or -99, and leaves it alone otherwise
newdata<-apply(originaldata[,c(2,4:6)], MARGIN=2, function(x) {ifelse(x==99 | x==-99, NA,x)})

##Combine original data with newdata, replacing the columns we changed
alldata<-cbind(originaldata[,c(-2,-4:-6)],newdata )

##Do the whole thing in one step
newdata<-cbind(apply(originaldata[,c(2,4:6)], MARGIN=2, function(x) {ifelse(x==99 | x==-99, NA,x)}), originaldata[,c(-2,-4,-6)])
