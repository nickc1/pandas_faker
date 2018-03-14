
pandas_faker
========

pandas_faker is a wrapper around the [Faker library](https://github.com/joke2k/faker) that dumps fake data into dataframes.


## Example

```python
import pandas as pd
from pandas_faker import PandasFaker

F = PandasFaker()
X = F.make_fakes(1000)
X.head(10)
```

<table border="1">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>free_email_domain</th>
      <th>job</th>
      <th>name</th>
      <th>random_digit</th>
      <th>random_digit_or_empty</th>
      <th>state_abbr</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Port Aaron</td>
      <td>hotmail.com</td>
      <td>Freight forwarder</td>
      <td>Connie Contreras</td>
      <td>6</td>
      <td></td>
      <td>OR</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Robertmouth</td>
      <td>yahoo.com</td>
      <td>Financial trader</td>
      <td>Meghan Keller</td>
      <td>7</td>
      <td>0</td>
      <td>OH</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East Carlland</td>
      <td>hotmail.com</td>
      <td>Therapist, occupational</td>
      <td>Joseph Schultz</td>
      <td>3</td>
      <td></td>
      <td>AZ</td>
    </tr>
    <tr>
      <th>3</th>
      <td>South Ericahaven</td>
      <td>hotmail.com</td>
      <td>Advertising art director</td>
      <td>Christopher Brown</td>
      <td>1</td>
      <td>0</td>
      <td>CT</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Amyport</td>
      <td>gmail.com</td>
      <td>Surveyor, planning and development</td>
      <td>Amanda Murphy</td>
      <td>2</td>
      <td></td>
      <td>DE</td>
    </tr>
  </tbody>
</table>


## Basic Fields
This is a small set of fields that are useful for testing.

```
name
free_email_domain
city
state_abbr
job
random_digit
random_digit_or_empty
```

## Quick Fields
There are some fields that are quicker to generate than others. If generating a lot of data, then stick to these fields.

```
random_element
random_digit
random_digit_not_null
uri_page
safe_color_name
free_email_domain
military_state
random_int
uri_extension
state_abbr
state
pybool
military_ship
pyint
tld
zipcode
random_letter
null_boolean
mac_processor
randomize_nb_elements
city_prefix
linux_processor
company_suffix
postalcode
city_suffix
unix_time
windows_platform_token
boolean
century
linux_platform_token
word
street_suffix
random_digit_not_null_or_empty
currency_code
hex_color
sha1
credit_card_provider
sha256
md5
country_code
random_digit_or_empty
country
safe_hex_color
timezone
uuid4
geo_coordinate
random_number
language_code
longitude
zipcode_plus4
latitude
postalcode_plus4
mime_type
file_extension
prefix_male
job
mac_platform_token
prefix_female
uri_path
ipv4
suffix_female
iso8601
locale
color_name
image_url
internet_explorer
file_name
ssn
bs
time
numerify
catch_phrase
prefix
suffix_male
lexify
suffix
secondary_address
date
month_name
month
year
file_path
pyfloat
credit_card_security_code
pydecimal
mac_address
am_pm
ipv6
building_number
bothify
slug
ean8
military_apo
military_dpo
```


## All Fields

```
am_pm
boolean
bothify
bs
building_number
catch_phrase
century
city
city_prefix
city_suffix
color_name
company
company_email
company_suffix
country
country_code
credit_card_expire
credit_card_number
credit_card_provider
credit_card_security_code
currency_code
date
domain_name
domain_word
ean
ean13
ean8
email
file_extension
file_name
file_path
first_name
first_name_female
first_name_male
free_email
free_email_domain
geo_coordinate
hex_color
image_url
internet_explorer
ipv4
ipv6
isbn10
isbn13
iso8601
job
language_code
last_name
last_name_female
last_name_male
latitude
lexify
linux_platform_token
linux_processor
locale
longitude
mac_address
mac_platform_token
mac_processor
md5
military_apo
military_dpo
military_ship
military_state
mime_type
month
month_name
name
name_female
name_male
null_boolean
numerify
password
phone_number
postalcode
postalcode_plus4
postcode
prefix
prefix_female
prefix_male
pybool
pydecimal
pyfloat
pyint
pystr
random_digit
random_digit_not_null
random_digit_not_null_or_empty
random_digit_or_empty
random_element
random_int
random_letter
random_number
randomize_nb_elements
safe_color_name
safe_email
safe_hex_color
secondary_address
seed
sentence
sha1
sha256
slug
ssn
state
state_abbr
street_address
street_name
street_suffix
suffix
suffix_female
suffix_male
text
time
timezone
tld
unix_time
uri
uri_extension
uri_page
uri_path
url
user_agent
user_name
uuid4
windows_platform_token
word
year
zipcode
zipcode_plus4
```

# Time

The plot below shows the time to generate 1k samples on a macbook air. Take these times into consideration if you are generating a lot of data

![generating samples](/examples/time_to_gen_1k_samples.png)







