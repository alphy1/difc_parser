import pytest
from pymongo import MongoClient
from difc_parser.settings import MONGO_URI, MONGO_DATABASE, MONGO_COLLECTION
from difc_parser.items import DifcParserItem


@pytest.fixture()
def client():
    client = MongoClient(MONGO_URI)
    return client


@pytest.fixture()
def db(client):
    db = client[MONGO_DATABASE]
    return db


@pytest.fixture()
def collection(db):
    collection = db[MONGO_COLLECTION]
    return collection


@pytest.fixture()
def fields():
    return list(DifcParserItem().fields)
