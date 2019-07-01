images := $(patsubst %.py,%.png,$(wildcard g*.py))
images := $(patsubst genI%,i%,${images})

# genImage_01.py doesn't follow the pattern - makes two images
images := $(patsubst image_01.png,,${images})

all: ${images} image_1000000_01.png

image_1000000_01.png image_100000000_01.png : genImage_01.py 
	python3 $<

${images}: image%.png : genImage%.py 
	python3 $<

clean:
	rm -rf *.png __pycache__
