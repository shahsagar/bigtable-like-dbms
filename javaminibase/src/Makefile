#This Makefile is used to create assignments.

#the following macros should be updated according to
#the assignment to be generated

JARFILES=bufmgr/*.class diskmgr/*.class global/*.class iterator/*.class\
         heap/*.class chainexception/*.class btree/*.class index/*.class tests/*.class


# ========== Modify the following path variables according to your environment ==========

UNAME_S := $(shell uname -s)

ifeq ($(UNAME_S), Linux)
# Linux

# These paths are also used by other Makefiles in subfolders
# Note: You also have to change paths in the tests/Makefile.
# Note: You don't have to change paths in the other Makefiles since I've removed variables there.
export JDKPATH=/usr/lib/jvm/jdk-11.0.6
export LIBPATH=/home/rickchung/Documents/CSE510_DBMSI/minjava/javaminibase/src
ASSIGN=$(LIBPATH)

# Doclet paths for Javadoc
DOCLETPATH=/home/rickchung/.m2/repository/nl/talsmasoftware/umldoclet/2.0.7/umldoclet-2.0.7.jar

endif

ifeq ($(UNAME_S), Darwin)
# macOS

export JDKPATH=/Users/rickchung/Projects/jdk-11.0.6.jdk/Contents/Home
export LIBPATH=/Users/rickchung/Projects/cse510-project-sp20/javaminibase
ASSIGN=$(LIBPATH)
DOCLETPATH=/Users/rickchung/.m2/repository/nl/talsmasoftware/umldoclet/2.0.7/umldoclet-2.0.7.jar

endif

# ========== Modify the above path variables according to your environment ==========


# Java class path and bin paths
CLASSPATH=$(LIBPATH)
BINPATH=$(JDKPATH)/bin
JAVAC=$(JDKPATH)/bin/javac -classpath $(CLASSPATH)
JAVA=$(JDKPATH)/bin/java  -classpath $(CLASSPATH)

# lib and src paths
LIBDIR=$(ASSIGN)/lib
KEY=$(ASSIGN)/key
SRC=$(ASSIGN)/src

# Javadoc resources
IMAGELINK=$(PACKAGEINDEX)/images
PACKAGEINDEX=$(ASSIGN)/javadoc
# Javadoc input
DOCLETARGS=-docletpath $(DOCLETPATH) -doclet nl.talsmasoftware.umldoclet.UMLDoclet -umlImageDirectory umldiagrams -umlImageFormat svg
DOCFILES=bufmgr diskmgr global chainexception heap btree iterator index
# Javadoc command
JAVADOC=$(BINPATH)/javadoc -public -d $(PACKAGEINDEX)

### Generate jar and javadoc files.  Apply to most assignments.
db: 
	make -C global
	make -C chainexception
	make -C btree
	make -C bufmgr
	make -C diskmgr
	make -C heap
	make -C index
	make -C iterator
	
doc:
	# Generate javadoc with class diagrams
	$(JAVADOC) $(DOCFILES) $(DOCLETARGS)

test: 
	cd tests; make bmtest dbtest; whoami; make hftest bttest indextest jointest sorttest sortmerge

clean:
	rm -f $(CLASSPATH)/*.class $(JARFILES)

