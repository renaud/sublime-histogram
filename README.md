# Counting input frequency (simple histogram)

Sublime Text 3 package that adds a command for creating simple histograms, à la `sort | uniq -c | sort`


About
-----

One of the most common data analysis things I do in Unix is something like

    cat wines | sort | uniq -c | sort -nr

Given an input file with a million bottles of wine in it, this shows me how many bottles of each type I have. It works for other things besides wine. In fact, it works for a lot of things. 


Usage
-----

Just run “Create Histogram” from the Command Palette, or from the Edit menu, which has a keyboard shortcut as well.


Credits
-------

@nelson (http://www.somebits.com/weblog/tech/python/countuniq.html)
