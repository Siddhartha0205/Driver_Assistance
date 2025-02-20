
<h1>Lane Detection</h1>

<p>This Issue aims to detect lanes of the road. </p>

<p>The simulation is carried out using an Image. </p>

<h2>Concepts involved</h2>

<h3>Edge Detection </h3>

<h3>Hough Transform </h3>


<h2>Results</h2>

<p>The below figures show that the model detected the location of the human face successfully and added a rectangle around the human face</p>

<p float="left">
  <img src="Dataset/51_Dresses_wearingdress_51_741_jpg.rf.9a7622017e5f79023ce1a8f256dcebc3.jpg" width="100" />
  <img src="Output/51_Dresses_wearingdress_51_741_jpg.rf.9a7622017e5f79023ce1a8f256dcebc3.jpg" width="100" /> 
</p>

<p float="left">
  <img src="Dataset/img_41_jpg.rf.ce77cacb4290c4ddc06e893f8da35b92.jpg" width="100" />
  <img src="Output/img_41_jpg.rf.ce77cacb4290c4ddc06e893f8da35b92.jpg" width="100" /> 
</p>

<p float="left">
  <img src="Dataset/40_Gymnastics_Gymnastics_40_869_jpg.rf.b2f1cfd8424ea811106fcd8bb347ac4f.jpg" width="100" />
  <img src="Output/40_Gymnastics_Gymnastics_40_869_jpg.rf.b2f1cfd8424ea811106fcd8bb347ac4f.jpg" width="100" /> 
</p>

<p>However, the model's accuracy could be affected by many other factors. In the below comparison, the model could predict only one human face despite the image containing two human faces.</p>

<p float="left">
  <img src="Dataset/0_Parade_marchingband_1_353_jpg.rf.02aabbd7a6ff54e4b558dca3ed51d06f.jpg" width="100" />
  <img src="Output/0_Parade_marchingband_1_353_jpg.rf.02aabbd7a6ff54e4b558dca3ed51d06f.jpg" width="100" /> 
</p>

<p><i>Note: The comparison for other images is left for self-analysis</i></p>

<h2>Limitations</h2>

<ul>
  
<li>Despite being lightweight and real-time efficient, this model is highly susceptible to extreme contrast conditions.</li>

<li>It is limited to the detection of only frontal faces.</li>

<li>This algorithm is associated with a high false positive rate.</li>

</ul>

<h2>References</h2>

<ol>
  
<li>Viola, P., Jones, M.J. Robust Real-Time Face Detection. International Journal of Computer Vision 57, 137–154 (2004). https://doi.org/10.1023/B:VISI.0000013087.49260.fb</li>

<li>“Face detection Object Detection Dataset (v1, FDDB) by FDDB,” Roboflow. https://universe.roboflow.com/fddb/face-detection-40nq0/dataset/1</li>

</ol>
