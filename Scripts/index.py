import streamlit as st;
import mysql.connector
import pandas as pd;
import numpy as np;
import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.express as px

def show_all_table_data():
    mydb = mysql.connector.connect(host="localhost", user="root", password="khushboo", database="customermanagement_system")
    c = mydb.cursor()
    c.execute("SHOW TABLES")
    tables = [table[0] for table in c]

    if tables:
        st.write("Tables in the database:")
        for table in tables:
            st.write(table)
            c.execute(f"SELECT * FROM {table}")
            table_data = [row for row in c]
            if table_data:
                df = pd.DataFrame(table_data, columns=[desc[0] for desc in c.description])
                st.write(f"Data in {table}:")
                st.dataframe(df)
            else:
                st.write(f"No data found in {table}.")
    else:
        st.write("No tables found in the database.")

st.set_page_config(page_title='Customer Management System',page_icon='random')
st.sidebar.title("Customer Management system")
st.sidebar.image("https://www.dzinepixel.com/wp-content/uploads/2022/11/Content-Management-System.gif")
st.sidebar.image("https://tse4.mm.bing.net/th?id=OIP.Zd4th3uQAkrmxJ00W4piywHaEQ&pid=Api&P=0&h=180")

choice=st.sidebar.selectbox("My Menu",("Home", "USER", "Admin" ,"Sentiment Analysis of sales"))
st.header(choice)

if(choice=="Home"):
    st.markdown("<h1 style= 'text-align:center;color:Red;'>CUSTOMER MANAGEMENT SYSTEM</h1>",unsafe_allow_html=True)
    st.markdown("<center><h1 style= 'color:Red;'>WELCOME</h1></center>",unsafe_allow_html=True)
    st.image("https://blog.ttisi.com/hs-fs/hubfs/072221_blog.gif?width=2400&name=072221_blog.gif")
    


elif(choice=="USER"):
    st.markdown("<h1 style= 'text-align:center;color:brown;'>WELCOME TO USER LOGIN SECTION</h1>",unsafe_allow_html=True)
    st.image("https://cdn.dribbble.com/users/798777/screenshots/3928976/dribbble_nyt.gif")

    if 'login' not in st.session_state:
        st.session_state['login']=False
    id=st.text_input("ENTERS USER ID") 
    password=st.text_input("ENTER PASSWORD")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
        c=mydb.cursor();
        c.execute("select * from user_login")
        for row in c:
            if(row[1]==id and row[2]==password):
                st.session_state['login']= True;
                break;
        if(st.session_state['login']==False):
            st.subheader("Incorrect ID or Password")
    if(st.session_state['login']==True):
        st.subheader("login Succesful")

        choice2=st.selectbox("Features",("None","VIEW ALL CUSTOMER DETAIL", "ADD CUSTOMER DETAILS", "ADD TRANSACTION DETAIL", "VIEW LOCATION","INCOME DETAIL"))
        if(choice2=="VIEW ALL CUSTOMER DETAIL"):
            mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
            c=mydb.cursor();
            c.execute("select * from customer_detail")
            l=[]
            for row in c:
                l.append(row)
            df=pd.DataFrame(data=l, columns=['cust_id', 'name', 'address', 'email', 'contact_no', 'gender'])
            st.dataframe(df)
        if(choice2=="ADD CUSTOMER DETAILS"):
            cust_id=st.text_input("Enter Id of Customer")
            name=st.text_input("Enter Name")
            add=st.text_input("Enter address")
            email =st.text_input("Enter Email")
            contact_no =st.text_input("Enter Contact Number")
            gender = st.text_input("Enter Gender")
            btn4=st.button("submit")
            if(btn4):
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
                c=mydb.cursor();
                c.execute("insert into customer_detail values(%s, %s, %s, %s, %s, %s)",(cust_id,name,add,email,contact_no,gender))
                mydb.commit()
                st.header("submittted successfully")
            btn5= st.button("Show details")
            if(btn5):
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
                c=mydb.cursor();
                c.execute("select * from customer_detail ")
                l=[]
                for row in c:
                    l.append(row)
                df=pd.DataFrame(data=l, columns=['cust_id', 'name', 'address', 'email', 'contact_no', 'gender'])
                st.dataframe(df)
        if(choice2=="ADD TRANSACTION DETAIL"):
            trans_id=st.text_input("Enter Id of transaction Id")
            cust_id=st.text_input("Enter Id of Customer")
            pro_id=st.text_input("Enter Product Id")
            loc=st.text_input("Enter location id")
            btn4=st.button("submit")
            if(btn4):
                doi=str(datetime.datetime.now())
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
                c=mydb.cursor();
                c.execute("insert into trans values(%s, %s, %s, %s, %s)",(trans_id,cust_id,pro_id,loc,doi))
                mydb.commit()
                st.header("submittted successfully")
            btn5= st.button("Show details")
            if(btn5):
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
                c=mydb.cursor();
                c.execute("select * from trans")
                l=[]
                for row in c:
                    l.append(row)
                df=pd.DataFrame(data=l, columns=['trans_id','cust_id', 'pro_id', 'loc', 'doi'])
                st.dataframe(df)
        if(choice2=="VIEW LOCATION"):
            loc_id=st.text_input("Enter Location Id")
            location=st.text_input("Enter Location")
            city=st.text_input("Enter City")
            
            btn4=st.button("submit")
            if(btn4):
                
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
                c=mydb.cursor();
                c.execute("insert into loction values(%s, %s, %s)",(loc_id,location,city))
                mydb.commit()
                st.header("submittted successfully")
            btn5= st.button("Show details")
            if(btn5):
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
                c=mydb.cursor();
                c.execute("select * from loction")
                l=[]
                for row in c:
                    l.append(row)
                df=pd.DataFrame(data=l, columns=['loc_id','location', 'city'])
                st.dataframe(df)
        if(choice2=="INCOME DETAIL"):
            emp_id=st.text_input("Enter Employee Id")
            pro_id=st.text_input("Enter Product Id")
            profit=st.text_input("Enter Profit")
            income=st.text_input("Enter Income")
            
            btn4=st.button("submit")
            if(btn4):
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
                c=mydb.cursor();
                c.execute("insert into income values(%s, %s, %s,%s)",(emp_id,pro_id,profit,income))
                mydb.commit()
                st.header("submittted successfully")
            btn5= st.button("Show details")
            if(btn5):
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
                c=mydb.cursor();
                c.execute("select * from income")
                l=[]
                for row in c:
                    l.append(row)
                df=pd.DataFrame(data=l, columns=['emp_id','pro_id', 'profit','income'])
                st.dataframe(df)
            
        
        

