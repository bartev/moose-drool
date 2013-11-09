
library("shiny")

if(!"googleVis" %in% installed.packages()) install.packages("googleVis", repos = "http://ftp5.gwdg.de/pub/misc/cran/")
library("googleVis")

load('data.RData')

#Buiding a HTML Table

shinyUI(pageWithSidebar(
  headerPanel(tags$body(tags$img(src="eoda_logo.png", width = "400px", align ="right"),
                        h1("Life-Expectancy ~ GDP per capita"),
                        h2("(random Country preselection)"),
                        h5("sometimes changes doen't take effect immediatly in this case please refresh the whole page"))),
  
  sidebarPanel(
    selectInput('xAchse', 'X Axis', c('GDP', 'log. GDB')),
    checkboxInput(inputId = 'all',label = 'all countries', value = TRUE),
    conditionalPanel(condition = 'input.all == true',
                     checkboxGroupInput(inputId = 'country_filter1',
                                        label = 'Countries', unique(data$Country),
                                        selected = unique(data$Country))),
    conditionalPanel(condition = 'input.all == false',
                     checkboxGroupInput('country_filter2',
                                        label = 'Countries', choices = unique(data$Country)))
  ),
  mainPanel(h3("MotionChart"),
            h4("(circle-size = population in tsd)"),
            htmlOutput(outputId = "main_plot"),
            h3("World Map"),
            h4("(colour range = GDP per capita/ additional Life-Expectancy per MouseOver Effect)"),
            htmlOutput(outputId = "map"),
            sliderInput(inputId = "year_filter",
                        label = "Year",
                        min = 1960,
                        max = 2008,
                        value = 2008,
                        format = "####")
  )
))
