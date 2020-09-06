# Introduction to OpenWPM Crawling

This mini project is a introduction to a open-source web-crawling tool called OpenWPM. Below is the analysis of data in two modes (vanilla mode and ad-blocking mode). 

## HTTP Requests 
### Differences between two distributions
![HTTP Requests Distribution](http.png)

The plot above shows a great difference bwteeen the number of third-party HTTP requests in vanilla mode and ad-blocking mode. Specifically, for each website, the number of third-party HTTP requests made without ad-blocker is at least greater than that with ad-blocker.

#### Top 10 third-party domains with HTTP(S) requests

|     | Domain (vanilla)      | # Third-Party HTTP Requests (vanilla) |     | Domain (ad-blocking)       | # Third-Party HTTP Requests (ad-blocking) |
| --: | :-------------------- | -----------------: | --- | :-------------------- | ----------------: |
|   1 | ssl-images-amazon.com |                531 |     | ssl-images-amazon.com |               533 |
|   2 | sohu.com              |                333 |     | msocdn.com            |               255 |
|   3 | doubleclick.net       |                301 |     |csdnimg.cn             |               217 |
|   4 | alicdn.com            |                265 |     | cloudfront.net        |               203 |
|   5 | msocdn.com            |                255 |     | pstatic.net           |               198 |
|   6 | google.com            |                245 |     | alicdn.com            |               197 |
|   7 | csdnimg.cn            |                214 |     | pinimg.com            |               195 |
|   8 | pstatic.net           |                210 |     | sinaimg.cn            |               155 |
|   9 | cloudfront.net        |                208 |     | qhimg.com             |               154 |
|  10 | pinimg.com            |                200 |     | awsstatic.com         |               149 |


## Cookies
![Cookies Distribution](cookies.png)

## JavaScript
![JavaScript Distribution](js.png)
