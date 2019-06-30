# IshiharaArt

Generates ishihara art from an image

**Technique**:

First we use k-means clustering to find dominant colours in the image - this forms our palette. Then the image matrix is decomposed randomly into a set of disjoint filling squares. Using our decomposition of the image, we fill the image with circles. For each circle we select the color which matches the region best from our palette.

**Future Ideas**:

Use entropy or perhaps contrast in specific regions of the image to determine radii of circles.
