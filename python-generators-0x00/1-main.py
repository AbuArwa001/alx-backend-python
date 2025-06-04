#!/usr/bin/env python3
from itertools import islice

stream_users = __import__('0-stream_users').stream_users


# iterate over the generator function and print only the first 6 rows
streamed_users = stream_users()
for user in islice(streamed_users, 6):
    print(user)
# stream_users()