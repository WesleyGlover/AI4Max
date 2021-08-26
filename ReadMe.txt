Creators: Wesley Glover, Chandler Franklin

Project: AI4Max - A use of machine learning to narrow down and determine leading factors of suicide rates within the depressed population of European countries.



There are four python3 files within this workspace.

AI4Max_Split.py 
        This file contained the linear regression models of each individual factors plotted against suicide rates.
        Produces a file called Plots.png that contains multiple plots.
        Displays the intercepts and coefficients to the console.

AI4Max_Together.py 
        This file contains the linear regressino model all plotted into one plot.
        Produces a file called Model.png that is one plot with legend.
        Displays the intercepts and coefficients to the console.

DataOrganizer.py 
        This file takes the multi-book excel sheet of data and chooses specific columns to be used.
        Then saves only the data that is needed within the project as a one book excel file called df.xlsx
      
Test.py
        This file is not needed for the project. It was used as a temporary place to explore with the code.


To Run:
        - Make sure all source code and excel file are in the same directory.
        - Run the DataOrganizer.py file, if sucessful a new excel file should be created called df.xlsx 
        - Choose wether you want a single model with all the factors or multiple models with only one factor 
                Run AI4Max_Split.py for single factor models 
                Run AI4Max_Together.py for multi-factor model. 
        - Each file produces their own png file. 
                Plots.png - Multiple plots of single factor models.
                Model.png - One plot of multiple factors.
        - Note: Each AI4Max program produces the intercepts and coefficients to the console after completion. 


Feed Back from presentation:
        Chandler and Wesley, great insight. For a two-member team as a first look into ML, you guys did great.
        - ZeroR is a cool way to compare your algorithm early on.
        - Some ways to also look going forward is to try a subset of features to see if there are better ways to classify the data. Like merge the data or considering other demographics.
        - This is a very vital open problem and kudos to you two for an inspirational direction.

