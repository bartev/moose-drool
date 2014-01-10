DF <- data.frame(community = factor(rep(c("Com1", "Com2"), each = 2)),
                 village = factor(paste0("Vil", seq(4))),
                 Mean = c(290.05, 322.54, 13.67, 38.14),
                 Median = c(186, 229, 11, 22))

# 'stack' the Mean and Median variables so that they can be used as
# aesthetics in ggplot2. We use the very useful reshape2 package for this purpose.
install.packages(c('reshape2', 'ggplot2'))
install.packages(c( 'ggplot2'))

library(reshape2)

# id.var indicates which variables are not to be stacked
DFm <- melt(DF, id.var = c("community", "village"))
str(DFm)    # show the structure of the reshaped data

library(ggplot2)

ggplot(DFm, aes(x = village, y = value, color = community, group = community)) +
  geom_point(size = 3) + geom_line(size = 1) +
  facet_wrap( ~ variable)

# The scales = "free_x" argument permits varying x-scales in each panel
ggplot(DFm, aes(x = village, y = value, color = variable, group = variable)) +
  geom_point(size = 3) + geom_line(size = 1) +
  facet_wrap(~ community, scales = "free_x")

Some other options:
  * plot the mean and median by village in a single panel;
* create a Cleveland dot chart by village

ggplot(DFm, aes(x = village, y = value, color = variable, group = variable)) +
  geom_point(size = 3) + geom_line(size = 1)

ggplot(DFm, aes(x = village, y = value, color = variable)) +
  geom_point(size = 3) + geom_vline(aes(xintercept = 1:4), linetype = "dotted") + 
  coord_flip()
