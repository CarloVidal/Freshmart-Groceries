from models import PersonalInfo
from bson import ObjectId

class EmployeeController:
    @staticmethod
    def create_employee(data):
        try:
            # Validate required fields
            required_fields = ["Name", "Date_Of_Birth", "Contact_Number", "Emergency_Contact_number"]
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Missing required field: {field}")

            # Create and save the employee
            employee = PersonalInfo(
                Name=data["Name"],
                Date_Of_Birth=data["Date_Of_Birth"],
                Contact_Number=data["Contact_Number"],
                Emergency_Contact_Number=data["Emergency_Contact_Number"]
            )
            employee.save()

            # Return the created employee data
            return {
                "Name": employee["Name"],
                "Date_Of_Birth": employee["Date_Of_Birth"],
                "Contact_Number": employee["contact_number"],
                "Emergency_Contact_Number": employee["Emergency_Contact_Number"]
            }
        except Exception as e:
            raise Exception(f"Error creating employee: {str(e)}")

    @staticmethod
    def get_employee_by_id(employee_id):
        try:
            # Convert string ID to ObjectId
            obj_id = ObjectId(employee_id)
            employee = PersonalInfo.get_by_id(obj_id)
            
            if employee:
                return {
                "Name": employee["Name"],
                "Date_Of_Birth": employee["Date_Of_Birth"],
                "Contact_Number": employee["contact_number"],
                "Emergency_Contact_Number": employee["Emergency_Contact_Number"]
                }
            return None
        except Exception as e:
            raise Exception(f"Error fetching employee: {str(e)}")

    @staticmethod
    def get_all_employees():
        try:
            employees = PersonalInfo.get_all()
            return [{
                "Name": emp["Name"],
                "Date_Of_Birth": emp["Date_Of_Birth"],
                "Contact_Number": emp["contact_number"],
                "Emergency_Contact_Number": emp["Emergency_Contact_Number"]
            } for emp in employees]
        except Exception as e:
            raise Exception(f"Error fetching employees: {str(e)}")
