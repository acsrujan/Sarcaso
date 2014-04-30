from user import user

user1 = user()

user1.set_screen_name('SuTTe')

print user1.get_screen_name()

f = open('tweet_data','r')

s=[]

for line in f:
    s.append(str(line))

print user1.create_subject_list(s)
