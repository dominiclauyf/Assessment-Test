def pre_process_email(email: str) -> tuple[str, str]:
    username, domain = email.split("@")
    company_name, _ = domain.split('.')
    return username, company_name


if __name__ == '__main__':
    username, company_name = pre_process_email('username@companyname.com')
    print(f"Username: {username}, Company Name: {company_name}")
