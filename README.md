TrashMail.net disposable email address
======================================

* Author:  Laszlo Szathmary, 2013 (<jabba.laci@gmail.com>)
* Website: <http://ubuntuincident.wordpress.com/2013/04/13/trashmail/>
* GitHub:  <https://github.com/jabbalaci/TrashMail.net-disposable-email-address>

Creates a disposable email address on TrashMail.net (<https://ssl.trashmail.net/>).

First, you must register yourself on trashmail.net (it's free). With these
credentials you can access the address manager of TrashMail.net. Emails will be
redirected to the address that you set upon registration.

Then, you must provide your credentials to this script. Either you
hard-code it in the source (USERNAME and PASSWORD variables), or
you provide them interactively.

The script will create a disposable email address for you on TrashMail.net.
The newly created email address will be copied to the clipboard (for this
you must have the "xsel" command installed on your system).

Tested under Linux with Python 2.7.

Usage
-----

    ./trashmail.py

Sample output:

    # copied to the clipboard
    prcb107f@trashmail.net