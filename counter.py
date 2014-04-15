import tweepy2
import time
import threading
import copy


################################################################
###############                    #############################
###############     FUNC DEFNS     #############################
###############                    #############################
################################################################

def calculate_unfollower_list(user_info, present_followers_ids, new_followers_ids):
    unfollower_user_list = []
    
    #TODO
    #can be an important part where you can
    #check each element to the cache and see
    #if a former following person has followed you
    #again
    for ids in present_followers_ids:
        if i not in user_info:
            time.sleep(5)
            user = api.get_user(i)
            follower_user_list.append(user)
            user_info.add(copy.deepcopy(user))
    return [user_info, follower_user_list]

def calculate_follower_list():  
    #the important part where one gets the people who have 
    #unfollowed
    for ids in list(unfollower_user_list):
        #search in cache
        if ids not in user_info:
            time.sleep(5)
            user = api.get_user(ids)
            unfollower_user_list.append(user)
            user_info.append(copy.deepcopy(user))


def calculate_difference(user_info):
    
    follower_user_list = []
    present_followers_ids = set(api.follower_ids(my_id))
    
    #original_follwer_list - present_follower_list = unfollowers
    unfollowers_ids = original_followers.difference(present_followers_ids)

    #present_follower_list - original_follower_list = followers
    new_followers_ids = present_followers.difference(original_followers_ids)
    
    user_info, follower_user_list = calculate_follower_list(user_info, present_followers_ids, new_followers_ids)
    
    user_info, unfollower_user_list = calculate_unfollower_list(user_info, unfollowers_ids, un)
    
    return [user_info, unfollowers_ids, follower_user_list]

    
def print_user_info(user):
    print "_______________________________"
    print "|", user.id, "|", user.screen_name
    print "-------------------------------"
    
    
################################################################
###############                    #############################
###############     MAIN SCRIPT    #############################
###############                    #############################
################################################################

#TODO 
#acquire constants from user
#while implementing the web app
#store the credentials in a user table
#for starting the app directly
#for logins set the app data in a session

#initialize on every user process
#keep out of loop

def main():
    #constants
    consumer_key = 'zrDvgegV0K1lBLIxukR0A'
    consumer_secret = 'dM2BpTPoEvFBZ9oVVNSGUi5j1T6JQcCcE4At7TeNmw'
    access_key = '1270521626-CuXFTkLQ58yZbEj2memLErALqMcRbeVp4j8izxz'
    access_secret = 'Qh3Z620M5ttqs3QTE5LNFCRadNmA9XabfakNkbuKMJzdj'
    
    auth = tweepy2.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    
    api = tweepy2.API(auth_handler=auth, proxy_url='172.31.16.10:8080')
    print "REACCHEDD HEREE!!!!"
    
    print api.me().name
    print "REACCHEDD HEREE TOOOO!!!!"
    i_am = api.me()
    
    my_id = i_am.id
    
    #cache to store users
    #implement cache here as ordered list wrt time
    #when the list size grows beyond a measure
    #delete the first n/3 entries
    #n = no of preset followers
    user_info = {}
    
    original_followers_ids = set(api.followers_ids(my_id))
    user_info = copy.deepcopy(original_followers_ids)
    
    #calcluate data after every given period
    #TODO get time period

    T = 10000
    
    #print user_info
    
    #data  = calculate_difference(user_info)
    #user_info, unfollowers_ids, followers_ids = data[0], data[1], data[2]
    
    #print all the unfollowers since last run
    """
    for ids in unfollowers_ids:
        #find user in user_info list
        if user_info
    """
    

if __name__ == "__main__":
    main()
