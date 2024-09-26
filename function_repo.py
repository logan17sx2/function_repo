def importmodules ():
    import pandas as pd
    import openpyxl
    import timeit
    from datetime import datetime
    from python_calamine import CalamineWorkbook
    import numpy as np
    
def savecsv (df,file_path,name):
    startsave= timeit.default_timer()
    finamewithfieltype = file_name +".csv"
    filepath=os.path.join(file_path,finamewithfieltype)
    df.to_csv(filepath)
    stopsave=timeit.default_timer()
    print(name,"save successful in:",stopsave-startsave,"seconds")
    

def saveexcel (df,file_path,name):
    startsave= timeit.default_timer()
    finamewithfieltype = file_name +".xlsx"
    filepath=os.path.join(file_path,finamewithfieltype)
    df.to_excel(filepath)
    stopsave=timeit.default_timer()
    print(name,"save successful in:",stopsave-startsave,"seconds")
    
def savemultitabexcel (df,file_path,name,sheet_name):
    startsave= timeit.default_timer()
    inamewithfieltype = file_name +".xlsx"
    filepath=os.path.join(file_path,finamewithfieltype)
    with pd.ExcelWriter(filepath, engine='openpyxl',mode=a) as writer:
    df.to_excel(writer,sheet_name=sheet_name)
    stopsave=timeit.default_timer()
    print(name,"save successful in:",stopsave-startsave,"seconds")
   
