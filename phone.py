import phonenumbers
from phonenumbers import geocoder
p_n1 = phonenumbers.parse("+923255339295")
print(geocoder.description_for_number(p_n1,"en"))