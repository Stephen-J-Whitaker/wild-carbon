# **Wild Carbon**
[‘Wild Carbon’]( https://wild-carbon-803b1e2f6e91.herokuapp.com/) is a website (hosted on [Heroku](https://www.heroku.com/) and implemented with the aid of the Python Django framework) that’s for people who want to offset their carbon footprint and care about the environment.

Wild Carbon offers a service where users of the website can commission trees to be grown and planted on their behalf at Wild Carbon’s site in the west of Ireland. Once planted, the trees are allowed to grow in the protected, newly rewilded, site for the duration of the trees’ lives, gradually sequestering carbon for the people who commissioned them.

The company isn’t only about providing a carbon sequestration service,
. It’s also about rewilding, the return of areas that have been cultivated, perhaps for many years, to a wild state. This involves the planting of the commissioned native trees along with other flora that would have naturally inhabited the site. In turn, this replanting of the site encourages the return of the native fauna.

Sequestering carbon for the Wild Carbon customers whilst increasing the natural biodiversity of areas of land is the mission of Wild Carbon.

- [Link to live ‘Wild Carbon’ website]( https://wild-carbon-803b1e2f6e91.herokuapp.com/)


![Responsive mockup]( docs/images/readme_responsive_mockup.jpg)

## **Contents**

1 [Project Initiation](#1-project-initiation)

2 [Wild Carbon development](#2-wild-carbon-development)

3 [Features](#3-features)

4 [Testing](#4-testing)

5 [Project Sign Off](#5-project-sign-off)

6 [Releases](#6-releases)

7 [Deployment](#7-deployment)

8 [Technologies Used](#8-technologies-used)

9 [Credits](#9-credits)

10 [Acknowledgements](#10-acknowledgements)


## **1. Project Initiation**

- ## Agile

    - ### Epics, User Stories and Tasks

        An agile approach was taken to the planning and implementation of the project. Epics were identified for the project from the basic requirements of an ecommerce store that would be selling the service of growing and planting trees to sequester carbon. As would be true of many e-commerce stores, these epics were the website, the shop functionality of the website and fulfillment management for orders placed.

        The epics were then refined into user stories, the user stories associated tasks and the acceptance criteria for the features developed to satisfy the user stories.

        As the project was planned, it was ensured that there was no functionality duplicated across features and that code could be reused wherever possible.

        As each user story was planned, new acceptance criteria were added to features as required for the user story in question to be satisfied. User stories were analysed in order of priority with functionality of later planned user stories building on the functionality of previously planned ones. This meant that the features functions that were worked on for later developed user stories were dependent on the earlier user stories being completed.

	    A stack of user stories in a kanban board was used to manage the order in which user stories were worked and ensure they were worked on in the correct order considering their priorities and interdependencies.  
        
        All feature acceptance criteria from all user stories were consolidated onto a single list from which a test plan could be produced.

        Note: During the planning and refinement phase, some features were combined with others and the feature ids of the features no longer required were removed from use, hence there are gaps in the feature id numbering system. No feature that is a requirement of the system has been omitted from the documentation.

        -   [Epics and User Stories](docs/pdfs/readme_epics.pdf)
        -   [Epic specifications](docs/pdfs/readme_epic_specifications.pdf)
        -   [Epic / User Story Acceptance Criteria](docs/pdfs/readme_epic_acceptance_criteria.pdf)
        -   [Consolidated Feature Acceptance Criteria](docs/pdfs/readme_feature_acceptance_criteria.pdf)

    - ### MoSCoW

        Once the design planning had taken place, the number of story points allocated to each user story was decided by considering the user storys’ tasks complexity and size. 

	    User stories were prioritised to ensure, firstly, the earliest possible return on investment for Wild Carbon followed by maximizing that return and lastly streamlining the fulfillment processes. In terms of the development of the software, this meant that the e-commerce part of the store being functional was the highest priority, followed by marketing for the company’s service to increase customer reach hence increasing the probability of making sales and, lastly, front end custom fulfillment functionality. Fulfillment functionality could easily be worked around in the standard Django admin pages should there be insufficient time to complete all fulfillment epic user stories. 

	    Using the MoSCoW technique all user stories were given a priority of 'must have', 'should have' or 'could have'. There were no ‘won't have’ user stories.

        -   [Iteration 1 MoSCoW Analysis](docs/pdfs/readme_moscow_analysis.pdf)

    - ### Agile tools

        Tools in GitHub were used to manage the project development phase. The user stories were entered as issues along with their associated tasks and acceptance criteria as well as the acceptance criteria for the features developed to satisfy the user stories.

        The user stories were given labels that indicated the epic they belonged to, their MoSCoW rating and the number of modified Fibonacci scaled story points that they had been allocated. 

        Initially the user stories (issues) were placed on the product backlog (implemented using a milestone) and were then moved onto the project Iteration 1 milestone when it was decided that they would be worked on during that iteration. The iteration was a 4 week period. 

        During the iteration, the user stories were managed in a GitHub project on a kanban board. As planned, in the order of priority, the user stories were moved from the 'ToDo' to 'In Progress' and, once complete, to 'Done. 

        Portion of Kanban

        ![Kanban](docs/images/readme_kanban.jpg)

    - ### User Story / Task Prioritisation

        The order that the user stories were worked on was dependent on the MoSCoW priority along with the dependencies of each of the user stories. 

        The features and functionality of user stories moved into the ‘in progress’ column were often dependent on the completion of user stories worked on before them. These dependencies were ascertained during the project initiation/planning stage and the additional acceptance criteria required for each feature for the user story in question were appended to those defined for the user stories developed beforehand. By appending all new requirements to the bottom of the list of previous feature acceptance criteria, a full set of feature acceptance criteria was developed. 

        Example User Story

        ![User Story](docs/images/readme_user_story.jpg)

    - ### Acceptance Tests

        From this full feature set list and those features acceptance criteria, manual testing procedures were developed that would ascertain if the acceptance criteria for the user stories, all the features and therefore the project as a whole had been satisfied. 

        When it was believed that a user story development had been completed, the test script compiled to that point was run through to ensure that both the new set of tests for the most recent user story and those defined beforehand, for previous user stories, all passed as all the previous functionality was required for the new user story and any other user story that uses the feature the tests relate to.

## **2. Wild Carbon Development**
  - ### **Website Interface Development**

    - ### Interface Mockups


- ### **Wild Carbon Style Development**



    -	### Typography



    -   ### Colour Schemes



    -   ### Images and Graphics


-	### SEO

## **3. Features**





-   ### **Potential future features**


## **4. Testing**
-   **Code Validation**

-   **Functionality Test Results**

    **Other Testing**

-   **Bugs Found and Resolved or Current**

## **5. Project Sign Off**

## **6. Releases**

## **7. Deployment**


## Forking the Repository

## Clone the Repository

## **8. Technologies Used**

- [Python](https://www.python.org/)

-   Django

-   HTML

-   CSS

-   JavaScript

-   ElephantSQL : Hosts a postgres database for the project

-   Amazon AWS S3 Bucket : Cloud storage for static and media files

-   Bootstrap : Used to implement the responsive navigation bar, add styles using their preconfigured classes and a dependency of some Django packages

-   Google Fonts : Used for fonts Khand’ and 'Lato'

-   Code institute student template for GitPod and Codeanywhere: Used to install the necessary IDE tools and set up GitPod, Codeanywhere and GitHub Codespaces as required

-   The W3C Markup Validation Service : Used to validate the website HTML

-   The W3C CSS Validation Service - Jigsaw : Used to validate the website CSS

-   JSHint, a JavaScript Code Quality Tool (linter): Used to validate and check the styling of the website JavaScript

-   Favicon.io : Used to create the favicon for the site

-   JQuery : Used for its implementation of Ajax

-   Font Awesome : Used to source icon svg files and serve icons as referenced in the code

-   Ajax : Used to validate data entered by the user

-   pgAdmin : Used to access the postgres database and verify create, read, update and delete was happening as required

-   [Corel Draw](https://www.coreldraw.com/en/) : Used for developing the mockups for the app

-   [Microsoft Excel](https://www.microsoft.com/en-ie/microsoft-365/excel) : Used for documenting features and recording test results

-   [Microsoft Visio](https://www.microsoft.com/en-ie/microsoft-365/visio/flowchart-software) : Used for producing Epics, User Stories and the database entity relationship diagram.

-   [Chrome](https://www.google.com/intl/en_ie/chrome/) : Used for research, development and testing (including DevTools and Lighthouse test suite)

-   [Safari](https://www.apple.com/safari/) : Used for testing

-   [Opera](https://www.opera.com/) : Used for testing

-   [Edge](https://www.microsoft.com/en-us/edge) : Used for testing

-   [Firefox](https://www.mozilla.org/en-US/firefox/new/) : Used for testing

-   [Notepad++](https://notepad-plus-plus.org/downloads/) : Used for text file editing

-   [GitPod](https://www.gitpod.io/) : Used for product development and testing

-   [GitHub](https://github.com/) : Used for accessing committed code repositories and produce development and testing in its Codespaces IDE

-   [Git](https://git-scm.com/): Used for code version control

-   [Code Institute Python Linter](https://pep8ci.herokuapp.com/#): Used to validate and check the styling of the Python code

-   Windows 10 snipping tool for creating screen grabbed jpeg files for the readme

-   [TinyJPG](https://tinyjpg.com/): compression of jpg files

-   [Cloud Convert](https://cloudconvert.com/): For conversion of JPEG to WEBP format

-   [Stripe](https://stripe.com/ie): For ecommerce payment implementation

-   [MailChimp](https://mailchimp.com/): Used to handle newletter signup

## **9. Credits**

-   ### **Code**

    -  All code and text content was written by the author, Stephen Whitaker, unless explicitly stated within the code or as described below.

    -   Code to implement the e-commerce store functionality for Wild Carbon including products, basket, and checkout handling was adapted from the Boutique Ado walkthrough project provided by [Code Institute](http://www.codeinstitute.net/). The Boutique Ado walkthrough also included instructions on sending of emails, integration with Amazon S3 Bucket for serving static and media files and the [Stripe]( https://stripe.com/ie) payment system and these instructions were followed during implementation of the Wild Carbon project. The code sourced from or adapted from the Boutique Ado project is referenced in the Wild Carbon project code at the locations where the Boutique Ado code is in use.

    -	[Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) was used for the creation of the responsive navigation bar, toasts and some styles throughout the template code were implemented using Bootstraps css classes.

    -	Code to show success messages on successful deletion was obtained from stack exchange at the following link : https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown. The code can be found in views.py of the plants app.

    -	Settings for the configuration of an ElephantSQL database were provided by Code Institute. The code is in [Settings.py](https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/wild_carbon/settings.py) for the wild_carbon project.

    -	Settings required to configure allauth were provided by Code Institute. The code is in [Settings.py](https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/wild_carbon/settings.py) for the wild_carbon project and [urls.py](https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/wild_carbon/urls.py)

    -	Code to use ajax to send and receive data to and from a Django view was adapted from code at the following link : https://www.geeksforgeeks.org/handling-ajax-request-in-django/. The code can be found in [views.py]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/plants/views.py) and [add_edit_plant.js]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/plants/static/plants/js/add_edit_plant.js) in the plants app

    -	Code used to reduce multiple white spaces in a string to single spaces was taken from the following site: https://www.tutorialrepublic.com/faq/how-to-replace-multiple-spaces-with-single-space-in-javascript.php. The code can be found in [add_edit_plant.js]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/plants/static/plants/js/add_edit_plant.js) in the plants app

    -   The code to serve the sitemap.xml and robots.txt were taken from the following tutorial https://ngangasn.com/sitemap-robot-txt-django/?utm_content=cmp-true . The code can be found in the [urls.py]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/wild_carbon/urls.py) of the Wild Carbon project folder

    -   The [sitemap.xml]( https://wild-carbon-803b1e2f6e91.herokuapp.com/sitemap.xml) was generated at https://www.xml-sitemaps.com/

    -   Code to integrate with MailChimp for newsletter signup handling was sourced at [MailChimp]( https://mailchimp.com/) and is imported in [index.html]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/home/templates/home/index.html)

    -   Code to implement the creation of many to many relationships between the location and plants available at that location was sourced at https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024. The code can be found in [forms.py](https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/locations/forms.py) and [views.py](https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/locations/views.py) of the locations app.
    
    -   Code to confirm if a user trying to access a view is a superuser was sourced at https://stackoverflow.com/questions/67351312/django-check-if-superuser-in-class-based-view. The code can be found in [mixins.py]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/wild_carbon/mixins.py) in the Wild Carbon project folder

    -   Code to confirm deletion of a plant was sourced from the [Music Aid project]( https://github.com/Stephen-J-Whitaker/music-aid). The code can be found in the DeletePlant class in [views.py]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/plants/views.py) in the plants app

    -   Code to validate whether a plant common name as entered by a user in the add and edit plant views was unique in the database was sourced from the [Music Aid project]( https://github.com/Stephen-J-Whitaker/music-aid). The code can be found in the common_name_validate function in [views.py]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/plants/views.py) and [add_edit_plant.js]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/plants/static/plants/js/add_edit_plant.js) in the plants app


-   ### **Content**

    -   The privacy policy for the site was generated at https://www.privacypolicygenerator.info/ and can be found in [privacy_policy.html]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/templates/includes/privacy_policy.html)

    -   The [Facebook business page](https://www.facebook.com/wild.carbon.sequestration) for Wild Carbon was generated and is hosted by [Facebook]( https://www.facebook.com/)

    -   A link to [carbonfootrint.com’s]( https://www.carbonfootprint.com/calculator.aspx) carbon footprint calculator was used in the [Useful Links]( https://wild-carbon-803b1e2f6e91.herokuapp.com/how_it_works/) section of the Wild Carbon website

    -   A link to [rewildingeurope.com’s]( https://rewildingeurope.com/what-is-rewilding/) description of rewilding was used in the [Useful Links]( https://wild-carbon-803b1e2f6e91.herokuapp.com/how_it_works/) section of the Wild Carbon website

    -   A link to [treecouncil.ie’s]( https://www.treecouncil.ie/carbon-footprint) carbon footprint facts was used in the [Useful Links]( https://wild-carbon-803b1e2f6e91.herokuapp.com/how_it_works/) section of the Wild Carbon website

    -   Plant information was sourced at the [RHS]( https://www.rhs.org.uk/) website

    -   [WordTracker](https://www.wordtracker.com/) was used for keyword research for search engine optimisation

    -   [FontAwesome]( https://fontawesome.com/) used to source icon SVG files and other icons as served by them. The icons are referenced in the code

-   ### **Media**

    -   The main heading image of a [glade]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/static/images/base_home_index_glade.webp) was sourced at https://www.pexels.com/photo/green-forest-under-white-sky-during-daytime-165537/

    -   The [carbon capture location]( https://raw.githubusercontent.com/Stephen-J-Whitaker/wild-carbon/main/static/images/carbon_capture_location.webp) image was soured at https://iowalandcompany.com/jones-county-iowa-80-acres-for-sale/

    -   The image of [a person holding a seedling]( https://raw.githubusercontent.com/Stephen-J-Whitaker/wild-carbon/main/home/static/home/images/home_about_us_plug_plant.webp) was sourced at https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/home/static/home/images/home_about_us_plug_plant.webp

    -   The image of a [tree with CO2 and O2 molecules around it]( https://raw.githubusercontent.com/Stephen-J-Whitaker/wild-carbon/main/home/static/home/images/home_how_it_works.webp) was sourced at https://ecotree.green/en/how-much-co2-does-a-tree-absorb

    -   The plant images used for the plant products were sourced at [treecouncil.ie](https://www.treecouncil.ie/native-irish-trees)

## **10. Acknowledgements**

-   A special thank you to my mentor Marcel Mulders

-   Thank you to all those who were kind enough to test the website and provide feedback
