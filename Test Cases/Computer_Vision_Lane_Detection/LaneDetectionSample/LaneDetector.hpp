//
//  LaneDetector.hpp
//  LaneDetectionSample
//
//  Created by Kenneth Chen on 8/6/20.
//

#ifndef LaneDetector_hpp
#define LaneDetector_hpp
#include <stdio.h>
#endif /* LaneDetector_hpp */
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

class LaneDetector {
    
public:
    
    /*
     Returns image with lane overlay
     */
    Mat detect_lane(Mat image);
    
private:
    
    /*
     Filters yellow and white colors on image
     */
    Mat filter_only_yellow_white(Mat image);
    
    /*
     Crops region where lane is most likely to be.
     Maintains image original size with the rest of the image blackened out.
     */
    Mat crop_region_of_interest(Mat image);
    
    /*
     Draws road lane on top image
     */
    Mat draw_lines(Mat image, vector<Vec4i> lines);
    
    /*
     Detects road lanes edges
     */
    Mat detect_edges(Mat image);
};
