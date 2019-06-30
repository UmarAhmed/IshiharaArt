# IshiharaArt

Generates ishihara art from an image

First we use k-means clustering to find dominant colours in the image - this forms our palette.

Then the image matrix is decomposed randomly into a set of disjoint filling squares.

Using our decomposition of the image, we fill the image with circles. 

For each circle we select the color which matches the region best from our palette.



Example:




![sample input](https://scontent-yyz1-1.xx.fbcdn.net/v/t1.15752-9/60861700_528182514255063_1300303784110456832_n.jpg?_nc_cat=101&_nc_oc=AQm5YVFw8828-SWLcB-119jdmHOsPSchcYF7ZUmKQhFI75WuNtRL6nFVvIL7H_5LkEI&_nc_ht=scontent-yyz1-1.xx&oh=488b36e2227e49eef0f31f80c674a4ec&oe=5DBDADA8)

Future Ideas:

Use entropy in specific regions of the image to determine radii of circles.
