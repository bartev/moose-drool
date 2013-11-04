Functions - Hadley master class
========================================================

## define data

```r
set.seed(123)
df <- data.frame(x = round(rnorm(20, mean = 99, sd = 5)), a = round(rnorm(20, 
    mean = 10, sd = 10)), b = round(rnorm(20, mean = 0, sd = 3)), c = round(rnorm(20, 
    mean = 50, sd = 2)))
df
```

```
##      x  a  b  c
## 1   96 -1 -2 51
## 2   98  8 -1 49
## 3  107  0 -4 49
## 4   99  3  7 48
## 5  100  4  4 48
## 6  108 -7 -3 51
## 7  101 18 -1 51
## 8   93 12 -1 50
## 9   96 -1  2 52
## 10  97 23  0 54
## 11 105 14  1 49
## 12 101  7  0 45
## 13 101 19  0 52
## 14 100 19  4 49
## 15  96 18 -1 49
## 16 108 17  5 52
## 17 101 16 -5 49
## 18  89  9  2 48
## 19 103  7  0 50
## 20  97  6  1 50
```


## Apply DRY (Don't Repeat Yourself) principle

```r
fix_missing <- function(x) {
    x[x == -99] <- NA
    x
}

df[] <- lapply(df, fix_missing)
```



```r
numeric <- vapply(df, is.numeric, logical(1))
numeric
```

```
##    x    a    b    c 
## TRUE TRUE TRUE TRUE
```

```r
df[numeric] <- lapply(df[numeric], fix_missing)
df
```

```
##      x  a  b  c
## 1   96 -1 -2 51
## 2   98  8 -1 49
## 3  107  0 -4 49
## 4   99  3  7 48
## 5  100  4  4 48
## 6  108 -7 -3 51
## 7  101 18 -1 51
## 8   93 12 -1 50
## 9   96 -1  2 52
## 10  97 23  0 54
## 11 105 14  1 49
## 12 101  7  0 45
## 13 101 19  0 52
## 14 100 19  4 49
## 15  96 18 -1 49
## 16 108 17  5 52
## 17 101 16 -5 49
## 18  89  9  2 48
## 19 103  7  0 50
## 20  97  6  1 50
```



```r
summary <- function(x) {
    c(mean(x), median(x), sd(x), mad(x), IQR(x))
}

summary(df$a)
```

```
## [1]  9.550  8.500  8.319 11.861 13.500
```

```r
summary(df$b)
```

```
## [1] 0.400 0.000 2.998 2.224 3.000
```

```r
summary(df$c)
```

```
## [1] 49.800 49.500  1.963  2.224  2.000
```

```r
summary(df$x)
```

```
## [1]  99.800 100.000   4.895   4.448   4.750
```

```r

summary <- function(x) {
    c(mean(x, na.rm = TRUE), median(x, na.rm = TRUE), sd(x, na.rm = TRUE), mad(x, 
        na.rm = TRUE), IQR(x, na.rm = TRUE))
}

summary(df$a)
```

```
## [1]  9.550  8.500  8.319 11.861 13.500
```

```r
summary(df$b)
```

```
## [1] 0.400 0.000 2.998 2.224 3.000
```

```r
summary(df$c)
```

```
## [1] 49.800 49.500  1.963  2.224  2.000
```

```r
summary(df$x)
```

```
## [1]  99.800 100.000   4.895   4.448   4.750
```


## Examine parts of a function

```r
formals(function(x = 4) g(x) + h(x))
```

```
## $x
## [1] 4
```

```r
body(function(x) g(x) + h(x))
```

```
## g(x) + h(x)
```

```r
environment(function(x) g(x) + h(x))
```

```
## <environment: R_GlobalEnv>
```


## Closures

```r
x <- 5
f <- function() {
    y <- 10
    c(x = x, y = y)
}
f()
```

```
##  x  y 
##  5 10
```

```r
g <- function() {
    x <- 20
    y <- 10
    c(x = x, y = y)
}
g()
```

```
##  x  y 
## 20 10
```



```r
x <- 0
y <- 10
f <- function() {
    x <- 1
    function() {
        y <- 2
        x + y
    }
}
```


Create a function that creates a whole class of functions

```r
power <- function(exponent) {
    function(x) x^exponent
}

square <- power(2)
c(square(2), square(3))
```

```
## [1] 4 9
```

```r
cube <- power(3)
c(cube(2), cube(3))
```

```
## [1]  8 27
```

```r

# examine square find environment and its parent
environment(square)
```

