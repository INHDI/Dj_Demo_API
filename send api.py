import requests

headers ={}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA1MDY3NzI5LCJqdGkiOiI5Zjg1NWM0YmVhNzQ0NjRjODhiYTMwZmVlZGI1MmZmZiIsInVzZXJfaWQiOjF9.bKKGDKqRM1INoolHmyIXGHRGrSZUPn6qrvbkH8f-EGg'
r = requests.get('http://127.0.0.1:8000/api_list', headers =headers)
print(r.text)