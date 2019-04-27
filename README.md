# expsmooth
Exponential smoothing function often used to make data forecasts and for analysis of time-series data.
Calculates value of alpha itself

The reason: 
Like we can see on Wikipedia or another sources, alpha value (called "smoothing factor") is шт between 0 and 1. 
In truth it should be in between 0 and 2 and this program takes this into account. 
What allows to achieve the best results in forecasting.


---Installation---
1. Install the Python on your computer.
2. Install xlwings add-in for Excel via command prompt. Use 'xlwings addin install'.
3. In your book make sure that you can see xlwings on the Excel ribbon, if it's not reinstall the add-in.

---Preps---
1. Put the python file in the directory of your Excel book.
1. To start your work with function you should rename the book to 'expsmooth' and save it as '.xlsm'
2. Open the xlsm book and press Import function from the tab xlwings on the ribbon. 
