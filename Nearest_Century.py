year_list = [1905,1700,1988,3000,200,734,54,143628,2314,3424,3421]

# Method 2
print(year_list)

for year in year_list:
    if(year % 100 == 0):
        x = year/100
        print(year, ' belongs to ', int(x), ' century')
    else:
        x = year//100
        print(year, ' belongs to ', x+1, ' century')

# Method 2
list(map(lambda y: print(y, ' belongs to ', int(y / 100), ' century') if(y % 100 == 0) else print(y, ' belongs to ',(y//100)+1, ' century'), year_list))

