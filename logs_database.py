#!/usr/bin/env python3
# 

import psycopg2

#Connects to the news database, runs the query, and returns the results
def run_query(query):
    db = psycopg2.connect('news')
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows


#Prints the top 3 most read articles
def top_three_articles():

    # fetches the query of the top three articles
    articles_query = """
        select articles.title, count(*) as num
        from articles, authors
        where articles.author = authors.id
        group by articles.title
        order by num desc
        limit 3;
    """

    results = run_query(articles_query)

    #Print Results
    print('Top three articles:')
    count = 1
    for row in results:
        number = '(' + str(count) + ') "'
        title = row[0]
        views = '" with ' + str(row[1]) + " views"
        print(number + title + views)
        count += 1


#Prints the three most popular authors
def top_three_authors():

    #fethces the query of most popular authors
    authors_query = """
        select authors.name, count(*) as num
        from authors
        join articles
        on authors.id = articles.author
        join log
        on log.path
        group by authors.name
        order by num DESC
        limit 3;
    """

    results = run_query(authors_query)

    #Print Results
    print('The three most popular authors:')
    count = 1
    for row in results:
        print('(' + str(count) + ') ' + row[0] + ' with ' + str(row[1]) + " views")
        count += 1


#Prints the days with more than 1% errors
def days_with_errors():

    #fetches the query of error days
    errors_query = "Select time, count(*) as num from log where status != '200 ok' order by time limit 3"

   
    results = run_query(errors_query)

    #Print Results
    print('days with more than 1% or requests that lead to errors')
    for row in results:
        print(str(row[0]) + ' ' + str(row[1] + '%')

top_three_authors()
top_three_articles()
days_with_errors()
