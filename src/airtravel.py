"""Da corso Python Fundamentals - Cap. 9 - Modello per voli aerei"""


class Flight:
    """Un volo con un particolare aereo di linea"""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("Nessun codice aeroplano in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Codice aeroplano non valido '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Numero aeroplano non valido '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat):
        """Fa il parsing dell'identificativo di un posto in una fila ed un posto validi

        :param seat: L'identificativo di un posto, ad esempio 7C
        :raises ValueError: Quando si hanno dei valori inseriti non validi (lettera posto, posto o numero fila)
        :return: Una tuple contenente un intero e una stringa per ogni fila e posto
        """
        row_numbers, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Lettera {} del posto non valida".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Posto {} della fila non valido".format(row_text))

        if row not in row_numbers:
            raise ValueError("Numero {} della fila non valido".format(row))

        return row, letter

    def allocate_seat(self, seat, passenger):
        """Assegna un posto ad un passeggero

        :param seat: Il posto preso in considerazione, ad esempio "10D"
        :param passenger: Il nome del passeggero
        :raises ValueError: quando il posto è già occupato
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Posto {} già occupato".format(seat))

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        """ Cambia il posto ad un passeggero

        :param from_seat: Il posto in cui si trova il passeggero da spostare
        :param to_seat: Il posto di destinazione del passeggero
        :raises ValueError: Quando nel posto selezionato non ci sono passeggeri o la destinazione è occupata
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("Nessun passeggero da riposizionare al posto {}".format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Posto {} già occupato".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None) for row in self._seating if row is not None)


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row]


def make_flight():
    f = Flight("AB2034", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
    f.allocate_seat("02F", "Fabio Vettori")
    f.allocate_seat("8D", "Tizio Incognito")
    f.allocate_seat("13A", "Ivo Avido")
    f.allocate_seat("4B", "Rupert Sciamenna")
    return f
