from mongoDB.connection import get_db
from mongoDB.const import collections

db = get_db()

# Helper function to fetch a document by user_id
async def get_document_by_user_id(user_id):
    collection = db[collections.MEMBER_SELECTION]
    try:
        document = await collection.find_one({'user_id': user_id})
        return document
    except Exception as e:
        print(f"Error fetching user document: {e}")
        return None

# Define the async function to update or insert selected member
async def update_selected_member(user_id, selected_member):
    collection = db[collections.MEMBER_SELECTION]

    try:
        # Check if the document exists
        document = await get_document_by_user_id(user_id)

        if document:
            # If user exists, update their selected_member
            await collection.update_one(
                {'user_id': user_id},
                {'$set': {'selected_member': selected_member}}
            )
            print(f"Updated selected_member for user {user_id}")
        else:
            # Otherwise, insert a new document
            await collection.insert_one({'user_id': user_id, 'selected_member': selected_member})
            print(f"Inserted new document for user {user_id}")
    except Exception as e:
        print(f"Error updating selected member: {e}")

# Function to get a user's selection
async def get_user_selection(user_id):
    try:
        document = await get_document_by_user_id(user_id)
        if document:
            print(document)
            return document
        else:
            print(f"No selection found for user {user_id}")
            return None
    except Exception as e:
        print(f"Error getting user selection: {e}")
        return None

# Function to get selected member from user's selection
async def get_selected_member_from_user_selection(user_id):
    try:
        document = await get_document_by_user_id(user_id)
        if document:
            selected_member = document.get('selected_member')
            print(f"Selected member for user {user_id}: {selected_member}")
            return selected_member
        else:
            print(f"No selection found for user {user_id}")
            return None
    except Exception as e:
        print(f"Error getting selected member: {e}")
        return None

# Function to delete a user's selection
async def delete_user_selection(user_id):
    collection = db[collections.MEMBER_SELECTION]
    try:
        document = await collection.find_one_and_delete({'user_id': user_id})
        if document:
            print(f"Deleted selection for user {user_id}")
            return document
        else:
            print(f"No selection found for user {user_id} to delete")
            return None
    except Exception as e:
        print(f"Error deleting user selection: {e}")
        return None
