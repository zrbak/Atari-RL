# Atari-RL
This is a Atari project that is using unique RL algorithms to train onto Atari games using only frames of pixels as input

# Setup
To start this project, first you need to clone this repo and download the AtariGym.yml file saved in the Environment folder.

Make sure that you have installed the latest version of Anaconda3 onto your device
Additionally, to work with the libraries you will need to download the latest C++ build tools found at: https://visualstudio.microsoft.com/visual-cpp-build-tools/

Go into Anaconda prompt and type in this code to set up the environment
>"conda env create -f AtariGym.yml"

To activate this environment type in
>"conda activate AtariGym"

Do not add more packages without my approval, this will cause very annoying issues to resolve and I will not like you anymore. I haven't included the packages for the RL algorithm yet so the current environment is not the final state. Keep that in mind if things no longer work anymore that you will have to update your environment manually as laid out previously.

# IDE

I recommend using Pycharm as the IDE of choice for this project. Additionally, using Juypiter Notebooks is also acceptable for dev work.

When you clone the project, you need to select the AtariGym as your environment or else none of the packages will be loaded. This will be found in the bottom right isde of the screen for PyCharm

# GitHub Desktop

Git is a very powerful tool for version control and dev work. Ideally, people should only work on separate files to minimize conflicts and headaches. Keep in close collaboration if 2 devs are working on the same file/ figure out livecoding methods (basically like shared Google docs except with code) for PyCharm.

FOR EVERY CHANGE YOU MAKE, MAKE A NEW BRANCH WITH A DESCRIPTIVE TITLE OF YOUR WORK INTENT (ie add-readme-file)

D O _ N O T  _  P U S H  _ Y O U R  _  C O D E  _  D I R E C T L Y  _  O N T O  _ T H E  _  M A I N  _  B R A N C H

After making a branch, make sure to actively commit any changes to that branch. When you are done push the changes up to the server and submit a pull request to merge your branch with the main. Once all conflicts (if there are any) have been successfully resolved, then the changes added will be reflected in the main branch. 
That's version control 101 for ya



# Openai Gym

We will be using the openai Atari wrapper to handle the pixel inputs

The link to the Openai gym is here: https://github.com/openai/gym

To get started: 

Homepage to the Gym - https://www.gymlibrary.dev/
Documentation outlining basic usage - https://www.gymlibrary.dev/content/basic_usage/


# Misc 

The following website shows the RL algorithms tried for each game: https://paperswithcode.com/task/atari-games

We will try to explore a RL algorithm and game that has not been attempted before and will compare performance using this website. 
Additionally, if we can find any updates to these algorithms, we can try these too


Some algorithms to look at:

Temporal Difference Learning for Model Predicitive Control (Most promising)
https://www.researchgate.net/publication/359129864_Temporal_Difference_Learning_for_Model_Predictive_Control
