<p align="center">
<img align="center" width="508" height="102" src='https://github.com/Chitrang-Bhoir/Linegorithm/blob/main/logo.png'>
</p>

---
A tool to simulate line, circle and ellipse drawing algorithms namely Digital Differential Analyzer Algorithm and Bresenham's Line Algorithm, midpoint circle algorithm and midpoint ellipse algorithm.

>**12-01-2022** I am writing this readme.md file, because my lecture just got cancelled and at the same time my mobile got discharged.:no_mouth:<br/>
>**20-01-2022** Our teacher asked us to create the same app as our course project and I found myself lucky as it was already partially implemented as Linegorithm.:smile: Now renaming it as Graphixo after adding circle and ellipse drawing algorithms.

## Usage
1. Clone the repository using... 
    ```shell
    git clone https://github.com/Chitrang-Bhoir/Graphixo.git
    ```
   or download and extract the zip folder from [here](https://github.com/Chitrang-Bhoir/Graphixo/archive/refs/heads/main.zip).
2. Install required library `PyQt5` using...
    ```shell
    pip install PyQt5
    ```
3. Open `main.py` in the folder.
4. Click on the algorithm(`DDA`, `BLA`, `Circle` or `Ellipse`) you want to simulate or press `D`, `B`, `C` or `E` key on keyboard respectively for each algorithm.
5. Different scenarios :
    * For drawing line using DDA or BLA, select 2 distinct points.
    * For drawing circle, firstly select centre point and then a point in the same column to denote radius.
    * For drawing ellipse, firstly select centre point. Then select a point in the same column to denote radius in y direction and then a point in the same row as that of the centre to denote radius in x direction.
7. `START` button will get enabled. Click on that or press `ENTER`. If you want to play the simulation automatically, press `SPACE` bar.
8. The simulation will start. Keep clicking `NEXT` or press `ENTER`(no need if playing automated simulation) and watch how the algorithm works. You can also view the parameters in the bottom-centre label. Also you can view the number pixels remaining to be highlighted in bottom of the window while algorithm is running. If pixels are too many, you can opt for simulation instead of manual operation. While playing simulation, you can adjust the speed by changing time interval for each iteration by sliding the handle of the slider in bottom.
9. Once the shape is completed(is in orange colour). You can clear the grid by clicking `CLEAR` or pressing `ENTER` to try new shapes.
10. If you want to close the application, click :x: or press `Q` key on keyboard.

## Shortcut Cheatsheet
|Shortcut|Task|
|--|--|
|B|Select Bresenham's Line Algorithm|
|D|Select Digital Differential Analyzer|
|C|Select Midpoint Circle Algorithm|
|E|Select Midpoint Ellipse Algorithm|
|Enter|START/NEXT/CLEAR|
|Space|Play simulation|
|Q|Close window|

## Screenshots
<p align="center">
<img align="center" width="683" height="364" src='https://github.com/Chitrang-Bhoir/Graphixo/blob/main/ss/base.png'>
</p>
<p align="center">
<img align="center" width="683" height="364" src='https://github.com/Chitrang-Bhoir/Graphixo/blob/main/ss/line.png'>
</p>
<p align="center">
<img align="center" width="683" height="364" src='https://github.com/Chitrang-Bhoir/Graphixo/blob/main/ss/circle.png'>
</p>
<p align="center">
<img align="center" width="683" height="364" src='https://github.com/Chitrang-Bhoir/Graphixo/blob/main/ss/ellipse.png'>
</p>

## References
<details>
  <summary>Wikipedia</summary>
    ⦿ https://en.wikipedia.org/wiki/Line_drawing_algorithm<br/>
    ⦿ https://en.wikipedia.org/wiki/Digital_differential_analyzer_(graphics_algorithm)<br/>
    ⦿ https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
</details>
<details>
  <summary>GeeksforGeeks</summary>
    ⦿ https://www.geeksforgeeks.org/mid-point-circle-drawing-algorithm/<br/>
    ⦿ https://www.geeksforgeeks.org/midpoint-ellipse-drawing-algorithm/
</details>

---
[![visitors](https://visitor-badge.glitch.me/badge?page_id=chitrang-bhoir.linegorithm&left_color=black&right_color=limegreen)](https://github.com/Chitrang-Bhoir/Graphixo/)
<a href="https://github.com/Chitrang-Bhoir" alt="https://github.com/Chitrang-Bhoir"><img align="right" src="https://img.shields.io/static/v1?style=for-the-badge&label=CREATED%20BY&message=CHITRANG&color=0ad37"></a>
