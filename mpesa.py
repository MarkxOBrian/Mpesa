from datetime import datetime


class MPESA:
	def __init__ (self):
		self.name = raw_input("Please enter your name: \n")
		self.number = raw_input("Please enter your number: \n")
		self.balance = 0.0
		self.deposits=[]
		self.withdrawals=[]
		self.loan= 0.0

		print("Welcome", self.name)
	

	def deposit(self, amount):
		"""
		-when a person deposits an amount, it adds to the balance/ self.balance variable.(The amount 			increments balance which is initially zero)
		-You cannot deposit any amount that is less than 50 bob.
		

		"""
		if amount < 50:
			print("Dear", self.name, "You cannot enter an amount less that 50 shillings")
		else:	
			self.balance += amount
			now = datetime.now()
			time= now.strftime("%c")
			details={ "time":time,"amount": amount}
			#self.deposits.append(amount)
			self.deposits.append(details)
			print("Dear,", self.name, "you have deposited", amount, 
			"your new balance is", self.balance)

		return

	def withdraw(self, amount):
		if amount <= 50:
			print("You cannot withdraw less than 50 bob")
		elif self.balance <= amount:
			print("You have insuffecient funds to withdraw that amount")
		else:
			self.balance-=amount
			now = datetime.now()
			time= now.strftime("%c")
			moneywithdrawn={ "time":time, "amount": amount}
			print("Dear,", self.name, "you have withdrawn",amount, "your new balance is",self.balance)
			self.withdrawals.append(moneywithdrawn)
		return


	def showdeposits(self):
		if len(self.deposits) < 1:
			print("You have no deposits to date")
		else:
			for deposit in self.deposits:
				print("On", deposit['time'], "you deposited",deposit['amount'])
		return


	def showithdrawals(self):
		if len(self.withdrawals) < 1:
			print("You have no withdrawals at this date")
		else:
			for withdrawal in self.withdrawals:
				print("On",withdrawal['time'], "you withdrew",withdrawal['amount'])
		return

	"""
			
			Conditions for getting a loan:
			-user has made at least 10 deposits.
			-Amount must be more than 50
			-Loan requested must be less than 1/3 the amount they have deposited in the past****
			-User has no deposit balance
			-User has no outstanding debts/loans
			-Loan has an interest of 10%

			The loan given is the amount of outstanding loan
		
		"""

	def getloan(self):
		amount= int(input("Please enter the amount: "))
		print(amount)
		if len(self.deposits) < 10:
			print("You cannot borrow a loan at this time because the number of transactions done was less than the minimum required number 10")
		elif amount <= 50:
			print("You have not repaid your previous debt")
		elif amount * 0.3 > sum([deposit['amount'] for deposit in self.deposits]):
			print("You don't have sufficient balance to do this transaction")
		elif self.balance < 50:
			print("You cannot borrow the required amount at this time as you have a balance in your account!")
		elif self.loan < 50:
			print("You cannot borrow an amount less than 50 bob")
		else:
			loan_interest= 0.1 *amount
			loan_amount= amount + loan_interest
			self.loan +=loan_amount
			print("Success: You have received a loan of", amount, "your outstanding balance is", self.loan)
		return

		
	def payloan(self,amount):
		"""
		Accept loan payment if:
		-Amount is larger than 50
		-user has a loan or else save as deposit
		-Amount contributes to the loan repayment
		If amount is larger than the remaining loan save the remainder as the deposit

		This code will also treat other loan payments that are not payments or
 		if they did not have a loan, as deposits 

 		Finally it needs to check fi the 
		"""


		now=datetime.datetime.now()
		time=now.strftime("%c")

		if amount < 50:
			print("You cannot deposit an amount that is less than 50 bob")

		elif self.loan == 0:
			self.balance+=amount
