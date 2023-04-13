import os
from gettestmail import GetTestMailClient


def main():
  api_key = os.environ["API_KEY"]
  client = GetTestMailClient(api_key)
  test_mail = client.create_new()
  print(test_mail.emailAddress)

  test_mail = client.wait_for_message(test_mail.emailAddress)
  print(test_mail.message)


main()