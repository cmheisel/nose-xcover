# nose-xmlcover

A companion to the built-in nose.plugins.cover, this plugin will write out an XML coverage report to a file named coverage.xml.

It will honor all the options you pass to the "Nose coverage plugin":http://somethingaboutorange.com/mrl/projects/nose/0.11.1/plugins/cover.html, especially --cover-package.

## Usage
    #nosetests --with-xcoverage {{ coverage options }}
    nosetests --with-xcoverage --cover-package=myapp --cover-tests


## Note

Due to changes in the nose coverage plugin you *cannot* run with *both* --with-xcoverage and --with-coverage.

As of nose-xcover 1.0.6 --with-xcoverage provides all the functionality of the built-in coverage plugin in addition to Cobertura-style output.