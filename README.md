# Search
Python app using Django framework that exposes a single endpoint: HTTP service that provides an endpoint for fuzzy search / autocomplete of English words.
You are given a dataset that contains 333,333 English words and the frequency of their usage in
some corpus. A very small sample is shown below:

	track 112385243
	australia 112197265
	discussion 111973466
	archive 111971865
	once 111882023
	others 111397714
	entertainment 111394818
	agreement 111356320
	format 111279626
Let us assume we’re building a web app where the user types in a single word from this list in a
search box. We wish to autocomplete the input in the search box.
Your objective is to write a Python app using Django/Flask framework that exposes a single
endpoint:

GET /search?word=<input>

where input is the (partial) word that the user has typed so far. For example, if the user is looking
up procrastination, the service might receive this sequence of requests:

GET /search?word=pro
GET /search?word=procr
GET /search?word=procra

and so on.

The response should be a JSON array containing upto 25 results, ranked by some criteria (see
below).
Constraints

1. Matches can occur anywhere in the string, not just at the beginning. For example, eryx
should match archaeopteryx (among others).
2. The ranking of results should satisfy the following:
a. We assume that the user is typing the beginning of the word. Thus, matches at the
start of a word should be ranked higher. For example, for the input pract, the result
practical should be ranked higher than impractical.
b. Common words (those with a higher usage count) should rank higher than rare
words.
c. Short words should rank higher than long words. For example, given the input
environ, the result environment should rank higher than environmentalism.
i. As a corollary to the above, an exact match should always be ranked as the
first result.

## Project Development:

We have developed this project using python [Django](https://docs.djangoproject.com/en/2.2/framework) framework.
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

See Project source code [source](https://github.com/shailendrasingh98/Search_Page).

## Deployment:

We have used a [Heroku](https://devcenter.heroku.com/categories/python-support). Heroku makes it easy to deploy and scale Python apps. Whether you prefer frameworks like Django or Flask, or getting your hands dirty with Twisted or raw sockets, Heroku helps you build things your way with the tools you love.

[click here to open app](https://shailu-search-app.herokuapp.com/).

## Instructions:
* Open App [click here](https://shailu-search-app.herokuapp.com/).
* You would see page as below.

![search_page](https://github.com/shailendrasingh98/Search_Page/blob/master/images/search_page.PNG)

* When you start entering word in search box, dropdown will show matching words.

![search](https://github.com/shailendrasingh98/Search_Page/blob/master/images/word_search.PNG)

* if you click search for any word or incomplete word, it will show a json message containing matching words up to 25.

![search_result](https://github.com/shailendrasingh98/Search_Page/blob/master/images/search_result.PNG)

