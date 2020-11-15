# Chicken Weights Analysis 
library(tidyverse)
library(DT)

# Descriptive Statistics
chickTable <- chickwts %>% 
  group_by(feed) %>% 
  summarise(n = length(feed),
            average = mean(weight),
            SD = sd(weight))
datatable(chickTable)%>%
  formatRound(columns=c('feed','average','SD'), digits=3)

# Box Plot 
chickwts %>%
  ggplot(aes(x=feed , y=weight)) + geom_boxplot()


# Jitter Plot
chickwts %>%
  ggplot(aes(x=feed , y=weight)) + geom_jitter()+
  stat_summary(fun.data = mean_sdl,
               fun.args = list(mult =1),
               col = "orange")
  

# Inferential Statistics

## The one-way ANOVA summary
res.aov <- aov(weight ~ feed, data = chickwts)

# create table for ANOVA 'list' '.aov, .av' using pander package
#install.packages("pander")
library(pander)
pander(ANOVATable, style='rmarkdown') # without style its normal table --
ANOVATable <- summary(res.aov)

# Tukey’s Post-hoc test Table 
chickwts.av <- aov(weight ~ feed, data = chickwts)
tukeyTest <- TukeyHSD(chickwts.av)
datatable(tukeyTest$feed)%>%
  formatRound(columns=c('diff','lwr','upr','p adj'), digits=3)




