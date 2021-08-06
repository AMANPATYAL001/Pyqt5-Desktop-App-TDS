import sys
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QApplication,QLabel,QPushButton,QWidget,QHBoxLayout,QVBoxLayout,QTableWidgetItem,QTableWidget,QLineEdit,QProgressBar,QFrame,QMessageBox
from PyQt5.QtGui import QPixmap,QMovie,QCursor,QRegExpValidator
from PyQt5.QtCore import Qt,QTimer,QRegExp
from PyQt5 import QtWidgets,QtCore
import tweepy

class About(QWidget):
    def __init__(self):
        super().__init__()
        self.title='About the Application'        
        self.setWindowTitle(self.title)
        self.setWindowOpacity(0.96)
        
        python_resized = QPixmap("res/python.png").scaled(250,225, QtCore.Qt.KeepAspectRatio)

        pandas_resized = QPixmap("res/pandas.png").scaled(250,250, QtCore.Qt.KeepAspectRatio)

        numpy_resized = QPixmap("res/numpy.png").scaled(250,250, QtCore.Qt.KeepAspectRatio)

        twitter_resized = QPixmap("res/twitter.png").scaled(250,250, QtCore.Qt.KeepAspectRatio)

        mat_resized = QPixmap("res/matplotlib.svg").scaled(250,250, QtCore.Qt.KeepAspectRatio)

        lb1 = QtWidgets.QLabel(self)
        lb1.setFixedSize(300, 275)
        lb2 = QtWidgets.QLabel(self)
        lb2.setFixedSize(300, 275)
        lb3 = QtWidgets.QLabel(self)
        lb3.setFixedSize(300, 275)
        lb4 = QtWidgets.QLabel(self)
        lb4.setFixedSize(300, 275)
        lb5 = QtWidgets.QLabel(self)
        lb5.setFixedSize(300,275)
        header=QLabel('<p style="font-size:75px;">Powered by <span style="color:#0091EA;">Pyt</span><span style="color:#FFEB3B;">hon</span></p><p style="font-size:75px;margin-left:200px;">rendered by <span style="color:#66BB6A;">PyQt5</span></p>',self)
        motive='''<br><p style='color:#C51162;font-size:29px;'>The Motive behind this application is to curate a particular number of Articles from <a href='https://towardsdatascience.com/'><b>Towards Data Science<b></a> and facilitate the search <br>functionality to find the desired Article/s.<br>

        Fetch data function may take very long time for large number of articles and if it does not able to collect all the "get data" in a specified time,<br> then the program will terminate itself with a warning.
        This app also provide a word-cloud to visualize the most frequent(or trending)<br> words in all the Article's topic. <br>
        <span style='color:#795548'>For any feedback please contact the Team.(<img src='res/yt.jpg'><a href='https://www.youtube.com/channel/UCBh0xDnTdouixDBmVVzRl1g'>YT</a>)</span></p><br><br>
        '''
        
        mo=QLabel(motive,self)
        mo.setOpenExternalLinks(True)
        text='<h1>Acknowledgement :</h1><div style="font-size:30px;margin-left:50px;"><img src="res/py.png"><span style="color:#43A047;">Jie Jenn(YouTube)</span><a href="https://www.youtube.com/user/jiejenn"> Link</a><br><span style="color:#AB47BC;"><img src="res/py.png">Duong Vu (Datacamp Article)</span><a href="https://www.datacamp.com/community/tutorials/wordcloud-python"> Link</a><br><span style="color:#BCAAA4;"><img src="res/py.png">Stack overflow</span><br><span style="color:#AA00FF;"><img src="res/py.png">Open Source Community</span><br><br><span>Thank You for the support</span><br><br><span>Thank You for the support</span></div>'
        label=QLabel(text,self)
        label.setOpenExternalLinks(True)
        
        lb1.setPixmap(numpy_resized)
        lb2.setPixmap(twitter_resized)
        lb5.setPixmap(python_resized)
        lb4.setPixmap(pandas_resized)
        lb3.setPixmap(mat_resized)

        lb1.setStyleSheet('QLabel{background-color: #D7CCC8;border-width:0px;border-style:solid;padding:30px;}QLabel:hover{background-color: #FFD54F;border-width:3px;border-style:ridge;}')
        lb2.setStyleSheet('QLabel{background-color: #D7CCC8;border-width: 0px;padding:30px;}QLabel:hover{border-width:3px;background-color:#F8BBD0;border-style:ridge;}')
        lb3.setStyleSheet('QLabel{background-color: #D7CCC8;border-style:solid;border-width:0px;padding:30px;}QLabel:hover{background-color:#B3E5FC;border-width:3px;border-style:ridge;}')
        lb4.setStyleSheet('QLabel{background-color: #D7CCC8;border-width:0px;border-style:solid;padding:30px;}QLabel:hover{border-width:3px;background-color:#69F0AE;border-style:ridge;}')
        lb5.setStyleSheet('QLabel{background-color:#D7CCC8;border-style:solid;border-width:0px;padding:30px;}QLabel:hover{border-width:3px;border-style:ridge;background-color:#FFAB91}')
        hbox=QHBoxLayout()
        vbox=QVBoxLayout(self)

        hbox.addWidget(lb1)
        hbox.addWidget(lb2)
        hbox.addWidget(lb5)
        hbox.addWidget(lb4)
        hbox.addWidget(lb3)
        vbox.addWidget(header)
        vbox.addWidget(mo)
        vbox.addWidget(label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.showMaximized()


class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(64,64)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        self.label_animation=QLabel(self)
        self.movie=QMovie('res/1490.gif')
        self.label_animation.setMovie(self.movie)
        timer=QTimer()
        self.startAnimation()
        timer.singleShot(2000,self.stopAnimation)
        self.show()

    def startAnimation(self):
        self.movie.start() 

    def stopAnimation(self):
        self.movie.stop()
        self.close()


class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(1100, 500)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.counter = 0
        self.n = 50 

        self.initUI()

        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.frame = QFrame()
        layout.addWidget(self.frame)

        self.labelTitle = QLabel(self.frame)
        self.labelTitle.setObjectName('LabelTitle')

        self.labelTitle.resize(self.width() - 10, 150)
        self.labelTitle.move(0, 40)
        self.labelTitle.setText('Towards Data Science')
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.labelDescription = QLabel(self.frame)
        self.labelDescription.resize(self.width() - 10, 50)
        self.labelDescription.move(0, self.labelTitle.height())
        self.labelDescription.setObjectName('LabelDesc')
        self.labelDescription.setText('<strong>Starting ...</strong>') 
        self.labelDescription.setStyleSheet('color:#50BFE6')
        self.labelDescription.setAlignment(Qt.AlignCenter)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(self.width() - 200 - 10, 50)
        self.progressBar.move(100, self.labelDescription.y() + 130)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, self.n)
        self.progressBar.setValue(20)

        self.labelLoading = QLabel(self.frame)
        self.labelLoading.resize(self.width() - 10, 50)
        self.labelLoading.move(0, self.progressBar.y() + 70)
        self.labelLoading.setObjectName('LabelLoading')
        self.labelLoading.setAlignment(Qt.AlignCenter)
        self.labelLoading.setText('loading...')

    def loading(self):
        self.progressBar.setValue(self.counter)

        if self.counter == int(self.n * 0.6):
            self.labelDescription.setText('<strong>Fetching...</strong>')

        elif self.counter >= self.n:
            self.timer.stop()
            self.close()

            self.myApp = Window()
            self.myApp.show()

        self.counter += 1
        
