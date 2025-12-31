from .query_base import QueryBase
import pandas as pd


class Team(QueryBase):

    name = "team"

    def names(self):
        sql = """
            SELECT team_name, team_id
            FROM team
        """
        return self.query(sql)

    def username(self, id):
        sql = f"""
            SELECT team_name
            FROM team
            WHERE team_id = {id}
        """
        return self.query(sql)

    def model_data(self, id):
        sql = f"""
            SELECT positive_events, negative_events FROM (
                SELECT employee_id,
                       SUM(positive_events) positive_events,
                       SUM(negative_events) negative_events
                FROM team
                JOIN employee_events USING(team_id)
                WHERE team.team_id = {id}
                GROUP BY employee_id
            )
        """
        return self.pandas_query(sql)
