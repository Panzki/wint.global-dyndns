# wint.global-dyndns
This repository provides a small script to update dyndns records for the hoster [wint.glonbal](https://wint.global/). There is also a docker image running a cron job calling the script once every minute. The docker image can be found on [docker hub](https://hub.docker.com/r/panzki/wint.global-dyndns).

## Usage
The easiest way is to use the docker container. You can start the container by running the the following command. Replace `userID`, `apiPassword` and `domain` with the correct values for your account. The FAQ in your wint.global account contains an article on setting up dyndns. 

`docker run -d -e USER_ID='userID' -e API_KEY='apiPassword' -e DOMAIN='domain' --rm --name wint.global-dyndns panzki/wint.global-dyndns:latest`

If you don't want to use the docker container you can run the script using Python 3.6+.

`python refresh_dyndns.py -u userID -k apiPassword -d domain`