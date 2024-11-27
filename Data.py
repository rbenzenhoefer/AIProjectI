import streamlit as st

countries_all = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina",
    "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados",
    "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana",
    "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon",
    "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo",
    "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia", "Denmark", "Djibouti",
    "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea",
    "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia",
    "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
    "Haiti", "Vatican City", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland",
    "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "North Korea",
    "South Korea", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya",
    "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali",
    "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco",
    "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru",
    "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway",
    "Oman", "Pakistan", "Palau", "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru",
    "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis",
    "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe",
    "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
    "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname",
    "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga",
    "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates",
    "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam",
    "Yemen", "Zambia", "Zimbabwe"]
#193

length = len(countries_all)
print(length)

countries_easy = [
    "Argentina", "Australia", "Austria", "Belgium", "Brazil",
    "Canada", "Chile", "China", "Colombia", "Croatia", "Czechia", "Denmark", "Egypt",
    "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "India", "Indonesia", "Ireland",
    "Israel", "Italy", "Japan", "North Korea", "South Korea",
    "Mexico", "Morocco", "New Zealand", "Norway", "Peru", "Poland", "Portugal",
    "Russia", "Saudi Arabia", "South Africa", "Spain", "Sweden", "Switzerland", "Thailand", "Turkey",
    "Ukraine", "United Kingdom", "United States of America",]
#45

length1 = len(countries_easy)
print(length1)

countries_mid = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Armenia", "Azerbaijan", "Bahamas",
    "Bangladesh", "Belarus", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Bulgaria",
    "Cambodia", "Cameroon", "Congo", "Costa Rica", "Cuba", "Cyprus", "Dominican Republic",
    "Ecuador", "El Salvador", "Eritrea", "Ethiopia", "Georgia", "Ghana", "Guatemala",
    "Haiti", "Honduras", "Iran", "Iraq", "Ivory Coast", "Jamaica", "Jordan", "Kazakhstan", "Kenya",
    "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Libya", "Liechtenstein", "Lithuania",
    "Luxembourg", "Madagascar", "Malaysia", "Maldives", "Mali", "Malta", "Mauritius",
    "Moldova", "Monaco", "Mongolia", "Montenegro", "Mozambique", "Myanmar", "Namibia",
    "Nepal", "Netherlands", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Oman",
    "Pakistan", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Philippines",
    "Qatar", "Romania", "Rwanda", "San Marino", "Senegal", "Serbia", "Seychelles",
    "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Sri Lanka", "Sudan", "Syria",
    "Tanzania", "Trinidad and Tobago", "Tunisia", "Uganda", "United Arab Emirates",
    "Uruguay", "Uzbekistan", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
#95

length2 = len(countries_mid)
print(length2)

countries_hard = [
    "Angola", "Antigua and Barbuda", "Bahrain", "Barbados", "Belize", "Benin", "Bhutan", "Brunei",
    "Burkina Faso", "Burundi", "Cabo Verde", "Central African Republic", "Chad", "Comoros", "Djibouti",
    "Dominica", "Equatorial Guinea", "Estonia", "Eswatini", "Fiji", "Gabon", "Gambia", "Grenada", "Guinea",
    "Guinea-Bissau", "Guyana", "Holy See", "Kiribati", "Latvia", "Lesotho", "Liberia", "Malawi",
    "Marshall Islands", "Mauritania", "Micronesia", "Nauru", "Palau", "Palestine State", "Saint Kitts and Nevis",
    "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "Sao Tome and Principe", "Solomon Islands",
    "Somalia", "South Sudan", "Suriname", "Tajikistan", "Timor-Leste", "Togo", "Tonga", "Turkmenistan",
    "Tuvalu", "Vanuatu"]
#54

length3 = len(countries_hard)
print(length3)


countries_africa = [
    "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde",
    "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo", "Djibouti",
    "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia",
    "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia",
    "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco",
    "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe",
    "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan",
    "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]
length4 = len(countries_africa)
print(length4)

countries_asia = [
    "Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei",
    "Cambodia", "China", "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan",
    "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives",
    "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan", "Palestine State", "Philippines",
    "Qatar", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", "Tajikistan",
    "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan",
    "Vietnam", "Yemen"]
length5 = len(countries_asia)
print(length5)

countries_europe = [
    "Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina",
    "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France",
    "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kosovo", "Latvia", "Liechtenstein",
    "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands",
    "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino",
    "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom",
    "Vatican City"]
length6 = len(countries_europe)
print(length6)

countries_north_america = [
    "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba",
    "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras",
    "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States of America"]
length7 = len(countries_north_america)
print(length7)

countries_oceania = [
    "Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand",
    "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"]
length8 = len(countries_oceania)
print(length8)

countries_south_america = [
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana",
    "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"
]
