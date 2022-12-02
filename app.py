#importing all classes from inside tkinter module
from tkinter import *
#ensuring that we are able to connect with the file that handle's all database's I/O operations
from mydb import Database

#to show error or success message boxes
from tkinter import messagebox

#for all api related activities
from api import api_functions

#class for all GUI related functions
class NLPApp:
    def __init__(self):
        
        #creating object of database
        self.dbo=Database()
        
        #creating object of APIs
        self.apio=api_functions()
        
        #creating obj of Tkinter. Tk() is a main class inside Tkinter
        self.root=Tk()
        #adding title to the app
        self.root.title('NLPApp')
        #adding icon at the top
        self.root.iconbitmap('resources/favicon.ico')
        #adding background color to the page
        self.root.configure(bg='#2ab7ca')
        # specifying the shape of the window on opening the app
        self.root.geometry('350x600')
        # calling the login page at the startup
        self.login_page()
        #
        self.root.mainloop()
    
    def login_page(self):
        """This is the login page, the first page to load when user open's the app. Takes' the user's credentials and compares with the database and gives appropriate outputs
        """
        
        
        #! clearing the contents of previous gui before loading this page's gui
        self.clear()
        
        #! main heading -> NLP App
        
        # mentioning text for heading,background color of text area, and color of text
        heading=Label(self.root,text="NLP App",bg="#2ab7ca",fg="black")
        #putting the text in the page with specific padding on y direction. The text inside Label() is shows only when it is packed
        heading.pack(pady=(30,30))
        #specifying font-family,size, and special property of font
        heading.configure(font=('verdana',24,'bold'))
        
        #! email and password entry area
        
        # shows "Enter EmailID" 
        email_label=Label(self.root,text='Enter EmailId')
        email_label.pack(pady=(10,10))
        # Input area for user to enter email id
        self.email=Entry(self.root,width=40)
        #making the above text visible in the page. ipady is internal ypadding. It is  for the size of the text box in which user inputs the data. Only for input box's height, we need to use ipady. For all other components, there is a height attribute during the component creation
        self.email.pack(pady=(10,10),ipady=3)
        

        
        # shows "Enter Password" 
        password_label=Label(self.root,text='Enter Password')
        #making the above text visible in the page
        password_label.pack(pady=(5,10))
        # allowing user to input the password
        self.password=Entry(self.root,width=40,show='*')
        #making the above text visible in the page. ipady is internal ypadding. It is  for the size of the text box in which user inputs the data
        self.password.pack(pady=(5,10),ipady=3)
        
        
        # login button
        
        login_button=Button(self.root,text='Login',width=15,height=2,command=self.check_login)
        login_button.pack(pady=(5,10))
        login_button.configure(font=('verdana',10,'bold'))
        
        #! Redirect to registration Page
        
        # shows "Not a registered user?" 
        registration_redirect_label=Label(self.root,text='Not a registered user?')
        #making the above text visible in the page
        registration_redirect_label.pack(pady=(10,10))
        # button redirecting to registration page
        registration_redirect_button=Button(self.root,text='Register Here',width=15,command=self.registration_page)
        registration_redirect_button.pack(pady=(5,5))
   
    def registration_page(self):
        
        #! clearing the contents of previous gui before loading this page's gui
        self.clear()
        
        #! main heading -> NLP App
        
        # mentioning text for heading,background color of text area, and color of text
        heading0=Label(self.root,text="NLP App",bg="#2ab7ca",fg="black")
        #putting the text in the page with specific padding on y direction. The text inside Label() is shows only when it is packed
        heading0.pack(pady=(30,30))
        #specifying font-family,size, and special property of font
        heading0.configure(font=('verdana',24,'bold'))
        
        #! name, email and password entry area
        # shows "Enter Name" 
        name1=Label(self.root,text='Enter Name')
        name1.pack(pady=(10,10))
        # Input area for user to enter name
        self.reg_name=Entry(self.root,width=40)
        #making the above text visible in the page. ipady is internal ypadding. It is  for the size of the text box in which user inputs the data. Only for input box's height, we need to use ipady. For all other components, there is a height attribute during the component creation
        self.reg_name.pack(pady=(10,10),ipady=3)
        
        
        # shows "Enter EmailID" 
        email_label1=Label(self.root,text='Enter EmailId')
        email_label1.pack(pady=(10,10))
        # Input area for user to enter email id
        self.reg_email=Entry(self.root,width=40)
        #making the above text visible in the page. ipady is internal ypadding. It is  for the size of the text box in which user inputs the data. Only for input box's height, we need to use ipady. For all other components, there is a height attribute during the component creation
        self.reg_email.pack(pady=(10,10),ipady=3)
        
        
        # shows "Enter Password" 
        password_label1=Label(self.root,text='Enter Password')
        #making the above text visible in the page
        password_label1.pack(pady=(5,10))
        # allowing user to input the password
        self.reg_password=Entry(self.root,width=40,show='*')
        #making the above text visible in the page. ipady is internal ypadding. It is  for the size of the text box in which user inputs the data
        self.reg_password.pack(pady=(5,10),ipady=3)
        
        
        #! Register button
        
        reg_button=Button(self.root,text='Register',width=15,height=2,command=self.registration_process)
        reg_button.pack(pady=(5,10))
        reg_button.configure(font=('verdana',10,'bold'))
        
        
        #! Redirect to login Page if already registered
        
        # shows "Not a registered user?" 
        login_redirect_label=Label(self.root,text='Already Registered?')
        #making the above text visible in the page
        login_redirect_label.pack(pady=(10,10))
        # button redirecting to login page
        login_redirect_button=Button(self.root,text='Login Here',width=15,command=self.login_page)
        login_redirect_button.pack(pady=(5,5))
        
    def home(self):
        #! clearing the contents of previous gui before loading this page's gui
        self.clear()
        
        #! main heading -> NLP App
        
        # mentioning text for heading,background color of text area, and color of text
        heading0=Label(self.root,text="NLP App",bg="#2ab7ca",fg="black")
        #putting the text in the page with specific padding on y direction. The text inside Label() is shows only when it is packed
        heading0.pack(pady=(30,30))
        #specifying font-family,size, and special property of font
        heading0.configure(font=('verdana',24,'bold'))
        
        
        #! 3 buttons for 3 different types of NLP analysis
        
        #button for NER
        ner_button=Button(self.root,text='Named Entity Recognition',width=25,height=5,command=self.ner)
        ner_button.pack(pady=(10,10))
        ner_button.configure(font=('verdana',10,'bold'))
        
        #button for sentiment analysis
        sentiment_button=Button(self.root,text='Sentiment Analysis',width=25,height=5,command=self.sentiment_analysis)
        sentiment_button.pack(pady=(10,10))
        sentiment_button.configure(font=('verdana',10,'bold'))
        
        #button for emotion analysis
        emotion_button=Button(self.root,text='Emotion Analysis',width=25,height=5,command=self.emotion_analysis)
        emotion_button.pack(pady=(10,10))
        emotion_button.configure(font=('verdana',10,'bold'))
        
        #logout button
        emotion_button=Button(self.root,text='Logout',width=15,height=3,command=self.login_page)
        emotion_button.pack(pady=(10,10))
        emotion_button.configure(font=('verdana',8,'bold'))
    
    def sentiment_analysis(self):
        #! clearing the contents of previous gui before loading this page's gui
        self.clear()
        
        #! main heading -> NLP App
        
        # mentioning text for heading,background color of text area, and color of text
        heading_s=Label(self.root,text="Sentiment Analyzer",bg="#2ab7ca",fg="black")
        #putting the text in the page with specific padding on y direction. The text inside Label() is shows only when it is packed
        heading_s.pack(pady=(30,30))
        #specifying font-family,size, and special property of font
        heading_s.configure(font=('verdana',20,'bold'))
        
        
        #! Taking user input
        
        user_data_label_s=Label(self.root,text='Enter the text here ...')
        user_data_label_s.pack(pady=(10,10))
        self.user_data_input_s=Entry(self.root,width=40)
        self.user_data_input_s.pack(pady=(10,10),ipady=3)
        
        #! Area to display output
        self.output_label_s=Label(self.root,text='',bg="#2ab7ca",width=40,height=4)
        self.output_label_s.pack(pady=(10,10))
        self.output_label_s.configure(font=('verdana','10','bold'))
        
        #! button to submit the input
        submit_button_s=Button(self.root,text='Analyze',width=15,height=2,command=self.get_sentiment_response)
        submit_button_s.pack(pady=(5,10))
        submit_button_s.configure(font=('verdana',10,'bold'))
        
        #! go back button
        go_back_button_s=Button(self.root,text='Go back',width=15,height=2,command=self.home)
        go_back_button_s.pack(pady=(5,10))
        go_back_button_s.configure(font=('verdana',10,'bold'))
        
    def get_sentiment_response(self):
        text_s=self.user_data_input_s.get()
        response_s=self.apio.sentiment_analysis(text_s)
        self.output_label_s['text']=response_s
    
    def ner(self):
        #! clearing the contents of previous gui before loading this page's gui
        self.clear()
        
        #! main heading -> NLP App
        
        # mentioning text for heading,background color of text area, and color of text
        heading_n=Label(self.root,text="Named Entity Recognition",bg="#2ab7ca",fg="black")
        #putting the text in the page with specific padding on y direction. The text inside Label() is shows only when it is packed
        heading_n.pack(pady=(30,30))
        #specifying font-family,size, and special property of font
        heading_n.configure(font=('verdana',20,'bold'))
        
        
        #! Taking user input
        
        user_data_label_n=Label(self.root,text='Enter the text here ...')
        user_data_label_n.pack(pady=(10,10))
        self.user_data_input_n=Entry(self.root,width=40)
        self.user_data_input_n.pack(pady=(10,10),ipady=3)
        
        #! Area to display output
        self.output_label_n=Label(self.root,text='',bg="#2ab7ca",width=40,height=7)
        self.output_label_n.pack(pady=(10,10))
        self.output_label_n.configure(font=('verdana','10','bold'))
        
        #! button to submit the input
        submit_button_n=Button(self.root,text='Analyze',width=15,height=2,command=self.get_ner_response)
        submit_button_n.pack(pady=(5,10))
        submit_button_n.configure(font=('verdana',10,'bold'))
        
        #! go back button
        go_back_button_n=Button(self.root,text='Go back',width=15,height=2,command=self.home)
        go_back_button_n.pack(pady=(5,10))
        go_back_button_n.configure(font=('verdana',10,'bold'))
    
    def get_ner_response(self):
        text_n=self.user_data_input_n.get()
        response_n=self.apio.ner(text_n)
        self.output_label_n['text']=response_n    
    
    def emotion_analysis(self):
        #! clearing the contents of previous gui before loading this page's gui
        self.clear()
        
        #! main heading -> NLP App
        
        # mentioning text for heading,background color of text area, and color of text
        heading_e=Label(self.root,text="Emotion Analysis",bg="#2ab7ca",fg="black")
        #putting the text in the page with specific padding on y direction. The text inside Label() is shows only when it is packed
        heading_e.pack(pady=(30,30))
        #specifying font-family,size, and special property of font
        heading_e.configure(font=('verdana',20,'bold'))
        
        
        #! Taking user input
        
        user_data_label_e=Label(self.root,text='Enter the text here ...')
        user_data_label_e.pack(pady=(10,10))
        self.user_data_input_e=Entry(self.root,width=40)
        self.user_data_input_e.pack(pady=(10,10),ipady=3)
        
        #! Area to display output
        self.output_label_e=Label(self.root,text='',bg="#2ab7ca",width=40,height=7)
        self.output_label_e.pack(pady=(10,10))
        self.output_label_e.configure(font=('verdana','10','bold'))
        
        #! button to submit the input
        submit_button_e=Button(self.root,text='Analyze',width=15,height=2,command=self.get_emotion_response)
        submit_button_e.pack(pady=(5,10))
        submit_button_e.configure(font=('verdana',10,'bold'))
        
        #! go back button
        go_back_button_e=Button(self.root,text='Go back',width=15,height=2,command=self.home)
        go_back_button_e.pack(pady=(5,10))
        go_back_button_e.configure(font=('verdana',10,'bold'))
        
    def get_emotion_response(self):
        text_e=self.user_data_input_e.get()
        response_e=self.apio.emotion_analysis(text_e)
        self.output_label_e['text']=response_e
           
    def check_login(self):
        """Checks the credibility of the user entered credentials inside the database. Shows error message and successful message based on the input
        """
        
        #fetching user entered email and password
        email=self.email.get()
        password=self.password.get()
        
        #using login_checker from mydb.py to check the existence of credentials
        response=self.dbo.login_checker(email,password)
        
        #if credentials match with those in db, show success message and redirect to nlp home page
        if response:
            res=messagebox.showinfo('Success','You have successfully logged in')
            if res=='ok':
                self.home()
        #else show error message
        else:
            messagebox.showerror('Error','Invalid Credentials')          
        
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
        
    def registration_process(self):
        
        #! if entered credentials are already present inside the db, show error. Else, add it to db
        
        # fetching the credentials entered by the user
        name=self.reg_name.get()
        email=self.reg_email.get()
        password=self.reg_password.get()
        
        
        #calling the database function to see if the credentials are present or not
        response=self.dbo.check_user_existence(name,email,password)
        
        
        #if emailid is already present in the database, show error message and then re-direct to login page
        if response:
            res=messagebox.showerror('Error','User mail ID already registered with us')
            if res=='ok':
                self.login_page()
        #if mail id is not already present in the database, show success after adding it to db, and then redirect to login page
        else:
            res=messagebox.showinfo('Success','Registration Successful')
            if res=='ok':
                self.login_page()
      
        
        
        
        
        
obj=NLPApp()
        
        
