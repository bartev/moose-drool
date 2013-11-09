Table of Fonts
========================================================

From http://www.cookbook-r.com/Graphs/Fonts/

## Table of fonts

```r
fonttable <- read.table(header = TRUE, sep = ",", stringsAsFactors = FALSE, 
    text = "\nShort,Canonical\nmono,Courier\nsans,Helvetica\nserif,Times\n,AvantGarde\n,Bookman\n,Helvetica-Narrow\n,NewCenturySchoolbook\n,Palatino\n,URWGothic\n,URWBookman\n,NimbusMon\nURWHelvetica,NimbusSan\n,NimbusSanCond\n,CenturySch\n,URWPalladio\nURWTimes,NimbusRom\n")

fonttable$pos <- 1:nrow(fonttable)

library(reshape2)
fonttable <- melt(fonttable, id.vars = "pos", measure.vars = c("Short", "Canonical"), 
    variable.name = "NameType", value.name = "Font")

# Make a table of faces. Make sure factors are ordered correctly
facetable <- data.frame(Face = factor(c("plain", "bold", "italic", "bold.italic"), 
    levels = c("plain", "bold", "italic", "bold.italic")))

fullfonts <- merge(fonttable, facetable)

library(ggplot2)
pf <- ggplot(fullfonts, aes(x = NameType, y = pos)) + geom_text(aes(label = Font, 
    family = Font, fontface = Face)) + facet_wrap(~Face, ncol = 2)
pf
```

![plot of chunk generate graphical table of fonts](figure/generate_graphical_table_of_fonts.png) 


print to png

```r
png("fonttable.png", width = 720, height = 720, res = 72)
print(pf)
```

