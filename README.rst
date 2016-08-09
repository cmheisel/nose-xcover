nose-xmlcover
--------------

A companion to the built-in nose.plugins.cover, this plugin will write out an XML coverage report to a file named coverage.xml.

It will honor all the options you pass to the `Nose coverage plugin <http://somethingaboutorange.com/mrl/projects/nose/1.0.0/plugins/cover.html>`_, especially --cover-package.

Usage
------
You can not use both --with-xcoverage and --with-coverage.  Using --with-xcover implies --with-coverage

If you want to change the name of the output file you can use --xcoverage-file=FILE (--cover-xml-file from coverage won't work)

As of nose-xcover 1.0.6 --with-xcoverage provides all the functionality of the built-in coverage plugin in addition to Cobertura-style output::

    #nosetests --with-xcoverage {{ coverage options }}
    nosetests --with-xcoverage --cover-package=myapp --cover-tests



