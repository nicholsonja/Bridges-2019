// Basic example of curve stitiching density plot in processing 3.

// number of sample points
// bigger value means less noise in final image, but takes
// longer to run
final int NUM_SAMPLES = 10000000;

// k for theta
final float KA = 4;
final float KB = 5;

// background and foreground colors
final color BG = color(255, 255, 255);
final color FG = color(0, 0, 255);

// image to display
PImage img;

void setup() {
  size(600, 600);
  final int SIZE = min(width, height);

  // matrix for counts.  initialize all entries to 0
  int data[] = new int[SIZE * SIZE];
  for (int i = 0; i < data.length; i++) {
    data[i] = 0;
  }
  
  // center coordinates
  double cx = SIZE / 2.0;
  double cy = SIZE / 2.0;
  
  // drawing radius
  double radius = SIZE/2.0 * .95;
  
  // computes the coordinates of
  // all the sample points and map to
  // coordinates in the matrix
  for (int i = 0; i < NUM_SAMPLES; i++) {
    float theta = random(0, 2 * PI);
    
    // point A of line
    double aX = cos(KA * theta) * radius + cx;
    double aY = sin(KA * theta) * radius + cy;
    
    // point B of line
    double bX = cos(KB * theta) * radius + cx;
    double bY = sin(KB * theta) * radius + cy;
    
    // random point on line AB
    float r = random(0, 1);
    double cX = (1 - r) * aX + r * bX;
    double cY = (1 - r) * aY + r * bY;
    
    // map to matrix index
    int x = (int) (cX + .5);
    int y = (int) (cY + .5);
    data[y * SIZE + x] += 1;
  }
    
  // START TO COLOR PIXELS
  
  // find maxCount in matrix
  int maxCount = 0;
  for (int i = 0; i < data.length; i++) {
    if (data[i] > maxCount) {
      maxCount = data[i];
    }
  }
  
  // create the image for drawing
  img = createImage(SIZE, SIZE, RGB);
  img.loadPixels();
  
  // color each pixel
  // based on the ratio of maxCounts
  // Uses some magic values - 1..33 and 20 - to make the image visible and "nicer"
  color current;
  for (int x = 0; x < SIZE; x++) {
     for (int y = 0; y < SIZE; y++) {
       int count = data[y * SIZE + x];
       double alpha = min(count/(1.33 * maxCount) * 20, 1.0);
       
       if (count == 0) {
         current = BG;
       } else {
         // weight the pixel color based on the alpha value
         current = color(
              (int) (alpha * red(FG)   + (1 - alpha) * red(BG) + .5),
              (int) (alpha * green(FG) + (1 - alpha) * green(BG) + .5),
              (int) (alpha * blue(FG)  + (1 - alpha) * blue(BG) + .5)
           );
       }

       // update the pixel color
       img.pixels[y * SIZE + x] = current;
     }
  }
  
  // save the pixel colors
  img.updatePixels();
}

void draw() {
  // finally. draw the image
  image(img, 0, 0);
}
