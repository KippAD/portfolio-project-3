# **The Voting Station**

## **Brief**
The Voting Station is a command line interface based voting system that is built to hold an election. The election is set in Sussex and is run between three candidates: The Red, Green, and Blue Parties. The application aims to automate the voting process by collecting votes from users, storing and counting them, and then presenting data back to the user in a visually appealing way.

**Login details for Admin Portal:**

Username: admin

Password: password

[Link to Heroku App](https://the-voting-station.herokuapp.com/) - [Link to Google Sheet](https://docs.google.com/spreadsheets/d/1xahaI5p6dAiUJqpnXbWY78Ph-1Lv-7vKWn3ZpGqIroU/edit?usp=sharing)

---

<p align="center"><img  src="assets/readme-images/readme-hero-img.png" width="75%"></p>

## Contents 
- [Planning](#planning)
    - [UX Objectives](#ux-objectives)
    - [Design](#design)
    - [Logic Chart](#logic-chart)
- [Features](#features)
    - [Current Features](#current-features)
    - [Future Features](#future-features)
- [Technology](#technology)
- [Python Modules](#python-modules)
- [Testing](#testing)
    - [Validator Tests](#validator-tests)
    - [Manual Input Testing](#manual-input-testing)
    - [Manual Data Testing](#manual-data-testing)
    - [Browser Compatibility](#browser-compatibility)
    - [Lighthouse Testing](#lighthouse-testing)
    - [Bugs](#bugs)
- [Deployment](#deployment)
- [Acknowledgements](#acknowledgements)

## **Planning**
---
### **UX Objectives**
The objectives for the Voting Station from a UX perspective are:

1. Create a fluid CLI application with easy navigation and a purpose that is clear to the user from the beginning. The user knows where to go within the application and how to get there, and has no trouble in doing so.

2. The application has a consistent design that makes it clear to the user what processes are happening and when input is required. From an aesthetic perspective, the user gets a positive emotional response from interacting with the application.

Due to the application being based in the command line interface, the design is more limited in its possibilities, meaning that more focus has to be put on creating a display that looks good and appeals to the user. These limitations can be countered by using external Python modules and libraries that offer more opportunities to customize the interface, and therefore improve the design and UX.

**To achieve the first objective:**
- The inputs that control the applications flow are clearly marked so that the user will always know when an action is required from them.
- The user will always know where they are within the application, enabling them to move through it more intuitively.
- User actions are clearly explained across the application so that the user will always know what will happen in response to their inputs.

**To achieve the second objective:**
- Consistent text colors will represent different actions: blue text is a loading message, cyan text indicates an input is required, and red text a warning.
- Colorama and ASCII title will add color and design throughout, expanding the possibilities of the terminal that would otherwise be limited to a black background with white text.
- Voting data in the application will be printed in bar chart format, improving the UX by presenting data in a neat and digestible way.

[Back to contents](#contents)

### **Design**
As mentioned in the UX objectives, the scope of the design is slightly limited due to the application being CLI based. In the planning phase, the following modules were researched and included in the project in order to maximize how much design could be added:

- **Termacolor and Pyfiglet** - These modules meant that a title of ASCII text could be generated and then printed into the terminal. The title is seen throughout the application.

<p  align="center"><img  src="assets/readme-images/ascii-title.png" width="50%"></p>

- **Colorama** - Gives color and background color to text within the application. As mentioned previously, this is useful in giving a consistent experience for the user by categorizing the text in the application to different functions and processes. For example cyan text always indicates to a user that an input is required, red text is a warning, and green indicates that a user action has been accepted. As a user continues to use the application they will build familiarity with the actions associated with the colors.

<p  align="center"><img  src="assets/readme-images/colorama.png" width="50%"></p>

- **Plotext and Tabulate** - These modules contributed greatly in improving the design and UX in the Voting Station. They allow data to be printed into the terminal in bar chart and tabular form respectively, and meant that large swathes of data were meaningfully presented.

<p  align="center"><img  src="assets/readme-images/plotext.png" width="50%"></p>

[Back to contents](#contents)

### **Logic Chart**
It was useful to map out the applications logic and functionality in order to better understand how to structure the code during development. Using [Lucidchart](https://www.lucidchart.com/pages/), the application was plotted out and it proved to be a very important resource to keep referring back to during the development process. 

<p  align="center"><img  src="assets/readme-images/lucid-chart.png" width="50%"></p>

[Back to contents](#contents)

## Features
---
## **Current Features**

### **Vote Casting**
---
<img  src="assets/readme-images/voting-collage.png" width="80%">

The vote casting function takes a user vote and stores the data externally. This is the main process of the application as its principal aim is to hold an election.

- Takes first and second names, age, region, and vote, validating all inputs to ensure that the user submits the correct data to the external Google Sheet.
- Allows users to review their inputs before submitting, meaning they can cancel their vote or complete the form again if they are not content.

### **Vote Results and Insights**
---
<img  src="assets/readme-images/results-collage-1.jpg" width="80%">
<img  src="assets/readme-images/results-collage-2.png" width="80%">

Using the data provided by the user that is stored in the Google Sheet, the Voting Station uses the Plotext and Gspread modules to build bar charts that display live calculations of data.

- The Current Vote Count area displays a bar chart that shows the current count of all votes in percentages. This chart is live and updates with each new vote.
- Voting insights provides further information about the voting demographics in bar chart form, these are the popularity of each party in each voting region and the popularity of each party in certain age brackets.

### **Information**
---
<img  src="assets/readme-images/information.png" width="50%">

The information page explains to the user the purpose of the application and suggests possible actions that they might take.

- Clearly describes the function of the application in more depth to the user if it is not immediately obvious on the main menu.

### **Admin Portal**
---
<img  src="assets/readme-images/admin-collage-1.png" width="80%">

The Admin Portal is separated from the rest of the application as it has access to sensitive data and has powers to manipulate the vote.

- Access to the Admin Portal is prohibited by login and password.
- Admin is able to view all vote data in tabular form, including names that are omitted in other areas of the application.
- Menu has access to other admin actions including the voting switch and vote deletion.

### **Admin Vote Deletion:**
---
<img  src="assets/readme-images/admin-collage-2.png" width="80%">

The admin has the power to delete votes from the election in the Admin Portal.

- Table of votes is neatly displayed using tabular, along with all voting details recorded in each vote.
- Admin can user voting number displayed in table to delete votes.
- This function would only be used in certain circumstances, for example if an illegitimate vote got through validation.

### **Admin Vote Switch**
---
<img  src="assets/readme-images/switch-collage.png" width="80%">

In the admin control area, the admin is able switch voting on or off.

- Voting toggle allows the vote casting function to be enabled and disabled by the admin, controlling whether users are able to submit votes. 
- This feature could be useful if there was an error with vote validation or if incorrect data was being submitted.

[Back to contents](#contents)

### **Future Features:**

#### **Create Custom Votes**
An idea for the future development of the Voting Station would be to give the user the ability to create separate votes for different elections of their choosing. This would involve giving full autonomy to choose what data is required to submit a vote, as well as how many candidates were taking part. 

#### **More Insights**
To build on the above idea, with more data points there would be a greater range of insights that could be drawn from an election. So automating the insights that are printed in the insights page could be an interesting idea to correlate with the different categories of data that would emerge with different elections.

[Back to contents](#contents)

## **Technology** 
The Voting Station was built with the following technologies:

1.  [**HTML**](https://en.wikipedia.org/wiki/HTML5) - Used to give content to the application.
2.  [**CSS**](https://en.wikipedia.org/wiki/CSS) - For styling the terminal in Heroku.
3.  [**JavaScript**](https://en.wikipedia.org/wiki/JavaScript) - Used to create the web environment of which the terminal app runs in.
4.  [**Python**](https://www.python.org/) - Used to develop the functionality and design of the application in the CLI.
5.  [**Gitpod**](https://gitpod.io) - The IDE used to develop the application and test the Python code.
6.  [**Github**](https://github.com) - For hosting the application repository and for version control.
7.  [**Heroku**](https://www.heroku.com/) - For hosting the actual application.
8.  [**Google Cloud Platform**](https://cloud.google.com/) - For creating the API's to connect the application with Google Sheets.
9.  [**Google Sheets**](https://www.google.com/sheets/about/) - For storing data accessed by the application.
10.  [**Lucid Chart**](https://www.lucidchart.com/pages/) - To design the logic path of the Python code.
11.  [**Am I Responsive**](http://ami.responsivedesign.is/) - To create the image at start of the readme.
12.  [**Favicon.io**](https://favicon.io/) - Used to create a favicon for the application.

[Back to contents](#contents)

## **Python Modules**
The following modules were used in developing the Voting Station:

1.  [**Time**](https://docs.python.org/3/library/time.html) - For adding time delays to application.
2.  [**OS**](https://docs.python.org/3/library/os.html) - Used for clearing the terminal.
3.  [**Collections**](https://docs.python.org/3/library/collections.html) - Used to count votes more concisely.
4.  [**Tabulate**](https://pypi.org/project/tabulate/) - For presenting the vote data in tabular format in the Admin Portal.
5.  [**Termcolor**](https://pypi.org/project/termcolor/) - For cprinting the ASCII title.
6.  [**Pyfiglet**](https://pypi.org/project/pyfiglet/0.7/) - For generating the ASCII title.
7.  [**Colorama**](https://pypi.org/project/colorama/) - To add color to the application text.
8.  [**Credentials**](https://pypi.org/project/credentials/) - To add credentials and control access to the Google Sheet.
9.  [**Plotext**](https://pypi.org/project/plotext/) - For plotting Google Sheet data in bar chart format in the terminal.
10.  [**Gspread**](https://docs.gspread.org/en/latest/) - To handle data stored in the Google Sheet.

[Back to contents](#contents)

## **Testing**

### **Validator Tests**

#### **Python PEP8 Validator**
All Python code in the Voting Station was tested using the [**Python Pep8 Validator**](http://pep8online.com/). When tested for the first time, no errors or warnings were returned. This is due to Gitpod???s built-in system that alerted any issues with the Python code during development, so all issues were resolved before the application was tested in the validator.

Most issues that arose during development pertained to trailing whitespace and lines that were too long, both of which were fairly straight forward to resolve. The results from the PEP8 Validator are below:

**Run.py:**

<img  src="assets/readme-images/run-validation.png" width="60%">

**Strings.py:**

<img  src="assets/readme-images/strings-validation.png" width="60%">

#### **HTML, CSS, and JavaScript**
As the Voting Station is developed from a template provided by Code Institute, the JavaScript in the application has not been adjusted and therefore there was no need to test the code.

However, small changes have been made to the HTML and CSS in order to format the position of the terminal in Heroku, so all HTML and CSS has been passed through the [**W3C HTML Validator**](https://validator.w3.org/) and the [**Jigsaw CSS Validator**](https://jigsaw.w3.org/css-validator/) respectively.

**For HTML**:

<img  src="assets/readme-images/html-warnings.png" width="100%">

The validator initially returned three errors, including a fatal error. These were all related to the placement of the site favicon in the wrong HTML file. All of these errors were removed when the favicon was moved to the head of the layout.html file.

The passed validator test is below:

<img  src="assets/readme-images/html-validation.png" width="100%">

**For CSS**:

CSS validation unsurprisingly returned no errors as the alterations to the code were very minor:

<img  src="assets/readme-images/css-validator.png" width="100%">

[Back to contents](#contents)

### **Manual Input Testing**
The Voting Station relies on user input for the application to function correctly. In order to fully test for issues, each input across the interface was individually tested to find any errors that might occur and also to ensure that any actions resulting from an input worked as intended.

This was done by inputting all incorrect data types - strings, numbers, negative numbers, empty inputs, misplaced capitalisation, misplaced spaces - in each input to try and beat the validation in the code. The result from each input was also double checked to ensure that the outcome of every user response was the correct action.

The results are below:

<img  src="assets/readme-images/input-testing.png" width="60%">

The first issue found when testing was related to the color of a warning being incorrect. The second more significant problem was the first bar chart in insights rendering incorrectly. This second issue is a known bug, although navigating to the results menu and then back into insights will load the chart successfully.

All input validation and functionality worked as expected, and no incorrect data types are able to compromise the application and pass through voting.

[Back to contents](#contents)

### **Manual Data Testing** 
To check that the data being presented in the bar charts was correct, manual tests were also conducted. This involved manually checking the data displayed in the Voting Station against the data in the Google Sheet and ensuring that they both matched up. This was done for both the current vote count display and bar charts in insights.

During testing it was discovered that in the vote by region bar chart, the titles of two regions were the wrong way around, meaning that the data represented in the bar chart was incorrect. This was resolved by switching the titles around. Other than that single issue, the data in the Google Sheets matched the data being printed in the application, indicating that all calculations were functioning correctly in the Voting Station.

[Back to contents](#contents)

### **Browser Compatibility** 
The Voting Station has been tested across multiple browsers:

- **Chrome**
- **Mozilla Firefox**
- **Safari**
- **Opera**

The only issue found during browser testing was in Safari where the opening input would not allow any keyboard entry, effectively freezing the application before it had begun. This issue occurred on a 2021 Macbook, but testing Safari on a different 2015 model did not recreate the error. On the older Macbook the application ran exactly as intended, which could indicate that the issue is to do with either the newer machine or a newer version of Safari and not the code itself.

In all other browsers, the application functioned exactly as anticipated, all user interactions were successful, and the Google Sheet was always updated appropriately.

[Back to contents](#contents)

### **Lighthouse Testing**
The Voting Station was tested using the Lighthouse extension of Google Chrome, the results are below:

**Mobile:**

<img  src="assets/readme-images/lh-mobile-2.png" width="80%">

**Desktop:**

<img  src="assets/readme-images/lh-desktop-2.png" width="80%">

The SEO score was originally lower due to the site not having a meta description, an issue that was easily resolved. The other low score was in Best Practices. This issue was related to the JavaScript library involved, which as mentioned earlier was preinstalled with the template.

[Back to contents](#contents)

### **Bugs**

#### **Resolved**

**Clearing Terminal**

A recurring issue once the application had been deployed to Heroku was related to clearing the terminal. Using the OS module there is a function to clear the terminal, however this is seemingly limited to the viewport size of the terminal itself and therefore with larger amounts of content that would exceed the terminal height, the function would not fully clear all content. Eventually a solution was found thanks to Helena, a fellow student on slack.

<img  src="assets/readme-images/slack-solution.png" width="60%">

**Favicon**

A persistent problem faced throughout the application development was the favicon not displaying in Heroku. This can be seen throughout the commit history where repeated attempts are made to resolve the issue. This is because in order to test a solution the changes had to be pushed to Github, and often that solution failed to work. Eventually changing the link to the favicon from a file path to a raw link solved the issue.

#### **Unresolved**

**First Insights Bar Chart**

The largest unresolved bug in the application is an error with one of the bar charts in the insights area failing to load properly. Upon loading, the chart does not plot data and instead prints a colorless square with no discernible information on it - this seemingly occurred on every instance that the insights page was loaded for the first time. However, by exiting the insights page and loading it once again, the bar chart would print as expected. Whilst not totally resolved, adding a timer between the calling of the two bar chart functions has managed to prevent the issue happening as regularly as before, but sometimes it still occurs. In this case, the user is instructed to reload the insights page.

**Double Barrel Names**

It was realized quite late into the project development that whilst the name validation is effective in preventing incorrect inputs by blocking special characters and spaces, problems can be caused for users with two first names or double barreled surnames that require hyphens or spaces.  This is cause for improvement in future development of the project.

**Bad UX**

There are also a couple of examples of bad UX which result from the application being based in the CLI. These occur in the admin votes table and the insights page, where due to larger amounts of content being printed, the user is dragged down to the bottom of the console and half of the content is cut off by the terminal. These do not affect the functionality of the application but still require the user to scroll up to read the data where it would be preferable if the data fit into the terminal.

[Back to contents](#contents)

### **Deployment**
The following steps detail how to deploy a project of your own on [**Heroku**](https://www.heroku.com/):

1. Navigate to Heroku and log in. (If you do not have an account then create one using the Sign Up button)

<p align="center"><img  src="assets/readme-images/heroku-1.png" width="40%"></p>

2. Once logged in, navigate to your account dashboard and click the "New" button, then click "Create New App "in the corresponding drop down.

<p align="center"><img  src="assets/readme-images/heroku-2.png" width="60%"></p>

3. Choose a name for your application and select an appropriate region before finally clicking "Create New App".

<p align="center"><img  src="assets/readme-images/heroku-3.png" width="40%"></p>

4. Within the application interface head to the "Settings" tab and click "Reveal Config Vars".

<p align="center"><img  src="assets/readme-images/heroku-4.png" width="60%"></p>

5. Once in Config Vars enter the key of "PORT" and the value of "8000". (If working with Google Sheets API you would also enter the credentials into the Config Vars)

<p align="center"><img  src="assets/readme-images/heroku-5.png" width="60%"></p>

6. In the Buildpack area below click the "Add Buildpack" button, select Python, and save. Repeat the process and add Node.js, also ensuring that in the buildpack order Python is above Node.js - the order of buildpacks can be easily adjusted by clicking and dragging one above or below the other.

<p align="center"><img  src="assets/readme-images/heroku-6.png" width="60%"></p>

7. Head back to the top of the page and select the "Deploy" panel. In this area select Github as the method of deployment and ensure that the appropriate Github account is connected to the Heroku account.

<p align="center"><img  src="assets/readme-images/heroku-7.png" width="60%"></p>

8. Using the search bar in the "Connect to Github" area, locate the chosen repository and click "Connect".

<p align="center"><img  src="assets/readme-images/heroku-8.png" width="60%"></p>

9. Once connected, click "Enable Automatic Deployment" and then scroll down and select "Deploy Branch". Once loaded a link will be displayed that will take you to the live project.

<p align="center"><img  src="assets/readme-images/heroku-9.png" width="60%"></p>

[Back to contents](#contents)

### **Acknowledgements**

I would like to thank my mentor Precious Ijege for all of the support and advice on creating this project.

Also to my fellow students on slack, who on countless occasions helped me solve issues that I was having.

I have loved learning Python but it was difficult at times, and without the guidance and support I would not have got very far.

[Back to contents](#contents)
