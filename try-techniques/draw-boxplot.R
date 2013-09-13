require(reshape2)
require(ggplot2)

df <- data.frame(Butterfinger = rnorm(50, 25, 10),
                 Snickers = rnorm(50, 75, 20),
                 Skor = rnorm(50, 115, 35),
                 AlmondJoy = rnorm(50, 45, 5))
head(df)

df.melt <- melt(df)
head(df.melt)

ggplot(df.melt, aes(x=variable, y=value)) + geom_boxplot()