# covid-compiler
This is a tool to compare covid data compiled from multiple sources - Built on windows, doesn't support linux/mac by default see below

Currently it compiles John Hopkins, covidtracking.com and CDC Excess death numbers.
Please note, that by default, it checks the servers no more than once every 6 hours to minimize web usage.


EXAMPLE: python3 main.py

---this will run the code, generate the html document and open it in your default browser

![alt text](https://github.com/Skwerl23/covid-compiler/blob/master/example.png?raw=true)

DEPENDENCIES: Plotly, Pandas





I plan to upgrade the options and layout over time


WINDOWS NOTE:
It will utilize local data in the c:/temp directory - so for linux variants you will need to update folder locations
(if requested i may make this self correct)



- Finally I am not a professional at Python yet, so forgive any crude code. I'm using this project as a way to get better at python
