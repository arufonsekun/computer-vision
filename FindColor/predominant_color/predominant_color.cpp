//g++ predominant_color.cpp `pkg-config --cflags --libs opencv` -std=c++11
#include <stdint.h>
#include <iostream>
#include <stdio.h>
#include <vector>
#include "opencv2/imgproc.hpp"
#include <opencv2/highgui.hpp>
#include <opencv2/core.hpp>
#include <array>
#include <string>
#include <fstream>
using namespace std;

vector<unsigned short int> frequency;
vector<unsigned int> indexes;

void countPixels(cv::Mat matrix){

  frequency.push_back(cv::countNonZero(matrix));

  //get the index of the color
  unsigned int j = 0;
  for (unsigned int i = 0; i < matrix.rows;){
      //add 0 if the hsv range is not find
      if (i == matrix.rows -1){
        indexes.push_back(0);
        indexes.push_back(0);
        break;
      }

      if (matrix.at<uint8_t>(i,j) != 0){
        //cout <<matrix.at<uint8_t>(i,j);
        indexes.push_back(i);
        indexes.push_back(j);
        break;
      }

      j++;
      if (j == matrix.cols){
        j = 0;
        i++;
      }
  }

}

//Write in the file
void write(){
  ofstream outPutFile;
  outPutFile.open("output.txt");
  for(int e = 0; e < frequency.size(); e++){
    outPutFile << frequency[e] << endl;
  }
  outPutFile.close();
}

int main(int argc, char** argv){
  //Don't need this
  int rgbColors[11][3] = { {255,0,0}, {255, 125, 0}, {255, 255, 0},
                   {0, 255, 0}, {0, 255, 255}, {0, 0, 255},
                   {128, 0, 128}, {255, 0, 255}, {0,0,0},
                   {125, 125, 125}, {255,255,255} };

  string path = "Images/";
  path.append(argv[1]);
  cv::Mat input = cv::imread(path);
  cv::Mat hsv_img;
  cv::cvtColor(input, hsv_img, cv::COLOR_BGR2HSV);

  cv::Mat countColors;
  //HSV ranges,red,orange,yellow,green,ciano,blue,deepPurple,magenta,black,gray,white, respectively
  unsigned short int lowHSV[11][3] = { {0,100,100},{8,100,100},{23,100,100},{36,100,
                        100},{81,100,100},{93,100,100},{131,100,100},
                        {144,100,100},{0,0,0},{0,0,31},{0,0,234} };

   unsigned short int highHSV[11][3] = {{7,255,255},{22,255,255},{35,255,255},
                          {80,255,255},{92,255,255},{130,255,255},
                          {143,255,255},{170,255,255},{180,30,30},
                          {180,30,233},{180,15,255}};
  //16 bits integer
  unsigned short int index = 0;
  unsigned short int biggest = 0;

  //the magic
  for(unsigned int i = 0; i <= 10; i++){
    cv::inRange(hsv_img, cv::Scalar(lowHSV[i][0], lowHSV[i][1], lowHSV[i][2]),
    cv::Scalar(highHSV[i][0], highHSV[i][1], highHSV[i][2]), countColors);
    countPixels(countColors);

    //gets the biggest value
    if (frequency.back() > biggest){
      biggest = frequency.back();
      index = i;
    }
  }

  //thanks stackoverflow
  int b = input.at<cv::Vec3b>(indexes[index*2],indexes[index*2+1])[0];
  int g = input.at<cv::Vec3b>(indexes[index*2],indexes[index*2+1])[1];
  int r = input.at<cv::Vec3b>(indexes[index*2],indexes[index*2+1])[2];

  write();

  cv::Mat color;
  color = cv::Mat::zeros(cv::Size(200,200), CV_8UC4);
  cv::rectangle(color, cv::Point(0,0), cv::Point(200,200), cv::Scalar(b,g,r), -1);
  cv::imshow("Color", color);
  cv::imshow("Image", input);
  cv::waitKey(0);

  return 0;
}