class AnotherWindow(QWidget):
    def __init__(self,df):
        super().__init__()
        self.title = "Search Result"
        self.width = 1600
        self.height = 700
        self.top, self.left=100,100
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.df=df
        layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.df.shape[0]+1)
        self.tableWidget.setColumnCount(self.df.shape[1])
        self.label=QLabel(f'{len(self.df)} Articles Found.',self)
        self.label.setStyleSheet('color:red;font-size:25px')
        for count,i in enumerate(self.df.columns):
            self.tableWidget.setItem(0,count, QTableWidgetItem(i))

        for k,i in enumerate(self.df.columns):
            for count,j in enumerate(self.df[i]):
                self.tableWidget.setItem(count+1,k, QTableWidgetItem(j))
        self.tableWidget.setColumnWidth(0, 1380)
        self.tableWidget.setColumnWidth(1, 40)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 230)

        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.label)
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)
        

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.no_of_articles_str=''
        self.largest_df=pd.DataFrame()
        self.second=False
        self.third=True
        self.title = "Towards Data Science Articles"
        self.top = 300
        self.left = 150
        self.width = 1200
        self.height = 800
        self.setStyleSheet("background-color: #EEE2DC;")

        self.prevCount=0
        self.getData(10)

        self.InitWindow()
        self.load_screen=LoadingScreen()
        self.show()
    def fetchData(self,noOfArticles):
        try:
            consumer_key='q1ISo2WrhUe2FpmAl7JwJLZeh'
            consumer_secret='CMum2I0SmIs1OJk0darIjT7TKeGc6ZPIrYaKrM2iZswky3Lc4F'
            access_token='1133384700339347456-vBK8jMkYpnPYzPXpZUTULhIA9MTaPH'
            access_token_secret='TsisvgkHekLum7xKchEMOJDHJ4S3ZzOBhVEL5voLwHbm9'

            auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
            auth.set_access_token(access_token,access_token_secret)

            api=tweepy.API(auth)
            print('process Started.....')
            cursor=tweepy.Cursor(api.user_timeline,id='tdatascience',tweet_mode='extended').items(noOfArticles)

            text=np.array([])
            date=np.array([])
            likes=np.array([])
            links=np.array([])
            for i in cursor:
                likes=np.append(likes,i.favorite_count)
                date=np.append(date,i.created_at)
                links=np.append(links,i.full_text[i.full_text.find('https://'):])
                text=np.append(text,i.full_text[:i.full_text.find('https://')])
            df=pd.DataFrame({'Articles':text,'Likes':likes,'Date':date,'Links':links})

            df.Likes=df.Likes.astype(str)
            df.Date=df.Date.astype(str)
            self.data=df
        except tweepy.error.TweepError:QMessageBox.warning(QMessageBox(), 'Error', 'Connection Error');sys.exit(app.exec_())

    def getData(self,noOfArticles):

        noOfArticles=int(noOfArticles)
        if len(self.largest_df)<noOfArticles:

            # if noOfArticles>=1000:
            #     QMessageBox.warning(QMessageBox(), 'Warning', f'Will take {round(noOfArticles*.115/60)} m.\n Press ok to proceed')
            
            self.fetchData(noOfArticles)

                
            self.largest_df=self.data
        else:
            self.data=self.largest_df.head(noOfArticles)

        

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        
        self.searchBox()
        self.creatingTables()
        
        self.show()

    def searchBox(self):

        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText('😀')
        self.textbox.setToolTip('Keywords to search Articles (use "|" as "or" for multiple keywords)')


        self.textbox.setFixedWidth(760)
        validator=QRegExpValidator(QRegExp(r'[0-9]+'))
        self.no = QLineEdit(self)
        self.textbox.setStyleSheet("border : 2px solid #AA00FF")
        self.no.setValidator(validator)
        self.no.setPlaceholderText('¯\_(ツ)_/¯')
        self.no.setToolTip('No. of Articles (more data takes more time) ⏳')
        self.no.setFixedWidth(495)

        self.no.setStyleSheet("border : 2px solid #D50000")
 
        font = self.textbox.font()
        font.setPointSize(15)
        self.textbox.setFont(font)
        font_no=self.no.font()
        font_no.setPointSize(15)
        self.no.setFont(font_no)
        self.button=QPushButton('Find Articles',self)
        self.button.setStyleSheet("font-size : 19px;color:#6200EE;")

        self.button.setFixedWidth(160)
        self.button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.refresh=QPushButton('Refresh',self)
        self.refresh.setStyleSheet('color:#ff0266;font-size:19px')
        self.about=QPushButton('About',self)
        self.about.setStyleSheet('color:#ff0266;font-size:19px')
        self.about.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.button_word=QPushButton('Show Word Cloud',self)
        self.button_word.setToolTip('"Word cloud" of words of all articles ☁ (Temporary suspension)')
        self.button_word.setStyleSheet("font-size : 19px;color:#6200EE;")
        # self.button_word.setEnabled(False)

        self.button_word.setFixedWidth(160)
        
        self.about.clicked.connect(self.aboutFunc)
        self.button.clicked.connect(self.show_new_window)
        # self.button_word.clicked.connect(self.show_new_window_matplotlib)
        self.refresh.clicked.connect(self.refreshFunc)
        self.button_word.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.refresh.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.refresh.setFixedWidth(160)
        self.about.setFixedWidth(160)
        self.refresh.setToolTip('Refresh after editing no. of Articles')
        self.vBoxLayout = QVBoxLayout()
        hBoxLayout1 = QHBoxLayout()
        hBoxLayout2 = QHBoxLayout()
        
        hBoxLayout1.addWidget(self.button)
        hBoxLayout1.addWidget(self.about)

        hBoxLayout2.addWidget(self.button_word)
        hBoxLayout2.addWidget(self.refresh)
        self.vBoxLayout.addWidget(self.textbox)
        self.vBoxLayout.addWidget(self.no)

        self.vBoxLayout.addLayout(hBoxLayout1)
        self.vBoxLayout.addLayout(hBoxLayout2)
        
    def aboutFunc(self):
        self.about=About()
        self.about.show()

    def refreshFunc(self):
        if self.no.text()!='':
            self.getData(self.no.text())
            self.tableWidget.deleteLater()
            self.tableWid()
            self.creatingTables()

    def tableWid(self):
    
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.data.shape[0]+1)
        self.tableWidget.setColumnCount(self.data.shape[1])
        for count,i in enumerate(self.data.columns):
            self.tableWidget.setItem(0,count,QTableWidgetItem(i))
                
        for k,i in enumerate(self.data.columns):
            for count,j in enumerate(self.data[i]):
                self.tableWidget.setItem(count+1,k, QTableWidgetItem(j))
                self.tableWidget.setStyleSheet('color:white;background-color:#303030;font-size:20px;border:1px solid black;')
    
    def creatingTables(self):

        if self.third:
            self.tableWid()
        self.third=False
            
        self.setWindowOpacity(0.87)
        self.tableWidget.setColumnWidth(0, 1380)
        self.tableWidget.setColumnWidth(1, 40)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 230)
        
        self.vBoxLayout.addWidget(self.tableWidget)
        
        self.setLayout(self.vBoxLayout)


    def show_new_window(self,checked):
        df=self.data[self.data.Articles.str.contains(self.textbox.text(),case=False)]
        self.w = AnotherWindow(df)
        self.w.show()
    # def show_new_window_matplotlib(self):
    #     import matplotlib.pyplot as plt
    #     from wordcloud import WordCloud, STOPWORDS
    #     topics_str = " ".join(topics for topics in self.data.Articles)
    #     stopwords = set(STOPWORDS)
    #     common_words={'python','Python','data','Data','science','Science','RT','guide','Guide','ML','Model','Learning','model','learning','Machine','machine','Part','part','AI','Using','using'}
    #     stopwords.update(common_words)
    #     wine_mask=np.full((512,512), 95, dtype=int)
    #     transformed_wine_mask = np.ndarray((wine_mask.shape[0],wine_mask.shape[1]), np.int32)

    #     for i in range(len(wine_mask)):
    #         transformed_wine_mask[i] = list(map(self.transform_format, wine_mask[i]))
    #     wordcloud = WordCloud(background_color="white", max_words=1000, mask=transformed_wine_mask,stopwords=stopwords, contour_width=3, contour_color='firebrick').generate(topics_str)

    #     plt.figure(figsize=(14,7))
    #     plt.gcf().canvas.manager.set_window_title('Word Cloud')
    #     plt.suptitle("Words like 'Python','Data','Guide','ML','Model','Machine','Learning','Part','Using','AI' and 'Science' are omitted because they are more frequent.",fontweight="bold")
    #     plt.axis("off")
    #     plt.imshow(wordcloud)
    #     plt.show()
    
    def transform_format(self,val):
        if val == 0:
            return 255
        else:
            return val
        


app = QApplication(sys.argv)


app.setStyleSheet('''
        #LabelTitle {
            font-size: 60px;
            
            color:#39ff14;
        }

        #LabelDesc {
            font-size: 30px;
            color: #c2ced1;
        }

        #LabelLoading {
            font-size: 30px;
            color: #e8e8eb;
        }

        

        QProgressBar {
            background-color: #DA7B93;
            color: rgb(200, 200, 200);
            border-style: none;
            border-radius: 10px;
            text-align: center;
            font-size: 30px;
        }

        QProgressBar::chunk {
            border-radius: 10px;
            background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #1C3334, stop:1 #376E6F);
        }
    ''') 



splash = SplashScreen()
splash.show()

sys.exit(app.exec())

