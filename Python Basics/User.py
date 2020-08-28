class User:
	def __init__(self, userName):
		self.userName = userName

	# display template and replace userName with user input
	def dispStrnTmplt(self):
		if (len(self.userName) > 2):
			print(f"Hello {self.userName}, How are you?")
		else:
			print("User name should have 3 characters minimum!")

if __name__ == "__main__":
	username = input("Enter name : ")
	nameObj = User(username)
	nameObj.dispStrnTmplt()
