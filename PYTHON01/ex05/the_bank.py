class Account(object):
	"""The Account"""
	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)
		
		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0

		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")
		
	def transfer(self, amount):
		self.value += amount

class Bank(object):
	"""The bank"""
	def __init__(self):
		self.accounts = []

	def security_check(self, account):
		"""Check the security of the account before add it to he bank"""
		if isinstance(account, Account):
			if len(account.__dict__) % 2 == 0:
				return False
			if not any(x.startswith("zip") for x in account.__dict__) or any(x.startswith("addr") for x in account.__dict__):
				return False
			if any(x.startswith('b') for x in account.__dict__):
				return False
			if not 'name' in account.__dict__ or not 'id' in account.__dict__ or not 'value' in account.__dict__:
				return False
			if not isinstance(account.__dict__['name'], str) or not isinstance(account.__dict__['id'], int) or not isinstance(account.__dict__['value'], (int, float)):
				return False
			return True
		return False

	def add(self, new_account):
		""" Add new_account in the Bank
			@new_account: Account() new account to append
			@return True if success, False if an error occured
		"""
		if isinstance(new_account, Account) and new_account not in self.accounts:
			self.accounts.append(new_account)
			return True
		return False

	def transfer(self, origin, dest, amount):
		"""" Perform the fund transfer
			@origin: str(name) of the first ac count
			@dest: str(name) of the destination account
			@amount: float(amount) amount to transfer
			@return True if success, False if an error occured
		"""
		if isinstance(origin, str) and isinstance(dest, str) and isinstance(amount, (int, float)):
			if any(origin == x.name for x in self.accounts):
				origin_account = next(x for x in self.accounts if x.name == origin)
			else:
				print("The origin account: \033[4;31m" + origin + "\033[m was not found")
				return False
			if any(dest== x.name for x in self.accounts):
				dest_account = next(x for x in self.accounts if x.name == dest)
			else:
				print("The dest account: \033[4;31m" + dest + "\033[m was not found")
				return False
			if not self.security_check(origin_account) or not self.security_check(dest_account):
				return False
			if not origin_account is dest_account:
				if amount > 0 and origin_account.value > amount:
					origin_account.transfer(-amount)
					dest_account.transfer(amount)
					print("\033[1;32mTransfer completed.\033[m")
					print(origin + " transfered \033[1;33m" + str(amount) + "\033[m to " + dest)
					return True
				else:
					print("The amount must be positive and superior than the origin account value")
					return False
			else:
				print("The transfer is between the same account. There will be no fund movement.")
				return True
		print("The parameters for the transfer are:\n \
	- Name of the origin account (string)\n \
	- Name of the destination account (string)\n \
	- Amount of the transfer (int/float)")
		return False

		

	def fix_account(self, name):
		""" fix account associated to name if corrupted
			@name: str(name) of the account
			@return True if success, False if an error occured
		"""
	
if __name__ == '__main__':
	bank = Bank()
	bank.add(Account(
		'Smith Jane',
		zip='911-745',
		value=1000.0,
		ref='1044618427ff2782f0bbece0abd05f31',
	))
	bank.add(Account(
		'William John',
		zip='100-064',
		value=6460.0,
		ref='58ba2b9954cd278eda8a84147ca73c87',
	))
	if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
		print('Failed')