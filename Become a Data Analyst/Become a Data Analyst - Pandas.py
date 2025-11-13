##Pandas

##Series

    import pandas as pd
    myseries = pd.Series([10, 20, 30])
    print(myseries)
    #----------------------------------------
    #Output
    #1.49s
    #0    10
    #1    20
    #2    30
    #dtype: int64
    
    # By default, Series is assigned an integer index, but it can be changed using the index parameter.
    
    import pandas as pd

    myseries = pd.Series(
         [10,20,30], 
         index = ["a","b","c"]
    )

    print(myseries)  
    
    #----------------------------------------
    #Output
    #1.52s
    #a    10
    #b    20
    #c    30
    #dtype: int64
    
    import pandas as pd

    myseries = pd.Series(
       ["Jane","John","Emily","Matt"]
    )

    # Print the first item
    print(myseries[0])
    
    #----------------------------------------
    
    #Output
    #1.2s
    #Jane
    
    import pandas as pd

    myseries = pd.Series([1,2,3])
    print(myseries.is_unique)
    #----------------------------------------
    #Output
    #1.71s
    #True
    
    import pandas as pd

    myseries = pd.Series([1,1,3])
    print(myseries.is_unique)
    #----------------------------------------
    #Output
    #1.58s
    #False
    
##DataFrame

    #DataFrame is the two-dimensional data structure of Pandas. It consists of labeled rows and columns.
    
    import pandas as pd

    df = pd.DataFrame({
        "Name": ["Jane", "John", "Matt", "Ashley"],
        "Age": [24, 21, 26, 32]
    })

    print(df)
    #----------------------------------------    
    #Output
    #0.97s
    #    Age    Name
    #0   24    Jane
    #1   21    John
    #2   26    Matt
    #3   32  Ashley
    
    print(df.shape) #(4, 2)
    
##Reading data from a csv file

    import pandas as pd

    sales = pd.read_csv("sales.csv")
    print(sales.head())
    
    #----------------------------------------    
    #Output
    #   product_code product_group  stock_qty    cost    price  last_week_sales  \
    #0          4187           PG2        498  420.76   569.91               13   
    #1          4195           PG2        473  545.64   712.41               16   
    #2          4204           PG2        968  640.42   854.91               22   
    #3          4219           PG2        241  869.69  1034.55               14   
    #4          4718           PG2       1401   12.54    26.59               50  
    
    import pandas as pd
    sales = pd.read_csv("sales.csv", usecols=["product_code","product_group","stock_qty"])
    print(sales.head())
    #----------------------------------------    
    #Output
    #   product_code product_group  stock_qty
    #0          4187           PG2        498
    #1          4195           PG2        473
    #2          4204           PG2        968
    #3          4219           PG2        241
    #4          4718           PG2       1401
    
#Two-dimensional array

    import numpy as np
    import pandas as pd

    arr = np.random.randint(1, 10, size=(3,5))
    df = pd.DataFrame(arr, columns=["A","B","C","D","E"])

    print(df)
    #----------------------------------------    
    #Output
    #   A  B  C  D  E
    #0  5  8  9  7  9
    #1  9  1  6  7  8
    #2  7  7  9  7  3
    
#The size, shape, and len methods


    import pandas as pd

    sales = pd.read_csv("sales.csv")

    print(sales.shape)
    print(sales.size)
    print(len(sales))
    #----------------------------------------    
    #Output    
    #(1000, 7)
    #7000
    #1000
    
#dtypes
    
    print(sales.dtypes)
    #----------------------------------------    
    #Output 
    #product_code          int64
    #product_group        object
    #stock_qty             int64
    #cost                float64
    #price               float64
    #last_week_sales       int64
    #last_month_sales      int64
    #dtype: object
    
