# InternshipTask

## Deploying an end-to-end website to store the data of students using AWS EC2 and Amazon RDS.

>First creating the database using Amazon RDS in mysql.

Amazon RDS-> Databases-> Create database.

> Now Creating an EC2 instance
 
EC2-> Launch instance-> ubuntu server -> Launch.

Now connecting to ec2 server.

logging in using public ip address or direct connect from your ec2 instance.

First select the directory in which our key file is located. then logging in using this command : 

```bash
ssh -i ./internship-task.pem ubuntu@IP_address

```
logged in.

> Now connecting RDS, First we need to deploy mysql client on this machine which will help us to connect to our RDS machine.

```bash
sudo apt-get update
sudo apt-get install mysql-client 

mysql -h url from Amazon RDS -u username -p password
Enter password=

```
> Now we have successfully created the RDS and we are at mysql shell.

```bash
mysql-> show databases;
     -> create database employee;
```
> Now we have to create a table inside 'students'.
where basically our information is now going to be stored.

```bash
-> create table students(
-> StudentID varchar(20),   # now specifying the column
-> FirstName varchar(20),
-> LastName varchar(20),
-> CurrentJob varchar(20),
-> Location varchar(20));
#ERROR 1046(30000): No Database selected.
-> use students:
#Database changed.

#Now again we are adding the table details in table 'students'

-> create table students(
-> StudentID varchar(20),  
-> FirstName varchar(20),
-> LastName varchar(20),
-> CurrentJob varchar(20),
-> Location varchar(20));

-> show tables;
exit       #exit fom mysql shell
logout     #logout from your ec2 instance
```
>Now let's try to run the website on our local system and then we will try to deploy on the AWS Management console.

>First we have to configure our website.

```bash
*config.py

customhost = "students.cszdt2jowlxz.us-east-2.rds.amazonaws.com"
customuser = "sarvesh"
custompass = "Sarvesh001"
customdb = "students"
custombucket = "add-student"

```
>Now, let's deploy the website on a local system.

> >open cmd

```bash
-> python3 app.py

#Search "localhost" on your web browser and now saving everything by pushing it to on github.

-> git add .
   git commit -m "saved code"
   
#Now, for pushing it on git we have to create a remote repository.

```
> Go to github.com
>>create repository  (public)

```bash
-> git remote add origin2 "git link"      
-> git push origin2 master   #My website has now been pushed on the github.

```
Now, logging in to EC2 Server.

```bash
-> ssh -i ./internship-task.pem ubuntu@IP_address

-> git clone git link
->ls                          #shows all the files that are present on our repository
-> cd InternshipTask/         #Deploying the code over here


-> sudo apt-get install python3   #For running the website on our server
                                  #we have to install python as our code is on this language.
-> sudo apt-get install python3-pip   
-> pip3 install pymysql boto3
-> pip3 install flask
-> sudo python3 app.py            #Website got deployed

```
>Go to EC2
>>Public IP- open it on web
>>>Entering the details of Student
>>>>Save

Open cmd

```bash
-> mysql

-> mysql -h url from Amazon RDS -u username -p password
Enter password=

mysql> use students;
       select * from students;     #EC2 is now connected to Amazon RDS.

```

" So, As our website is now created go to the web browser and open this website using the [IP](http://3.141.164.147:5000/add) address that I have created."