```
## Warning: no font could be found for family "URWHelvetica" Warning: no font
## could be found for family "URWHelvetica" Warning: no font could be found
## for family "URWHelvetica" Warning: no font could be found for family
## "URWTimes" Warning: no font could be found for family "URWTimes" Warning:
## no font could be found for family "URWTimes" Warning: no font could be
## found for family "AvantGarde" Warning: no font could be found for family
## "AvantGarde" Warning: no font could be found for family "AvantGarde"
## Warning: no font could be found for family "Bookman" Warning: no font
## could be found for family "Bookman" Warning: no font could be found for
## family "Bookman" Warning: no font could be found for family
## "Helvetica-Narrow" Warning: no font could be found for family
## "Helvetica-Narrow" Warning: no font could be found for family
## "Helvetica-Narrow" Warning: no font could be found for family
## "NewCenturySchoolbook" Warning: no font could be found for family
## "NewCenturySchoolbook" Warning: no font could be found for family
## "NewCenturySchoolbook" Warning: no font could be found for family
## "URWGothic" Warning: no font could be found for family "URWGothic"
## Warning: no font could be found for family "URWGothic" Warning: no font
## could be found for family "URWBookman" Warning: no font could be found for
## family "URWBookman" Warning: no font could be found for family
## "URWBookman" Warning: no font could be found for family "NimbusMon"
## Warning: no font could be found for family "NimbusMon" Warning: no font
## could be found for family "NimbusMon" Warning: no font could be found for
## family "NimbusSan" Warning: no font could be found for family "NimbusSan"
## Warning: no font could be found for family "NimbusSan" Warning: no font
## could be found for family "NimbusSanCond" Warning: no font could be found
## for family "NimbusSanCond" Warning: no font could be found for family
## "NimbusSanCond" Warning: no font could be found for family "CenturySch"
## Warning: no font could be found for family "CenturySch" Warning: no font
## could be found for family "CenturySch" Warning: no font could be found for
## family "URWPalladio" Warning: no font could be found for family
## "URWPalladio" Warning: no font could be found for family "URWPalladio"
## Warning: no font could be found for family "NimbusRom" Warning: no font
## could be found for family "NimbusRom" Warning: no font could be found for
## family "NimbusRom" Warning: no font could be found for family
## "URWHelvetica" Warning: no font could be found for family "URWHelvetica"
## Warning: no font could be found for family "URWHelvetica" Warning: no font
## could be found for family "URWTimes" Warning: no font could be found for
## family "URWTimes" Warning: no font could be found for family "URWTimes"
## Warning: no font could be found for family "AvantGarde" Warning: no font
## could be found for family "AvantGarde" Warning: no font could be found for
## family "AvantGarde" Warning: no font could be found for family "Bookman"
## Warning: no font could be found for family "Bookman" Warning: no font
## could be found for family "Bookman" Warning: no font could be found for
## family "Helvetica-Narrow" Warning: no font could be found for family
## "Helvetica-Narrow" Warning: no font could be found for family
## "Helvetica-Narrow" Warning: no font could be found for family
## "NewCenturySchoolbook" Warning: no font could be found for family
## "NewCenturySchoolbook" Warning: no font could be found for family
## "NewCenturySchoolbook" Warning: no font could be found for family
## "URWGothic" Warning: no font could be found for family "URWGothic"
## Warning: no font could be found for family "URWGothic" Warning: no font
## could be found for family "URWBookman" Warning: no font could be found for
## family "URWBookman" Warning: no font could be found for family
## "URWBookman" Warning: no font could be found for family "NimbusMon"
## Warning: no font could be found for family "NimbusMon" Warning: no font
## could be found for family "NimbusMon" Warning: no font could be found for
## family "NimbusSan" Warning: no font could be found for family "NimbusSan"
## Warning: no font could be found for family "NimbusSan" Warning: no font
## could be found for family "NimbusSanCond" Warning: no font could be found
## for family "NimbusSanCond" Warning: no font could be found for family
## "NimbusSanCond" Warning: no font could be found for family "CenturySch"
## Warning: no font could be found for family "CenturySch" Warning: no font
## could be found for family "CenturySch" Warning: no font could be found for
## family "URWPalladio" Warning: no font could be found for family
## "URWPalladio" Warning: no font could be found for family "URWPalladio"
## Warning: no font could be found for family "NimbusRom" Warning: no font
## could be found for family "NimbusRom" Warning: no font could be found for
## family "NimbusRom" Warning: no font could be found for family
## "URWHelvetica" Warning: no font could be found for family "URWHelvetica"
## Warning: no font could be found for family "URWHelvetica" Warning: no font
## could be found for family "URWTimes" Warning: no font could be found for
## family "URWTimes" Warning: no font could be found for family "URWTimes"
## Warning: no font could be found for family "AvantGarde" Warning: no font
## could be found for family "AvantGarde" Warning: no font could be found for
## family "AvantGarde" Warning: no font could be found for family "Bookman"
## Warning: no font could be found for family "Bookman" Warning: no font
## could be found for family "Bookman" Warning: no font could be found for
## family "Helvetica-Narrow" Warning: no font could be found for family
## "Helvetica-Narrow" Warning: no font could be found for family
## "Helvetica-Narrow" Warning: no font could be found for family
## "NewCenturySchoolbook" Warning: no font could be found for family
## "NewCenturySchoolbook" Warning: no font could be found for family
## "NewCenturySchoolbook" Warning: no font could be found for family
## "URWGothic" Warning: no font could be found for family "URWGothic"
## Warning: no font could be found for family "URWGothic" Warning: no font
## could be found for family "URWBookman" Warning: no font could be found for
## family "URWBookman" Warning: no font could be found for family
## "URWBookman" Warning: no font could be found for family "NimbusMon"
## Warning: no font could be found for family "NimbusMon" Warning: no font
## could be found for family "NimbusMon" Warning: no font could be found for
## family "NimbusSan" Warning: no font could be found for family "NimbusSan"
## Warning: no font could be found for family "NimbusSan" Warning: no font
## could be found for family "NimbusSanCond" Warning: no font could be found
## for family "NimbusSanCond" Warning: no font could be found for family
## "NimbusSanCond" Warning: no font could be found for family "CenturySch"
## Warning: no font could be found for family "CenturySch" Warning: no font
## could be found for family "CenturySch" Warning: no font could be found for
## family "URWPalladio" Warning: no font could be found for family
## "URWPalladio" Warning: no font could be found for family "URWPalladio"
## Warning: no font could be found for family "NimbusRom" Warning: no font
## could be found for family "NimbusRom" Warning: no font could be found for
## family "NimbusRom" Warning: no font could be found for family
## "URWHelvetica" Warning: no font could be found for family "URWHelvetica"
## Warning: no font could be found for family "URWHelvetica" Warning: no font
## could be found for family "URWTimes" Warning: no font could be found for
## family "URWTimes" Warning: no font could be found for family "URWTimes"
## Warning: no font could be found for family "AvantGarde" Warning: no font
## could be found for family "AvantGarde" Warning: no font could be found for
## family "AvantGarde" Warning: no font could be found for family "Bookman"
## Warning: no font could be found for family "Bookman" Warning: no font
## could be found for family "Bookman" Warning: no font could be found for
## family "Helvetica-Narrow" Warning: no font could be found for family
## "Helvetica-Narrow" Warning: no font could be found for family
## "Helvetica-Narrow" Warning: no font could be found for family
## "NewCenturySchoolbook" Warning: no font could be found for family
## "NewCenturySchoolbook" Warning: no font could be found for family
## "NewCenturySchoolbook" Warning: no font could be found for family
## "URWGothic" Warning: no font could be found for family "URWGothic"
## Warning: no font could be found for family "URWGothic" Warning: no font
## could be found for family "URWBookman" Warning: no font could be found for
## family "URWBookman" Warning: no font could be found for family
## "URWBookman" Warning: no font could be found for family "NimbusMon"
## Warning: no font could be found for family "NimbusMon" Warning: no font
## could be found for family "NimbusMon" Warning: no font could be found for
## family "NimbusSan" Warning: no font could be found for family "NimbusSan"
## Warning: no font could be found for family "NimbusSan" Warning: no font
## could be found for family "NimbusSanCond" Warning: no font could be found
## for family "NimbusSanCond" Warning: no font could be found for family
## "NimbusSanCond" Warning: no font could be found for family "CenturySch"
## Warning: no font could be found for family "CenturySch" Warning: no font
## could be found for family "CenturySch" Warning: no font could be found for
## family "URWPalladio" Warning: no font could be found for family
## "URWPalladio" Warning: no font could be found for family "URWPalladio"
## Warning: no font could be found for family "NimbusRom" Warning: no font
## could be found for family "NimbusRom" Warning: no font could be found for
## family "NimbusRom"
```

```r
dev.off()
```

```
## pdf 
##   2
```

print to pdf

```r
pdf("fonttable.pdf", width = 10, height = 10)
print(pf)
dev.off()
```

```
## pdf 
##   2
```

