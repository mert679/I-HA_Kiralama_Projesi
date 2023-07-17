# IHA_Kiralama_Projesi


- **Welcome Page**: Displays the welcome page of the application.
    - URL: `127.0.0.1:8000/`
    - View: `WelcomePageView`

- **Home Page**: Displays the home page of the application.
    - URL: `127.0.0.1:8000/home/`
    - View: `HomePageView`

- **Register**: Allows users to register a new account.
    - URL: `127.0.0.1:8000/register/`
    - View: `register_view`

- **Login**: Allows users to log in to their account.
    - URL: `127.0.0.1:8000/login/`
    - View: `login_view`

- **Logout**: Logs out the current user.
    - URL: `127.0.0.1:8000/logout/`
    - View: `logout_view`

- **Create**: Creates a new Iha object.
    - URL: `127.0.0.1:8000/create/`
    - View: `IhaCreateView`

- **Delete**: Deletes the specified Iha object.
    - URL: `127.0.0.1:8000/<int:id>/delete/`
    - View: `iha_delete_view`

- **Update**: Updates the specified Iha object.
    - URL: `127.0.0.1:8000/<int:pk>/update/`
    - View: `IhaUpdateView`

- **Rent**: Creates a new rental record.
    - URL: `127.0.0.1:8000/rent/`
    - View: `RentalRecordCreateView`

- **Rent List**: Displays a list of rental records.
    - URL: `127.0.0.1:8000/rent-list/`
    - View: `RentRecordListView`

- **Rent Update**: Updates the specified rental record.
    - URL: `127.0.0.1:8000/<int:pk>/rent-update/`
    - View: `RentRecordUpdateView`

- **User Rent**: Displays a list of rental records for the current user.
    - URL: `127.0.0.1:8000/user-rent/`
    - View: `UserRentRecordView`

- **Rent Delete**: Deletes the specified rental record.
    - URL: `127.0.0.1:8000/<int:id>/rent-delete/`
    - View: `rent_delete_view`
