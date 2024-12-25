from num2words import num2words
from num2words.currency import parse_currency_parts

# https://www.reddit.com/r/Python/comments/239cv3/if_were_all_consenting_adults_does_it_make_sense/ 💪💪💪💪💪

class Bank:
    def __init__(self, name, routing_number):
        self.name = name
        self.routing_number = routing_number


class Issuer:
    def __init__(self, name, details, bank, account_number):
        self.name = name
        self.details = details
        self.bank = bank
        self.account_number = account_number


class Payment:
    def __init__(self, payee, amount, date, memo=None):
        self.payee = payee
        self._amount = amount
        self._date = date
        self.memo = memo

    @property
    def amount(self):
        return f"{self._amount:,.2f}"

    @property
    def date(self):
        return f"{self._date.month}/{self._date.day}/{self._date.year}"

    def written_amount(self):
        dollars, cents, _ = parse_currency_parts(self._amount, is_int_with_cents=False)

        dollars = num2words(dollars).replace(' and', '').replace(',', '').replace('-', ' ')

        cents = f"{cents:02}" if cents else "XX"

        return f"{dollars.capitalize()} and {cents}/100"
