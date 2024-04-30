# Helper Website

A Flask website in a Docker container with helpful snippets for offline use

## Build
1. Create `favourites.yml`. See `Config` Section for an example
1. `docker build --tag helper-website .`

## Run
1. `docker run -d -p 9876:9876 helper-website`  
1. Access website on *HostIP*:9876


## Config
The `favourites.yml` config defines a list of links to display on the home page. Below is a sample config
```yml
SO:
  - Stack Overflow: https://stackoverflow.com/
  - Merge rows in pandas dataframe: https://stackoverflow.com/questions/78407529/i-need-to-merge-top-2-rows-in-dataframe

Social Media:
  - FB: https://www.facebook.com/
  - Reddit: https://www.reddit.com/
  - Instagram: https://www.instagram.com/
```
