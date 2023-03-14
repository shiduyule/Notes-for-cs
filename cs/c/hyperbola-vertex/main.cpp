#include <opencv2/opencv.hpp>
#include <iostream>
#include <cmath>

using namespace cv;
using namespace std;

int main(int argc, char** argv)
{
    // 读取图像
    Mat image = imread(argv[1]);

    // 将图像转换为灰度图像
    Mat gray;
    cvtColor(image, gray, COLOR_BGR2GRAY);

    // 对灰度图像进行二值化处理
    Mat binary;
    threshold(gray, binary, 0, 255, THRESH_BINARY_INV | THRESH_OTSU);

    // 对二值化图像进行边缘检测
    Mat edges;
    Canny(binary, edges, 50, 150, 3);

    // 对边缘图像进行霍夫变换
    vector<Vec2f> lines;
    HoughLines(edges, lines, 1, CV_PI / 180, 100);

    // 选择符合条件的线段
    Vec2f line;
    for (size_t i = 0; i < lines.size(); i++) {
        float rho = lines[i][0];
        float theta = lines[i][1];
        if (theta < CV_PI / 4 || theta > 3 * CV_PI / 4) {
            line = lines[i];
            break;
        }
    }

    // 计算线段的两个端点
    double a = cos(line[1]);
    double b = sin(line[1]);
    double x0 = a * line[0];
    double y0 = b * line[0];
    Point2d p1(x0 + 1000 * (-b), y0 + 1000 * a);
    Point2d p2(x0 - 1000 * (-b), y0 - 1000 * a);

    // 计算线段两端点之间的距离
    double distance = sqrt(pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2));
    cout << "Distance between two endpoints of the hyperbola: " << distance << endl;

    return 0;
}