#Changing the data type

    print("As index:")
    print(sales.columns)

    print("As list:")
    print(list(sales.columns))
    #----------------------------------------    
    #Output 
    #As index:
    #Index(['product_code', 'product_group', 'stock_qty', 'cost', 'price',
    #       'last_week_sales', 'last_month_sales'],
    #      dtype='object')
    #As list:
    #['product_code', 'product_group', 'stock_qty', 'cost', 'price', 'last_week_sales', 'last_month_sales']
    
    sales["stock_qty"] = sales["stock_qty"].astype("float")

    print(sales.dtypes)
    #----------------------------------------    
    #Output 
    #product_code          int64
    #product_group        object
    #stock_qty           float64
    #cost                float64
    #price               float64
    #last_week_sales       int64
    #last_month_sales      int64
    #dtype: object    
    
    sales = sales.astype({
      "stock_qty": "float",
      "last_week_sales": "float"
    })

    print(sales.dtypes)
    #----------------------------------------    
    #Output 
    #product_code          int64
    #product_group        object
    #stock_qty           float64
    #cost                float64
    #price               float64
    #last_week_sales     float64
    #last_month_sales      int64
    #dtype: object

##Using the unique and nunique functions

    import pandas as pd

    sales = pd.read_csv("sales.csv")

    print(sales["product_group"].nunique())
    print(sales["product_group"].unique())
    #----------------------------------------    
    #Output 
    #6
    #['PG2' 'PG4' 'PG6' 'PG5' 'PG3' 'PG1']
 
    print(sales["product_group"].value_counts())
    
    #----------------------------------------    
    #Output 
    #PG4    349
    #PG5    255
    #PG6    243
    #PG2     75
    #PG1     39
    #PG3     39
    #Name: product_group, dtype: int64

##Measures of Central Tendency

    import pandas as pd
    myseries = pd.Series([1, 2, 5, 7, 11, 36])
    print(myseries.median())
    #----------------------------------------    
    #Output    
    #6.0
    
    import pandas as pd
    myseries = pd.Series([1, 4, 6, 6, 6, 11, 11, 24])
    print(f"The mode of my series is {myseries.mode()[0]}")
    #----------------------------------------    
    #Output    
    #The mode of my series is 6


    import pandas as pd

    sales = pd.read_csv("sales.csv")

    print("mean: ")
    print(sales["price"].mean())

    print("median: ")
    print(sales["price"].median())

    print("mode: ")
    print(sales["price"].mode()[0])

    print("minimum: ")
    print(sales["price"].min())

    print("maximum: ")
    print(sales["price"].max())
    #----------------------------------------    
    #Output       
    #mean: 
    #67.06351000000001
    #median: 
    #23.74
    #mode: 
    #10.44
    #minimum: 
    #0.66
    #maximum: 
    #1500.05
    
    #The var and std methods of Pandas can be used to calculate the variance and standard deviation, respectively.
    
    print("variance: ")
    print(sales["price"].var())

    print("standard deviation: ")
    print(sales["price"].std())
    #----------------------------------------    
    #Output    
    #variance: 
    #20766.243824604506
    #standard deviation: 
    #144.10497501684148
    
##Filtering with "loc" and "iloc" Methods

    #loc uses row and column labels.
    #iloc uses row and column indexes.

    import pandas as pd

    sales = pd.read_csv("sales.csv")
    
    #Let’s first use the loc method to select the first five rows and two columns in the sales.
    print(sales.loc[:4, ["product_code","product_group"]])
    #----------------------------------------    
    #Output   
       product_code product_group
    0          4187           PG2
    1          4195           PG2
    2          4204           PG2
    3          4219           PG2
    4          4718           PG2
    
    #The :4 is the equivalent of 0:4 and it indicates the rows starting from 0 to 4. The column names are passed as a list to the loc method. Let’s do the same operation using the iloc method.
    
    print(sales.iloc[[5,6,7,8], [0,1]])

    print(sales.iloc[5:9, :2])

    #----------------------------------------    
    #Output  
       product_code product_group
    5          5630           PG4
    6          5631           PG4
    7          5634           PG4
    8          2650           PG4
       product_code product_group
    5          5630           PG4
    6          5631           PG4
    7          5634           PG4
    8          2650           PG4
    
    #The loc and iloc methods are frequently used to select or extract a part of a data frame. The main difference is that loc works with labels whereas iloc works with indices.
    
