Data Prep
========================================================

From http://www.r-bloggers.com/data-preparation-part-i/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+RBloggers+%28R+bloggers%29

## Using apply, lapply, tapply

```r
set.seed(123)
matriz <- matrix(round(runif(12, 1, 10), 0), nrow = 3)
```


apply(X, MARGIN, FUN, ...)
MARGIN = 1 = row
MARGIN = 2 = column
MARGIN = c(1, 2) = rows and columns


```r
matriz
```

```
##      [,1] [,2] [,3] [,4]
## [1,]    4    9    6    5
## [2,]    8    9    9   10
## [3,]    5    1    6    5
```

```r
apply(matriz, 1, sum)  # Sum by row
```

```
## [1] 24 36 17
```

```r
apply(matriz, 2, sum)  # Sum by column
```

```
## [1] 17 19 21 20
```

```r
apply(matriz, c(1, 2), function(x) x^2)  # square everything
```

```
##      [,1] [,2] [,3] [,4]
## [1,]   16   81   36   25
## [2,]   64   81   81  100
## [3,]   25    1   36   25
```


## tapply - useful on descriptive analysis
tapply(X, INDEX, FUN = NULL, ..., simplify = TRUE)
INDEX = list of one or more factors

```r
head(mtcars)
```

```
##                    mpg cyl disp  hp drat    wt  qsec vs am gear carb
## Mazda RX4         21.0   6  160 110 3.90 2.620 16.46  0  1    4    4
## Mazda RX4 Wag     21.0   6  160 110 3.90 2.875 17.02  0  1    4    4
## Datsun 710        22.8   4  108  93 3.85 2.320 18.61  1  1    4    1
## Hornet 4 Drive    21.4   6  258 110 3.08 3.215 19.44  1  0    3    1
## Hornet Sportabout 18.7   8  360 175 3.15 3.440 17.02  0  0    3    2
## Valiant           18.1   6  225 105 2.76 3.460 20.22  1  0    3    1
```

```r
str(mtcars)
```

```
## 'data.frame':	32 obs. of  11 variables:
##  $ mpg : num  21 21 22.8 21.4 18.7 18.1 14.3 24.4 22.8 19.2 ...
##  $ cyl : num  6 6 4 6 8 6 8 4 4 6 ...
##  $ disp: num  160 160 108 258 360 ...
##  $ hp  : num  110 110 93 110 175 105 245 62 95 123 ...
##  $ drat: num  3.9 3.9 3.85 3.08 3.15 2.76 3.21 3.69 3.92 3.92 ...
##  $ wt  : num  2.62 2.88 2.32 3.21 3.44 ...
##  $ qsec: num  16.5 17 18.6 19.4 17 ...
##  $ vs  : num  0 0 1 1 0 1 0 1 1 1 ...
##  $ am  : num  1 1 1 0 0 0 0 0 0 0 ...
##  $ gear: num  4 4 4 3 3 3 3 4 4 4 ...
##  $ carb: num  4 4 1 1 2 1 4 2 2 4 ...
```

```r
# mean power by cylinder capacity
tapply(mtcars$hp, mtcars$cyl, mean)
```

```
##      4      6      8 
##  82.64 122.29 209.21
```


If you have a list, can use lapply or sapply (simplify the output)

```r
# Generate data
lista <- list(a = c("one", "tow", "three"), b = c(1, 2, 3), c = c(12, "a"))
lista
```

```
## $a
## [1] "one"   "tow"   "three"
## 
## $b
## [1] 1 2 3
## 
## $c
## [1] "12" "a"
```

```r

# How many elements in each list?
lapply(lista, length)  # return a list
```

```
## $a
## [1] 3
## 
## $b
## [1] 3
## 
## $c
## [1] 2
```

```r
sapply(lista, length)  # return a vector
```

```
## a b c 
## 3 3 2
```


## Split - apply - combine without plyr
Use split, *apply, rbind/cbind

### Split

```r
data <- split(mtcars, mtcars$gear)  # split
data
```

