colnames(df)[which( names(df) = "Eran"]) = "Raz"
m[m[, "three"] == 11,]

# יצירת ווקטור עם ערכים
y = 5:14 # 5  6  7  8  9 10 11 12 13 14
# NOTE !
is.na(x) # NO!! x===NA

for (i in 1:nrow(long_human_data1)){  # 1:nrow
  if (long_human_data1$Test[i]== 'PLT'){
    long_human_data1$Test_Value[i] = long_human_data1$Test_Value[i]*100
  }
}

x= seq(1,50,5) # seq(1:50)

# כמה איברים מתחלקים ל 3 ללא שארית
x = c(1,5,3, 12, 30,33)
sum(x%%3 ==  0)

class(x)
x=c(rep(4,3),rep(5,2))

sqrt(x)
sum( , na.rm = T) # na.rm only on functions

#מאחד וקטורים ללא כפילות
union(x,y) # 
# מאחד איברים כפולים בווקטור
intersect(x,y)
# איברים שונים בווקטורים
setdiff(x,y)
#יצירת ווקטור רנדומלי 
vec = runif(10,1,3) #  10 random numbers	

is.na(x[1]) #FALSE FALSE  TRUE FALSE FALSE FALSE

#נותן שמות למסגרת נתונים
df = data.frame(name1=x, name2= y, name3 = z)

#מתן שמות למסגרת הנתונים
names(df) = c('name1','name2')

nrow() \ ncol
# מוציא עמודה ממסגרת ומשאיר אותה כמסגרת
df[,'col' , drop = FALSE]

#list  - יכולה להחזיק ערכים שונים
list1=list(seq(1,3),seq(4,6),seq(7,9)) # [1] 1 2 3 [2] 4 5 6 [3] 7 8 9
list(a,b)

# יצירת מטריצה מוקטורים
A=matrix(c(seq(1:3),seq(from=15, to=25, by=5),rep(15,3)), nrow = 3)
cbind(A,B) # אחוד מטריצות עפ עמודות
C= A%*%B

#Array 
array2 = array(seq(1,3,2),dim = c(2,4,3)) #dim: row,col,dim

# DataFrame
df$colm2[df$colm1 %%2 ==0] = 4 # set value in colm2 by condition in colm1 (*) 
# הסרת שורות ממסגרת הנתונים ע"פ תנאי  
data1 = data1[which(data1$ID>4),]     #(*)    
# MERGE (all=F == inner ,all=T == outer )
df3 = merge(df1,df1, by = 'ID', all.x = T , sort = T)  # Left join, sorted by ID (*) 
names(df) = c('name1','name2')
# Removing the fifth cell of "ID" and the second column 
df = df[-ID[5],-2]
# Rename column (x>y)
colnames(df)[which(names(df) == 'x')] = 'y'           #(*)
# sort by x1 & x2
df[order(df$x1,df$x2),]                               # (*) NOTE : ,] 
# check duplicated - A logical vector indicating which rows are duplicated based on 2 first columns
duplicated(df[,1:2])
no_dups= df[!duplicated(df[,1:2]),]
# Recoding - change values
#for ID = 3 change col1 value to 40
df$col1[which(df$ID ==2)]=40
row.names(df) = c('Alex', 'Lilly', 'Mark', 'Oliver','Martha') # set a column as row name
all(df) > 0 # TRUE
dim(df)[1] # > rows | 2=columns
df[df>3] = 10 # 									#(*) change any df cell by condition


######### reshape2 #########
library(reshape2)
long_df = melt(df, id.vars = c('ID','Gender',',fixed'),variable.name = 'test', value.name = 'test_values') (*)
# Long to wide
wide_df = dcast(df,Gender +ID +Fix ~ test_field, value.var = 'Test_Values' )
######### aggregate - function
aggregate (value1 ~ SaleOrg + SaleOffice, df, sum) # cbind(value1, value2) > for several value calc (*)


# Apply # for matrix / array
apply(mtx,1,sum) # sum the rows (1) - sum the columns (2)
	B = array(c(1:12),dim = c(4,3,2)) #array of 2 matrix
	apply(B, 3,sum) # sum the 2 matrices of B (3)
list1=list(A=A,B=c(1:5),c=2) # list of 3 matrix/vector/value
lapply(list1,sum) # returns results a list
sapply(list1, sum)   # returns a vector

#random select
random_df = df[sample(nrow(df),size = 2, replace = F),] # from nrow(amount of lines), bring 2 rows, no return 

# subset
Newdt1=subset(DF5,select = -y)

#  שינוי מערך לערך בפונקציה SWITCH
cn1= function(i){  switch(i, '1'= 11, '2' =22, '3'= 33)} #(*) switch - only works on vectors
cn1(3) 

# בןדק כמה איברים בווקטור עומדים בתנאי
sum(ifelse(vec >0 ,1,0))
	a = c(1,2,3,4,5)
	b = c(1,1,1,1,1)
b= ifelse(a>2,0,b)


library(dplyr)
###### Filter ######
subset = filter(df,col1 ==8 , col2>3) #and
new_df = filter(df, co1 ==1 | col2 < 3) # or
###### Arrange ######
df = arrange(df, col1, desc(col2))         #(*) NOTE the arrange syntex
df= arrange(df,
###### Select ######
df= select(df,col1,col2,col3)
df= select(df,-(col1:col3)) # remove cols
subset6=select(data,ends_with("t"))
rename(subset6,new_name= old_name)

###### Mutate ######
library(tibble)
df = mutate(subset, new_var = var1+ var2, new_var2 = var1*2 ) # new columns with calculation
df = mutate_all(df, round)
###### Mutate_if ######
df = mutate_if(df1, is.numeric, round)
###### recode ######
mutate(df, new_col = ifelse(col1 <4, 1,0))  #(*)
mutate(human_data, Health =  ifelse(human_data$ID > 20 , 0,1))  # IMPORTANT VVV
min_rank(y)  # מיקומי דירוג הערכים
###### summarize ######
by_var = group_by(df, col1,col3)
summarize(group_by(df,gender),summary = mean(weight , na.rm = T))  (*)

na.rm
na.omit(human_data)
df = rownames_to_column(df, var = 'Names1') # from row.names

human_data[num_cols] = sapply(human_data[num_cols], function(i){ifelse(i<0,NA,i)})  # *** review solution VVV
df = mutate(df, new_colname = recode(old_col, '4' = '2',.default = 'other' ))  #VVV


format(my_number, scientific = F)  # 1e+09 >> "1000000001"
memory.size()