##Filtering by Selecting a Subset of Columns

    import pandas as pd

    sales = pd.read_csv("sales.csv")

    selected_columns = ["product_code","price"]

    print(sales[selected_columns].head())
    
    #We don’t have to create a list that contains the column names. The same operation can also be handled through this line:

    print(sales[["product_code","price"]].head())

##Filtering by Condition

    #The following line of code selects the products that belong to product group PG2. Remember that each row in the sales represents a product.

    sales_filtered = sales[sales.product_group == "PG2"]
    
    #The following line of code does the same operation.

    sales_filtered = sales[sales["product_group"] == "PG2"]
    
    #We can use any of the options above, unless there’s a space in the column name. In such cases, the first option won’t work.
    #We can also filter a DataFrame based on numerical values. For instance, the following line of code selects the products with a price higher than 100.

    sales_filtered = sales[sales["price"] > 100]
    
    The operators we can use to create conditions are:

    ==: equal
    !=: not equal
    >: greater than
    >=: greater than or equal to
    <: less than
    <=: less than or equal to
    
##Multiple conditions
    
    # filter the sales data frame
    sales_filtered = sales[(sales["price"] > 100) & (sales["stock_qty"] < 400)]
    print(sales_filtered[["price","stock_qty"]].head())
    
    #For instance, the following line of code selects the products that belong to the product group PG1 or PG2.

    sales_filtered = sales[(sales["product_group"] == "PG1") | (sales["product_group"] == "PG2")]
    
    #We can select the products that belong to product groups PG1, PG2, and PG3 as follows:

    sales_filtered = sales[sales["product_group"].isin(["PG1","PG2","PG3"])]
    
    #We can select the products that aren’t in product groups PG1, PG2, or PG3 as follows:

    sales_filtered = sales[~sales["product_group"].isin(["PG1","PG2","PG3"])]
    
    
    
##The query function
    
    #Here’s how we can select products with a price higher than 100 by using the query function:

    sales_filtered = sales.query("price > 100")
    
    sales_filtered = sales.query("price > 100 and stock_qty < 400")
    print(sales_filtered[["product_code","price","stock_qty"]].head())
    #----------------------------------------    
    #Output  
    #     product_code    price  stock_qty
    #3            4219  1034.55        241
    #8            2650   111.06        239
    #165          1657   208.91        244
    #186          7269   427.41        369
    #199          3530   104.49        144
    
    #For instance, we may want to select the products that belong to the product group, PG2.

    sales_filtered = sales.query("product_group == 'PG2'")
    #As we can see, single quotes are used to specify the string value used for filtering.
    
    '''
    dsds
    sdsdsd
    '''
    
##Challenge: Average

    average_price = sales["price"].mean() # find the mean value of the price column
    sales_filtered = sales[sales["price"] > average_price] # filter the products that have a price higher than the average price
    number_of_products = sales_filtered["product_code"].nunique() # find the number of unique product codes in sales_filtered
    return number_of_products
        
        
