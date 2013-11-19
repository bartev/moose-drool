# Package development

install.packages('devtools', dependencies=TRUE)

# Check to make sure everything is installed
library(devtools)
has_devel()
# create('mypackage')