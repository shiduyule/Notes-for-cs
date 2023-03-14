#include <opencv2/opencv.hpp>
#include <iostream>
#include <cmath>

using namespace cv;
using namespace std;

int main(int argc, char** argv)
{
    // ��ȡͼ��
    Mat image = imread(argv[1]);

    // ��ͼ��ת��Ϊ�Ҷ�ͼ��
    Mat gray;
    cvtColor(image, gray, COLOR_BGR2GRAY);

    // �ԻҶ�ͼ����ж�ֵ������
    Mat binary;
    threshold(gray, binary, 0, 255, THRESH_BINARY_INV | THRESH_OTSU);

    // �Զ�ֵ��ͼ����б�Ե���
    Mat edges;
    Canny(binary, edges, 50, 150, 3);

    // �Ա�Եͼ����л���任
    vector<Vec2f> lines;
    HoughLines(edges, lines, 1, CV_PI / 180, 100);

    // ѡ������������߶�
    Vec2f line;
    for (size_t i = 0; i < lines.size(); i++) {
        float rho = lines[i][0];
        float theta = lines[i][1];
        if (theta < CV_PI / 4 || theta > 3 * CV_PI / 4) {
            line = lines[i];
            break;
        }
    }

    // �����߶ε������˵�
    double a = cos(line[1]);
    double b = sin(line[1]);
    double x0 = a * line[0];
    double y0 = b * line[0];
    Point2d p1(x0 + 1000 * (-b), y0 + 1000 * a);
    Point2d p2(x0 - 1000 * (-b), y0 - 1000 * a);

    // �����߶����˵�֮��ľ���
    double distance = sqrt(pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2));
    cout << "Distance between two endpoints of the hyperbola: " << distance << endl;

    return 0;
}
