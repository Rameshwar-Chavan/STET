# Project Installation Steps:

#### Step 1:
- Go to [Python](/https://python.org/downloads) and download the python version 3.7
- Install python 3.7 in your system and set path.
- Check is python installed successfuly or not using following command 
```
python --version
``` 
cammand.
- Check is pip is latest one ex. pip-20.1 or latest
- Check it using following command:
```
python pip --version
```
- Install Django using following command:
``` 
pip install django
```

#### Step 2:
- Install requirements.txt using following command 
``` 
python pip install -m requirements.txt
```
- If it is not working on your system do manual installation of all the package using following commands:
``` 
1. pip install django
2. pip install pillow
3. pip install mysqlclient
4. pip install djangootp
```
#### Step 3:
- Extract STET.zip folder in your system and open it on your Favourite __IDE__ or __Text Editor__
* Go to settings.py and change __Allowed Host__ to your HOST Name in my case it is [Localhost]

#### Step 4:
* Open your database service provider and create Database named "stet_db"
- Open your file manager and go to STET right click on STET and open it with your command pallet
- Exicute following commands for Database Table Migrations:
``` 
python manage.py migrate
```
- After succesfull migrations run following command:
```
python manage.py runserver
```
If you execute above command following link is generated:
```
System check identified 2 issues (0 silenced).
January 20, 2022 - 19:40:26
Django version 3.0.5, using settings 'STET.settings'
Starting development server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
Quit the server with CTRL-BREAK.
```
Just copy and pest it into Browser of simpaly click on it redirect you to homepage.
The homepage looks like
![alt text](https://github.com/Rameshwar-Chavan/STET/blob/main/templates/screenshots/homepage.PNG "Home Page")








# STET

## 1. Candidate Requirements:

#### Registration:
- Mobile No , Email id(User ID), password
- First Name, Last Name 
- Login using Password or OTP

### Profile
#### Personal Details:
- First Name, Middle Name, Last Name
- Email, Mobile No
- DOB, Gender,Age, Marital Status
- Aadhar Number*

#### Address Details:
- Local:Address 1, Local:Address 2
- Permenant: Address 1, Address 2
- State, District, Taluka, Village, Pincode

#### Other Information:
- Religion, Caste

#### Academics Deatils:
- Qualification, Stream
- Institute Name, University/ Board name
- Passing Year , Percentage

#### Documents:
- SSC, HSC/Diploma*
- Graduation, Post Graduation
- Caste, Non Creamy layer, Nationality
- Photo, signature


## Admin :

#### Login:
- User Name : Mobile No / Email id
- Password : Own Password

##### Dashboard:
- Home, Hall ticket, Time Table, Notifications, Results.


#### Apply Application:
- Candidate Full Name, Mobile No
- Email, Qualification, Caste
- Fees/Payment*





## 3. ChatBot

- FAQ
- Exam Query
- Registration Issues
- Login Demo

## 4. Mock Exam Interface:

- It Provides demo quetions and Online exam interface to end user/ Candidates.
  created by rameshwar
