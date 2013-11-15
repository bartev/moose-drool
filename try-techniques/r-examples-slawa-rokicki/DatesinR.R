###R code for: Dates in R
###July 2013
###Slawa Rokicki srokicki@fas.harvard.edu

##Dates in R

#libraries you will need:
library(date)
library(chron)


##Numeric Dates 

#set up data
dates<-as.data.frame(cbind(c(1,3,6,11,4,12,5,3), 
                           c(30,14,NA,NA,16,NA,20,31), 
                           c(1980, 1980, 1980, 1983,1983, 1983, 1986, 1980), 
                           c(2, NA, NA, NA, NA, 12, 4, NA), 
                           c(2, NA, NA, NA, NA, NA, 29, NA), 
                           c(1980, NA, NA, 1985, NA, 1983, 1987, NA)))
colnames(dates)<-c("birth_month", "birth_day", "birth_year", "death_month", "death_day", "death_year")
dates


#create ISOdate using POSIXt class, just from base R
dates$DOB<-ISOdate(dates$birth_year, dates$birth_month, dates$birth_day)
class(dates$DOB)

#strptime so that the formatting loses the time component
dates$DOB<-strptime(dates$DOB, format="%Y-%m-%d")
dates$DOD<-strptime(ISOdate(dates$death_year, dates$death_month, dates$death_day), format="%Y-%m-%d")


##intervals in time, calculate age at death
dates$Age.atdeath<-difftime(dates$DOD, dates$DOB, unit="days")
dates$Age.atdeath
class(dates$Age.atdeath)

#check if there were an infant mortalities
dates$Age.atdeath<365

#change to numeric
dates$Age.atdeath<-as.numeric(difftime(dates$DOD, dates$DOB, unit="days"))
class(dates$Age.atdeath)

##deal with the NAs by assigning largest possible age
dates$DOB2<-strptime(ISOdate(year=dates$birth_year, 
                             month=ifelse(is.na(dates$birth_month), 1, dates$birth_month), 
                             day=ifelse(is.na(dates$birth_day),1, dates$birth_day)), 
                     format="%Y-%m-%d")

dates$DOD2<-strptime(ISOdate(year=dates$death_year, 
                             month=ifelse(is.na(dates$death_month),12,dates$death_month), 
                             day=ifelse(is.na(dates$death_day),30, dates$death_day)), 
                     format="%Y-%m-%d")

dates$Ageatdeath_2<-as.numeric(difftime(dates$DOD2,dates$DOB2,unit="days"))

dates[,c(1:6,10:12)]


###Character Dates

#can always pull apart with substr
dates2<-as.data.frame(cbind(c(1:5), 
                            c("8/31/70", "NA", "10/12/60", "1/1/66", "12/31/80"), 
                            c("8/31/56", "12-31-1977", "12Aug55", "July 31 1965" ,"30jan1952")))
colnames(dates2)<-c("ID", "date_factor", "date_horrible")
dates2

#if reading a table in and first two columns are date - to keep as character do:
df <- read.table("data_with_dates.txt", header = TRUE, as.is = 2:3)

#NO: this gives an error, you can't do this with characters, need the date format
dates2$age<-difftime("02/27/13", as.character(dates2$date_factor), unit="days")

#YES: this is correct (although gives warnings about the NA entry)
library(chron)
dates2$date.fmt<-chron(as.character(dates2$date_factor), format="m/d/y")
class(dates2$date.fmt)
dates2[,c(1,2,4)]


#to format it differently (outgoing format)
dates2$date.fmt<-chron(as.character(dates2$date_factor), format="m/d/y", out.format="month day year")
dates2[,c(1,2,4)]

#calculate age using difftime as before
dates2$age<-as.numeric(floor(difftime(chron("03/01/2013"), dates2$date.fmt, unit="days")/360))
dates2[c(1,2,4,5)]

#Add a day to everyone's date for some reason
dates2$date.fmt+1

#Compare the date to some other date to see which came first using < operator
dates2$date.fmt<chron("04/02/62")


##If your data is terrible and everything is in a different format

#NO: chron needs the same format
chron(as.character(dates2$date_horrible))

#YES: as.date will do it when enclosed with as.Date, now a date object
library(date)
as.date(as.character(dates2$date_horrible))

#adds it as the number of days since 1960 to the dataframe
dates2$date_autofmt<-as.date(as.character(dates2$date_horrible))
dates2[,c(1,3,6)]

#fix this with as.Date
dates2$date_amazing<-as.Date(as.date(as.character(dates2$date_horrible)))
dates2[,c(1,3,7)]

