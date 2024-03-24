import time
import scalability.improve_social_app.before_optimization.social_media_before as social_before

file1 = open('/scalability/improve_social_app/average_time', 'a+')

file1.write("************* Before optimization *****************\n")
social_media_before = social_before.SocialMediaPlatform()
total = 0
start = time.perf_counter()
social_media_before.register_user('user1')
end = time.perf_counter()
total += (end - start)
start = time.perf_counter()
social_media_before.register_user('user2')
end = time.perf_counter()
total += (end - start)
start = time.perf_counter()
social_media_before.register_user('user3')
end = time.perf_counter()
total += (end - start)
average = total / 3
file1.write("Average run time for 'social_media.register_user' is " + str(average) + "\n")

user1 = social_media_before.get_user_by_username('user1')
user2 = social_media_before.get_user_by_username('user2')
total = 0
start = time.perf_counter()
user1.follow(user2)
end = time.perf_counter()
total += (end - start)
start = time.perf_counter()
user1.follow(user2)
end = time.perf_counter()
total += (end - start)
start = time.perf_counter()
user2.follow(user1)
end = time.perf_counter()
total += (end - start)
average = total / 3
file1.write("Average run time for 'user.follow' is " + str(average) + "\n")

total = 0
start = time.perf_counter()
user2.post_message("user2 _ msg1")
end = time.perf_counter()
total += (end - start)
start = time.perf_counter()
user1.post_message("user1 _ msg1")
end = time.perf_counter()
total += (end - start)
start = time.perf_counter()
user2.post_message("user2 _ msg2")
end = time.perf_counter()
total += (end - start)
average = total / 3
file1.write("Average run time for 'social_media.post_message' is " + str(average) + "\n")

total = 0
start = time.perf_counter()
social_media_before.get_user_by_username('user1')
end = time.perf_counter()
total += (end - start)
start = time.perf_counter()
social_media_before.get_user_by_username('user2')
end = time.perf_counter()
total += (end - start)
start = time.perf_counter()
social_media_before.get_user_by_username('user3')
end = time.perf_counter()
total += (end - start)
average = total / 3
file1.write("Average run time for 'social_media.generate_timeline' is " + str(average) + "\n")
