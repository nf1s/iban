# IBAN Validator

## Simple REST API to handle validation of an IBAN (International Bank Account Numbers)

## Requirements

1. One endpoint
2. Cross-Platform
3. Run in docker

### IBAN Validation Requirements

#### Examples of IBAN

| Country        | IBAN Example                            |
| -------------- | --------------------------------------- |
| Belgium        | BE71 0961 2345 6769                     |
| Brazil         | BR15 0000 0000 0000 1093 2840 814 P2    |
| Costa Rica     | CR99 0000 0000 0000 8888 88             |
| France	FR76   | 3000 6000 0112 3456 7890 189            |
| Ireland        | IE12 BOFI 9000 0112 3456 78             |
| Germany        | DE91 1000 0000 0123 4567 89             |
| Greece         | GR96 0810 0010 0000 0123 4567 890       |
| Mauritius      | MU43 BOMM 0101 1234 5678 9101 000 MUR   |
| Pakistan       | PK70 BANK 0000 1234 5678 9000           |
| Poland         | PL10 1050 0099 7603 1234 5678 9123      |
| Portugal       | PT50 0033 0000 5013 1901 2290 5         |
| Romania        | RO09 BCYP 0000 0012 3456 7890           |
| Saint Lucia    | LC14 BOSL 1234 5678 9012 3456 7890 1234 |
| Saudi Arabia   | SA44 2000 0001 2345 6789 1234           |
| Slovakia       | SK08 0900 0000 0001 2312 3123           |
| Spain          | ES79 2100 0813 6101 2345 6789           |
| Sweden         | SE87 3000 0000 0101 2345 6789           |
| Switzerland    | CH56 0483 5012 3456 7800 9              |
| United Kingdom | GB98 MIDL 0700 9312 3456 78             |

According to [wikipedia](https://en.wikipedia.org/wiki/International_Bank_Account_Number)

An IBAN is validated by converting it into an integer and performing a basic
mod-97 operation (as described in ISO 7064) on it. If the IBAN is valid, the
remainder equals 1. The algorithm of IBAN validation is as follows

0. Trim and clean white Spaces.
1. Check length, Min = 15 and Max = 34
2. Check for non-alpha-numeric chars -> Invalid
3. Check that the total IBAN length is correct as per the country. If not, the
   IBAN is invalid.
4. Move the four initial characters to the end of the string
5. Replace each letter in the string with two digits, thereby expanding the
   string, where A = 10, B = 11, ..., Z = 35
6. Interpret the string as a decimal integer.
7. Compute the remainder of that number on division by 97 If the remainder is
   1, the check digit test is passed and the IBAN might be valid.
8. Check if the IBAN is valid per country's format.

Example (fictitious United Kingdom bank, sort code 12-34-56, account number
98765432):

  - IBAN:		GB82 WEST 1234 5698 7654 32
  - Rearrange:		W E S T12345698765432 G B82	
  - Convert to integer:		3214282912345698765432161182
  - Compute remainder:		3214282912345698765432161182	mod 97 = 1

## Solution
1. REST API with one endpoint.
2. Rules Engine Pattern fits the problem.

### Technologies
1. Python 3.10.5
2. FastAPI

### MVP
1. Endpoint
2. Simple rules engine
  - Check for Alphanumeric
  - Check for Mod-97 operation as described in ISO 7064
  - check for valid IBAN length (per country and in general)
  - Check Iban has valid format per country
3. Docker
4. Unit Tests

### Full Solution
1. Tests with good coverage
2. Memoization: In memory caching for IBAN results
3. Refactoring and docstrings


## Setup (Locally)
If you are using docker skip to the docker section

### Requirements
- python 3.10.5
- pipenv
- make

```
make setup
```

Run locally

```
make run
```
Run tests

```
make test
```

## Using Docker

### Requirements
1. docker
2. docker-compose

```
make docker-run
```
Run tests

```
make docker-test
```


Server will be running at

```
  http://localhost:8000
```

#### IBAN endpoint

```
http://localhost:8000/api/v1/iban

```

### Documentation
```
1. openapi.v3 - http://localhost:8000/docs
2. redoc      - http://localhost:8000/redoc
```
## Examples

#### CURL
```
curl -X 'POST' \
  'http://localhost:8000/api/v1/iban' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "iban": "GB82 WEST 1234 5698 7654 32"
}'
```

#### Httpie
```
http http://localhost:8000/api/v1/iban iban="GB82 WEST 1234 5698 7654 32"
```

#### Response
```
{
  "description": "IBAN Validation",
  "content": {
    "iban": "GB82WEST12345698765432",
    "valid": true,
    "message": "IBAN validation was successful"
  }
}
```
