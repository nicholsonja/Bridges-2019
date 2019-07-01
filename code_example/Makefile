images := $(patsubst %.py,%.png,$(wildcard g*.py))
images := $(patsubst genI%,i%,${images})

all: ${images}

${images}: image%.png : genImage%.py 
	python3 $<

clean:
	rm -rf *.png __pycache__
