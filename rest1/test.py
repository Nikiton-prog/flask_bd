from requests import get, post

#print(get('http://localhost:5000/api/jobs').json())
#print(get('http://localhost:5000/api/jobs/2').json())
#print(get('http://localhost:5000/api/jobs/20').json())
#print(get('http://localhost:5000/api/jobs/t').json())

#print(post('http://localhost:5000/api/jobs', json={}).json())

# print(post('http://localhost:5000/api/jobs',
#            json={'job': 'Заголовок'}).json())
#
print(post('http://localhost:5000/api/jobs',
           json={'job': 'Заголовок',
                 'team_leader': 1,
                 'work_size': 1}).json())

print(get('http://localhost:5000/api/jobs').json())