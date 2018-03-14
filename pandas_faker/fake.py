# By Nick Cortale
# 2017-06-28
#
# Extends the functionality of faker to a more data scientist-esque approach.
# Implements some of the functions from numpy to create some fake data. This is
# also useful for creating data sets with a certain demensionality and integer
# fields.

import faker
import pandas as pd
import time as time


FIELD_LIST = ['am_pm', 'boolean', 'bothify', 'bs', 'building_number', 'catch_phrase',
'century', 'city', 'city_prefix', 'city_suffix', 'color_name', 'company',
'company_email', 'company_suffix', 'country', 'country_code', 'credit_card_expire',
'credit_card_number', 'credit_card_provider', 'credit_card_security_code',
'currency_code', 'date', 'domain_name', 'domain_word', 'ean', 'ean13', 'ean8',
'email', 'file_extension', 'file_name', 'file_path', 'first_name',
'first_name_female', 'first_name_male', 'free_email', 'free_email_domain',
'geo_coordinate', 'hex_color', 'image_url', 'internet_explorer', 'ipv4', 'ipv6',
'isbn10', 'isbn13', 'iso8601', 'job', 'language_code', 'last_name',
'last_name_female', 'last_name_male', 'latitude', 'lexify',
'linux_platform_token', 'linux_processor', 'locale', 'longitude', 'mac_address',
'mac_platform_token', 'mac_processor', 'md5', 'military_apo', 'military_dpo',
'military_ship', 'military_state', 'mime_type', 'month', 'month_name', 'name',
'name_female', 'name_male', 'null_boolean', 'numerify',
'password', 'phone_number', 'postalcode', 'postalcode_plus4', 'postcode',
'prefix', 'prefix_female', 'prefix_male', 'pybool', 'pydecimal', 'pyfloat',
'pyint', 'pystr', 'random_digit', 'random_digit_not_null',
'random_digit_not_null_or_empty', 'random_digit_or_empty', 'random_element',
'random_int', 'random_letter', 'random_number', 'randomize_nb_elements',
'safe_color_name', 'safe_email', 'safe_hex_color', 'secondary_address', 'seed',
'sentence', 'sha1', 'sha256', 'slug', 'ssn', 'state',
'state_abbr', 'street_address', 'street_name', 'street_suffix', 'suffix',
'suffix_female', 'suffix_male', 'text', 'time',
'timezone', 'tld', 'unix_time', 'uri', 'uri_extension', 'uri_page', 'uri_path',
'url', 'user_agent', 'user_name', 'uuid4', 'windows_platform_token', 'word',
'year', 'zipcode', 'zipcode_plus4']


QUICK_LIST = ['random_element', 'random_digit', 'random_digit_not_null',
  'uri_page', 'safe_color_name', 'free_email_domain', 'military_state',
  'random_int', 'uri_extension', 'state_abbr', 'state', 'pybool', 'military_ship',
  'pyint', 'tld', 'zipcode', 'random_letter', 'null_boolean', 'mac_processor',
  'randomize_nb_elements', 'city_prefix', 'linux_processor', 'company_suffix',
  'postalcode', 'city_suffix', 'unix_time', 'windows_platform_token', 'boolean',
  'century', 'linux_platform_token', 'word', 'street_suffix',
  'random_digit_not_null_or_empty', 'currency_code', 'hex_color', 'sha1',
  'credit_card_provider', 'sha256', 'md5', 'country_code',
  'random_digit_or_empty', 'country', 'safe_hex_color', 'timezone', 'uuid4',
  'geo_coordinate', 'random_number', 'language_code', 'longitude',
  'zipcode_plus4', 'latitude', 'postalcode_plus4', 'mime_type', 'file_extension',
  'prefix_male', 'job', 'mac_platform_token', 'prefix_female', 'uri_path',
  'ipv4', 'suffix_female', 'iso8601', 'locale', 'color_name', 'image_url',
  'internet_explorer', 'file_name', 'ssn', 'bs', 'time', 'numerify',
  'catch_phrase', 'prefix', 'suffix_male', 'lexify', 'suffix',
  'secondary_address', 'date', 'month_name', 'month', 'year', 'file_path',
  'pyfloat', 'credit_card_security_code', 'pydecimal', 'mac_address', 'am_pm',
  'ipv6', 'building_number', 'bothify', 'slug', 'ean8', 'military_apo',
  'military_dpo']


BASIC_LIST = ['name', 'free_email_domain', 'city', 'state_abbr', 'job',
    'random_digit', 'random_digit_or_empty']



class PandasFaker(object):
    """Create fake data for data analysis or database testing purposes.

    fields : list or None
        If fields is none, will use the basic list.
    """

    def __init__(self, fields=None):

        if not fields:
            fields = BASIC_LIST
        
        self.fields = fields
        self.faker_obj = faker.Faker()


    def _gen_fake(self):
        """Create a fake dictionary of attributes as defined in fields.

        fields : list
            Fields to grab to generate some fake data.
        """

        #fake = faker.Faker()
        data = {}

        for field in self.fields:

            try:
                x = getattr(self.faker_obj, field)
                data[field] = x()
            except:
                print("{} is not currently implemented".fomrat(field) )


        return data

    def make_fakes(self, num_fakes):
        """Create multiple fake records that will be output as a pandas
        dataframe.

        num_fakes : int
            Number of fakes to create
        """

        data_list = []

        for i in range(num_fakes):

            data = self._gen_fake()
            data_list.append(data)

        return pd.DataFrame(data_list)
