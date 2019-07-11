images := $(patsubst %.py,%.png,$(wildcard g*.py))
images := $(patsubst genI%,i%,${images})

images := $(patsubst image_25.png,,${images})


HELPER_DIR=../../code_example

all: ${images} image_100000_25.png image_100000000_25.png 

${images}: image%.png : genImage%.py 
	export PYTHONPATH="${HELPER_DIR}"  ; python3 $<

image_100000_25.png image_100000000_25.png : genImage_25.py 
	export PYTHONPATH="${HELPER_DIR}"  ; python3 $<

clean:
	rm -f *.png
