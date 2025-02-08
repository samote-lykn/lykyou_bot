from typing import Optional
from mongoDB.connection import get_db
from mongoDB.collections import collections

# Get database connection
db = get_db()

class User:
    # Define collection within the class
    collection = db[collections.MEMBER_SELECTION]

    def __init__(self, user_id: str, selected_member: Optional[str] = None):
        self.user_id = user_id
        self.selected_member = selected_member

    # Method to save the document to MongoDB
    async def save(self):
        # Check if the user already exists
        existing_user = await self.collection.find_one({'user_id': self.user_id})

        if existing_user:
            # If exists, update the document
            await self.collection.update_one(
                {'user_id': self.user_id},
                {'$set': {'selected_member': self.selected_member}}
            )
            print(f"User {self.user_id} updated.")
        else:
            # If not, insert a new document
            await self.collection.insert_one(self.__dict__)
            print(f"User {self.user_id} created.")

    # Static method to find a user by user_id
    @staticmethod
    async def find_by_user_id(user_id: str):
        user_data = await User.collection.find_one({'user_id': user_id})
        if user_data:
            return User(user_id=user_data['user_id'], selected_member=user_data.get('selected_member'))
        return None

    # Static method to delete a user by user_id
    @staticmethod
    async def delete_by_user_id(user_id: str):
        result = await User.collection.delete_one({'user_id': user_id})
        if result.deleted_count > 0:
            print(f"User {user_id} deleted.")
        else:
            print(f"User {user_id} not found.")

    # Method to delete user's selected member (sets to None or deletes)
    async def delete_selection(self):
        # Set the selected member to None (or could delete the document entirely)
        result = await User.collection.update_one(
            {'user_id': self.user_id},
            {'$set': {'selected_member': None}}  # Or use delete_one to remove the document entirely
        )
        if result.modified_count > 0:
            print(f"Selection removed for user {self.user_id}")
        else:
            print(f"No selection found for user {self.user_id}")

    # Method to print user info (for convenience)
    def __str__(self):
        return f"User ID: {self.user_id}, Selected Member: {self.selected_member}"