```
## <environment: 0x105639b58>
```

```r
parent.env(environment(square))
```

```
## <environment: R_GlobalEnv>
```

```r

# inspect objects defined in that environment
ls(environment(square))
```

```
## [1] "exponent"
```

```r
get("exponent", environment(square))
```

```
## [1] 2
```

```r
environment(square)$exponent
```

```
## [1] 2
```

```r
as.list(environment(square))
```

```
## $exponent
## [1] 2
```


Multiple counters

```r
new_counter <- function() {
    i <- 0
    function() {
        # do something useful, then...
        i <<- i + 1
        i
    }
}
counter_one <- new_counter()
counter_two <- new_counter()

counter_one()
```

```
## [1] 1
```

```r
counter_two()
```

```
## [1] 1
```

```r
counter_two()
```

```
## [1] 2
```

```r
counter_one()
```

```
## [1] 2
```


Built in functions that make closures

```r
Negate(is.numeric)("abc")
```

```
## [1] TRUE
```

```r
Negate
```

```
## function (f) 
## {
##     f <- match.fun(f)
##     function(...) !f(...)
## }
## <bytecode: 0x104045380>
## <environment: namespace:base>
```

```r

`?`(Vectorize)
vrep <- Vectorize(rep.int, "times")
vrep(42, times = 1:4)
```

```
## [[1]]
## [1] 42
## 
## [[2]]
## [1] 42 42
## 
## [[3]]
## [1] 42 42 42
## 
## [[4]]
## [1] 42 42 42 42
```

```r
vrep
```

```
## function (x, times) 
## {
##     args <- lapply(as.list(match.call())[-1L], eval, parent.frame())
##     names <- if (is.null(names(args))) 
##         character(length(args))
##     else names(args)
##     dovec <- names %in% vectorize.args
##     do.call("mapply", c(FUN = FUN, args[dovec], MoreArgs = list(args[!dovec]), 
##         SIMPLIFY = SIMPLIFY, USE.NAMES = USE.NAMES))
## }
## <environment: 0x105419228>
```

```r
as.list(environment(vrep))
```

```
## $FUNV
## function (x, times) 
## {
##     args <- lapply(as.list(match.call())[-1L], eval, parent.frame())
##     names <- if (is.null(names(args))) 
##         character(length(args))
##     else names(args)
##     dovec <- names %in% vectorize.args
##     do.call("mapply", c(FUN = FUN, args[dovec], MoreArgs = list(args[!dovec]), 
##         SIMPLIFY = SIMPLIFY, USE.NAMES = USE.NAMES))
## }
## <environment: 0x105419228>
## 
## $arg.names
## [1] "x"     "times"
## 
## $FUN
## function (x, times) 
## .Internal(rep.int(x, times))
## <bytecode: 0x100ada800>
## <environment: namespace:base>
## 
## $vectorize.args
## [1] "times"
## 
## $SIMPLIFY
## [1] TRUE
## 
## $USE.NAMES
## [1] TRUE
```

```r

e <- ecdf(runif(1000))
str(e)
```

```
## function (v)  
##  - attr(*, "class")= chr [1:3] "ecdf" "stepfun" "function"
##  - attr(*, "call")=length 2 ecdf(runif(1000))
##   ..- attr(*, "srcref")=Class 'srcref'  atomic [1:8] 10 1 10 22 1 22 10 10
##   .. .. ..- attr(*, "srcfile")=Classes 'srcfilecopy', 'srcfile' <environment: 0x1052a1478>
```

```r
e(0.5)
```

```
## [1] 0.5
```

```r
class(3)
```

```
## [1] "numeric"
```


## Higher Order Functions

```r
# Data structure HOFs Provide basic tools for when you have a predicate
# function instead of a logical vector.  Filter: keeps true Find: value of
# first true Position: location of first true
head(Filter(is.factor, iris))
```

```
##   Species
## 1  setosa
## 2  setosa
## 3  setosa
## 4  setosa
## 5  setosa
## 6  setosa
```

```r
head(Find(is.factor, iris))
```

```
## [1] setosa setosa setosa setosa setosa setosa
## Levels: setosa versicolor virginica
```

```r
Position(is.factor, iris)
```

```
## [1] 5
```

```r
# One function I use a lot: Not sure what this does - get rid of null
# values?  null != NA
compact <- function(x) Filter(Negate(is.null), x)

set.seed(123)
samples <- replicate(5, sample(10, 20, rep = T), simplify = FALSE)
# Want to find intersection of all values
int <- intersect(samples[[1]], samples[[2]])
int <- intersect(int, samples[[3]])
int <- intersect(int, samples[[4]])
int <- intersect(int, samples[[5]])
```


