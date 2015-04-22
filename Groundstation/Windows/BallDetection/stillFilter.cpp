#include "opencv2/highgui/highgui.hpp"
#include <iostream>
#include "opencv2\imgproc\imgproc.hpp"

using namespace cv;
using namespace std;

double alpha; /**< Simple contrast control */
int beta;  /**< Simple brightness control */

int main(int argc, const char** argv)
{
	Mat img = imread("C:/Users/Tyler/Desktop/Capture.JPG", CV_LOAD_IMAGE_UNCHANGED); //read the image data in the file "MyPic.JPG" and store it in 'img'
	Mat new_image = Mat::zeros(img.size(), img.type());

	if (img.empty() | new_image.empty()) //check whether the image is loaded or not
	{
		cout << "Error : Image cannot be loaded..!!" << endl;
		system("pause"); //wait for a key press
		return -1;
	}

	threshold(img, new_image, 200, 255, THRESH_BINARY);
	imwrite("C:/Users/Tyler/Desktop/Capture_NEW.JPG", new_image);

	/// Create Windows
	namedWindow("Original Image", 1);
	namedWindow("New Image", 1);

	/// Show stuff
	imshow("Original Image", img);
	imshow("New Image", new_image);

	/// Wait until user press some key
	waitKey();
	return 0;
}