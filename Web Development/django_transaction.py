"""
Django transactions ensure that a set of database operations either complete
successfully as a unit or roll back entirely if any operation fails. Django’s atomic transactions
provide an all-or-nothing approach, ensuring that if an error occurs, changes are not saved to
the database, maintaining data integrity.
The transaction.atomic context manager allows for nested transactions and can be used
to group multiple database operations.
"""

from django.db import transaction

def create_user_with_profile():
    try:
        with transaction.atomic():
            user = User.objects.create(username='john_doe')
            profile = Profile.objects.create(user=user, bio='Profile of John Doe')
    except Exception as e:
        print('Error:', e)
        # Roll back the transaction if an error occurs
        transaction.set_rollback(True)