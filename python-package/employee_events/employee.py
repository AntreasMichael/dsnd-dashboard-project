from .query_base import QueryBase
import pandas as pd


class Employee(QueryBase):

    name = "employee"

    def names(self):
        sql = """
            SELECT first_name || ' ' || last_name AS name, employee_id
            FROM employee
        """
        return self.query(sql)

    def username(self, id):
        sql = f"""
            SELECT first_name || ' ' || last_name
            FROM employee
            WHERE employee_id = {id}
        """
        return self.query(sql)

    def model_data(self, id):
        sql = f"""
            SELECT SUM(positive_events) positive_events,
                   SUM(negative_events) negative_events
            FROM employee
            JOIN employee_events USING(employee_id)
            WHERE employee.employee_id = {id}
        """
        return self.pandas_query(sql)
