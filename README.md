# makingwikiagain
Maybe I don't need to model everything in models.py before doing in in forms.py
Perhaps making a class/function/definition in forms.py will suffice
Our Page has to look like a form with a field for new title and content and ability to save (if Title is None)

Maybe I don't even need to put that class in forms.py only to import it later to views.py
Then again, I'm already importing util, another file.py doesn't matter

Leave crp for later 
# Making new data(POST Form)

# Where to start
Make index work first: url for entries.md hyperlinked
# Example in index.html
<a href="{% url 'tasks:index' %} 

# Don't forget about registered namespace
app_name = "tasks" in urls.py

# First bug (0st bug: previous for reserved namspace that wasn't found)
NoReverseMatch at /
Reverse for 'index' not found. 'index' is not a valid view function or pattern name.
            
# Example code from index.html
            return HttpResponseRedirect(reverse("tasks:index"))

# Step 3: work out indents so syntaxis typos become clear!
debugged (closed all "'s and }'s in >'s)

# Question time
1)
Why do I:
from django.urls import reverse
or 
from django.shortcuts import reverse
in views.py
On what does it depend?

2)
NoReverseMatch at /view/
Reverse for 'detail view' with no arguments not found. 1 pattern(s) tried: ['(?P<title>[^/]+)$']

3)
Is the difficulty a url with a space in between?

4) No. Even named app in url.py didn't resolve issue (and 'fix' of that to folder every url [supposedly but only in url searches not really?])
                    <a href="{% url 'encyclopedia:detail view' title %}">Detail View</a>
Reverse for 'detail view' with arguments '('',)' not found. 1 pattern(s) tried: ['(?P<title>[^/]+)$']


