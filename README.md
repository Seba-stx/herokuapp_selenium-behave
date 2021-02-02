This is a private project, I'm developing automation tests which can be run on page http://the-internet.herokuapp.com/

Run command:
For all tests:

behave -D driver=chrome -D base_url=http://localhost:3001/bp/login

For single feature file:

behave features/application_form.feature -D driver=chrome -D base_url=http://localhost:3001/bp/login

For single tag add:

--tags=@tag_name

For multiple tags add:

--tags=@tag_name1, @tag_name2

Exclude tag/s:

--tags ~@tag_name
