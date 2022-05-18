# E2E_predictor
Final version of E2E's course' predictor

## Information about the source data and some statistics 

The data is coming from Yandex Real Estate's database, relating to Saint-Petersburg - Russia's cultural capital - real estate market. 
Mostly, the data consists of end prices, and a myriad of characteristcs, such as the address, date of sales, floor, area, ... of the property.

![image](https://user-images.githubusercontent.com/91207015/169153922-78c7dae9-2070-4312-84d4-dae4de026c10.png)

It was thouroughly cleaned and checked for outliers etc

![image](https://user-images.githubusercontent.com/91207015/169153972-5efdf947-33f5-4299-95f3-570a7cbc7755.png)

The final tables look as follows:

![image](https://user-images.githubusercontent.com/91207015/169154063-f211ccf4-20fe-4459-9aea-6e8bb6674d9d.png)

## Information about the model

The models used here are a random forest and CatBoost.

The model 1 was made using a random forest with the parameters open plan, rooms, area, and renovation.

The model 2 uses catboosting and floor, open plan, rooms, and area.

Why 2 different types? Simply to crosscheck results.

In both cases the MAE, MSE, and RMSE are reasonable enough to conclude that the models are not full of errors

## How to install instructions and run the app with a virtual environment

After creating a virtual machine, or VM, (for instance on Yandex Cloud), with Ubuntu as the OS, you must:

Install Python3 
Install and initialise git
Install the required libraries (included in the requirements.txt file)
Pull this GitHub folder
run app.py by typing > python app.py

MAYBE ADD HERE

## Information about Dockerfile's content

The Dockerfile contains a list of commands to be executed when the Docker is to be used on the VM. It allows you to create a container there, making a copy of the app

## How to open the port in your remote VM

To open the port in your remote VM, you should use the following line:

http://YourVirtualMachineAddress:ThePort/predict_price?model_version=1&floor=2&open_plan=1&rooms=1&area=1&renovation=1

Make sure to enter numbers that make sense if you do not wish to get an error!

## How to run app using docker and which port it uses

To run the app using docker, initialise docker and build a container, and run it. You may see the reference to docker containers by using the command docker ps
