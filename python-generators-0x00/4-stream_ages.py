#!/usr/bin/env python3

# def stream_user_ages():
#     """Generator function that yields user ages from a database."""
#     def wrapper(*args, **kwargs):
#         """Wrapper function to calculate average age."""
#         total_age = 0
#         count = 0
#         for user in func(*args, **kwargs):
#             if 'age' in user:
#                 total_age += user['age']
#                 count += 1
#                 # print(total_age)
#                 yield user['age']
#         if count > 0:
#             print(f"Average age of users: {total_age / count}")
#         else:
#             print("No users found.")
        
#     return wrapper
seed = __import__('seed')

def stream_user_ages():
    """
    Implementing a generator stream_user_ages() that yields user ages one by one.
    Use the generator in a different function to calculate 
    the average age without loading the entire dataset into memory
    """
    # connect to the MySQL database
    connection = seed.connect_to_prodev()
    if connection:
        # create a cursor object
        cursor = connection.cursor()

        # execute a query to select all rows from the user_data table
        cursor.execute("SELECT * FROM user_data")

        # fetch all rows from the result set
        rows = cursor.fetchall()
        # iterate over the rows and yield each row as a dictionary
        for row in rows:
            yield {
                'user_id': row[0],
                'name': row[1],
                'email': row[2],
                'age': int(row[3]),
            }
        # close the cursor and connection
        cursor.close()
        connection.close()
    else:
        print("Failed to connect to the database.")
        return None
    # if the connection fails, return an empty generator
    return iter([])

def calculate_average_age():
    """Calculates average age using the generator"""
    total = 0
    count = 0
    
    for age in stream_user_ages():
        total += age
        count += 1
    
    return total / count if count > 0 else 0