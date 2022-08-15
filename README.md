# End2End-Movie-Recommendation-App
This app ask the user for their favourite movie and based on the content of the favourite movie it recommend 5 more movies that are relevant to the user. It uses a content based recommendation system to find out the similarity between the movies and returns the best 5 movies that are most similar to the one that is inserted by the user.

### Getting Started
1. Download the entire project folder and create an environment inside the folder
2. Next in the cmd prompt activate the created environment and use the commandline 'pip install -r requirements.txt' to install all the required module in the environment. Once all the installation is done run the file by using commandline 'streamlit run client/ben-hpp-app.py' keeping the created virtual environment activated.
It will open on a web app favourite movie. Choose your favourite and click the button for recommended movies.
3. Enjoy the app!

### Dataset
Here the dataset size is so large that it couldn't be uploaded in the gitHub. But the link to the dataset is https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata . You can download two csv file namely tmdb_5000_movies.csv and and tmdb_5000_credits.csv. Once you have downloaded the dataset files, keep it inside a folder named 'dataset' to avoid the FileNotFoundError because the code are written, assuming this particular allocations of file. However, you can keep these files in some other locations also but in that case you have to manually  change the file path of these to file wherever it is required.

### Artifacts
Also we have not uploaded two pickle files namely movies_df.pkl and similarity_score.pkl due to the file size restriction. Here also when you are generating these two files from running codes from the ipynb files, keep these two file in a folder named 'artifacts' to avoid FileNotFoundError. But like previous, you can also choose to keep it in other locations, but in that case you have to make sure that the file path is consistent. 
