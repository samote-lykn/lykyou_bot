from mongoDB.connection import get_db
from mongoDB.collections import collections
from mongoDB.classes import User

db = get_db()
collection = db[collections.MEMBER_SELECTION]

# Helper function to fetch a document by user_id
async def get_document_by_user_id(user_id):
    try:
        document = await collection.find_one({'user_id': user_id})
        return document
    except Exception as e:
        print(f"Error fetching user document: {e}")
        return None

# Define the async function to update or insert selected member
async def update_selected_member(user_id, selected_member):
    try:
        user = User(user_id, selected_member)  # Create a User instance
        await user.save()  # Save the user (either insert or update)
    except Exception as e:
        print(f"Error updating selected member for user {user_id}: {e}")

# Function to get a user's selection
async def get_user_selection(user_id):
    try:
        user = await User.find_by_user_id(user_id)  # Use User's find method
        if user:
            print(user)
            return user
        else:
            print(f"No selection found for user {user_id}")
            return None
    except Exception as e:
        print(f"Error getting user selection: {e}")
        return None

# Function to get selected member from user's selection
async def get_selected_member_from_user_selection(user_id):
    try:
        # Find user by user_id
        user = await User.find_by_user_id(user_id)

        if not user:
            print(f"No user found with ID {user_id}")
            return None

        # Return selected_member if it exists
        if user.selected_member:
            print(f"Selected member for user {user_id}: {user.selected_member}")
            return user.selected_member

        # If no selected_member, return None
        print(f"No selection found for user {user_id}")
        return None

    except Exception as e:
        # Log the exception with user_id context
        print(f"Error getting selected member for user {user_id}: {e}")
        return None


# Function to delete a user
async def delete_user(user_id):
    try:
        await User.delete_by_user_id(user_id)  # Use User's delete method
    except Exception as e:
        print(f"Error deleting user selection for user {user_id}: {e}")

# Function to delete a user's selection
async def delete_user_selection(user_id):
    try:
        user = await User.find_by_user_id(user_id)  # Use User's find method
        if user:
            await user.delete_selection()  # Delete the selection using the User instance
        else:
            print(f"No user found with ID {user_id}")
    except Exception as e:
        print(f"Error removing selected member for user {user_id}: {e}")
