#!/usr/bin/env python3

def stream_user_ages(func):
    """Generator function that yields user ages from a database."""
    def wrapper(*args, **kwargs):
        """Wrapper function to calculate average age."""
        total_age = 0
        count = 0
        for user in func(*args, **kwargs):
            if 'age' in user:
                total_age += user['age']
                count += 1
                # print(total_age)
                yield user['age']
        if count > 0:
            print(f"Average age of users: {total_age / count}")
        else:
            print("No users found.")
        
    return wrapper