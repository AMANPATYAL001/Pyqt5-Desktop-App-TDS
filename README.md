# PyQt5-Desktop-App-TDS

## **[App Link ( just install it [.exe file 165MB], {not requirements} )](https://drive.google.com/file/d/1R8HqzhDboD9iiafNJtBPOewwSjwN0FS0/view?usp=sharing)**
<br>

## The idea behind this project is to provide free link for the desired blog or article to the user, from the **Towards Data Science** platform.

- ### It also provide keyword search functionality.
- ### And also the option to list down a particular no. of aritcles.
- ### Like Count and published Date are also there as columns.

## How it is accessing the free links?
- ### It scrapes the twitter account of **[Towards Data Science](https://twitter.com/tdatascience)**. Links on twitter (I don't know how 💃  😏😏) are free to open.
- ### I used **[tweepy](https://docs.tweepy.org/en/stable/)** for scraping( which has a limit of 3200 tweets and also require to have authentication for using twitter API), but you can use **[snscrape](https://github.com/JustAnotherArchivist/snscrape)** which is free and does not have limit (with many other features), just change the code on **line 235**, otherwise put api key token on **line 225**.

## Deployment : 
- ### I converted the **.py** to **.exe** file (using **[pyinstaller](https://pyinstaller.readthedocs.io/en/stable/)**) to run on systems which doesn't have **python** or **required libraries**.

- ### Use of NSIS software ([Tech with Tim Video]((https://youtu.be/UZX5kH72Yx4))), for converting **.exe and resource folder** into **one folder** for easy installation  and transfer.
## Screenshots :

### Home Page

![](res/ss1.png)
<br><br>

### About Page

![](res/ss2.png)
<br><br>

### Result Page

![](res/ss3.png)
<br><br>

## Requirements for running **[TDS.py]()** file : 
- PyQt5
- numpy
- pandas
- tweepy( Auth.) or snscrape
### In Terminal : 
```bash
python3 TDS.py
```
<br>

## Requirements for running **TDS.exe** file : 
### **No Requirements** as I already said, just install it like any other **.exe software**.

<br>

## Any feedback is Welcome. Thankyou for Visiting.