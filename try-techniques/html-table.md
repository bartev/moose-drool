HTML tables
========================================================

Use melanoma data set in boot package

http://gforge.se/2014/01/fast-track-publishing-using-knitr-part-iv/#regression

```r
library(boot)

head(melanoma)
```

```
##   time status sex age year thickness ulcer
## 1   10      3   1  76 1972      6.76     1
## 2   30      3   1  56 1968      0.65     0
## 3   35      2   1  41 1977      1.34     0
## 4   99      3   0  71 1968      2.90     0
## 5  185      1   1  52 1965     12.08     1
## 6  204      1   1  28 1971      4.84     1
```

```r
summary(melanoma)
```

```
##       time          status          sex             age      
##  Min.   :  10   Min.   :1.00   Min.   :0.000   Min.   : 4.0  
##  1st Qu.:1525   1st Qu.:1.00   1st Qu.:0.000   1st Qu.:42.0  
##  Median :2005   Median :2.00   Median :0.000   Median :54.0  
##  Mean   :2153   Mean   :1.79   Mean   :0.385   Mean   :52.5  
##  3rd Qu.:3042   3rd Qu.:2.00   3rd Qu.:1.000   3rd Qu.:65.0  
##  Max.   :5565   Max.   :3.00   Max.   :1.000   Max.   :95.0  
##       year        thickness         ulcer      
##  Min.   :1962   Min.   : 0.10   Min.   :0.000  
##  1st Qu.:1968   1st Qu.: 0.97   1st Qu.:0.000  
##  Median :1970   Median : 1.94   Median :0.000  
##  Mean   :1970   Mean   : 2.92   Mean   :0.439  
##  3rd Qu.:1972   3rd Qu.: 3.56   3rd Qu.:1.000  
##  Max.   :1977   Max.   :17.42   Max.   :1.000
```

```r
nrow(melanoma)
```

```
## [1] 205
```

```r

# set time to years instead of days
melanoma$time_years <- melanoma$time / 365.25

# Factor the basic variables that we're interested in
melanoma$status <- factor(melanoma$status,
                          levels = c(2, 1, 3),
                          labels = c('Alive', #Reference
                                     'Melanoma death',
                                     'Non-melanoma death'))

melanoma$sex <- factor(melanoma$sex,
                       labels = c('Male', 'Female'))

melanoma$ulcer <- factor(melanoma$ulcer,
                         labels=c('Present', 'Absent'))
```


Load Gmisc package from source

```r
# reps = c('http://ftp.sunet.se/pub/lang/CRAN', 'http://cran.gforge.se')
# install.packages('Gmisc', repos=reps, dependencies=TRUE, type='source')
library(Gmisc)
```

```
## Loading required package: rms
```

```
## Loading required package: Hmisc
```

```
## Loading required package: cluster
```

```
## Loading required package: grid
```

```
## Loading required package: lattice
```

```
## Attaching package: 'lattice'
```

```
## The following object is masked _by_ '.GlobalEnv':
## 
## melanoma
```

```
## The following object is masked from 'package:boot':
## 
## melanoma
```

```
## Loading required package: survival
```

```
## Loading required package: splines
```

```
## Attaching package: 'survival'
```

```
## The following object is masked from 'package:boot':
## 
## aml
```

```
## Loading required package: Formula
```

```
## Hmisc library by Frank E Harrell Jr
## 
## Type library(help='Hmisc'), ?Overview, or ?Hmisc.Overview') to see overall
## documentation.
```

```
## Attaching package: 'Hmisc'
```

```
## The following object is masked from 'package:survival':
## 
## untangle.specials
```

```
## The following object is masked from 'package:base':
## 
## format.pval, round.POSIXt, trunc.POSIXt, units
```

```
## Loading required package: SparseM
```

```
## Attaching package: 'SparseM'
```

```
## The following object is masked from 'package:base':
## 
## backsolve
```

```
## Attaching package: 'rms'
```

```
## The following object is masked from 'package:Hmisc':
## 
## num.intercepts
```

```
## Loading required package: sandwich
```

```
## Loading required package: stringr
```


Using getDescriptionStatsBy

```r
# A function that takes the variale name, applies it to the melanoma
# dataset and then runs the results by the status variable
getT1Stat <- function(varname, digits = 0) {
    getDescriptionStatsBy(melanoma[, varname], melanoma$status, add_total_col = TRUE, 
        show_all_values = TRUE, hrzl_prop = TRUE, statistics = FALSE, html = TRUE, 
        digits = digits)
}

# Save everything in a list This simplifies the row grouping
table_data <- list()

# Get the basic stats
table_data[["Sex"]] <- getT1Stat("sex")
table_data[["Age"]] <- getT1Stat("age")
table_data[["Ulceraction"]] <- getT1Stat("ulcer")
table_data[["Thickness<sup>a</sup>"]] <- getT1Stat("thickness", 1)
```


After running the previous code I loop through the list to extract the variable matrix and the rgroup/n.rgroup variables that I then input to my htmlTable function

```r
# Merge everything into a matrix
rgroup <- c()
n.rgroup <- c()
output_data <- NULL
for (varlabel in names(table_data)) {
    output_data <- rbind(output_data, table_data[[varlabel]])
    rgroup <- c(rgroup, varlabel)
    n.rgroup <- c(n.rgroup, nrow(table_data[[varlabel]]))
}

# add a column spanner for the death columns
cgroup <- c("", "Death")
n.cgroup <- c(2, 2)
colnames(output_data) <- gsub("[ ]*death", "", colnames(output_data))

htmlTable(output_data, align = "rrrr", rgroup = rgroup, n.rgroup = n.rgroup, 
    rgroupCSSeparaor = "", cgroup = cgroup, n.cgroup = n.cgroup, rowlabel = "", 
    caption = "Basic stats", tfoot = "<sup>a</sup> Also known as Breslow thickness", 
    ctable = TRUE)
```

