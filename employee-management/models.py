from pymongo import MongoClient
from bson.objectid import ObjectId
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client.get_database()

class PersonalInfo:
    def __init__(self, Name, Date_Of_Birth, Contact_Number, Emergency_Contact_Number):
        self.Name = Name
        self.Date_Of_Birth = Date_Of_Birth
        self.Contact_Number = Contact_Number
        self.Emergency_Contact_Number = Emergency_Contact_Number

    def save(self):
        personal_info_data = {
            "Name": self.Name,
            "Date_Of_Birth": self.Date_Of_Birth,
            "Contact_Number": self.Contact_Number,
            "Emergency_Contact_Number": self.Emergency_Contact_Number
        }
        result = db.personal_info.insert_one(personal_info_data)
        return str(result.inserted_id)

    @staticmethod
    def get_all():
        return list(db.personal_info.find())

    @staticmethod
    def get_by_id(info_id):
        return db.personal_info.find_one({"_id": ObjectId(info_id)})

