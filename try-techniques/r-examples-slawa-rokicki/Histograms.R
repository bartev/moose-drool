###R code for: Histograms
###December 2012
###Slawa Rokicki srokicki@fas.harvard.edu

##Create normal data

BMI<-rnorm(n=1000, m=24.2, sd=2.2) 
hist(BMI)

###save the histogram into an object called histinfo and print the results
histinfo<-hist(BMI)
histinfo

##change breaks

par(mfrow=c(1,2))
hist(BMI, breaks=20, main="Breaks=20")
hist(BMI, breaks=5, main="Breaks=5")

par(mfrow=c(1,1))
hist(BMI, breaks=c(17,20,23,26,29,32), main="Breaks is vector of breakpoints")
hist(BMI, breaks=seq(17,32,by=3), main="Breaks is vector of breakpoints")

##change to density instead of frequency
hist(BMI, freq=FALSE, main="Density plot")

##breaks are separated by 1
hist1<-hist(BMI, plot=FALSE)
hist1$density
sum(hist1$density)

##breaks are not separated by 1
hist2<-hist(BMI, plot=FALSE, breaks=c(17, 25, 26, 32))
hist2$density
sum(hist2$density)
sum(diff(hist2$breaks)*hist2$density)


##change aethetics

hist(BMI, xlab="Body Mass Index", freq=FALSE, main="Distribution of Body Mass Index", col="lightgreen", xlim=c(15,35),  ylim=c(0, .20))

##add a normal curve to the plot
curve(dnorm(x, mean=mean(BMI), sd=sd(BMI)), add=TRUE, col="darkblue", lwd=2) 






