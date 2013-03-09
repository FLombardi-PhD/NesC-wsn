COMPONENT=FloodingAppC
BUILD_EXTRA_DEPS = Flooding.py

Flooding.py: Flooding.h
	mig python -target=$(PLATFORM) $(CFLAGS) -python-classname=Flooding Flooding.h radio_count_msg -o $@

#RadioCountMsg.class: RadioCountMsg.java
#	javac RadioCountMsg.java

#RadioCountMsg.java: RadioCountToLeds.h
#	mig java -target=$(PLATFORM) $(CFLAGS) -java-classname=RadioCountMsg RadioCountToLeds.h radio_count_msg -o $@


include $(MAKERULES)

