# beancounttime

After installing through `pip`, like this

    $ pip install beancounttime

you can use the plugin in beancount to track time like this:

    ;; timetracking.beancount
    plugin "beancounttime.time"  "HR"

    1900-01-01 open Equity:Universe        HR
    1900-01-01 open Expenses:Work          HR
    1900-01-01 open Expenses:Work:Hacking  HR
    1900-01-01 open Expenses:Work:Meeting  HR

    2000-01-01 * ""
      Expenses:Work:Hacking   4.50 HR
      Expenses:Work:Meeting   3.30 HR
      Equity:Universe        -8.20 HR

As you can see time is tracked in the form of `HH.MM`. The plugin will take
care of converting this format into the decimal form, so beancount can work
with it.

E.g. `3.30 HR` (3 hours, 30 minutes) will be converted to `3.50 HR`.

The plugin will only apply the conversion to transactions with the commodity
that is passed as a parameter to the plugin (in the example `HR`).


## Contributing

Any contribution is appreciated! Report bugs in issues or via email to the
authors.

The source code can be found on
[vonshednob.cc](https://vonshednob.cc/beancounttime) and on
[PyPi](https://pypi.org/project/beancounttime/).

Pull requests through github are no longer supported, but patches and code
discussions via email are most welcome! If you don't quite know how to do
that, have a look at the [blog article that gives detailed instructions how to
work without github](https://spacepanda.se/participating.html).

