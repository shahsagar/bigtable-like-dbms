# modify the paths appropriately
# JDKPATH = /usr/lib/jvm/jdk-11.0.6
# LIBPATH=/home/rickchung/Documents/CSE510_DBMSI/Assign1/minjava/javaminibase/construction:.:..

CLASSPATH = $(LIBPATH)
BINPATH = $(JDKPATH)/bin
# These classpaths have to include their parent folder. Otherwise Java cannot find the src code
JAVAC = $(JDKPATH)/bin/javac -classpath $(CLASSPATH):..
JAVA  = $(JDKPATH)/bin/java  -classpath $(CLASSPATH):..

# test buffer manager

BMTest:BMTest.java
	$(JAVAC) TestDriver.java BMTest.java

bmtest: BMTest
	$(JAVA) tests.BMTest

# test disk manager

DBTest:DBTest.java
	$(JAVAC) TestDriver.java DBTest.java

dbtest: DBTest
	$(JAVA) tests.DBTest

# test heapfile 

HFTest:HFTest.java
	$(JAVAC) TestDriver.java HFTest.java

hftest: HFTest
	$(JAVA) tests.HFTest

# test btree

BTTest:BTTest.java
	$(JAVAC) TestDriver.java BTTest.java

bttest: BTTest
	$(JAVA) tests.BTTest

# test index

IndexTest:IndexTest.java
	$(JAVAC) TestDriver.java IndexTest.java

indextest: IndexTest
	$(JAVA) tests.IndexTest

# test join

JoinTest:JoinTest.java
	$(JAVAC) TestDriver.java JoinTest.java

jointest: JoinTest
	$(JAVA) tests.JoinTest

# test sort

SortTest:SortTest.java
	$(JAVAC) TestDriver.java SortTest.java

sorttest: SortTest
	$(JAVA) tests.SortTest

# test sortMerge

SMJoin:SM_JoinTest.java
	$(JAVAC) SM_JoinTest.java TestDriver.java

sortmerge: SMJoin
	$(JAVA) tests.SM_JoinTest