##Slicing and Indexing on Strings

    import pandas as pd

    staff = pd.read_csv("staff.csv")

    print(f"\nStaff data frame has the following columns: \n{list(staff.columns)}\n")

    print(staff)
    
    '''OUTPUT:'''        
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Staff data frame has the following columns: 
    ['name', 'city', 'date_of_birth', 'start_date', 'salary', 'department']

                   name             city  ...   salary       department
    0          John Doe      Houston, TX  ...  $65,000       Accounting
    1          Jane Doe     San Jose, CA  ...  $70,000    Field Quality
    2        Matt smith       Dallas, TX  ...  $58,500  human resources
    3     Ashley Harris        Miami, FL  ...  $49,500       accounting
    4  Jonathan targett  Santa Clara, CA  ...  $62,000    field quality
    5         Hale Cole      Atlanta, GA  ...  $54,500      engineering
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 

    # The strings have integer indexes starting from zero. If we want to take a slice from a string, we simply need to specify the start and end index.

    print(staff["name"].str[0])
    
    '''
    0    J
    1    J
    2    M
    3    A
    4    J
    5    H
    '''
    
    print(staff["name"].str[0:3])
    
    '''
    0    Joh
    1    Jan
    2    Mat
    3    Ash
    4    Jon
    5    Hal
    '''
    
    # If the desired slice starts from the first index (zero), we needn’t write the initial index. Thus, the following line of code does the same thing as above.

    print(staff["name"].str[:3])
    
    # It’s possible to use an index that starts from the end of a string. 
    # In this case, the indexes start from -1 and continue as -2, -3, and so on. 
    # The following line of code returns the last two characters of the city column.
    
    print(staff["name"].str[-2:])

    '''
    0    oe
    1    oe
    2    th
    3    is
    4    tt
    5    le
    '''
    
    # To make the slicing and indexing operations even more flexible, Pandas allows for customizing the step size as well. 
    # For instance, we can create a slice that involves every other character, starting from the second-to-last index.
    
    print(staff["name"].str[1::2])
    
    '''
    0        onDe
    1        aeDe
    2       atsih
    3      slyHri
    4    oahntret
    5        aeCl
    '''
    
    # The structure is as follows:

    str[start : end : step size]
    
    # If the end is left blank, then the slice goes up to the end of the string.
    
    # The structure str[start : end : step size] is used for slicing strings, 
    
    # where start is the starting index, 
    # end is the stopping index (exclusive), 
    # and step size is the interval between characters taken.
    
    # If end is left blank, slicing continues to the string’s end.
    
##Splitting and Combining Strings
    
    # The Pandas split function is available under the str accessor. It splits a string at the position of the given character and then returns a list of all parts.
    # The following code snippet splits the name column at the space character.
    
    import pandas as pd

    staff = pd.read_csv("staff.csv")

    print(staff["name"].str.split(" "))  
    
    '''
    0            [John, Doe]
    1            [Jane, Doe]
    2          [Matt, smith]
    3       [Ashley, Harris]
    4    [Jonathan, targett]
    5           [Hale, Cole]
    '''
    
    #The expand parameter of the split function can be used to create separate columns after splitting. We can then select the column we need.

    #Let’s create a column that only contains the last names.
    
    staff["last_name"] = staff["name"].str.split(" ", expand=True)[1]

    print(staff[["name","last_name"]])
    
    '''
                   name last_name
    0          John Doe       Doe
    1          Jane Doe       Doe
    2        Matt smith     smith
    3     Ashley Harris    Harris
    4  Jonathan targett   targett
    5         Hale Cole      Cole
    '''
    
    # Just like we split strings, we can combine multiple strings into a single one.
    
    print(staff["name"] + " - " + staff["department"])
    
    '''
    0               John Doe - Accounting
    1            Jane Doe - Field Quality
    2        Matt smith - human resources
    3          Ashley Harris - accounting
    4    Jonathan targett - field quality
    5             Hale Cole - engineering
    '''
    
    # Upper and lower case
    
    #The lower function under the str accessor converts all characters to lowercase. The upper function does the opposite. 
    
    staff["name_lower"] = staff["name"].[0].lower()

    print(staff[["name","name_lower"]])
    
    '''
                   name        name_lower
    0          John Doe          john doe
    1          Jane Doe          jane doe
    2        Matt smith        matt smith
    3     Ashley Harris     ashley harris
    4  Jonathan targett  jonathan targett
    5         Hale Cole         hale cole
    '''
    
    # Another function that we can use is the capitalize function. It only converts the first letter to upper case.
    
    print(staff["department"].str.capitalize())
    
    '''
    0         Accounting
    1      Field quality
    2    Human resources
    3         Accounting
    4      Field quality
    5        Engineering
    '''
    
    # In addition to converting the first letter to upper case, the capitalize function ensures all other letters are lowercase. 
    # Thus, if there’s an uppercase letter other than the first one, it’s converted to lowercase.
    
    # For instance, we can apply the built-in upper function on the value in the first row of the department column.
    
    print(sales["department"][0].upper())
    
    '''
    ACCOUNTING
    '''
    
    print(sales["department"][0].str.upper())
    
    ###TAMPOCO FUNCIONA!!! 

