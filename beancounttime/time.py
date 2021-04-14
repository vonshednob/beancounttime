import decimal
from decimal import Decimal

from beancount.core import data
from beancount.core.amount import Amount
from beancount import loader


__plugins__ = ['mangle_time']


def convert_to_decimal_time(value):
    factor = Decimal(100/60.)
    hours = value.to_integral_value(rounding=decimal.ROUND_DOWN)
    minutes = value - hours
    return Decimal(hours + minutes*factor)


def mangle_time(entries, options_map, conf=None):
    errors = []
    for entry in entries:
        if not isinstance(entry, data.Transaction):
            continue

        for posting in entry.postings[:]:
            if posting.units.currency != conf:
                continue
            duration = posting.units.number
            if not isinstance(duration, Decimal):
                continue
            conv_time = convert_to_decimal_time(posting.units.number)
            converted = data.Posting(posting.account,
                                     Amount(conv_time, posting.units.currency),
                                     posting.cost,
                                     posting.price,
                                     posting.flag,
                                     posting.meta)
            entry.postings.remove(posting)
            entry.postings.append(converted)

    return entries, errors


if __name__ == '__main__':
    assert convert_to_decimal_time(Decimal(2.56)) - Decimal(2.9333) < Decimal(0.001)
    assert convert_to_decimal_time(Decimal(1.15)) - Decimal(1.25) < Decimal(0.001)
    assert convert_to_decimal_time(Decimal(1.30)) - Decimal(1.5) < Decimal(0.001)
    assert convert_to_decimal_time(Decimal(0.55)) + convert_to_decimal_time(Decimal(0.05)) - Decimal(1) < Decimal(0.001)
    assert convert_to_decimal_time(Decimal(-1.57)) + convert_to_decimal_time(Decimal(-0.03)) + Decimal(2) < Decimal(0.001)

    entries, errors, options = loader.load_string("""
2010-01-01 open Equity:Time HR
2010-01-01 open Expenses:Hacking HR
2010-01-02 * ""
  Expenses:Hacking  2.55 HR
  Expenses:Hacking  1.05 HR
  Equity:Time      -4.00 HR
""")
    entries, _ = mangle_time(entries, {}, "HR")

    print(entries)

