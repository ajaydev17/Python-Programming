"""
Django’s select_related and prefetch_related methods are used to optimize
database queries by reducing the number of database hits in related model lookups.
select_related performs a single SQL join to retrieve related data for foreign key or one-toone relationships, while prefetch_related is used for many-to-many and one-to-many
relationships, retrieving related data in separate queries but optimizing the process
"""

# Example
authors = Author.objects.select_related('profile').all()

# Example
books = Book.objects.prefetch_related('authors').all()