```
## <table class='gmisc_table' style='border-collapse: collapse;' >
## 	<caption align='top' style='text-align: left;'>
## 	Basic stats</caption>
## 	<thead>
## 	<tr>
## 		<th style='border-top: 2px solid grey;'></th>
## 		<th colspan='2' style='font-weight: 900; border-top: 2px solid grey;; text-align: center;'>&nbsp;</th><th style='border-top: 2px solid grey;; border-bottom: hidden;'>&nbsp;</th>
## 		<th colspan='2' style='font-weight: 900; border-bottom: 1px solid grey; border-top: 2px solid grey;'>Death</th>
## 	</tr>
## 	<tr>
## 		<th style='border-bottom: 1px solid grey; '>&nbsp;</th>
## 		<th style='border-bottom: 1px solid grey;; text-align: center;'>Total</th>
## 		<th style='border-bottom: 1px solid grey;; text-align: center;'>Alive</th>
## 		<th style='border-bottom: 1px solid grey;' colspan='1'>&nbsp;</th>
## 		<th style='border-bottom: 1px solid grey;; text-align: center;'>Melanoma</th>
## 		<th style='border-bottom: 1px solid grey;; text-align: center;'>Non-melanoma</th>
## 	</tr>
## 	</thead><tbody>
## 	<tr><td colspan='6' style='font-weight: 900;'>Sex</td></tr>
## 	<tr>
## 		<td style=' text-align: left;'>&nbsp;&nbsp;Male</td>
## 		<td style=';; text-align: right;'>126 (61 %)</td>
## 		<td style=';; text-align: right;'>91 (72 %)</td>
## 		<td style=';' colspan='1'>&nbsp;</td>
## 		<td style=';; text-align: right;'>28 (22 %)</td>
## 		<td style=';; text-align: right;'>7 (6 %)</td>
## 	</tr>
## 	<tr>
## 		<td style=' text-align: left;'>&nbsp;&nbsp;Female</td>
## 		<td style=';; text-align: right;'>79 (39 %)</td>
## 		<td style=';; text-align: right;'>43 (54 %)</td>
## 		<td style=';' colspan='1'>&nbsp;</td>
## 		<td style=';; text-align: right;'>29 (37 %)</td>
## 		<td style=';; text-align: right;'>7 (9 %)</td>
## 	</tr>
## 	<tr><td colspan='7' style='font-weight: 900; border-top: 1px solid grey;'>Age</td></tr>
## 	<tr>
## 		<td style=' text-align: left;'>&nbsp;&nbsp;Mean (SD)</td>
## 		<td style=';; text-align: right;'>52 (&plusmn;  17)</td>
## 		<td style=';; text-align: right;'>50 (&plusmn;  16)</td>
## 		<td style=';' colspan='1'>&nbsp;</td>
## 		<td style=';; text-align: right;'>55 (&plusmn;  18)</td>
## 		<td style=';; text-align: right;'>65 (&plusmn;  11)</td>
## 	</tr>
## 	<tr><td colspan='8' style='font-weight: 900; border-top: 1px solid grey;'>Ulceraction</td></tr>
## 	<tr>
## 		<td style=' text-align: left;'>&nbsp;&nbsp;Present</td>
## 		<td style=';; text-align: right;'>115 (56 %)</td>
## 		<td style=';; text-align: right;'>92 (80 %)</td>
## 		<td style=';' colspan='1'>&nbsp;</td>
## 		<td style=';; text-align: right;'>16 (14 %)</td>
## 		<td style=';; text-align: right;'>7 (6 %)</td>
## 	</tr>
## 	<tr>
## 		<td style=' text-align: left;'>&nbsp;&nbsp;Absent</td>
## 		<td style=';; text-align: right;'>90 (44 %)</td>
## 		<td style=';; text-align: right;'>42 (47 %)</td>
## 		<td style=';' colspan='1'>&nbsp;</td>
## 		<td style=';; text-align: right;'>41 (46 %)</td>
## 		<td style=';; text-align: right;'>7 (8 %)</td>
## 	</tr>
## 	<tr><td colspan='9' style='font-weight: 900; border-top: 1px solid grey;'>Thickness<sup>a</sup></td></tr>
## 	<tr>
## 		<td style='border-bottom: 2px solid grey;; text-align: left;'>&nbsp;&nbsp;Mean (SD)</td>
## 		<td style='border-bottom: 2px solid grey;; text-align: right;'>2.9 (&plusmn; 3.0)</td>
## 		<td style='border-bottom: 2px solid grey;; text-align: right;'>2.2 (&plusmn; 2.3)</td>
## 		<td style='border-bottom: 2px solid grey;' colspan='1'>&nbsp;</td>
## 		<td style='border-bottom: 2px solid grey;; text-align: right;'>4.3 (&plusmn; 3.6)</td>
## 		<td style='border-bottom: 2px solid grey;; text-align: right;'>3.7 (&plusmn; 3.6)</td>
## 	</tr>
## 	</tbody>
## 	<tfoot><tr><td colspan=9>
## 	<sup>a</sup> Also known as Breslow thickness</td></tr></tfoot>
## </table>
```

