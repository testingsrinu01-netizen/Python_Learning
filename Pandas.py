#“Python Data Analysis Library”

import pandas as pd;

studentData = {
"Name":["Alice","Bob","Mary"],
"Math":[60,80,90],
"Physics":[10,77,56],
"Chemistry":[90,90,90],
}

df = pd.DataFrame(studentData);
print(df)

print(df.head(2)); #Print 2 rows apart from top of table.
print(df.tail(1)); #Print 1 rows apart from bottom of table.
print(df.shape); # (rows, columns)
print(df.columns);  # list of column names
print(df.keys());