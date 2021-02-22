import pandas as pd
from matplotlib.pyplot import pie, show ,title



df = pd.read_csv ('Survey-on-Regular-Life-Responses.csv')

title('Felling that everything you have done has been a failure.')



#sums = df.groupby(df["Gender"])["Gender"].count()

#sums = df.groupby(df["Occupation"])["Occupation"].count()

#sums = df.groupby(df["All the tasks you have performed, are taking much more time than usual."])["All the tasks you have performed, are taking much more time than usual."].count()

#sums = df.groupby(df["You are facing a lack of concentration."])["You are facing a lack of concentration."].count()

#sums = df.groupby(df["You are feeling you have no future."])["You are feeling you have no future."].count()

#sums = df.groupby(df["You are facing problems with making decisions."])["You are facing problems with making decisions."].count()

sums = df.groupby(df["You feel, your life is sad, as there is no joy in your life anymore."])["You feel, your life is sad, as there is no joy in your life anymore."].count()

#sums = df.groupby(df["You have lost interest in all things that were important to you once upon a time."])["You have lost interest in all things that were important to you once upon a time."].count()

#sums = df.groupby(df["You have been feeling guilty for everything you do."])["You have been feeling guilty for everything you do."].count()

#sums = df.groupby(df["You have been very irritated and angry recently."])["You have been very irritated and angry recently."].count()

#sums = df.groupby(df["You have been feeling very fatigued."])["You have been feeling very fatigued."].count()

sums = df.groupby(df["You are feeling that everything you have done has been a failure."])["You are feeling that everything you have done has been a failure."].count()

#sums = df.groupby(df["You are having suicidal thoughts."])["You are having suicidal thoughts."].count()

#sums = df.groupby(df["You have lost or gained weight without any diet programs."])["You have lost or gained weight without any diet programs."].count()

#sums = df.groupby(df["You are having a loss of appetite."])["You are having a loss of appetite."].count()

#sums = df.groupby(df["You are having trust issues with everyone around you."])["You are having trust issues with everyone around you."].count()

#sums = df.groupby(df["You are having trouble in all your relationships (home as well as professional)."])["You are having trouble in all your relationships (home as well as professional)."].count()

#sums = df.groupby(df["You are having a lack of sleep."])["You are having a lack of sleep."].count()

#sums = df.groupby(df["You are having a problem with your sexual life."])["You are having a problem with your sexual life."].count()

#sums = df.groupby(df["You are losing interest on your opposite gender."])["You are losing interest on your opposite gender."].count()

#sums = df.groupby(df["How often do you use the Internet?"])["How often do you use the Internet?"].count()

#sums = df.groupby(df["On average, how many hours per day do you spend on the internet?"])["On average, how many hours per day do you spend on the internet?"].count()

#sums = df.groupby(df["Which device do you use to use the Internet?"])["Which device do you use to use the Internet?"].count()

#sums = df.groupby(df["Which internet connection do you use?"])["Which internet connection do you use?"].count()

#sums = df.groupby(df["What do you like doing most online?"])["What do you like doing most online?"].count() ??????????????????????????????????????????????????????????????????????????????????????????

#sums = df.groupby(df["How often do you use... [Chat Rooms]"])["How often do you use... [Chat Rooms]"].count()

#sums = df.groupby(df["How often do you use... [Instant Messenger]"])["How often do you use... [Instant Messenger]"].count()

#sums = df.groupby(df["How often do you use... [Social Networking Sites]"])["How often do you use... [Social Networking Sites]"].count()

#sums = df.groupby(df["How often do you use... [Blogs]"])["How often do you use... [Blogs]"].count()

#sums = df.groupby(df["How often do you use... [Gaming]"])["How often do you use... [Gaming]"].count()

#sums = df.groupby(df["How often do you use... [Web Browsing]"])["How often do you use... [Web Browsing]"].count()

#sums = df.groupby(df["How often do you use... [Music]"])["How often do you use... [Music]"].count()

#sums = df.groupby(df["How often do you use... [File Sharing]"])["How often do you use... [File Sharing]"].count()

#sums = df.groupby(df["How often do you use... [Shopping]"])["How often do you use... [Shopping]"].count()

#sums = df.groupby(df["How often do you use... [News]"])["How often do you use... [News]"].count()

#sums = df.groupby(df["How often do you use... [Internet TV]"])["How often do you use... [Internet TV]"].count()

#sums = df.groupby(df["Where do you use the internet?"])["Where do you use the internet?"].count()?????????????????????????????????????????????????????????????????????????????????????????????????????

#sums = df.groupby(df["If you use Internet at home, what room do you use it in?"])["If you use Internet at home, what room do you use it in?"].count()

#sums = df.groupby(df["What is the main way of communication with your offline friends?"])["What is the main way of communication with your offline friends?"].count()????????????????????????????????????????????????????

#sums = df.groupby(df["Have you ever met someone in the real world you have only met online?"])["Have you ever met someone in the real world you have only met online?"].count()

#sums = df.groupby(df['If you answered "yes" to the previous question, did you take someone with you?'])['If you answered "yes" to the previous question, did you take someone with you?'].count()

#sums = df.groupby(df["How often do you go out in a day?"])["How often do you go out in a day?"].count()

#sums = df.groupby(df["Do you like outing with friends?"])["Do you like outing with friends?"].count()

#sums = df.groupby(df["Does it make you smile?"])["Does it make you smile?"].count()

#sums = df.groupby(df["Remark this image."])["Remark this image."].count()



pie(sums, labels=sums.index,autopct='%1.1f%%')
show()







