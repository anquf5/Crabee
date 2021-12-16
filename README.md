# Install

## Backend
Go to the file 'backend' and run cmd, excute the following command:

    pip install -r requirement.txt

Create and migrate database:

    python manage.py migrate
    python manage.py makemigrations
Create admin account:

    python manage.py createsuperuser
Input username and password.
Start project:

    python manage.py runserver
The backend default deployment address is 127.0.0.1:8000
### API List
| url | description |
|--|--|
| /admin | Admin address 
| /api/company/ | All companies
|/api/index_company| Index company
|/api/company/1| Company detail
|/api/company_review/add| Add company
|/api/company/search| Search company
|/api/topic| All topics
|/api/topic/add| Create topic
|/api/topic/1| Topic detail
|/api/topic/reply| Reply topic

## Frontend
Go to the 'frontend' file, open cmd, execute the following sentence

    npm run serve
The frontend will default deploy on 127.0.0.1:8080
### Site Map
|url|  |
|--|--|
|/home  |  |
|/company/1  |  |
|/all_company  |  |
|/discussion  |  |
|/topic/1 |  |
|/login |  |
|/signup  |  |
|/search  |  |
|/myaccount  |  |


