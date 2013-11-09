Select operations on R
========================================================

From http://www.r-bloggers.com/select-operations-on-r-data-frames/


```r
set.seed(123)
# round(runif(12,1,10))

# bmi <- rnorm(n=1000, m=24.2, sd=2.2)

df <- data.frame(Butterfinger = rnorm(25, 25, 10), Snickers = rnorm(25, 75, 
    20), Skor = rnorm(25, 115, 35), AlmondJoy = rnorm(25, 45, 5))
```


Get shape of data frame

```r
dim(df)
```

```
## [1] 25  4
```


Select columns by name

```r
df[, c("Snickers", "Skor")]
```

```
##    Snickers   Skor
## 1     41.27 123.87
## 2     91.76 114.00
## 3     78.07 113.50
## 4     52.24 162.90
## 5    100.08 107.10
## 6     83.53 168.08
## 7     69.10  60.79
## 8     92.90 135.46
## 9     92.56 119.33
## 10    91.43 122.56
## 11    88.77 128.29
## 12    86.08  97.42
## 13    73.76 103.34
## 14    68.88  79.35
## 15    67.39  77.49
## 16    61.11 125.62
## 17    70.84 130.69
## 18    49.69 116.86
## 19   118.38 147.28
## 20    99.16 186.75
## 21    52.54  97.81
## 22    66.94  34.18
## 23    65.67 150.20
## 24    90.60  90.18
## 25    73.33  90.92
```


Select by row names and column names

```r
df[4:8, c("Snickers", "Skor")]
```

```
##   Snickers   Skor
## 4    52.24 162.90
## 5   100.08 107.10
## 6    83.53 168.08
## 7    69.10  60.79
## 8    92.90 135.46
```


Select rows by criteria (like sql where clause)

```r
df[df$Skor > 150, ]
```

```
##    Butterfinger Snickers  Skor AlmondJoy
## 4         25.71    52.24 162.9     45.91
## 6         42.15    83.53 168.1     45.03
## 20        20.27    99.16 186.8     51.80
## 23        14.74    65.67 150.2     52.66
```


Select using grep on row names

```r
mtcars[grep("Mazda", rownames(mtcars), ignore.case = T), ]
```

```
##               mpg cyl disp  hp drat    wt  qsec vs am gear carb
## Mazda RX4      21   6  160 110  3.9 2.620 16.46  0  1    4    4
## Mazda RX4 Wag  21   6  160 110  3.9 2.875 17.02  0  1    4    4
```


Every other row - is this the best way?

```r
df[as.numeric(rownames(df))%%2 == 0, ]
```

```
##    Butterfinger Snickers   Skor AlmondJoy
## 2        22.698    91.76 114.00     43.58
## 4        25.705    52.24 162.90     45.91
## 6        42.151    83.53 168.08     45.03
## 8        12.349    92.90 135.46     43.15
## 10       20.543    91.43 122.56     43.90
## 12       28.598    86.08  97.42     50.48
## 14       26.107    68.88  79.35     43.37
## 16       42.869    61.11 125.62     49.97
## 18        5.334    49.69 116.86     46.19
## 20       20.272    99.16 186.75     51.80
## 22       22.820    66.94  34.18     55.94
## 24       17.711    90.60  90.18     43.82
```

```r
df[as.numeric(rownames(df))%%2 == 0 & df$Skor > 150, grep("^[^AB]", colnames(df), 
    ignore.case = T)]
```

```
##    Snickers  Skor
## 4     52.24 162.9
## 6     83.53 168.1
## 20    99.16 186.8
```

