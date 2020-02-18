# EasyVisitors

EasyVisitors is a simple to use Django App that counts website visitors and displays them without any hassles. It uses cookies to keep a track of how many people visited you website and doesnot increments simply upon a refresh unlike other simple counters. 

  - Easy to use
  - Easy to setup
  - Easy to configure
  - Easy to customize


## Installation
Installation is same for virtualenv and non virtualenv (because it is that simple XD)
```
> pip install EasyVisitors
```
## Configration
In `settings.py` of your django project -
```python
INSTALLED_APPS = [
    ...
    'EasyVisitors',
    ...
]
```

```python
MIDDLEWARE = [
    ...
    'EasyVisitors.middleware.VisitorCounterMiddleware',
    ...
]
```
## Getting Started
It is a local counter so it is necessary to create some space for recording it's values in the database. But no worries all of it has been taken care off. You just have to run - 
```python
python manage.py makemigrations EasyVisitors
```
```python
python manage.py migrate EasyVisitors
```
This will create a simple table to store the values of the counter in the database. This step is very important as without these migrations the app wont be able to run as it wont be able to store it's values and hence will show an error.

## Using the app
This simple to configure app is also simple to use. To use the value of counter in your templates - 
```html
{{ request.visitors }}
```
And to use it anywhere else - 
```python
request.visitors
```
## Customization

In `settings.py` of your django project you can customize some aspects of EasyVisitors app -
1. EASY_COUNTER_VISITOR_ALIVE_TIME - It determines how long a visitor is concidered as a unit and after that time, that user is concidered as a new vsitor.
Datatype : *int*  
Unit : *seconds*  
Default: *300*  
&nbsp;
2. EASY_COUNTER_IGNORED_PATHS - List comprising of all paths, which donot alter the state of the counter upon being visited.  
Datatype : *list*  
Default: *['/admin']*  
&nbsp;
2. EASY_COUNTER_RESET - Value for the counter to begin from upon next refresh of any page. If it has any value except `None` then the counter will stay at that value forever untill changed to `None` after which it begins counting from that value.  
Datatype : *int*  
Default: `None`  
OnChange : *Counter stay at the changed value*  
&nbsp;
## Creator
Deekshant Wadhwa
## License
MIT
