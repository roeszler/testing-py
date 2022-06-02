# N(3)Orthotics Order Portal
### HTML, CSS and JavaScript Essentials - Portfolio Project 3
Repository link : https://github.com/roeszler/n3orthotics

Terminal : https://n3orthotics.herokuapp.com/

Link to Sample Dataset : [Google Sheets](https://docs.google.com/spreadsheets/d/1j2uLuW9sjskI7YEP7Af2G9hhqsFQbMjJ13Ewthm7Nbc/edit?usp=sharing)

## 1. Project Purpose

N(3)Orthotics order portal is a Python terminal application, which runs in the [Code Institutes](https://codeinstitute.net/) python terminal deployed [Heroku](https://www.heroku.com/platform).
* Users can select and submit orders for the N3D product range of printed foot insoles produced at [northotics.com](https://northotics.com/shop/semi-customised-orthosis/n3d/). 
* Users can create, retrieve and navigate through orders to update information, check production status and/or re-order products. 

[A live version of the app can be accessed here](https://n3orthotics.herokuapp.com/)

[![AMI Responsive Design Mockup](assets/pics/n3orthotics-terminal.webp)](https://n3orthotics.herokuapp.com/)

N(3)orthotics was created as the third project while studying the [Code Institute’s Full Stack Software Developer course](https://codeinstitute.net/se/full-stack-software-development-diploma/). It has been built from the ground up to extend programming skills, demonstrate the use of python as a programming language and have some more fun. 

The application is targeted to those looking to implement similar python based concepts, while also attending to a common business need: *originating new orders in a simple way*.

## 2. User Experience Design

N(3)Orthotics is an app that aims to allow users to access order information quickly and easily. Each user decision, accessible by numerical selection, have been constructed to reflect an intuitive flow through a product ordering process. 

This has been derived from reviewing the first 4 of the 5 planes in the [User Experience Design process](https://en.wikipedia.org/wiki/User_experience_design). This process is  part of an overarching [User Centred Design](https://en.wikipedia.org/wiki/User-centered_design) process that would be undertaken in the creation of a commercial project.

User Experience (UX) Design planes:
1. [Strategy Plane](assets/ucd/1-strategy.md)
2. [Scope Plane](assets/ucd/2-scope.md)
3. [Structure Plane](assets/ucd/3-structure.md)
4. [Skeleton Plane](assets/ucd/4-skeleton.md)
5. [Surface Plane](assets/ucd/5-surface.md) (not required for this project)

### User Stories
Highlight the value users gain by using the n3orthotics order portal and used as the logic in functional testing.
#### First Time Visitors
* As a first time user, I want to quickly understand the purpose of the application.
* As a first time user, I want to understand the ordering process.
* As a first time user, I want to understand how the exit the application.
* As a first time user, I want to intuitively navigate within the application.
* As a first time user, I want to initiate the ordering process in a simple and intuitive way.
* As a first time user, I want to be able to understand how to recall existing orders.
* As a first time user, I want the application to present me with information to make a decision or change order information.
* As a first time user, I want to understand how to change the status of an order.
* As a first time user, I want to have errors detected with relevant information to correct them.
#### Returning Visitors
* As a returning user, I want to initiate the ordering process in a simple and intuitive way.
* As a returning user, I want be able to recall order I have previously made.
* As a returning user, I want to be able to retrieve the current status of existing orders.
* As a returning user, I want to be able to cancel an existing order.
* As a returning user, I want to be able to change the features of an existing order.
* As a returning user, I want to be notified when existing orders are unable to be changed.
* As a returning user, I want to be able to re-produce existing orders.
* As a returning user, I want to be able to save and not submit partially completed order.
* As a returning user, I want to be provided contact information for further questions.

#### Coding Colleagues
* As a fellow code writing user, I want to see how the python programming language has been written and operates.
* As a fellow code writing user, I want to see the file structure behind the application.
* As a fellow code writing user, I want to clearly understand what role each function performs within the application.
* As a fellow code writing user, I want to be able to contact the author.
### Design
#### Structure
The application is intended to allow users to easily navigate through a product ordering process. A tree structure style of navigation allowing users to drill down and/or return to previous levels until their objectives are met.
#### Application Mockup & Wireframe
Four graphics of the application have been designed to show stakeholders and potential clients early concepts before any coding started. They provide a pre-build indication of: 
* The variety of functions required.
* The critical pathways of functions needed to reach each user outcome.
* The relationships between each function.
* The logical approach to code creation, promoting readability and aiding future fault-finding processes.
* The experience as users navigate through the order, retrieve, update and/or re-order processes.

##### Flowchart 1 - Order / Re-Order Process:
![Flowchart 1 - Order Process](assets/pics/flowchart1-addorders.webp)
##### Flowchart 2 - Retrieve Order Process:
![Flowchart 2 - Retrieve Order Process](assets/pics/flowchart2-displayorder.webp)
##### Flowchart 3 - Change Features / Status:
![Flowchart 3 - Update Status Process](assets/pics/flowchart3-update_status.webp)
##### Critical Pathway and Testing Tree:
![testing-tree](assets/pics/testing-tree.webp)
## 3. Features 
### Existing Features
#### Landing Screen & Welcome
* The landing page is intended to ground the user into the purpose of the application.
* N(3)Orthotics is a python based application that allows direct addition and recall of information stored in a sample [google sheets](https://docs.google.com/spreadsheets/d/1j2uLuW9sjskI7YEP7Af2G9hhqsFQbMjJ13Ewthm7Nbc/edit?usp=sharing) database.

[![AMI Responsive Design Mockup](assets/pics/n3orthotics-terminal.webp)](https://n3orthotics.herokuapp.com/)

#### Place New Order
This is the start of the order process collecting user information that populates the `user_data` list object. 
    
![Place New Order](assets/pics/1-place-new-order-screen.webp)

* The functions behind this screen are: 
  * `instruct_user_data()` 
  * `get_user_data()`

* It sequentially requests users to input their First Name, Last Name and Email details
* Each text input is sequentially converted using `.capitalize()` and validated for typical alpha text input errors using the inbuilt `isalpha()` method within `validate_user_f_name()` and `validate_user_l_name()` functions.
* The email input is converted to lowercase using `.lower()`and  validated for typical email input errors using a `validate_user_email()` function.
  * This uses an imported regular expression feature `import re` to provide a REGEX email validation that checks the structure of an email address.
* Should the inputs fail validation, the user is prompted to correct the data, and revalidated until it passes:

  ![fail validation](assets/pics/fail-validation.webp)

  ![fail email validation](assets/pics/fail-email-validation.webp)

* Upon passing validation, the user is required confirm the data with a `yes_no_user()` function and proceeds to the [Input Order Data](#input-order-data) feature.

![pass validation](assets/pics/pass-user-input.webp)

#### Input Order Data

* This section allows users to select three product based variables of EU shoe size, Insole height (support) and Insole width.
* Each variable is validated to the choices displayed.

EU Shoe size (`get_size_data()`):
  * Converted to a `float()` value to 1 decimal point.
  * Validated to be between the values of `19` to `50`.
  * Validated to only be divisible by `0.5` (hence increment in units of `0.5`).

Height (`get_height_data()`) and Width (`get_width_data()`):
  * Convert each input to lowercase `lower()`.
  * Update its relative `order_data` index with a string value that is associated with that selection, i.e.: 
    * height index = `order_data[1]` and a 'l' selection will assign a `'Low'` string value to `order_data[1]` in preparation for manipulation with other functions.

![Input Order Data](assets/pics/add-order-data.webp)

* Following successful validation of each Input Order Data selection, proceeds to the `summary_order_data()` function with a choice to [Submit Order](#submit-order) else [Save Order](#save-order). 

#### Submit Order

![Submit Order](assets/pics/submit-order-data.webp)
* The `submit_order()` function allows user to submit details to database, or
* Proceed to save the order process for future recall. 

#### Save Order

![Save Order](assets/pics/save-order.webp)
* The `save_order()` function allows user to save the order as `PENDING` to the database for future recall, or 
* Discards the order information and starts over to the landing screen.

#### Successful Submission Screen

![order-submitted](assets/pics/order-submitted.webp)
* Indicates a successful connection and update of the sample database at [Google Sheets](https://docs.google.com/spreadsheets/d/1j2uLuW9sjskI7YEP7Af2G9hhqsFQbMjJ13Ewthm7Nbc/edit?usp=sharing).
* A full summary of entire order details that combines the `user_data` and `order_data` lists into an `export_data` list.
* Existing and New information (such as order number, submission date, row number and order status) are also included in the local `order_data` list and dsplayed on this screen. 
* __To reach this stage is the primary goal of the application__.

From here users are provided a range of options that feed into five primary goals:
1. Change the features of this order (`change_feature_of_order()`)
2. Start a new N3D order using existing `user_data` information, with an option to change it (`get_user_data()`).
3. Retrieve an existing order from the sample database (`retrieve_order()`)
4. Return to home screen (`main()`)
5. Exit the application (`exit()`)

#### Change Order Features
This feature is aimed to allow users to modify the details of the immediately preceding submitted order in case of error.

![Change Order Features](assets/pics/change-order-features.webp)

* Change features pathway from a newly submitted order, takes the user to a summary of the order.
* The current status of the order is used to validate the capacity of the order to be changed.
  * Anything before the SUBMITTED TO PRINT stage of production can be modified as production costs are minimal before this point.
  * Any order past this stage will not be able to be modified with an explanation of why.
* Users can select which order feature they would like to change
  * This takes them through a cycle of updating the local data in preparation for submission back into the exact same row of the database, updating the update_order_date in column `J` as it does so.
* __Note__: the conversion from a nested list to a list that occurs from the data imported from the database:
  * Using a `flatten_nested_list()` function coded from a derivation of those explained at [pythonpool.com](https://www.pythonpool.com/flatten-list-python/).
  * This allows the manipulation of the row data imported to be modified as the `flat_order` variable within the `validate_change_feature_of_order` function.

Once the user is satisfied as to the content of the order details, they have the option to:
  7. Submit the details to the database as summarised above
  8. Keep local changes and return to the home screen

#### Place New Order (from completed order screen)
* Same pathway as [place new order](#place-new-order) function, with the addition of allowing users to re-confirm their current `user_data` information.

#### Retrieve Existing Order

![Retrieve existing order](assets/pics/retrieve-order.webp) 

* Allows the user to retrieve existing order information from the database.
* Uses a `.get_values()` method to source data from the row range A:K of the matching order number:
  * `order_row = SHEET.worksheet('orders').get_values(f'A{row}:K{row}')` where `row` is the validated search input, returned as an integer `row = int(retrieve_order())`.
* The retrieved nested list is then flattened for local manipulation in three data sets `user_data`, `order_data`, and `flat_order`.

#### Take Me Home
* Simple function to return to `main()` screen.

#### Exit Portal
* Simple function to exit the N(3)Orthotics portal using the inbuilt python function `exit()`.

#### Order Number / Date Ordered / Date Updated feature
Order Number:
* The order number is a combination of the date in `YYYYMMDD` format _plus_ a 4 digit integer (`0000`).
  * For Example: `2205190001` was placed on 19/05/2022 and is the first ever order!
* Generated at the `generate_order_no()` function it is inserted to the database once and only ever as part of a new / re-printed order.

Date Ordered:
* Is generated in ISO format to Universal Coordinated Time (UTC) using a `datatime.now().isoformat()` method.
* This time and date is also inserted to the database one time and only at as part of a new order process.
* __Note__: this date 'is not' inserted at the `save_order()` process to help signify that the order has not yet been placed.

Date Updated:
* Is generated the same way as Date Ordered however it is only inserted when: 
  1. An order is saved or
  2. An order is updated or
  3. An order is cancelled.

Date Updated and Date Ordered can exist independently of each other, but __all states will have an Order Number associated to them__.

### Possible Future Features
#### Email Data
* Adding the functionality of automatically sending events and/or order information to the recorded users recorded email address for that order.
#### Print to Local Machine
* Including a print function that saves summary data as a text file, retrieves local operating system information and sends a text file to an attached printer.
#### Display Graphics
* Info-graphics that detail the finite differences between the product options
  * Height: Low / Medium / High support?
  * Width: Narrow / Standard / Wide shoe fit?
#### Refactoring using loop() functions
* A feature of the app is to return user to the landing page regularly. Although working as intended, this places the code at risk of incurring a [RecusionError](https://stackoverflow.com/questions/53786145/recursionerror-in-python) and/or a [StackOverflowError](https://stackoverflow.com/questions/214741/what-is-a-stackoverflowerror). Future branches will include code refactored with more `loop()` functions.
#### Python File Structure
* All the code in the app is in a single [run.py](run.py) file. To promte clarity when reading the code, future features will include code refactored and split into separate `.py` files and accessed through `import` functions. 
* Conatining these more descriptive `.py` files into a parent folder is good practice and promtes the depth, breadth and readability of the code written.
  * Accessing `.py` files in a subsequent file folder involves containing a `__init__.py` within the parent file folder, as researcched at [stackoverflow.com](ttps://stackoverflow.com/questions/44977227/how-to-configure-main-py-init-py-and-setup-py-for-a-basic-package-setu).
#### Application Programming Interface (API)
* Including an API to efficiently automate ordering functions into popular, commercially available clinical practice management software(s).
#### Inclusion into a full stack project
* The functions and value of this order portal lends itself to expansion and integration into wider ranging full stack projects.

## 4. Technologies
### Tools
The skillsets used in the creation and review of this project are based around a working knowledge of Python. The tools and the benefit of using each in the application development are : 

* [GitHub](https://github.com/)
  * Allows a variety of benefits to create, document, store, showcase and share a project in development.
* [GitPod](https://www.gitpod.io/)
  * Provides a relatively secure workspace to code and develop software projects in a remotely accessible cloud based platform.
* [Heroku Platform](https://www.heroku.com/platform)
  * Provides a platform for deploying and running python based apps.
* Python Terminal by [Code Institute](https://codeinstitute.net/)
  * The [n3orthotics](https://n3orthotics.herokuapp.com/) app is embedded in a python terminal for display, testing and assessment.
* [Convertio Image Optimiser](https://convertio.co/)
  * Able to reduce the file size and format of images ready for rapid access, improving device performance, accessibility and user experience.
* [Lucidchart Flowchart Diagrams](https://www.lucidchart.com/pages/)
  * A diagramming application that allows the mapping and creation of flowcharts to visualise design workflows.
* [Replit](https://replit.com/)
  * An in-browser integrated development environment (IDE) that allows simple testing and code development.


### Supported Screens and Browsers
The live application ([n3orthotics](https://n3orthotics.herokuapp.com/)) has been tested on each of the following popular browsers to check for maintained function and interactivity :
- [Google Chrome](https://www.google.com/chrome/)
- [Microsoft Edge](https://www.microsoft.com/en-us/edge) 
- [Apple Safari](https://www.apple.com/safari/)
- [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/)

## 5. Testing 
### User Story Testing
#### User: First Time Visitor (Investigating Stage)
> As a first time user, I want to quickly understand the purpose of the application.
  * Landing screen with welcome information attends to this.
> As a first time user, I want to understand the ordering process.
  * Sequential selection process leads user through order processes.
  * Functions designed to have an intuitive nature.
> As a first time user, I want to understand how the exit the application.
  * Seen as exit commands at landing screen and throughout key navigation menus.
> As a first time user, I want to intuitively navigate within the application.
  * Seen as the numerical selector method of navigation throughout the app.
> As a first time user, I want to initiate the ordering process.
  * Seen as selection 1 of landing screen.
> As a first time user, I want to be able to understand how to recall existing orders.
  * Seen as selection 2 of landing screen.
> As a first time user, I want the application to present me with information to make a decision or change order information.
  * Seen as summary order information presented prior to submission and recall of order details.
> As a first time user, I want to understand how to change the status of an order.
  * Seen as selection 2 of recall order details screen.
> As a first time user, I want to have errors detected with relevant information to correct them.
  * Tested by placing incorrect value formats at each input.
#### User: Returning Visitor (Ordering Stage)
> As a returning user, I want to initiate the ordering process in a simple and intuitive way.
  * Seen as selection 1 of landing screen.
> As a returning user, I want be able to recall order I have previously made.
  * Seen as selection 2 of landing screen.
> As a returning user, I want to be able to retrieve the current status of existing orders.
  * Seen in summary of recalled order.
> As a returning user, I want to be able to cancel an existing orders.
  * Seen as selections 4 of recalled order screen.
> As a returning user, I want to be able to change the features of an existing order.
  * Seen as selections 2 of recalled order screen.
> As a returning user, I want to be notified when existing orders are unable to be changed.
  * Seen as notification beyond change, where status fails validation to change any order details past the design stage :

![not editable](assets/pics/not-editable.webp)

> As a returning user, I want to be able to re-produce existing orders.
  * Seen as selections 1 of the recalled order screen.
> As a returning user, I want to be able to save and not submit partially completed order.
  * Seen as child sequence of 'no' to order submit process
> As a returning user, I want to be provided contact information for further questions.
  * Seen at landing screen [northotics.com](https://northotics.com/home/) and unable to cancel notification [email](mailto:info@northotics.com).

#### Coding Colleagues
> As a fellow code writing user, I want to see how the python programming language has been written and operates.
  * See [GitHub repository](https://github.com/roeszler/n3orthotics)
> As a fellow code writing user, I want to see the file structure behind the application.
  * See [GitHub repository](https://github.com/roeszler/n3orthotics)
> As a fellow code writing user, I want to clearly understand what role each function performs within the application.
  * File structure, order and docstrings aid in the readability of code.
> As a fellow code writing user, I want to be able to contact the author.
  * See [GitHub repository](https://github.com/roeszler/n3orthotics)

### Testing Tree
The [testing tree](#critical-pathway-and-testing-tree) process has been performed to a documented process. Users/testers complete tasks by clicking through the app in a sequential way. In a live version the results of the task would indicate:
* How many users got it right?
* How many users got it wrong?
* The paths users took before they selected an answer.
* How long it took users to complete the task?
* Sample: see [critical pathway and testing tree](#critical-pathway-and-testing-tree) mentioned previously.

### Issues & Resolutions

* Heroku based:
  * The browser based interface was not functioning as it should at the onset of this project. 
    * A CLI method was needed for initial deployment and a few recurrent glitches seemed to occur that were not always repeatable. 
    * Since then, a new version of n3orthotics app was installed on heroku. This seems to have rectified the intermittent errors. 
  * Initial python version installed as default with Heroku cased an error with a [backports-zoneinfo dependacy](https://stackoverflow.com/questions/72265234/failed-to-build-backports-zoneinfo) installed at the time. 
    * Further research indicated the current stable (and secure) build is `python-3.8.13`. This can be found in the [runtime.txt](runtime.txt) file to override the information pushed to the live [Python Terminal](https://n3orthotics.herokuapp.com/).
    * The [requirements.txt](requirements.txt) information was refactored and reduced by using more of the inbuilt python methods and functions throughout the code.
* An pylint error suggested to use `enumerate()` in place of `range(len())` to produce the order search row number. The code was refactored to suit and error corrected. 
* Initial manipulation of the row_data imported from the database would not occur as it was in a nested list format. Corrected by developing code similar to that researched at [Pythonpool - flattening nested lists](https://www.pythonpool.com/flatten-list-python/).
* Index [out of range error](https://stackoverflow.com/questions/24812679/what-is-an-index-out-of-range-exception-and-how-do-i-fix-it) was a common bug dealt with by better use of loop functions and/or appropriate index referencing.
* Handling dates and times into `isoformat()` was corrected using researched from [The Python Coding Book](https://thepythoncodingbook.com/dates-and-times-in-python/).
* A small error was occurring with the use of list`.append()` vs `list[element at index no] = replace_with_element` and subsequently resolved.
* General document formatting errors also fixed with the aid of the various problem identifiers installed into the development environment like [flake8](https://pypi.org/project/flake8/) and [ptlint](https://pypi.org/project/pylint/).


### Validator Testing 

* [PEP8 Python Validator](http://pep8online.com/)
    * No errors were found when passing through the PEP8 validator
    * Results : [All right](assets/validation/result_20220531_083536.txt)

## 6. Deployment

This project was deployed using Code Institute's mock terminal for Heroku. The steps to deploy are as follows:
* Fork or clone the [Code-Institute-Org: python-essentials-template](https://github.com/Code-Institute-Org/python-essentials-template)
* Click the Use this template to create a clone in GitHub
* Follow Display environment settings below:
### Display Environment (GitHub / GitLab / BitBucket)

The application has been deployed to GitHub pages. The steps to deploy are as follows: 
  * Create / open an existing repository for the project with the name of your choice on your GitHub, GitLab or Bitbucket account page.
  * Navigate within the GitHub repository you chose, and then navigate to the "settings" tab, which displays the general title.
  * On the left hand navigation menu, I selected the "pages" option midway down the menu.
  * At the top of the pages tab, the source section drop-down menu changed to select the branch: "main" with the folder selected as "/(root)"
  * Committed to the save and waited a few moments for the settings to coordinate with the server. 
  * On refresh of the browser, the dedicated ribbon changed to the selected web address, indicating a successful deployment.

> The live application link can be found here - https://n3orthotics.herokuapp.com/

> The accessible GitHub repository for this application is https://github.com/roeszler/n3orthotics

### Development Environment (GitPod)
The application has been deployed to GitPod pages. The steps to deploy are as follows:
* In the GitHub, GitLab or Bitbucket account page where you created a repository for the project, navigate to the tab titled '<> Code'
* From here, navigate to the button on the top right of the repository navigation pane titled 'Gitpod'.
* If you press this it will create a new GitPod development environment each time.

Alternatively, if you have already created the GitPod environment for your project : 

* In the browser’s address bar, prefix the entire URL with [gitpod.io/#](https://gitpod.io/#) or [gitpod.io/workspaces](https://gitpod.io/workspaces) and press Enter. This will take you to a list of workspaces that have been active within the past 14 days.
* Search for the workspace you wish to work on and access the link to it that lies within the pathway https://gitpod.io/.
* Sign in to the workspace each time with [gitpod.io/#](https://gitpod.io/#) using one of the listed providers (GitHub / GitLab / BitBucket) and let the workspace start up.
* On navigating to the workspace for the first time, it may take a little while longer than normal to initially install all it needs. Be patient.
* It is recommend that you install the GitPod browser extension to make this a one-click operation into the future.

### Deployment Environment (Heroku)
* Login Heroku and create new Heroku app
* In 'settings' tab: set the buildpacks to `heroku/python` and `heroku/nodejs` in that order
* Reveal config vars, add and save KEY : VALUE variables in this order :
  * CREDS : Copy and paste entire contents of 'your' creds.json file
  * PORT : 8000
* Within 'deploy' tab: choose GitHub as deployment method and link app to the repository
* Choose 'Deploy Branch' option you prefer.

## 7. Credits 
* Deployment portal from the [Code Institute](https://codeinstitute.net/), hosted at [Heroku](https://www.heroku.com/platform).
* Primary and additional Python coding was studied and reworked from modules provided through the Code Institute's [Diploma in Full Stack Software Development](https://codeinstitute.net/se/full-stack-software-development-diploma/), [W3 Schools](https://www.w3schools.com/), [Stack overflow](https://stackoverflow.com/), [mozilla.org](https://developer.mozilla.org/en-US/docs/Web/JavaScript) and [GeeksforGeeks](https://www.geeksforgeeks.org/).
* How to best handle rows information in [gspread](https://support.google.com/docs/thread/37808063/google-sheets-script-to-hide-specific-rows-based-on-cell-value?hl=en)
* [Importing validation]((https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/)) for email and [removing blank spaces](https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/) from a string at Geeks for Geeks.
* Create a clear screen function from [Codecap](https://codecap.org/clear-screen-in-python/)
* Testing tree process sourced from [Optimal Workshop](https://www.optimalworkshop.com/learn/101s/tree-testing/)

---
__COPYRIGHT NOTICE__ :

 *The n(3)orthotics app is a functional program intended for educational purposes at the time of coding. Notwithstanding, it has been written as a proof of concept and invitation to treat for a business [northotics.com](https://northotics.com/home/) and possible stakeholders into the future. Copyrights for code, ideas, concepts and materials strictly lies with Stuart Roeszler © 2022. All rights reserved.*