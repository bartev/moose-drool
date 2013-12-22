getwd()
setwd("~/Development/moose-drool/test-knitr/r/markdown/")
opts_chunk$set(tidy=TRUE)

# load packages
require(knitr)
require(markdown)

# Create slides
knit('master.Rmd')
system("pandoc --from markdown-yaml_metadata_block -s master.md -o master.html")
system("pandoc --from markdown-yaml_metadata_block -s master.md -o p-master.pdf")
system("pandoc --from markdown-yaml_metadata_block -s -t slidy master.md -o s-master.html")
system("pandoc --from markdown-yaml_metadata_block -t beamer master.md -o b-master.pdf")
system("pandoc --from markdown-yaml_metadata_block -s --mathml -i -t dzslides master.md -o d-master.html")
system("pandoc --from markdown-yaml_metadata_block -s --webtex -i -t slidy master.md -o w-master.html")
system("pandoc --from markdown-yaml_metadata_block -s --mathjax -i -t revealjs master.md -o r-master.html")


list.files('r/markdown/', full.names=TRUE)

# for (f in list.files('r/markdown/', '\\.md$', full.names=TRUE)) {
#   unlink(basename(f))
#   knit(f, output = basename(f))
# }