##Problem statement
###Using the string manipulation techniques we’ve just learned, create a column that contains only the state part of the city column.
     
    import pandas as pd

    staff = pd.read_csv("staff.csv")

    def create_city_column():

      staff["state"] = staff["city"].str.split(", ", expand=True)[1]

      return list(staff["state"])
      
    '''
    ['TX', 'CA', 'TX', 'FL', 'CA', 'GA']
    '''
    
##The replace function

    print(staff["city"].str.replace(",", "-"))
    
    '''
    0        Houston- TX
    1       San Jose- CA
    2         Dallas- TX
    3          Miami- FL
    4    Santa Clara- CA
    5        Atlanta- GA
    '''
    
    # The Pandas library also provides the DataFrame.replace function that can be used to replace entire values.
    
    # Create a state colum
    staff["state"] = staff["city"].str[-2:]

    # Replace state abbreviations with actual state names
    staff["state"].replace(
        {"TX": "Texas", "CA": "California", "FL": "Florida", "GA": "Georgia"},
        inplace = True
    )
    
    '''
    0         Texas
    1    California
    2         Texas
    3       Florida
    4    California
    5       Georgia
    '''
    
    #The inplace parameter is set to True to save changes in the DataFrame.

    #It’s important to emphasize the difference between str.replace and DataFrame.replace:

    #str.replace can be used to replace a part of a string. We can replace one character, multiple characters, or the entire string.
    #DataFrame.replace can be used to replace the entire value. We can also use this function to replace values with other data types such as integer and boolean.
    
##Combining multiple operations

    # We can combine multiple string manipulation operations into a single chained operation. For instance, we can extract the state part from the city column and convert it to lowercase letters in a single line of code.

    print(staff["city"].str.split(",", expand=True)[1].str.lower())
    
    '''
    0     tx
    1     ca
    2     tx
    3     fl
    4     ca
    5     ga
    '''

    # Consider a case where we need to change the name of the “field quality” department to “quality.” 
    # In the department column of the staff, there are both lower and upper case letters. 
    # We first need to convert them to either lower or upper case and then do the replacement.

    print(staff["department"].str.lower().replace("field quality","quality"))
    
    '''
    0         accounting
    1            quality
    2    human resources
    3         accounting
    4            quality
    5        engineering
    '''
    
    # Chained operations aren’t limited to string manipulation methods. We can combine operations of different types as well.

    # For instance, line 5 in the following code snippet performs a filtering operation with the query function, 
    # extracts the year from the start_date column, and changes its data type to integer.

    print(staff.query("name > 'John Doe'").start_date.str[:4].astype("int"))
    
    '''
    2    2020
    4    2020
    '''

###CHALLENGE:
    '''
    The values in the salary column of the staff (DataFrame) are stored as a string. We need to convert it to a numerical format to make calculations.

    There are two issues that we need to solve before converting it to a numerical data type.

    We need to remove the “$” sign at the beginning.
    We need to remove the “,” used as the thousands separator.
    '''
    import pandas as pd

    staff = pd.read_csv("staff.csv")

    def make_salary_proper():
      try:
        staff["salary_cleaned"] = staff["salary"].str[1:].str.replace(",","") # Write your solution here
        staff["salary_cleaned"] = staff["salary_cleaned"].astype("int")
        return list(staff["salary_cleaned"])
      except:
        pass
        

##Date and Time Data Types

'''We can express dates and times in three main forms:

A specific date or time (2021-12-10, 2021-11-25 14:59:00)
A fixed interval (hour, week, month).
A duration (3 weeks, 4 hours and 30 minutes).'''

import pandas as pd

mydate = pd.to_datetime("2021-11-10")

print(mydate)

#2021-11-10 00:00:00

       
        