# using shiny

install.packages('rdatamarket')
install.packages('shiny')
library('rdatamarket')
library('shiny')

# get data from datamarket.com
# life_expectancy and gdp
dminit('ba22bf5bdf044aaf980cdbde3504248c')
life_expectancy <- dmlist('15r2!hrp')
head(life_expectancy)
str(life_expectancy)

gdp <- dmlist('15c9!hd1')
head(gdp)

# popultation
dminit("ba22bf5bdf044aaf980cdbde3504248c")
population <- dmlist("1cfl!r3d")

# rename the value variable
names(gdp)[3] <- 'GDP'
names(life_expectancy)[3] <- 'life_expectancy'
names(population)[3] <- 'Population'

# merge to one dataframe
data <- merge(gdp, life_expectancy, by=c('Country', 'Year'))
data <- merge(data, population, by=c('Country', 'Year'))

# data is only until 2008 complete
data <- data[data$Year <= 2008, ]

# reducint data for only a few countries
data$Country <- as.character(data$Country)

selection <- c('Afghanistan', 'Armenia', 'Brazil', 
               'Spain', 'France', 'United States', 
               'United Kingdom')

data <- subset(data, Country %in% selection)

# Saveing the data
save(data, file='shiny_beispiel/data.RData')

#run shiny app localy
runApp("shiny_beispiel")
