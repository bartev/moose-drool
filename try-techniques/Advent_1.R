# Goes with Advent1.Rmd

# Doesn't work - no RWordPress for R 3.0
opts_knit$set(upload.fun = WrapWordpressUpload, base.url = NULL)
opts_chunk$set(fig.width = 5, fig.height = 5, cache = FALSE)

WrapWordpressUpload = function(file) {
  require(RWordPress)
  result = RWordPress::uploadFile(file)
  result$url
}

library(knitr)
options(WordPressLogin = c(bartev = pswd), WordPressURL = "http://bartev.wordpress.com/xmlrpc.php")

# knit2pdf("Advent1.Rmd", 'Advent1.pdf')

# ?knit2pdf
# ?knit2wp
# ls(package:knitr)