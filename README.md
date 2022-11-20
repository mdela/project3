# project3
I wrote this program because we now unfortunately live in a time where we have to ask our friends for gas money after hanging out with them.

This program calculates how much each passenger should pay their best friend, the driver.

The program takes these inputs from:
* the driver:
  * car's MPG
  * current price per gallon
* the passenger:
  * name
  * distance to drop-off
  
It then appends to a data frame. Provided below is the example of the output:

| name    | distance | city          | cost |
|---------|----------|---------------|------|
| Martin  | 30       | Santa Clarita | 8    |
| James   | 20       | Los Angeles   | 7    |
| Robert  | 25       | Koreatown     | 9    |
| David   | 30       | Monterey Park | 5    |
| John    | 20       | Los Angeles   | 7    |
| Richard | 10       | Glendale      | 8    |
| Michael | 15       | Northridge    | 4    |
| Joseph  | 20       | Los Angeles   | 7    |
| Daniel  | 10       | Glendale      | 5    |

Finally, it graphs this data onto a bar chart:
 ![newplot](https://user-images.githubusercontent.com/47103500/202881415-d1f8a06b-a3b4-4501-9c96-4b4141783a3e.png)


# update log
Version 2.1
* I've completely redesigned the code so that it's much simpler to read
* in an effort to learn the tools used in Data Analytics, I've tried to incorporate plotly and pandas into this project
 * here are the notable changes:
  * instead of using lists to plot it onto a graph, I've created a DataFrame, and then used the columns to project it onto a graph
  * used plotly instead of matplotlib
 * I have found this change to be much more appreciated because I find using pandas and plotly delightful
 * output
 ![newplot](https://user-images.githubusercontent.com/47103500/202881415-d1f8a06b-a3b4-4501-9c96-4b4141783a3e.png)


Version 2.0
* in an effort to become more familiar with Python, I've decided to redo this project in this programming language.
  * here are some notable changes to this project:
    * visualized the data onto a bar graph
    * color codes the bars:
      * farthest distance is red
      * shortest distance is green
      * the rest are blue
    * displays each passenger's fare in the center of each bar
* to broaden my knowledge, I will be continuing this project in Python
* output:
<img width="1112" alt="program screenshot" src="https://user-images.githubusercontent.com/47103500/201498426-1af4b1fd-ae5b-402d-b041-4859bd0d1324.png">
      
Version 1.0
* initial commit
* this project was initially written in Java:
  * I've utilized arrays and objects as Passengers to achieve this project
  * the files for the Java version can still be found in this repository
