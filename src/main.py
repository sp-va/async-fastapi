import asyncio

from transactions.insert_data import insert_users, insert_documents
from transactions.retrieve_data import retrieve_data
from db.base import AsyncSessionLocal

if __name__ == '__main__':
    pass
    #asyncio.run(insert_users(AsyncSessionLocal))
    #asyncio.run(retrieve_data(AsyncSessionLocal))
    #asyncio.run(insert_documents(AsyncSessionLocal))