Simple example of Reduce

```r
# Reduce recursively applies a function in this way
Reduce(intersect, samples)
```

```
## [1] 3 8 5 9 1 2 4
```

```r
add <- function(x, y) x + y
Reduce(add, 1:10)
```

```
## [1] 55
```

```r
Reduce(add, 1:10, 5)
```

```
## [1] 60
```

```r
Reduce(add, 1:10, accumulate = TRUE)
```

```
##  [1]  1  3  6 10 15 21 28 36 45 55
```

```r
length(Reduce(add, 1:10, accumulate = TRUE))
```

```
## [1] 10
```


## Mathematical HOFs

```r
integrate(sin, 0, pi)
```

```
## 2 with absolute error < 2.2e-14
```

```r
uniroot(sin, pi * c(1/2, 3/2))
```

```
## $root
## [1] 3.142
## 
## $f.root
## [1] 1.225e-16
## 
## $iter
## [1] 2
## 
## $estim.prec
## [1] 6.104e-05
```

```r
optimise(sin, c(0, 2 * pi))
```

```
## $minimum
## [1] 4.712
## 
## $objective
## [1] -1
```

```r
optimise(sin, c(0, 2 * pi))[[1]]/pi
```

```
## [1] 1.5
```

```r
optimise(sin, c(0, pi), maximum = TRUE)
```

```
## $maximum
## [1] 1.571
## 
## $objective
## [1] 1
```

```r
optimise(sin, c(0, pi), maximum = TRUE)[[1]]/pi
```

```
## [1] 0.5
```


## Combine closure and HOF
## MLE

```r
# Combination of closures and HOF particularly useful.  For statistics,
# maximum likelihood estimation is a great example.
poisson_nll <- function(x) {
    n <- length(x)
    function(lambda) {
        n * lambda - sum(x) * log(lambda)  # + ...
    }
}
nll1 <- poisson_nll(c(41, 30, 31, 38, 29, 24, 30, 29))
nll2 <- poisson_nll(c(6, 4, 7, 3, 3, 7, 5, 2, 2, 7))
optimise(nll1, c(0, 100))
```

```
## $minimum
## [1] 31.5
## 
## $objective
## [1] -617.4
```

```r
optimise(nll2, c(0, 100))
```

```
## $minimum
## [1] 4.6
## 
## $objective
## [1] -24.2
```

 ## Lists of Functions
 

```r
compute_mean <- list(base = function(x) mean(x), sum = function(x) sum(x)/length(x), 
    manual = function(x) {
        total <- 0
        n <- length(x)
        for (i in seq_along(x)) {
            total <- total + x[i]/n
        }
        total
    })
call_fun <- function(f, ...) f(...)
x <- runif(1e+06)
lapply(compute_mean, call_fun, x)
```

```
## $base
## [1] 0.4995
## 
## $sum
## [1] 0.4995
## 
## $manual
## [1] 0.4995
```

```r
lapply(compute_mean, function(f) system.time(f(x)))
```

```
## $base
##    user  system elapsed 
##   0.008   0.000   0.009 
## 
## $sum
##    user  system elapsed 
##   0.004   0.000   0.005 
## 
## $manual
##    user  system elapsed 
##   1.104   0.002   1.107
```



### Modify summary to return return a user specified list of functions

```r
summary <- function(x) {
    c(mean(x, na.rm = TRUE), median(x, na.rm = TRUE), sd(x, na.rm = TRUE), mad(x, 
        na.rm = TRUE), IQR(x, na.rm = TRUE))
}
summary(df$a)
```

```
## [1]  9.550  8.500  8.319 11.861 13.500
```

```r
summary(df$b)
```

```
## [1] 0.400 0.000 2.998 2.224 3.000
```

```r
summary(df$c)
```

```
## [1] 49.800 49.500  1.963  2.224  2.000
```

```r

summary2 <- function(x, ys) {
    call_fun <- function(f, ...) f(...)
    lapply(ys, call_fun, x)
}
summary2(df$a, compute_mean)
```

```
## $base
## [1] 9.55
## 
## $sum
## [1] 9.55
## 
## $manual
## [1] 9.55
```

```r
summary2(1:100, list(length = function(x) length(x), sum = function(x) sum(x)))
```

```
## $length
## [1] 100
## 
## $sum
## [1] 5050
```

