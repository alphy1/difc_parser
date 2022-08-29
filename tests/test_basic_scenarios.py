from difc_parser.settings import MONGO_COLLECTION


class TestBasicScenarios:
    def test_collections(self, db):
        collections = db.list_collection_names()
        assert len(collections) == 1
        assert collections[0] == MONGO_COLLECTION

    def test_fields(self, collection, fields):
        sample = collection.find_one()
        assert sample is not None
        for item in sample:
            if item.endswith("_id"):
                continue
            assert item in fields

    def test_query_by_name(self, collection):
        sample = collection.find_one({"Name": "Remittances Hub Ltd"})
        assert sample["Registered Number"] == 6049

    def test_query_by_registered_number(self, collection):
        sample = collection.find_one({"Registered Number": 6054})
        assert sample["Name"] == "SPL PC 47 Holding Limited"

    def test_for_1000_companies(self, collection):
        sample = collection.find_one({"Registered Number": 5555})
        assert sample["Name"] == "FoodYoung Ventures Investment Ltd"
        sample = collection.find_one({"Name": "GC Equity Co-Invest IV Holding Limited"})
        assert sample["Registered Number"] == 5060