# Drowsiness Detection

This is a Flask API that detects faces in an image using the dlib library and returns 68 facial points as a response.

## Installation

Note
- It is suggested to create a virtual environment cause we use lower versions of Python to use dlib library.
- The dlib file used in the project is a wheel supported for windows OS. If you use Linux distros or Mac OS follow the steps mentioned [here](https://kumarvinay.com/installing-dlib-library-in-ubuntu/).
- Python3.8 is recommended for the same results.

You can create and activate a virtual environment in Python using the following commands
```bash
python --version
```

If the Python version is not 3.7 3.8 or 3.9 then download any of the versions.
After installing any of the above three versions create a virtual environment with that version.
Let's say we installed the 3.8 version then the command goes like this

```bash
python3.8 -m venv my_env
```

Activate the virtual environment using the following command
```bash
my_env\Scripts\activate
```
The terminal will look like this
```bash
(my_env) PS C:\Users\lenovo\WALKER\Drowsiness Detection\Drowsiness Detection Flask API>
```

We cannot directly install dlib library from [pip](https://pip.pypa.io/en/stable/) package manager. Instead, we use the wheel file separately to install it.

Download the dlib .whl file from [https://github.com/sachadee/Dlib/tree/main](https://github.com/sachadee/Dlib/tree/main) which matches your current version of python. 

For Python 3.7 it's numbered 37, for 3.8 it's 38, and for 3.9 it's 39, and place it in the working directory.

Currently, we are using the python3.8 version dlib library in the repository. 

Now install the dependencies from requirements.txt and wheel file.

```bash
pip install -r .\requirements.txt, "dlib-19.22.99-cp38-cp38-win_amd64.whl"
```

Remember to replace the wheel file according to the Python version being used.

## How to run
```bash
python app.py
```
This runs the app at default port 5000.


## Usage
An example code that uses react webcam to get screenshots and sends the request to API to get an array of size 68 containing landmarks and status of detected faces.

```javascript
const imageSS = webcamRef.current.getScreenshot();

const base64Image = imageSS.split(",")[1];
const res = await fetch("http://localhost:5000/get_landmarks", {
    method: "POST",
    body: JSON.stringify({ image: base64Image }),
    headers: {
      "Content-Type": "application/json",
    },
  });

const data = await res.json();
const landmarks=data.landmarks; //array containing 68 facial points
const status=data.status
```

> The standard facial points are taken from
[https://b2633864.smushcdn.com/2633864/wp-content/uploads/2017/04/facial_landmarks_68markup-768x619.jpg?lossy=2&strip=1&webp=1](https://b2633864.smushcdn.com/2633864/wp-content/uploads/2017/04/facial_landmarks_68markup-768x619.jpg?lossy=2&strip=1&webp=1).
