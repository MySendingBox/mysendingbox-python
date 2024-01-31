# mysendingbox-python

[![PyPI version](https://badge.fury.io/py/mysendingbox.svg)](http://badge.fury.io/py/mysendingbox)
[![Dependency Status](https://gemnasium.com/badges/github.com/mysendingbox/mysendingbox-python.svg)](https://gemnasium.com/github.com/mysendingbox/mysendingbox-python)

Mysendingbox.fr Python bindings is a simple but flexible wrapper for the [Mysendingbox.fr](https://www.mysendingbox.fr) API.

See full Mysendingbox.fr documentation [here](https://docs.mysendingbox.fr/?python#).

For best results, be sure that you're using the latest version of the Mysendingbox API and the latest version of the Python wrapper.

#### French

Un module Python pour envoyer du courrier postal ou électronique en ligne depuis votre application Python.

Mysendingbox propose une API permettant d'envoyer très facilement du courrier postal depuis votre ERP, CRM ou application web.

Pas de frais d'installation. Pas d'engagement. Vous payez ce que vous consommez.

Documentation : https://docs.mysendingbox.fr/?python

Bien démarrer : https://www.mysendingbox.fr/guide/bien-demarrer-avec-l-api-d-envoi-de-courrier

## Table of Contents

- [Getting Started](#getting-started)
  - [Registration](#registration)
  - [Installation](#installation)
  - [Letters](#letters)
  - [Accounts](#accounts)
  - [Invoices](#invoices)
- [Examples](#examples)

## Getting Started

Here's a general overview of the Mysendingbox services available, click through to read more.

Please read through the official [API Documentation](https://docs.mysendingbox.fr/?python#) to get a complete sense of what to expect from each endpoint.

### Registration

First, you will need to first create an account at [Mysendingbox.fr](https://www.mysendingbox.fr/signup) and obtain your Test and Live API Keys.

Once you have created an account, you can access your API Keys from the [API Keys Panel](https://www.mysendingbox.fr/app/dashboard/keys).

### Installation

mysendingbox-python can be installed through the `pip` or `easy_install`:

```
pip install mysendingbox
easy_install mysendingbox
```

### Usage

#### Create a new letter

```python
import mysendingbox
mysendingbox.api_key = 'your-api-key'

example_letter = mysendingbox.Letter.create(
    description='Test Letter from Python Bindings',
    to_address={
        'name': 'Erlich',
        'address_line1': '30 rue de rivoli',
        'address_city': 'Paris',
        'address_postalcode': '75004',
        'address_country': 'France'
    },
    source_file="""<html>Hello {{name}},</html>""",
    source_file_type="html",
    variables={
        'name': 'Erlich'
    },
    postage_type="prioritaire",
    color="bw"
)

print "Letter Response : "
print "\n"
print example_letter
print "\n"
```

#### Create a new electronic letter

```python
import mysendingbox
mysendingbox.api_key = 'your-api-key'

example_letter = mysendingbox.Letter.createElectronic(
    description='Test Electronic Letter from Python Bindings',
    to_address={
        email: 'erlich.dumas@example.com',
        first_name: 'Erlich',
        last_name: 'Dumas',
        status: 'individual'
    },
    content: 'Please review the attached documents:',
    source_file="""<html>Hello {{name}},</html>""",
    source_file_type="html",
    variables={
        'name': 'Erlich'
    },
    postage_type="lre"
)

print "Letter Response : "
print "\n"
print example_letter
print "\n"
```

#### List all letters

```python
import mysendingbox
mysendingbox.api_key = 'your-api-key'

list_letters = mysendingbox.Letter.list()

print "List Letters : "
print "\n"
print list_letters
print "\n"
```

#### Retrieve a specific letter

```python
import mysendingbox
mysendingbox.api_key = 'your-api-key'

get_letter = mysendingbox.Letter.retrieve('ID_OF_THE_LETTER')

print "Get Letter : "
print "\n"
print get_letter
print "\n"
```

### Accounts

#### Create a new account for the company

```python
import mysendingbox
mysendingbox.api_key = 'your-api-key'

example_account = mysendingbox.Account.create(
  email="msb.partner@example.com",
  name="Erlich Bachman",
  phone="+33104050607",
  company_name="MSB Partner from Python Wrapper",
  address_line1='30 rue de rivoli',
  address_line2='',
  address_city='Paris',
  address_country='France',
  address_postalcode='75004'
)

print "New Account Response : "
print "\n"
print example_account
print "\n"
```

#### Update the account company email

```python
import mysendingbox
mysendingbox.api_key = 'your-api-key'

mysendingbox.Account.updateEmail(
    "ACCOUNT COMPANY ID",
    "msb.partner.new@example.com",
)

print "Email Account Updated"
print "\n"
```

### Invoices

#### List all invoices for a company

```python
import mysendingbox
mysendingbox.api_key = 'your-api-key'

example_list_invoices = mysendingbox.Invoice.list(
  status="paid",
  date_start="2020-01-01"
)

print "List Invoice Response : "
print "\n"
print example_list
print "\n"
```

#### Retrieve a specific invoice

```python
import mysendingbox
mysendingbox.api_key = 'your-api-key'

example_invoice = mysendingbox.Invoice.retrieve("INVOICE ID")

print "Invoice Response : "
print "\n"
print example_invoice
print "\n"
```

## Examples

We've provided various examples for you to try out [here](https://github.com/mysendingbox/mysendingbox-python/tree/master/examples).

=======================

Copyright &copy; 2017 Mysendingbox.fr

Released under the MIT License, which can be found in the repository in `LICENSE.txt`.
