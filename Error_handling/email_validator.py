from Error_handling.custom_errors import NameTooShortError, MustContainAtSymbolError, InvalidDomainError

while True:
    email_name = input()
    domains_set = ('com', 'bg', 'org', 'net')

    # Checking if username is too short
    user_name = email_name.split('@')
    if len(user_name[0]) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    if '@' not in email_name:
        raise MustContainAtSymbolError('Email must contain @')

    # Checking if the domain is correct
    domain_name = email_name.split('.')
    if domain_name[-1] not in domains_set:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print('Email is valid')
    break
