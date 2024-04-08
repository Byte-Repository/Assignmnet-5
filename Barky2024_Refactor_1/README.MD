# Barky Refactor 1

Barky is inspired by Dane Hillard's (https://github.com/daneah/practices-of-the-python-pro) Bark example of an application that demonstrates some basic software engineering principles such as:

Let's look at the elements in this list more carefully to guide what we'll do in this firs refactor:

* Abstraction - The ability to design for extension by separating the generic from the concrete.
* Extensibility - The ability to design for future expansion or redefinition
* Inheritance - The ability for code to evolve through extension and obscuration
* Loose Coupling and Cohesion - Code belongs together without inhibiting the ability for that code to independently evolve.
* Refactoring - Changing/Improving code structure without changing code function.
* Separation of concerns - Organizing code around broad or categorical focus.

This repository is an extension of Dane's example to also include testing.  This is all inspired by Dane's [Practices fo the Python Pro](https://www.manning.com/books/practices-of-the-python-pro) book, which I have found to be a great read.

# Layered Architecture

At a basic level, the architecture is designed with a layered strategy to include the following common/typical elements:

* **Presentation Layer** (will be a module called barky.py here)
* **Business Logic Layer** (will be a module called commands.py here)
* **Presistence Layer** (will be a module called database.py here)

We'll implement this layered archicture alongside and within the provisions of Django.

# Leveraging the Django ORM

## Persistence
If we use the Django ORM then our task is to create a model to represent the table rather than raw SQL.

So, whereas we utilize a table in the database called `bookmarks`:

``` sql
CREATE TABLE IF NOT EXISTS bookmarks
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    notes TEXT,
    date_added TEXT NOT NULL
);
```

We also create a Django model class that mirrors the SQL Schema:

```python
class Bookmark(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    url = models.URLField()
    notes = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

```

## Django REST Framework

[Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)

For comparitive convenience, I will merge the **snippets** project with Barky for the refactor.

## Barky Refactoring Roadmap
Dane Hillard's code focused on a command-line interface, but we will systematically refactor that code, across a series of branches, to do the following:

1. Replace the custom data handling (the DatabaseManager module) with the [Django O/RM](https://docs.djangoproject.com/en/5.0/topics/db/queries/)
    1. Replace the existing DatabaseManager with the Django ORM.
    2. Replace the CLI web-based REST API using the Django REST Framework.
    3. SOLID
    4. Use [DRF's testing facilities](https://www.django-rest-framework.org/api-guide/testing/#api-test-cases)
2. Adopt the suggestions from Percival and Gregory regarding the Unit of Work and Respository Pattern and Django: [Appendix D: Repository and Unit of Work Patterns with Django](https://www.cosmicpython.com/book/appendix_django.html)
    1. Add a separate Domain Model and explore the pros and cons of this: [Appendix D: Repository and Unit of Work Patterns with Django](https://www.cosmicpython.com/book/appendix_django.html)
3. Introduce messaging using Celery with Django.  This will serve as a message bus to augment event-driven architecture.
    1. [Django is well supported using Celery](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html) as an asynchronous message/task queue.
    2. Reintroduce the [Command pattern](https://refactoring.guru/design-patterns/command) as a means to encapsule the transactional intent of messages passed within Celery.
4. Improve architecture:
    1. [CQRS in general](https://douwevandermeij.medium.com/the-repository-pattern-via-cqrs-with-python-django-elasticsearch-cb38437721d3) and in [Django](https://django-cqrs.readthedocs.io/en/latest/)
    2. Dependency injection - [A good overview](https://thinhdanggroup.github.io/python-dependency-injection/), [DI with specific Flask and Django examples](https://snyk.io/blog/dependency-injection-python/), and a [Comprehensive Python Dependency Injection Framework](https://python-dependency-injector.ets-labs.org/)



## Refactor to Assignments Map

1. Refactor 1 (DRF, ORM, and Repository Pattern): Assignment 5 
2. Refactor 2 (UoW): Assignment 6
3. Refactor 3 (Celery/Messages and the Return of the Command): Assignment 7
4. Refactor 4 (CQRS and DI/Bootstrapping): Assignment 8

## Refactoring Notes relative to APP

1. The [Command](https://refactoring.guru/design-patterns/command) pattern and Barky: Whereas Barky uses the `Command` design pattern, the Django Rest Framework's [ViewSet](https://www.django-rest-framework.org/api-guide/viewsets/) structure as a controller in the [Model View Controller](https://www.askpython.com/django/django-mvt-architecture) sense.  As such, the objective of the Command pattern - to achieve a separation of concerns such that all pathways to effect a state change in the application use the same facility - is achieved with the ViewSet acting as a controller.  A Django app's views module works with DRF's ViewSet to handle the same thing.  As such, we no longer require the Command module from Barky.
