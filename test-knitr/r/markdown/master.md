Main Rmd
========================================================

Run something here

```r
# getwd() opts_chunk$get('root.dir') opts_knit$get('root.dir')

# opts_chunk$set(root.dir='../..') Set root directory when knitting
opts_knit$set(root.dir = "../..")

opts_chunk$set(aliases = c(h = "fig.height", w = "fig.width", oh = "out.height", 
    ow = "out.width", cap = "fig.cap", scap = "fig.scap"), eval.after = c("fig.cap", 
    "fig.scap"))
opts_chunk$set(dev = c("png"), fig.path = "graphics/", fig.keep = "high", fig.align = "center", 
    comment = NA, tidy = TRUE)
opts_chunk$set(oh = 4, ow = 6, h = 4, w = 8)

options(replace.assign = TRUE, width = 50)
options(stringsAsFactors = FALSE, papersize = "letter")
# opts_knit$get('root.dir') base(opts_knit$get('root.dir'))
getwd()
```

```
## [1] "/Users/bvartanian/Development/moose-drool/test-knitr/r/markdown"
```


---

set global options

```r
# wd <- getwd()
opts_chunk$get("root.dir")
```

```
NULL
```

```r
# opts_chunk$set(root.dir=wd)
# opts_chunk$get('root.dir')

# load('r/raw/basic-r-script.R')
source("r/raw/basic-r-script.R")

system("ls")
source("./r/raw/basic-r-script.R")
ls()
```

```
[1] "a"              "check.packages"
[3] "df"             "x"             
[5] "y"             
```


--- 


```r
x <- rnorm(2000)
y <- x + rnorm(2000)
df <- data.frame(x, y)
ggplot(df, aes(x, y)) + geom_point() + geom_smooth()
```

<img src="graphics/plot-something.png" title="plot of chunk plot-something" alt="plot of chunk plot-something" style="display: block; margin: auto;" />


---


```
R version 3.0.1 (2013-05-16)
Platform: x86_64-apple-darwin10.8.0 (64-bit)

locale:
[1] en_US.UTF-8/en_US.UTF-8/en_US.UTF-8/C/en_US.UTF-8/en_US.UTF-8

attached base packages:
[1] graphics  grDevices utils     datasets 
[5] stats     methods   base     

other attached packages:
[1] codetools_0.2-8 Cairo_1.5-2    
[3] mgcv_1.7-22     markdown_0.6.3 
[5] knitr_1.4.1     devtools_1.3   
[7] plyr_1.8        stringr_0.6.2  
[9] ggplot2_0.9.3.1

loaded via a namespace (and not attached):
 [1] cairoDevice_2.19   colorspace_1.2-2  
 [3] dichromat_2.0-0    digest_0.6.3      
 [5] evaluate_0.4.7     formatR_0.9       
 [7] grid_3.0.1         gtable_0.1.2      
 [9] httr_0.2           labeling_0.2      
[11] lattice_0.20-15    MASS_7.3-26       
[13] Matrix_1.0-12      memoise_0.1       
[15] munsell_0.4.2      nlme_3.1-109      
[17] parallel_3.0.1     proto_0.3-10      
[19] RColorBrewer_1.0-5 RCurl_1.95-4.1    
[21] reshape2_1.2.2     scales_0.2.3      
[23] tcltk_3.0.1        tools_3.0.1       
[25] whisker_0.3-2     
```



