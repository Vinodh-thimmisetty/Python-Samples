"""
	Air Ticket Booking Application - Pluralsight Course.

"""

class Flight():
	
	def __init__(self, number, aircraft):

		""" 
			First 2 chars - Upper Case Alphabets - AIRLINE Code
			Remaining chars	- Number - Route Code
		"""
		if not number[:2].isalpha():
			raise ValueError(f'No AirLine code - {number}')

		if not number[:2].isupper():
			raise ValueError(f'Invalid AirLine code - {number}')

		if not number[2:].isdigit() and int(number[2:]) <= 9999:
			raise ValueError(f'Invalid Route - {number}')

		self.__number=number
		self.__aircraft = aircraft

		self.__rows,self.__seats = self.__aircraft.seating_plan()
		self.__seating = [None] + [ { s: None for s in self.__seats} for _ in self.__rows]

	def __aircraft_model(self):
		return self.__aircraft.model()

	def current_seating(self):
		return self.__seating

	def available_seats(self):
		# tot=0;
		# for row in self.current_seating():
		# 	if row is not None:
		# 		for col in row:
		# 			if row[col] is None:
		# 				tot +=1
		# print(f'Total >>>>>> {tot}')
		# return sum([1 for row in self.current_seating() if row is not None for col in row  if row[col] is None ])
		return sum(sum(1 for s in row.values() if s is None) for row in self.current_seating() if row is not None)

	def book_seat(self, seatNumber, passenger):
		# print(self.__rows, self.__seats)
		rowNum, rowLet = self.__validate(seatNumber)
		cuBooking = self.current_seating()
		if cuBooking[rowNum][rowLet] is not None:
			raise ValueError(f'Seat {seatNumber} is already occupied. Please {passenger}, book other seat.')
		
		cuBooking[rowNum][rowLet] = passenger

	def relocate_passenger(self, fromSeat, toSeat):
		cuBooking = self.current_seating()
		fromRow, fromLet = self.__validate(fromSeat)
		if cuBooking[fromRow][fromLet] is None:
			raise ValueError(f'No passenger Available in {fromSeat}')

		toRow, toLet = self.__validate(toSeat)
		if cuBooking[toRow][toLet] is not None:
			raise ValueError(f'Seat {toSeat} is already Booked')
		
		cuBooking[toRow][toLet] = cuBooking[fromRow][fromLet]
		cuBooking[fromRow][fromLet] = None

	def __validate(self, seatNumber):
		rowLet = seatNumber[-1]
		if rowLet not in self.__seats:
			raise ValueError(f'Invalid Seat Letter - {rowLet}')
		rowNum = int(seatNumber[:-1])		
		if rowNum not in self.__rows:
			raise ValueError(f'Invalid Seat Row - {rowNum}')
		return rowNum, rowLet
	
	def generate_boarding_pass(self, printFn):
		for passenger, seatNumber in self.__passenger_seats():
			printFn(passenger, seatNumber, self.__number, self.__aircraft_model())

	def __passenger_seats(self):
		rows, seats = self.__aircraft.seating_plan()
		for r in rows:
			for s in seats:
				passenger = self.current_seating()[r][s]
				if passenger is not None:
					yield (passenger,f'{r}{s}') 

class AirCraft():
	def __init__(self, registration, model, noOfRows, noOfSeatsPerRow):
		self.__registration = registration
		self.__model = model
		self.__noOfRows = noOfRows
		self.__noOfSeatsPerRow = noOfSeatsPerRow

	def model(self):
		return self.__model;

	def seating_plan(self):
		return (range(1, self.__noOfRows+1), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:self.__noOfSeatsPerRow])

class Boeing777(AirCraft):
	def __init__(self, registration, model, noOfRows, noOfSeatsPerRow):
		AirCraft.__init__(self, registration, model, noOfRows, noOfSeatsPerRow)

class Airbus319(AirCraft):
	def __init__(self, registration, model, noOfRows, noOfSeatsPerRow):
		AirCraft.__init__(self, registration, model, noOfRows, noOfSeatsPerRow)

		
def print_boarding_pass(passenger, seatNumber, flightNumber, aircraft):
	output = f"| Name: {passenger}"		 \
			 f"  Flight: {flightNumber}" \
			 f"	 Seat: {seatNumber}"	 \
			 f"	 Aircraft: {aircraft}"	 \
			 " |"
	banner = "+" + "-" * (len(output)-2) + "+"
	# print(f'Out >> {len(output)}; {len(banner)}')
	border = '|' + " " * (len(output)-2) + '|'
	lines = [banner, border, output, border, banner]
	card ="\n".join(lines)
	print(card)
	print()

from pprint import pprint as pp

def boeing():
	print('------ Boeing777 -----')
	b=Boeing777('B-EUR', 'Boeing 777', noOfRows=25, noOfSeatsPerRow=10)
	# pp(b.seating_plan())
	fb=Flight('SN060', b) 
	# pp(fb.current_seating())
	fb.book_seat('1A', 'Vinodh Kumar T')
	fb.book_seat('2A', 'Ginoo C')
	fb.book_seat('3A', 'Raj B') 
	fb.book_seat('5A', 'Ginoo C')
	fb.book_seat('6A', 'Raj B') 
	fb.book_seat('8A', 'Vinodh Kumar T')
	# pp(fb.current_seating())
	fb.relocate_passenger('1A', '2B')
	fb.relocate_passenger('3A', '2C') 
	pp(f'Availale Seats : {fb.available_seats()}')
	# pp(fb.current_seating())
	fb.generate_boarding_pass(print_boarding_pass)
	print('------ Boeing777 -----')

def airbus():
	print('------ Airbus319 -----')
	a=Airbus319('A-EUR', 'Airbus 319', noOfRows=20, noOfSeatsPerRow=6)
	# pp(a.seating_plan())
	fa=Flight('SN060', a) 
	# pp(fa.current_seating())
	fa.book_seat('1A', 'Vinodh Kumar T')
	fa.book_seat('2A', 'Ginoo C')
	fa.book_seat('3A', 'Raj B') 
	fa.book_seat('5A', 'Ginoo C')
	fa.book_seat('6A', 'Raj B') 
	fa.book_seat('8A', 'Vinodh Kumar T')
	# pp(fa.current_seating())
	fa.relocate_passenger('1A', '2B')
	fa.relocate_passenger('3A', '2C') 
	pp(f'Availale Seats : {fa.available_seats()}')
	# pp(fa.current_seating())
	fa.generate_boarding_pass(print_boarding_pass)
	print('------ Airbus319 -----')


if __name__ == '__main__': 
	boeing()
	airbus()