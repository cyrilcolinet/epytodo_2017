##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## models
##

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class User(Model):

	__tablename__ = "user"

	user_id = Column(Integer, primary_key=True)
	username = Column(String(255), unique=True, nullable=False)
	password = Column(String(255), nullable=False)

	def __repr__(self):
		return self.username

	def get_username(self):
		return self.username

	def get_user_id(self):
		return self.user_id

	def user_exists(username):
		cur = conn.cursor
		cur.execute("SELECT COUNT(1) FROM %s WHERE username = %s" % (table, username))
		print(cur.description)
		print()
		for row in cur:
			print(row)
		cur.close()
