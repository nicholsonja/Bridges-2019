images := $(patsubst %.py,%.png,$(wildcard g*.py))
images := $(patsubst genI%,i%,${images})

HELPER_DIR=../../code_example

all: ${images}

${images}: image%.png : genImage%.py 
	export PYTHONPATH="${HELPER_DIR}"  ; python3 $<
clean:
	rm -f *.png