```
## $`3`
##                      mpg cyl  disp  hp drat    wt  qsec vs am gear carb
## Hornet 4 Drive      21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1
## Hornet Sportabout   18.7   8 360.0 175 3.15 3.440 17.02  0  0    3    2
## Valiant             18.1   6 225.0 105 2.76 3.460 20.22  1  0    3    1
## Duster 360          14.3   8 360.0 245 3.21 3.570 15.84  0  0    3    4
## Merc 450SE          16.4   8 275.8 180 3.07 4.070 17.40  0  0    3    3
## Merc 450SL          17.3   8 275.8 180 3.07 3.730 17.60  0  0    3    3
## Merc 450SLC         15.2   8 275.8 180 3.07 3.780 18.00  0  0    3    3
## Cadillac Fleetwood  10.4   8 472.0 205 2.93 5.250 17.98  0  0    3    4
## Lincoln Continental 10.4   8 460.0 215 3.00 5.424 17.82  0  0    3    4
## Chrysler Imperial   14.7   8 440.0 230 3.23 5.345 17.42  0  0    3    4
## Toyota Corona       21.5   4 120.1  97 3.70 2.465 20.01  1  0    3    1
## Dodge Challenger    15.5   8 318.0 150 2.76 3.520 16.87  0  0    3    2
## AMC Javelin         15.2   8 304.0 150 3.15 3.435 17.30  0  0    3    2
## Camaro Z28          13.3   8 350.0 245 3.73 3.840 15.41  0  0    3    4
## Pontiac Firebird    19.2   8 400.0 175 3.08 3.845 17.05  0  0    3    2
## 
## $`4`
##                 mpg cyl  disp  hp drat    wt  qsec vs am gear carb
## Mazda RX4      21.0   6 160.0 110 3.90 2.620 16.46  0  1    4    4
## Mazda RX4 Wag  21.0   6 160.0 110 3.90 2.875 17.02  0  1    4    4
## Datsun 710     22.8   4 108.0  93 3.85 2.320 18.61  1  1    4    1
## Merc 240D      24.4   4 146.7  62 3.69 3.190 20.00  1  0    4    2
## Merc 230       22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2
## Merc 280       19.2   6 167.6 123 3.92 3.440 18.30  1  0    4    4
## Merc 280C      17.8   6 167.6 123 3.92 3.440 18.90  1  0    4    4
## Fiat 128       32.4   4  78.7  66 4.08 2.200 19.47  1  1    4    1
## Honda Civic    30.4   4  75.7  52 4.93 1.615 18.52  1  1    4    2
## Toyota Corolla 33.9   4  71.1  65 4.22 1.835 19.90  1  1    4    1
## Fiat X1-9      27.3   4  79.0  66 4.08 1.935 18.90  1  1    4    1
## Volvo 142E     21.4   4 121.0 109 4.11 2.780 18.60  1  1    4    2
## 
## $`5`
##                 mpg cyl  disp  hp drat    wt qsec vs am gear carb
## Porsche 914-2  26.0   4 120.3  91 4.43 2.140 16.7  0  1    5    2
## Lotus Europa   30.4   4  95.1 113 3.77 1.513 16.9  1  1    5    2
## Ford Pantera L 15.8   8 351.0 264 4.22 3.170 14.5  0  1    5    4
## Ferrari Dino   19.7   6 145.0 175 3.62 2.770 15.5  0  1    5    6
## Maserati Bora  15.0   8 301.0 335 3.54 3.570 14.6  0  1    5    8
```


### Apply

```r
fits <- lapply(data, function(x) return(lm(x$mpg ~ x$disp)$coef))
fits
```

```
## $`3`
## (Intercept)      x$disp 
##    24.51557    -0.02577 
## 
## $`4`
## (Intercept)      x$disp 
##     39.5675     -0.1222 
## 
## $`5`
## (Intercept)      x$disp 
##    31.66095    -0.05078
```


### Combine

```r
do.call(rbind, fits)
```

```
##   (Intercept)   x$disp
## 3       24.52 -0.02577
## 4       39.57 -0.12221
## 5       31.66 -0.05078
```



