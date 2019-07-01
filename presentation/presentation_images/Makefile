images := $(patsubst %.py,%.png,$(wildcard g*.py))
images := $(patsubst genI%,i%,${images})

all: ${images}

${images}: image%.png : genImage%.py 
	/opt/local/bin/python3.7 $<
clean:
	rm -f *.png
