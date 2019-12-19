# mutual-followers
mutual-followers is a tool that allows you to discover the mutual friends of twitter accounts.

## Why?

I personally use mutual-followers to discover influential people on software engineering by inspecting the mutual friends of reputable people.

## Installation

Currently the only method to install this is to clone the repository and run pip install on requirements file.

Note that you need twitter consumer and secret keys for mutual-followers to work.

## Twitter credentials

Please take a look at https://stackoverflow.com/questions/1808855/getting-new-twitter-api-consumer-and-secret-keys to get your consumer keys.

## Usage

run this with arguments `--consumer_key <> --consumer_secret <> --access_token <> --access_token_secret <> --users dhh,jasonfried`

and you will find out who @dhh and @jasonfried is following mutually.
