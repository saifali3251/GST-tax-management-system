
## Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```
---



<h1 align="center">GST tax management system</h1>

A tax management system with following features:
  - Users can register and login. By default all the new users are "Tax-Payer" 
  - Users can add bills using bill form.
  - Each users have their Profile
  - Users can list, view and update there own bills
  - Users can pay the tax-amount which is dependant on the user's State. Untill paid, users can update there bill
  - Once bill is PAID the payment status is marked as PAID. 
  - Bill status are marked as NEW and DELAYES based on "DueDate"
  - Users can filter there own bills based on different fields e.g, PAID,DELAYED,NEW, etc
  - ADMIN can only assign user as "Tax-Accountant"
  - TA can Update any user's bill and can update the Tax Due based on dueDate
  - TA can also edit the user's tax-due but only until the bill is NOT paid. Once paid, it can't be updated
  - TA can view all the users list and their bills and can filter the bills based on different params
  - ADMIN has all the rights except User's bill update once bill is paid
  - ADMIN can create any number of TA and can also revert those changes


User Dashboard :
![image](https://user-images.githubusercontent.com/37900854/166160074-8ee7708d-42a7-4bf9-a7df-ff597f4d3e6f.png)

Add Bill :
![image](https://user-images.githubusercontent.com/37900854/166160182-6b009f8b-1575-43a3-b9ef-4e8fa1247916.png)

Update Bill :
![image](https://user-images.githubusercontent.com/37900854/166160209-aa4565a3-b866-4eff-9093-f04fedf149a6.png)



Admin Dashboard :

![image](https://user-images.githubusercontent.com/37900854/166160252-e0b5aaaf-707a-4c99-b10f-096db4ddea23.png)

Bill list(for all users)(only accessed by Admin and Tax Accountant)

![image](https://user-images.githubusercontent.com/37900854/166160308-d754ccf3-7ad2-4184-9a12-06126ed55cb1.png)

User List(Can be accessed by Admin Only) :

![image](https://user-images.githubusercontent.com/37900854/166160360-8323460a-102a-4d6f-818d-59b4e8f029a1.png)




