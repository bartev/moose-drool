###R code for: What a nice looking scatterplot!
###October 2012
###Slawa Rokicki srokicki@fas.harvard.edu


##Set working directory
# setwd("/Putyourdirectoryhere")

####CSV files##################
##Read in CSV file
mydata<-read.csv(file="mydata.csv")
mydata

##Plot 3 columns against each other
plot(mydata[,c(2,4,5)])


##Set up plot area
par(mfrow=c(1,1))

##Plot Height vs Weight
plot(mydata$Weight, mydata$Height)

##Add some features: x and y labels, x and y axes specification, title, plot symbol, colors
plot(mydata$Weight, mydata$Height, xlab="Weight (lbs)", ylab="Height (inches)", xlim=c(80,200), ylim=c(55,75), main="Height vs Weight", pch=2, cex.main=1.5, frame.plot=FALSE , col="blue")

##Change the color depending on the sex
plot(mydata$Weight, mydata$Height, xlab="Weight (lbs)", ylab="Height (inches)", xlim=c(80,200), ylim=c(55,75), main="Height vs Weight", pch=2, cex.main=1.5, frame.plot=FALSE, , col=ifelse(mydata$Sex==1, "red", "blue"))

##Add a legend to the above plot
legend(80, 75, pch=c(2,2), col=c("red", "blue"), c("Male", "Female"), bty="o", cex=.8, box.col="darkgreen")

##This adds the same legend but uses "topleft" instead of points (80,75)
legend("topleft", pch=c(2,2), col=c("red", "blue"), c("Male", "Female"), bty="o", cex=.8, box.col="darkgreen")

##Set up plot area - one row by 2 columns
par(mfrow=c(1,2))

##First plot: Plot Height vs Weight again
plot(mydata$Weight, mydata$Height, xlab="Weight (lbs)", ylab="Height (inches)", xlim=c(80,200), ylim=c(55,75), main="Height vs Weight", pch=2, cex.main=1.5, frame.plot=FALSE, col="blue")

##Add an orange vertical line for the mean of Weight
abline(v=mean(mydata$Weight, na.rm=TRUE), col="orange")

##Add text to the plot to describe the orange line
text(140,73, cex=.8, pos=4, "Orange line is\n sample average\n weight")

##Second plot: Plot Height vs Age
plot(mydata$Age, mydata$Height, xlab="Age (years)", ylab="Height (inches)", xlim=c(0,80), ylim=c(55,75), main="Height vs Age", pch=3, cex.main=1.5, frame.plot=FALSE, col="darkred")

##Linear regression line of Height on Age
reg<-lm(Height~Age, data=mydata)

##Add the regression line to the plot
abline(reg)

##Add text to the plot describing the regression line
text(0,72, paste("Height ~ ",round(reg$coef[1],2),"+",round(reg$coef[2],2),"*Age"), pos=4, cex=.8)





