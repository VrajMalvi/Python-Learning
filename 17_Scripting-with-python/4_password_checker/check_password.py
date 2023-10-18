import requests  # to manually request something like browser
import hashlib  # for hashing SHA series
import sys

# from passwordsgenerator.net we hash password123 to CBFDAC6008F9CAB4083784CBD1874F76618D2A97
# now we use only first five chars becauser if send full pass then it might decoded so using only first five when we need pass we try all the pass with that first five char
# responce 400 means something is not right
# 200 is a standard response for successful HTTP requests


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leaks_count(hashes, hashes_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    # print(hashes)
    for h, count in hashes:
        if h == hashes_to_check:
            return count
    return 0


def pwned_api_check(password):
    # object must be encoded before hashing here it is encoded in utf-8 or it will give error
    sha1password = hashlib.sha1(password.encode('Utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    responce = request_api_data(first5_char)
    # print(first5_char, tail)
    # print(responce)
    return get_password_leaks_count(responce, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f'{password} was found {count} times .....you should change your password')
        else:
            print(f'{password} not found. carry on!')
    return 'done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


# to run : python 17_Scripting-with-python/4_password_checker/check_password.py passtry1 passtry2 ....


# in this code passwords are stored in memory (sys.argv) which is not secured to make more secured we store passwords in txt file and fetch it
