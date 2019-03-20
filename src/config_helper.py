import json

def read_client_credentials(credentials_file):
    try: 
        print("Using config file:" + credentials_file)
        with open(credentials_file, 'r') as outfile:
            data = json.load(outfile)
            client_id = data['client_id']
            client_secret = data['client_secret']

    except FileNotFoundError:
        print("You must define a {} with client_id, client_secret".format(credentials_file))
        print("""{"client_id": "your_client_id", "client_secret": "your_client_secret"}""")
        sys.exit

    print("client_id: " + client_id)
    print("client_secret: " + client_secret)

    return (client_id, client_secret)
