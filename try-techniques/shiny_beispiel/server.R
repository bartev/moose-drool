if(!"googleVis" %in% installed.packages()) install.packages("googleVis", repos = "http://ftp5.gwdg.de/pub/misc/cran/")
library("googleVis")

shinyServer(function(input, output) {
  
  load("data.RData")
  
  data$Population <- data$Population/1000
  
  output$main_plot <- renderGvis({
    
    if(input$xAchse == "log. GDB"){
      data$GDP <- log(data$GDP)
    }else{
      data$GDP <- data$GDP
    }
    
    if(input$all == TRUE){
      country_filter <- input$country_filter1
    }
    if(input$all == FALSE){
      country_filter <- input$country_filter2
    }
    
    
    #it seems that gvisMotionChart needs different variables for idvar and colorvar
    data$CountryCol <- data$Country
    
    gvisMotionChart(data[data$Country %in% country_filter,],
                    idvar = "Country",
                    timevar = "Year",
                    xvar = "GDP",
                    yvar = "life_expectancy",
                    colorvar = "CountryCol",
                    sizevar = "Population",
                    options = list(showChartButtons = FALSE,
                                   showSidePanel = FALSE,
                                   showXScalePicker = FALSE,
                                   showYScalePicker = FALSE)
    )
  })
  
  output$map <- renderGvis({
    
    if(input$all == TRUE){
      country_filter <- input$country_filter1
    }
    if(input$all == FALSE){
      country_filter <- input$country_filter2
    }
    
    year_filter <- input$year_filter
    
    data$hover <- paste0("Life-Expectancy ",data$Country,": ",round(data$life_expectancy))
    
    gvisGeoChart(data[data$Country %in% country_filter & data$Year == year_filter,], locationvar = "Country", colorvar = "GDP", hovervar = "hover")
  })
})
