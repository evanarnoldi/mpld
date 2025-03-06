---
description: The materials used for this project.
icon: table
---

# Datasets

## Harry Potter and the Prisoner of Azkaban

“**Harry Potter and the Prisoner of Azkaban**”, which is the third novel in the series of “**Harry Potter**”, is used for this project. To scrape the necessary data, clean text of the book is obtained here:

{% file src="../.gitbook/assets/Harry Potter and the Prisoner of Azkaban Chapter 1-9.txt" %}
Chapters pre-introduction of Marauder's Map
{% endfile %}

{% file src="../.gitbook/assets/Harry Potter and the Prisoner of Azkaban Chapter 10-22.txt" %}
Chapters post-introduction of Marauder's Map
{% endfile %}

The book is divided into two section for data scraping since the Marauder's Map is introduced right at the end of **Chapter 9**, and the beginning of **Chapter 10**.

## Characters

To scrape the occurrences of character’s appearances in the novel, the first names of the characters are identified as the author uses the character’s first name both in dialogues, actions, descriptions, and expositions in the novel. The names that would be parsed would be:

| Harry’s Hogwarts Friends |  The Marauders  |
| :----------------------: | :-------------: |
|        Dean Thomas       |   James Potter  |
|       Fred Weasley       | Peter Pettigrew |
|      George Weasley      |   Remus Lupin   |
|    Neville Longbottom    |   Sirius Black  |
|      Seamus Finnigan     |                 |

The core characters of the novel that appear in Harry’s closest circle of network including Ron Weasley, Hermione Granger, Hagrid, and Professor Dumbledore is excluded due to the fact that they are ever present throughout the novel and can be inferred to exist in both chapters of the novel, potentially muddling the curated dataset to identify the phenomenon which is being researched in this project.

The datasets are gathered by searching for the presence of the mentioned characters in a mise-en-scène, dialogues, and expositions, denoting the frequency and the degree of their closeness when appearing together in the abovementioned criteria.
