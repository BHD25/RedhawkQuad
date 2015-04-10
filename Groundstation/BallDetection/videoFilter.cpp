#include "opencv2\highgui\highgui.hpp"
#include <iostream>
#include "opencv2\imgproc\imgproc.hpp"

using namespace cv;
using namespace std;

//Threshold for canny
int thresh = 100;
RNG rng(12345);

int main(int argc, const char** argv)
{
	// open the image file for reading
	Mat image = imread("D:/Nick/Pictures/test.jpg", CV_LOAD_IMAGE_COLOR); 
	Mat gray;
	// if not success, exit program
	if (!image.data)
	{
		cout << "Cannot open the image file" << endl;
		system("pause"); //wait for a key press
		return -1;
	}
	cvtColor(image, gray, CV_BGR2GRAY);

	Mat drawing;
	Mat rgb[3];
	split(image, rgb);
	rgb[1] -= .5*(rgb[0] + rgb[2]);
	GaussianBlur(rgb[1], drawing, Size(9, 9), 2, 2);

	namedWindow("Display window", WINDOW_AUTOSIZE);// Create a window for display.
	imshow("Display window", drawing);                   // Show our image inside it.
	waitKey(0);                                          // Wait for a keystroke in the window

	vector<Vec3f> circles;
	HoughCircles(drawing, circles, CV_HOUGH_GRADIENT, 2, rgb[1].rows / 4, 200, 100);
	for (size_t i = 0; i < circles.size(); i++)
	{
		Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
		int radius = cvRound(circles[i][2]);
		cout << center << " " << radius << endl;
	}

	waitKey(0);                                          // Wait for a keystroke in the window

	return 0;
}