elif(choice=="Admin"):
    st.markdown("<h1 style= 'text-align:center;color:green;'>WELCOME TO ADMIN</h1>", unsafe_allow_html=True)
    st.image("https://indsaccrm.com/navigate/assets/images/sg.gif")
    if 'login2' not in st.session_state:
        st.session_state['login2']=False
    id=st.text_input("Enter admin ID") 
    password=st.text_input("Enter password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
        c=mydb.cursor();
        c.execute("select * from admin_login")
        for row in c:
            if(row[1]==id and row[2]==password):
                st.session_state['login2']= True;
                break;
        if(st.session_state['login2']==False):
            st.subheader("Incorrect ID or Password")
    if(st.session_state['login2']==True):
        st.subheader("login Succesful")
        choice2=st.selectbox("Features",("None","ADD USER", "ADD EMPLOYEE DETAILS","PRODUCT DETAILS","VEIW TRANSACTION DETAIL","VIEW ALL TABLES"))

        if(choice2=="ADD USER"):
            name=st.text_input("Enter New User")
            user_id=st.text_input("Enter user id")
            pas_id = st.text_input("Enter password", key="password_input")

            btn4=st.button("submit")
            if(btn4):
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
                c=mydb.cursor();
                c.execute("insert into user_login values(%s, %s, %s)",(name,user_id,pas_id))
                mydb.commit()
                st.header("submittted successfully")
            btn5= st.button("Show details")
            if(btn5):
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
                c=mydb.cursor();
                c.execute("select * from user_login ")
                l=[]
                for row in c:
                    l.append(row)
                df=pd.DataFrame(data=l, columns=['name', 'user_id','pas_id'])
                st.dataframe(df)


        
        if(choice2=="ADD EMPLOYEE DETAILS"):
            emp_id=st.text_input("Enter Employee Id")
            name=st.text_input("Enter Name")
            job=st.text_input("Enter job title")
            contact_no =st.text_input("Enter Contact Number")
            hd = st.text_input("Enter Hired date")
            sal =st.text_input("Enter salary")
            btn4=st.button("submit")
            if(btn4):
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
                c=mydb.cursor();
                c.execute("insert into employee_detail values(%s, %s, %s, %s, %s, %s)",(emp_id,name,job,contact_no,hd,sal))
                mydb.commit()
                st.header("submittted successfully")
            btn5= st.button("Show details")
            if(btn5):
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
                c=mydb.cursor();
                c.execute("select * from employee_detail ")
                l=[]
                for row in c:
                    l.append(row)
                df=pd.DataFrame(data=l, columns=['emp_id', 'name', 'job', 'contact_no', 'hd', 'sal'])
                st.dataframe(df)
        if(choice2=="PRODUCT DETAILS"):
            pro_id=st.text_input("Enter Product ID")
            pro_name=st.text_input("Enter Product Name")
            pro_des=st.text_input("Enter Product description")
            price=st.text_input("Enter Price")
            
            btn4=st.button("submit")
            if(btn4):
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
                c=mydb.cursor();
                c.execute("insert into product values(%s,%s, %s, %s)",(pro_id,pro_name,pro_des,price))
                mydb.commit()
                st.header("submittted successfully")
            btn5= st.button("Show details")
            if(btn5):
                mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
                c=mydb.cursor();
                c.execute("select * from product ")
                l=[]
                for row in c:
                    l.append(row)
                df=pd.DataFrame(data=l, columns=['pro_id','pro_name', 'pro_des','price'])
                st.dataframe(df)
        if(choice2=="VEIW TRANSACTION DETAIL"):
            mydb=mysql.connector.connect(host="localhost", user="root", password="khushboo",database="customermanagement_system");
            c=mydb.cursor();
            c.execute("select * from trans")
            l=[]
            for row in c:
               l.append(row)
            df=pd.DataFrame(data=l, columns=['trans_id','cust_id', 'pro_id', 'loc', 'doi'])
            st.dataframe(df)
        if(choice2=="VIEW ALL TABLES"):
            show_all_table_data()



elif(choice =="Sentiment Analysis of sales"):
    st.markdown("<h1 style= 'text-align:center;color:red;'>ANALYSIS OF CUSTOMER REVIEW </h1>", unsafe_allow_html=True)
    st.image("https://miro.medium.com/proxy/1*_JW1JaMpK_fVGld8pd1_JQ.gif")
    choice3=st.selectbox("Features",("None","Analyze Sentiment","Visualize the Results","CSV Files"))
    if(choice3 == "Analyze Sentiment"):
        st.image("https://i.pinimg.com/originals/52/ad/6a/52ad6a11c1dcb1692ff9e321bd520167.gif")
        url=st.text_input("Enter Google Sheet URL")
        r=st.text_input("Enter Range")
        c=st.text_input("Enter Column")
        btn = st.button("Analyze")
        if btn:
            if 'cred' not in st.session_state:
                f=InstalledAppFlow.from_client_secrets_file('key.json',['https://www.googleapis.com/auth/spreadsheets'])
                st.session_state['cred']=f.run_local_server(port=0)
            mymodel=SentimentIntensityAnalyzer()
            service=build('Sheets','v4',credentials=st.session_state['cred']).spreadsheets().values()
            d=service.get(spreadsheetId=url,range=r).execute()
            mycolumns=d['values'][0]
            mydata=d['values'][1:]
            df=pd.DataFrame(data=mydata,columns=mycolumns)
            l=[]
            for i in range(0,len(df)):
                k=df._get_value(i,c)
                pred = mymodel.polarity_scores(k)
                if(pred['compound']>0.5):
                    l.append("positive")
                elif(pred['compound']<-0.5):
                    l.append("Negative")
                else:
                    l.append("Neutral")
            df['Sentiment']=l
            st.dataframe(df)
            df.to_csv("Review.csv",index=False)
            st.header("This data has been saved by name of review.csv")
    if(choice3=="Visualize the Results"):
        st.image("https://cdn.dribbble.com/users/72535/screenshots/2630779/data_visualization_by_jardson_almeida.gif")
        st.image("https://cdn.dribbble.com/users/3083633/screenshots/8258363/media/55d788add27fc8029c22aefe21603f73.gif")
    
        choice2=st.selectbox("Choose Visualization",("None","Pie","Histogram","Scatter Plot"))
        if(choice2=="Pie"):
            df=pd.read_csv("Review.csv")
            posper=(len(df[df['Sentiment']=='positive'])/len(df))*100
            negper=(len(df[df['Sentiment']=='Negative'])/len(df))*100
            neuper=(len(df[df['Sentiment']=='Neutral'])/len(df))*100
            fig=px.pie(values=[posper,negper,neuper],names=['positive','Negative','Neutral'])
            st.plotly_chart(fig)
        elif(choice2=="Histogram"):
            t=st.text_input("Choose any Categorical Column")
            if t:
                df=pd.read_csv("Review.csv")
                fig=px.histogram(x=df['Sentiment'],color=df[t])
                st.plotly_chart(fig)
        elif(choice2=="Scatter Plot"):
            df=pd.read_csv("Review.csv")
            x=st.selectbox("Choose any continious data for x-axis",df.columns)
            y=st.selectbox("Choose any continious data for y-axis",df.columns)
            if st.button("Generate Scatter Plot") and x and y:
                fig = px.scatter(df, x=x, y=y, title="Scatter Plot Representation", labels={x: 'X-axis', y: 'Y-axis'})
                st.plotly_chart(fig)
    if(choice3=="CSV Files"):
        st.image("https://i.pinimg.com/originals/52/ad/6a/52ad6a11c1dcb1692ff9e321bd520167.gif")
        path=st.text_input("Enter Files Path")
        c=st.text_input("Enter Column")
        btn = st.button("Analyze")
        if btn:
            if 'cred' not in st.session_state:
                f=InstalledAppFlow.from_client_secrets_file('key.json',['https://www.googleapis.com/auth/spreadsheets'])
                st.session_state['cred']=f.run_local_server(port=0)
            mymodel=SentimentIntensityAnalyzer()
            df=pd.read_csv(path)
            l=[]
            for i in range(0,len(df)):
                k=df._get_value(i,c)
                pred = mymodel.polarity_scores(k)
                if(pred['compound']>0.5):
                    l.append("positive")
                elif(pred['compound']<-0.5):
                    l.append("Negative")
                else:
                    l.append("Neutral")
            df['Sentiment']=l
            st.dataframe(df)
            df.to_csv("Review.csv",index=False)
            st.header("This data has been saved by name of review.csv")
        
                         
    
    




                         


    
