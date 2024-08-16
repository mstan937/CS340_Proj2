# CS340_Proj2
Project 2_READ ME
Grazioso Salvare Dashboard
Project Overview
Grazioso Salvare is a company dedicated to identifying and training dogs for search-and-rescue operations. This project involves developing a full-stack application to help Grazioso Salvare categorize and identify suitable dogs using data from a nonprofit agency operating five animal shelters in the Austin, Texas, area.
The core functionality of this application is a client-facing dashboard that connects to a MongoDB database. This dashboard allows Grazioso Salvare to interact with and visualize the data. It is designed to be user-friendly and intuitive, reducing user errors and training time.
Dashboard Features
Branding Elements
•	Grazioso Salvare Logo: The dashboard includes the Grazioso Salvare logo, linked to the company’s home page: www.snhu.edu.
•	Creator Identifier: The dashboard features a unique identifier with the creator's name, Marcus Stanley, to credit the dashboard's development.
Required Widgets
The dashboard includes the following interactive widgets:
•	Interactive Filter Options: Users can filter the data by rescue type using buttons or drop-downs:
o	Water Rescue
o	Mountain or Wilderness Rescue
o	Disaster Rescue or Individual Tracking
o	Reset: Resets all widgets to their original, unfiltered state.
•	Dynamic Data Table: The data table updates dynamically in response to the filtering options.
•	Geolocation Chart: A map that visualizes the shelters' locations, dynamically updated based on the selected filter.
•	Secondary Chart: An additional chart (e.g., pie chart) that responds dynamically to the filtering options.
Functionality
Filtering Mechanism
The dashboard's filtering options allow users to query the database for dogs suited to specific types of rescue training. Based on the selected filter, the data table, geolocation chart, and secondary chart will be updated to display the relevant data.
Rescue Types and Preferred Dog Breeds
Grazioso Salvare uses the following guidelines for selecting dogs:
•	Water Rescue: Preferred breeds include Labrador Retriever Mix, Chesapeake Bay Retriever, and Newfoundland. The preferred sex is intact female, with an age range of 26 to 156 weeks.
•	Mountain or Wilderness Rescue: Preferred breeds include the German Shepherd, Alaskan Malamute, Old English Sheepdog, Siberian Husky, and Rottweiler. The preferred sex is an intact male.
•	Disaster or Individual Tracking: Preferred breeds include Doberman Pinscher, German Shepherd, Golden Retriever, Bloodhound, and Rottweiler. The preferred sex is intact male, with an age range of 20 to 300 weeks.
Technical Specifications
•	Backend: MongoDB for database management.
•	Frontend: The dashboard is built with user-friendly UI components that allow intuitive interaction with the data.
Installation and Setup
To set up the application locally, follow these steps:
1.	Clone the Repository:
bash
Copy code
git clone  https://github.com/mstan937/CS340_Proj2
2.	Install Dependencies: Navigate to the project directory and install the necessary packages:
Copy code
npm install
3.	Set Up MongoDB: Ensure MongoDB is installed and running. Import the provided dataset into your MongoDB instance.
4.	Run the Application: Start the development server:
MongoDB
Copy code
npm start
5.	Access the Dashboard: Open your browser and navigate to http://localhost:3000 to interact with the dashboard.
