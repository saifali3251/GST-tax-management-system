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
  - ADMIN can only create "Tax-Accountant"
  - TA can Update any user's bill and can update the Tax Due based on dueDate
  - TA can also edit the user's tax-due but only until the bill is NOT paid. Once paid, it can't be updated
  - TA can view all the users list and their bills and can filter the bills based on different params
  - ADMIN has all the rights except User's bill update once bill is paid
  - ADMIN can create any number of TA and can also revert those changes
